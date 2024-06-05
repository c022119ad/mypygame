from PIL import Image
img = Image.open("mygame/fig/title.jpg")
resize_img = img.resize((1600,1000))
resize_img.save("mygame/fig/title_resize.jpg")

