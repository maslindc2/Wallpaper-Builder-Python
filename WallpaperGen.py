from PIL import Image, ImageOps
import tkinter as tk
from tkinter import filedialog


def resize():
    root = tk.Tk()
    root.withdraw()
    
    #Get the filepath for the images using tkinter
    image1FilePath = filedialog.askopenfilename(filetypes=(("All files", "*.*"),))
    image2FilePath = filedialog.askopenfilename(filetypes=(("All files", "*.*"),))

    image1 = Image.open(image1FilePath)
    image2 = Image.open(image2FilePath)

    # Set the output vars to global and then use ImageOps to crop the images to 
    # 1920x1080
    global resizedImage1
    resizedImage1 = ImageOps.fit(image1, (1920,1080), Image.ANTIALIAS)

    global resizedImage2
    resizedImage2 = ImageOps.fit(image2, (1920,1080), Image.ANTIALIAS)

def dual():
    # Call resize and then place the images in the order left, right and output the
    # final file
    resize()
    combined = Image.new("RGB", (3840, 1080))
    combined.paste(resizedImage1, (0,0))
    combined.paste(resizedImage2, (resizedImage1.size[0], 0))
    combined.save("combined.png")
    
def stacked():
    resize()
    combined = Image.new("RGB", (1920, 2160))
    combined.paste(resizedImage2, (0,1080))
    combined.paste(resizedImage1, (0,0))
    combined.save("combined.png")

def triple():
    #Call resize method for left image and middle image
    resize()

    #For triple we need three images so get the path for another image and resize it    
    image3FilePath = filedialog.askopenfilename(filetypes=(("All files", "*.*"),))
    image3 = Image.open(image3FilePath)
    resizedImage3 = ImageOps.fit(image3, (1920,1080), Image.ANTIALIAS)
    combined = Image.new("RGB", (5760, 1080))

    #Pasting images in the order left middle right
    combined.paste(resizedImage1, (0,0))
    combined.paste(resizedImage2, (1920,0))
    combined.paste(resizedImage3, (3840,0))
    combined.save("combined.png")

if __name__ == "__main__":
    print("How would you like your wallpaper")
    result = input("Dual (1), Stacked (2), Triple(3), or Quit ")
    
    if result == "1" or result == "Dual" or result == "dual":
        dual()
    elif result == "2" or result == "Stacked" or result == "stacked":
        stacked()
    elif result == "3" or result == "triple" or result == "triple":
        triple()
    else:
        print(result + " is not an option try again")