import cv2
import numpy as np

class img_trans:
    def __init__(self, img, path=None):
        self.img = img
        self.path = path

    def import_img(self):
        image = cv2.imread(self.path)
        rgb_img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        return rgb_img

    def make_bw(self):
        bw_img = cv2.cvtColor(self.img, cv2.COLOR_RGB2GRAY)
        return bw_img

    def change_bright(self, value):
        image = self.img

        lim = 255 - value
        image[image > lim] = 255
        image[image <= lim] = np.add(image[image <= lim], value, out=image[image <= lim], casting='unsafe') # have to do np.add b/c += will not accept neg
        
        return image

    def change_sat(self, value):
        hsv = cv2.cvtColor(self.img, cv2.COLOR_RGB2HSV)
        h, s, v = cv2.split(hsv)

        lim = 255 - value
        s[s > lim] = 255
        s[s <= lim] = np.add(s[s <= lim], value, out=s[s <= lim], casting='unsafe')

        final_hsv = cv2.merge((h, s, v))
        image = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2RGB)

        return image

    def change_hue(self, value):
        hsv = cv2.cvtColor(self.img, cv2.COLOR_RGB2HSV)
        h, s, v = cv2.split(hsv)

        lim = 179 - value
        h[h > lim] = 179
        h[h <= lim] = np.add(h[h <= lim], value, out=h[h <= lim], casting='unsafe')

        final_hsv = cv2.merge((h, s, v))
        image = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2RGB)

        return image

    def change_angle(self, angle, scaling=1):
        if self.img.shape == None:
            pass
        else:
            rows, cols = self.img.shape

        M = cv2.getRotationMatrix2D((cols/2,rows/2), angle, scaling)
        dst = cv2.warpAffine(self.img,M,(cols,rows))

        return dst

    def gaussian_blur(self, size, sigma=0):
        blur = cv2.GaussianBlur(self.img,(size,size),sigma)

        return blur
