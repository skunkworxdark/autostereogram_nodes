# `autostereogram-nodes` for InvokeAI
Discord Link :- [autostereogram-nodes](https://discord.com/channels/1020123559063990373/1198696869178638506)

InvokeAI nodes to generate autostereogram images from a depth map.  This is not a very useful node but more a 90s nostalgic indulgence as I used to love these images as a kid. 

## Usage

### <ins>Install</ins><BR>
There are two options to install the nodes:

1. **Recommended**: Use Git to clone the repo into the `invokeai/nodes` directory. This allows updating via `git pull`.

    - In the InvokeAI nodes folder, run:

        For Latest Invoke (4.0+):
        ```bash
        git clone https://github.com/skunkworxdark/autostereogram_nodes.git
        ```
        For Invoke (3.5-3.7):
        ```bash
        git clone https://github.com/skunkworxdark/autostereogram_nodes/tree/invoke-3.7
        ```

2. Manually download and place [autostereogram.py](autostereogram.py) & [__init__.py](__init__.py) in a subfolder in the `invokeai/nodes` folder.

### <ins>Update</ins><BR>
Run a `git pull` from the `autostereogram_nodes` folder.

Or run the `update.bat` or `update.sh`.

For manual installs, download and replace the files.

### <ins>Remove</ins><BR>
Delete the `autostereogram_nodes` folder. Or rename it to `_autostereogram_nodes` and Invoke will ignore it.

## Nodes
This pack consists of two nodes `Autosteteogram` and `Adv Autostereogram`.

<ins>Common inputs</ins><BR>
- Board: Board name to save images to.
- Depth Map: The grayscale depth map to convert into.
- Pattern: Optional image to use as the background pattern for the autostereogram. If no image is provided random dots will be used.
- Invert Depth Map: Inverts the depth map. This has the impact of inverting the direction of the 3D effect. It is also the difference between crossing or uncrossing your eyes to view the image.
- Grayscale: Convert the output to grayscale.

<ins>Autostereogram</ins><BR>
- Pattern Divisions: How many times the pattern repeats in output images 5-10 is in generally a good range. The lower the repeats the greater the depth effect but the harder it is to see.

<ins>Adv Autostereogram</ins><BR>
- Pattern Width: The width to rescale the pattern. As a guide 5-10 pattern repeats across the output image is a good start.
- Depth Steps: The number of depth steps, 30-127 is a good range. A good starting point is to have the number of steps be around half of the pattern width.


## Examples
Take an image and create a depth map from it then feed it into the autostereogram node along with an optional pattern image.

Workflow example [autostereogram.json](workflows/autostereogram.json)
![Workflow](images/workflow.png)

![Alt text](images/spider.png)
![Alt text](images/spider-depth.png)
![Alt text](images/spider-dots.png)
![Alt text](images/spider-pattern.png) 

![Alt text](images/judo.png)
![Alt text](images/judo_depth.png)
![Alt text](images/judo-pattern.png)

![Alt text](images/pig.png)
![Alt text](images/pig-depth.png)
![Alt text](images/pig-pattern.png) 

Example background patterns. These were generated in InvokeAI using the seamless tiling option and the prompt "a random spiderweb pattern". Good patterns will have quite a lot of small details across the x-axis of the image and will avoid large blocks of single color.<BR>

![Alt text](images/50ec14e1-5a78-47fd-9936-2e9ac39cef75.png)
![Alt text](images/2733c9ce-48f9-4319-93c6-8f095aa1d08f.png)
![Alt text](images/c0ad3be3-8949-40f2-9920-1e8cc785cfa3.png)
