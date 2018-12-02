from PIL import Image, ImageDraw, ImageFont

for i in range(0,1000):

  img = Image.new('RGB', (60, 30), color = "#ffffff")

  d = ImageDraw.Draw(img)
  d.text((10,10), str(i), fill=(0, 0, 0))

  img.save('img/'+str(i)+'.png')