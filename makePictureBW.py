from PIL import Image
import sys

def convert_to_black_and_white(input_path, output_path):
    try:
        # Open the input image
        image = Image.open(input_path)
        # Convert the image to grayscale (black and white)
        bw_image = image.convert("L")
        # Save the black and white image
        bw_image.save(output_path)
        print(f"Black and white image saved to {output_path}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python makePictureBW.py <input_image> <output_image>")
    else:
        input_image = sys.argv[1]
        output_image = sys.argv[2]
        convert_to_black_and_white(input_image, output_image)