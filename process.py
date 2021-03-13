import os.path
from os import path
import cv2 as cv
import argparse
from gradients import compute_gradient
from spaces import color_space_convert
from rescale import rescale_frame

def parser():
    parser = argparse.ArgumentParser(description='OpenCV Reader')
    parser.add_argument("--image", type=str, required=True, help='Path to the image')
    parser.add_argument("--space", type=str, default="original", help='Color space to convert to [hsv, lab, gray, rgb]')
    parser.add_argument("--gradient", type=str, help='Show Image Gradient [laplacian, sobelx, sobely, sobelxy, canny]')
    parser.add_argument("--scale", type=float, default=1.00, help='Scale size of output')
    parser.add_argument("--show", type=bool, default=True, help='Show output')
    parser.add_argument("--output", type=str, default='output/output_image.jpg', help='Output location of file')

    return parser.parse_args()

if __name__=='__main__':
    args = parser()
    image_path = args.image
    if path.exists(image_path):
        image=cv.imread(image_path)
        
        if args.scale:
            image = rescale_frame(image, args.scale)
            
        if args.space:
            color_space_convert(image, args.space, show=args.show)
        
        if args.gradient:
            gray_image = color_space_convert(image, 'gray')
            compute_gradient(gray_image, args.gradient, show=args.show)


        output=args.output
    else:
        print('Invalid File Path')