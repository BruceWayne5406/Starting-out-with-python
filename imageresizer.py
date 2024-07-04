from PIL import Image

img=Image.open("spaceship.png")

print(f"current image size is {img.size}")

resized_image=img.resize((100,100))
resized_image.save("new_image.png")