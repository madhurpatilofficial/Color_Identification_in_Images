#Color Detection
#Madhur Patil


import pandas as cl
import cv2


image_path = 'img1.jpg'
image_path = 'img2.jpg'
image_path = 'img3.jpg'
csv_path = 'colors.csv'


ind = ['color', 'name', 'hex', 'R', 'G', 'B']
data_frame = cl.read_csv(csv_path, names=ind, header=None)  # created header to know column_name

image = cv2.imread(image_path)
image = cv2.resize(image, (512, 512))
print(image)  # computer will see arrays of pixels


clicked = False
r = g = b = xpo = ypo = 0  # initialising x, y position with 0


def get_color_name(R, G, B):
    min = 2000
    for i in range(len(data_frame)):
        d = abs(R - int(data_frame.loc[i, 'R'])) + abs(G - int(data_frame.loc[i, 'G'])) + abs(
            B - int(data_frame.loc[i, 'B']))  # will scan our csv file
        if d <= min:
            min = d
            cname = data_frame.loc[i, 'name']
    return cname


print(get_color_name(255, 0, 0))  # colors


def position(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global clicked, r, g, b, xpo, ypo
        clicked = True
        xpo = x
        ypo = y
        b, g, r = image[y, x]
        b = int(b)
        g = int(g)
        r = int(r)


cv2.namedWindow('image')
cv2.setMouseCallback('image', position)


while True:
    cv2.imshow('image', image)
    if clicked:
        cv2.rectangle(image, (20, 20), (600, 70), (b, g, r), -1)
        txt = get_color_name(r, g, b) + 'R=' + str(r) + 'G=' + str(g) + 'B=' + str(b)
        cv2.putText(image, txt, (50, 50), 2, 0.8, (255, 255, 255), 2, cv2.LINE_AA)  # initial position, font,color_name, thickness, line
        if r + g + b > 600:
            cv2.putText(image, txt, (50, 50), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)
    if cv2.waitKey(20) & 0xFF == 27:
        break


# cv2.imshow('image',image)
# cv2.waitKey(0)  #no need to close windows


cv2.destroyAllWindows()  # clicking cancel button will stop the image
