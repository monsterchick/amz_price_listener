import os


def find_image_path(image_name):
    image_dir = os.path.abspath('image')
    image_name = image_name
    image_path = os.path.join(image_dir, image_name)
    # print(image_path)

    return image_path