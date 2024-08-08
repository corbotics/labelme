
## About SAM:
#### 1. Installation
You can use `pip install .` as described below to install all the dependencies. Except the original dependencies, additional dependencies are
```
torch>=1.7
torchvision>=0.8
appdirs
opencv-python-headless
segment-anything @ git+https://github.com/facebookresearch/segment-anything.git
```
Note that latest `opencv-python` could cause conflicts with pyqt5, need to install older versions of it or use `opencv-python-headless`
#### 2. Configuration
The SAM related configuration is available in config file. You can find a `.labelmerc` file at user home directory after you open labelme for the first time (You need to delete old ones if you used official labelme previously).
Under sam section, you can adjust the settings accordingly.
```
sam:
  weights: vit_h # vit_h, vit_l or vit_b
  maxside: 1280 # will downsize the image during inference to the maxsize.
  approxpoly_epsilon: 1. # adjust the poylgon simplification algorithm. The larger the lesser vertices.
  device: "cuda" # "cuda" or "cpu"
```
#### 3. Use
After loaded one image, you can click `Edit` -> `Create Polygons with Segment Anything`. At the first time you use this option, it will freeze for a while and download the model weights(vit_h's weights file is around 2gb, so it could take some time).
After it downloaded, you can start annotating. Only points prompt is supported, you can left click to mark positive prompt and right click for negative prompt. When done, hit enter and it will generate polygons from the result.

Since we are editing in video mode, you should start at the frame that has some segmented object visible. All frames before that are not used.
### Config
Default init config: `labelme/config/default_config.yaml`
Your config: `~/.labelmerc`

Useful keys:
-  W: start SAM editing
-  S: compute SAM video
-  C: continue frame
- Enter: save current mask to label
- D: open_next
- A: open_prev

## Todo
- able to skip a frame completely by sam.
- able to load in masks from previous editing
- PROBLEM WHEN HAVING JSON IN FILE 