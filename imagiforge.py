from PIL import Image, ImageEnhance

def change_aspect_ratio(image):
    aspect_ratio = input("Enter the new aspect ratio (width:height): ").split(':')
    width, height = map(int, aspect_ratio)
    resized_image = image.resize((width, height))
    return resized_image

def change_brightness(image):
    brightness = float(input("Enter the brightness value (-1.0 to 1.0): "))
    enhancer = ImageEnhance.Brightness(image)
    adjusted_image = enhancer.enhance(brightness)
    return adjusted_image

def change_contrast(image):
    contrast = float(input("Enter the contrast value (0.0 to 2.0): "))
    enhancer = ImageEnhance.Contrast(image)
    adjusted_image = enhancer.enhance(contrast)
    return adjusted_image

def save_image(image, filename):
    image.save(filename)

def main():
    image_path = input("Enter the path of the image: ")
    image = Image.open(image_path)

    operations = {
        1: change_aspect_ratio,
        2: change_brightness,
        3: change_contrast
    }

    print("Available operations:")
    for key, operation in operations.items():
        print(f"{key}. {operation.__name__.replace('_', ' ').title()}")

    operation_choice = int(input("Enter the number corresponding to the desired operation: "))

    if operation_choice not in operations:
        print("Invalid operation!")
        return

    modified_image = operations[operation_choice](image)

    output_filename = input("Enter the output filename prefix: ")
    save_image(modified_image, f"{output_filename}_{operation_choice}.jpg")

if __name__ == "__main__":
    main()
