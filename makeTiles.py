# make tiles from command line input

import argparse
from PIL import Image
from PIL import ImageDraw, ImageFont

def read_letter_file(fileObj, verbose):
    if (verbose):
        print ("Loading letter files..")
    text_file = open(fileObj.name,"r")
    
    data = text_file.read().splitlines()

    text_file.close()

    if (verbose):
        print(f" . read {(len(data))} lines from {(fileObj.name)}")     

    return data   

def read_image_file(fileObj, verbose):
    if (verbose):
        print ("Loading Image file..")
    img = Image.open(fileObj.name)
    img.width, img.height

    if (verbose):
        print(f" . found image that is ({(img.width)}w X {(img.height)}h) from {(fileObj.name)}")  
    
    return img
    
def draw_text_on_image(image, text, output): 
    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype("font/AlumniSansCollegiateOne-Regular.ttf", 225)
    text_color = (200, 128, 128) 
    text_color_back = (40, 10, 10) 
    width, height = image.size

    box = draw.textbbox((1,1), text=text, stroke_width=1, font=font)

    text_width = box[2] - box[0]
    text_height = 250 # box[3] - box[1]

    # text_width, text_height = draw.textsize(text, font)
    x = (width - text_width) / 2
    y = (height - text_height) / 2

    draw.text((x+5, y), text, stroke_width=1, fill=text_color_back, font=font)
    draw.text((x-5, y-10), text, stroke_width=0, fill=text_color, font=font)

    image.save(output)   

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
    parser.add_argument("textFile", type=argparse.FileType('r'), help="Text File containing letters")
    parser.add_argument("imageFile", type=argparse.FileType('r'), help="Text File containing letters")

    args = parser.parse_args()
    
    letters = read_letter_file(args.textFile, args.verbose)
    image = read_image_file(args.imageFile, args.verbose)

    # for each letter, create an imgge, and save it. 
    for letter in letters:  
        iback = image.copy()
        if (args.verbose):
            print(f" . Creating image for letter {letter}")
        draw_text_on_image(image, letter, f"output/{letter}.png")
        image.paste(iback)
     
    

