# autostereogram-nodes
InvokeAI nodes to generate autostereogram images from a depth map.  This is not a very useful node but more a nostalgic indulgence as I used to love these images as a kid. 

## Usage
<ins>Install:</ins><BR>
There are two options for installing these nodes. (Option 1 is the recommended option) 
1. Git clone the repo into the `invokeai/nodes` directory. (**Recommended** - as it allows updating via a git pull)
    - open a command prompt/terminal in the invokeAI nodes directory ( or choose `8. Open the developer console` option from the invoke.bat then `cd nodes`)
    - run `git clone https://github.com/skunkworxdark/autostereogram_nodes.git`
2. Manually download and place [autostereogram.py](autostereogram.py) & [__init__.py](__init__.py) in a subfolder in the `invokeai/nodes` folder.

<ins>Update:</ins><BR>
Run a `git pull` from the `autostereogram_nodes` folder. Or run the `update.bat` or `update.sh` that is in the `invokeai/nodes/autostereogram_nodes` folder. If you installed it manually then the only option is to monitor the repo or discord channel and manually download and replace the file yourself.

<ins>Remove:</ins><BR>
Simply delete the `autostereogram_nodes` folder or you can rename it by adding an underscore `_autostereogram_nodes` and Invoke will ignore it.


## Examples
Basically, You take an image and create a depth map from it then feed it into the autostereogram node. 

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

Example background pattern - these were generated in InvokeAI using the seamless tiling and the prompt "a random spiderweb pattern"

![Alt text](images/50ec14e1-5a78-47fd-9936-2e9ac39cef75.png)
![Alt text](images/2733c9ce-48f9-4319-93c6-8f095aa1d08f.png)
![Alt text](images/c0ad3be3-8949-40f2-9920-1e8cc785cfa3.png)
