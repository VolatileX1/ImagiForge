from PIL import Image, ImageEnhance

def change_aspect_ratio(image):
    width, height = map(int, input("Enter the new aspect ratio (width:height): ").split(':'))
    return image.resize((width, height))

def change_brightness(image):
    brightness = float(input("Enter the brightness value (-1.0 to 1.0): "))
    enhancer = ImageEnhance.Brightness(image)
    return enhancer.enhance(brightness)

def change_contrast(image):
    contrast = float(input("Enter the contrast value (0.0 to 2.0): "))
    enhancer = ImageEnhance.Contrast(image)
    return enhancer.enhance(contrast)

def crop_image(image):
    left, upper, right, lower = map(int, input("Enter the crop region (left, upper, right, lower): ").split())
    return image.crop((left, upper, right, lower))

def rotate_image(image):
    angle = float(input("Enter the rotation angle in degrees: "))
    return image.rotate(angle)

def save_image(image, filename):
    image.save(filename)

def main():
    image_path = input("Enter the path of the image: ")
    image = Image.open(image_path)

    operations = {
        1: change_aspect_ratio,
        2: change_brightness,
        3: change_contrast,
        4: crop_image,
        5: rotate_image
    }

    print("Available operations:")
    for key, operation in operations.items():
        print(f"{key}. {operation.__name__}")

    operation_choice = int(input("Enter the number corresponding to the desired operation: "))

    if operation_choice not in operations:
        print("Invalid operation!")
        return

    modified_image = operations[operation_choice](image)

    output_filename = input("Enter the output filename prefix: ")
    save_image(modified_image, f"{output_filename}_{operation_choice}.jpg")

if __name__ == "__main__":
    main()
