# 2024 skunkworxdark (https://github.com/skunkworxdark)

from typing import Optional

import numpy as np
from PIL import Image, ImageOps

from invokeai.app.invocations.baseinvocation import (
    BaseInvocation,
    FieldDescriptions,
    Input,
    InputField,
    InvocationContext,
    WithMetadata,
    invocation,
)
from invokeai.app.invocations.primitives import (
    BoardField,
    ImageField,
    ImageOutput,
)
from invokeai.app.services.image_records.image_records_common import (
    ImageCategory,
    ResourceOrigin,
)


@invocation(
    "autostereogram",
    title="AutoStereogram",
    tags=["image"],
    category="image",
    version="1.0.0",
)
class AutostereogramInvocation(BaseInvocation, WithMetadata):
    """create an autostereogram from a depth map"""

    # Inputs
    board: Optional[BoardField] = InputField(default=None, description=FieldDescriptions.board, input=Input.Direct)
    depth_map: ImageField = InputField(description="The depth map to create the image from")
    pattern: Optional[ImageField] = InputField(
        default=None,
        description="The pattern image to use as the background, if not provided then random dots will be used",
    )
    separation: int = InputField(
        default=100,
        gt=20,
        description="The eye separation in pixels",
    )
    depth: int = InputField(
        default=50,
        gt=10,
        description="The number of depth steps, 20-80 is good a range but should be less than separation",
    )
    invert_depth_map: bool = InputField(
        default=False,
        description="Invert the depth map (difference between crossing and uncrossing eyes)",
    )
    grayscale: bool = InputField(
        default=False,
        description="Color or Grayscale output",
    )

    def invoke(self, context: InvocationContext) -> ImageOutput:
        # Load the depth map
        depth_map = context.services.images.get_pil_image(self.depth_map.image_name).convert("L")

        # extend the left of the depthmap by the separation value
        depth_map = ImageOps.expand(depth_map, border=(self.separation, 0, 0, 0), fill=0)

        width, height = depth_map.size

        # Convert the depth map to a numpy array (invert if requested)
        depth_np = np.array(depth_map) ^ 0xFF if self.invert_depth_map else np.array(depth_map)

        if self.pattern:
            # Load the pattern
            pattern = context.services.images.get_pil_image(self.pattern.image_name).convert("RGB")

            # Resize pattern width to separation size
            new_height = int(self.separation * (pattern.height / pattern.width))
            pattern = pattern.resize((self.separation, new_height))

            pattern_width, pattern_height = pattern.size
            pattern_np = np.array(pattern)

        # Create an output image
        output_image = Image.new("RGB", (width, height))
        pixels = output_image.load()

        # Generate the autostereogram
        for y in range(height):
            for x in range(width):
                if x < self.separation:
                    if self.pattern:
                        r, g, b = pattern_np[y % pattern_height, x % pattern_width]
                    else:
                        r = g = b = np.random.randint(0, 255)
                        if not self.grayscale:
                            g = np.random.randint(0, 255)
                            b = np.random.randint(0, 255)
                else:
                    shift = depth_np[y, x] / 255.0 * self.depth
                    r, g, b = pixels[int(x - self.separation + shift), y]
                pixels[x, y] = (int(r), int(g), int(b))

        # Cut off the left hand pattern section
        output_image = output_image.crop((self.separation, 0, width, height))

        if self.grayscale:
            output_image = output_image.convert("L")

        # Save the image
        image_dto = context.services.images.create(
            image=output_image,
            image_origin=ResourceOrigin.INTERNAL,
            image_category=ImageCategory.GENERAL,
            board_id=self.board.board_id if self.board else None,
            node_id=self.id,
            session_id=context.graph_execution_state_id,
            is_intermediate=self.is_intermediate,
            metadata=self.metadata,
            workflow=context.workflow,
        )

        return ImageOutput(
            image=ImageField(image_name=image_dto.image_name),
            width=image_dto.width,
            height=image_dto.height,
        )
