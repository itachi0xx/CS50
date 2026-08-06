import sys
from PIL import Image, ImageOps


def main():
    if len(sys.argv) != 3:
        sys.exit("Usage: python shirt.py input output")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    valid_extensions = [".jpg", ".jpeg", ".png"]

    input_ext = get_extension(input_file)
    output_ext = get_extension(output_file)

    if input_ext not in valid_extensions:
        sys.exit("Invalid input")

    if output_ext not in valid_extensions:
        sys.exit("Invalid output")

    if input_ext != output_ext:
        sys.exit("Input and output have different extensions")

    try:
        input_image = Image.open(input_file)

        shirt = Image.open("shirt.png")

        fitted = ImageOps.fit(input_image, shirt.size)

        fitted.paste(shirt, shirt)

        fitted.save(output_file)

    except FileNotFoundError:
        sys.exit("Input does not exist")


def get_extension(filename):
    return "." + filename.lower().split(".")[-1]


if __name__ == "__main__":
    main()