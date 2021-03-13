import cv2 as cv
import argparse
from spaces import color_space_convert

def parser():
    parser = argparse.ArgumentParser(description='OpenCV Reader')
    parser.add_argument("--image", type=str, help='Path to the image')
    parser.add_argument("--space", type=str, default="original", help='Color space to convert to [hsv, lab, gray, rgb]')
    parser.add_argument("--scale", type=float, default=1.00, help='Scale size of output')
    parser.add_argument("--show", type=bool, default=False, help='Show output')
    parser.add_argument("--output", type=str, default='output/output_image.jpg', help='Output location of file')

    return parser.parse_args()

if __name__=='__main__':
    args = parser()
    image_path = args.image
    image=cv.imread(image_path)
    conversion=args.space
    output=args.output
    color_space_convert(image, conversion, show=args.show)