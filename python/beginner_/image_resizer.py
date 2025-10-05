
from PIL import Image

def resize_image(size1, size2):
    image = Image.open("image.png")
    print(f"Current size: {image.size}")
    resized_image = image.resize((size1, size2))
    resized_image.save("image-" + str(size1) + ".png")
size1 = int(input("Enter width: "))
size2 = int(input("Enter height: "))
resize_image(size1, size2)


