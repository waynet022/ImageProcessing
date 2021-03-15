## Image Processing 

### Requirements
- python3
### Libraries
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
[Required] Image path (ex: assets/images/nature1.jfif)
--image path-to-image 
[Optional] Show image gradients (options: laplacian, sobelx, sobely, sobelxy, canny)
--gradient gradient_option
[Optional] Convert image color space (options: gray, hsv, lab, rgb)
--space color_space_option
[Optional] Resize the output image (original is 1.0)
--scale factor_value
```
### Sample Outputs
#### Gradient

`process.py --image assets/images/nature3.jfif --gradient canny`

Original             |  Canny
:-------------------------:|:-------------------------:
<img src="assets/images/nature3.jfif" width="800">|<img src="assets/images/sample_output/nature3_gd_canny.png" width="800">

#### Color Space

`process.py --image assets/images/nature5.jfif --space hsv`

Original             |  HSV
:-------------------------:|:-------------------------:
<img src="assets/images/nature5.jfif" width="800">|<img src="assets/images/sample_output/nature5_sp_hsv.png" width="800">

#### Color Mapping Intensity 

`process.py --image assets/images/nature2.jfif --channel red`

Lighter regions mean higher intensities of the pixel value and vice versa

Original             |  Red pixel intensity
:-------------------------:|:-------------------------:
<img src="assets/images/nature2.jfif" width="800">|<img src="assets/images/sample_output/nature2_ch_red.png" width="800">



### References
- [Jason Dsouza OpenCV tutorial](https://www.youtube.com/watch?v=oXlwWbU8l2o&t=10147s)
- [Murtaza's Workshop OpenCV tutorial](https://www.youtube.com/watch?v=WQeoO7MI0Bs)
- [OpenCV Python tutorial for Image Processing](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_table_of_contents_imgproc/py_table_of_contents_imgproc.html#py-table-of-content-imgproc)
