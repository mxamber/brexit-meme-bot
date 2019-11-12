import PIL.ImageFont
import PIL.ImageDraw
import PIL.Image
import logging
import io

logging.basicConfig(level=logging.INFO)

text = "allie"

font = PIL.ImageFont.truetype("font.ttf", 200)
font_s = PIL.ImageFont.truetype("font2.ttf", 50)
blue = (26,52,84)
red = (218,64,50)

def draw_text(text, text2):
  img = PIL.Image.open("blank.png")
  draw = PIL.ImageDraw.Draw(img)

  posx = 240
  posy = 200

  size = draw.textsize("Get ", font=font)
  draw.text((posx, posy),"Get", blue, font=font)
  posx += size[0]

  size = draw.textsize("ready", font=font)
  draw.text((posx, posy),"ready", red, font=font)
  posx += size[0]

  draw.text((posx, posy)," for", blue, font=font)
  posy += size[1] - 150; # i added the -150

  posx = 240
  draw.text((posx, posy), text.title(), blue, font=font)

  posx = 430
  posy = 850 # originally 835

  size = draw.textsize(f"Get ready for {text.title()} at ", font=font_s)
  draw.text((posx, posy),f"Get ready for {text.title()} at ", blue, font=font_s)
  posx += size[0]

  size = draw.textsize(f"gov.uk/{text2.lower().replace(' ', '-')}", font=font_s)
  draw.text((posx, posy), f"gov.uk/{text2.lower().replace(' ', '-')}", red, font=font_s)

  draw.line((posx, posy + size[1] + 10, posx + size[0], posy + size[1] + 10), fill=red, width=7)

  return img

text = input("Please enter text: ")
text2 = input("URL (optional, leave blank): ")
if (text2.isspace()) == True or (not text2):
  text2 = text
  
img = draw_text(text, text2)
filename = input("File name (no extensions): ")
filename = filename + ".png"
img.save(filename, "PNG")
