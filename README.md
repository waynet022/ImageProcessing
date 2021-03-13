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
