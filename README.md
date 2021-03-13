## Image Processing 

### Requirements
- python3
#### Libraries
- opencv-python
- numpy

### Setup
```
[Recommended] Create a python virtual environment
python -m venv env

[Required] Install libraries
pip install opencv-python
pip install numpy
```

### Commands
run `process.py` with the following options

```
[Required] image path (ex: assets/images/nature1.jfif)
--image path-to-image 
[Optional] show image gradients (options: rgb, hsv, gray, lab)
--gradient gradient_option 
[Optional] resize the output image (original is 1.0)
--scale factor_value
```
### Sample Output
Gradient

`process.py --image assets/images/nature3.jfif --gradient canny`

Original             |  Canny
:-------------------------:|:-------------------------:
<img src="assets/images/nature3.jfif" width="800">|<img src="assets/images/sample_output/nature3_gd_canny.png" width="800">
