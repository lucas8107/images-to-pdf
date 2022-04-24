from PIL import Image
import sys

def get_input():
    return sys.argv[1:]


def usage_msg():
    return "Usage 😱: output_name <image_0> <image_1> ... <image_n>"


def main():
    try:
        [name, *image_paths] = get_input()
    except ValueError:
        print(usage_msg())
        return

    if not name or not image_paths:
        print(usage_msg())
        return

    images = []
    for _, path in enumerate(image_paths):
        try:
            images.append(Image.open(path))
        except FileNotFoundError:
            print(f"The file {repr(path)} was not found 😞, check your files and try again 😉.")
            return

    images[0].save(f"{name}.pdf", "pdf", save_all=True, append_images=images[1:])


if __name__ == "__main__":
    main()
