from PIL import Image

def resize_image(input_img, output_img, size):
    original = Image.open(input_img)
    resized = original.resize(size)
    resized.save(output_img)



input_img = './haris.png.jpg'

output_img = 'output.png'

new_size = ( 400, 400)


resize_image(input_img=input_img, output_img=output_img, size=new_size)