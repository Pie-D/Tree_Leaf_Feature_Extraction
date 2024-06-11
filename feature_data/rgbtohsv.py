import numpy as np
import cv2


def rgb_to_hsv(pixel):
    r, g, b = pixel
    r, g, b = b / 255.0, g / 255.0, r / 255.0

    v = max(r, g, b)
    delta = v - min(r, g, b)

    if delta == 0:
        h = 0
        s = 0
    else:
        s = delta / v
        if r == v:
            h = (g - b) / delta
        elif g == v:
            h = 2 + (b - r) / delta
        else:
            h = 4 + (r - g) / delta
        h = (h / 6) % 1.0

    return [int(h*180), int(s*255), int(v*255)]


def covert_image_rgb_to_hsv(img):
    hsv_image = []
    for i in img:
        hsv_image2 = []
        for j in i:
            new_color = rgb_to_hsv(j)
            hsv_image2.append((new_color))
        hsv_image.append(hsv_image2)
    hsv_image = np.array(hsv_image)
    return hsv_image


a = int(input("Nhập giá trị cho a: "))
b = int(input("Nhập giá trị cho b: "))
c = int(input("Nhập giá trị cho c: "))

# Tiếp tục xử lý với các biến a, b, c...
data = [a, b, c]
print(rgb_to_hsv(data))
