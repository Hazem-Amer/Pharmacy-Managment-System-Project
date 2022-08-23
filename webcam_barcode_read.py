import cv2
import numpy as np
from pyzbar.pyzbar import decode
import sqlite3
import datetime




#img = cv2.imread('qr_code_5cdd30e269752.png')   #to read qrcode or barcode taken from image
# decoded  = decode(img)
# for barcode in decoded:   # to print the data from the list of items which are [Decoded(data=b'https://barcodesegypt.com', type='QRCODE', rect=Rect(left=73, top=73, width=664, height=664), polygon=[Point(x=73, y=735), Point(x=737, y=737), Point(x=735, y=73), Point(x=74, y=74)])]
#     mydata = barcode.data.decode('utf-8')
#     print(mydata)





def add_to(x):  
    db = sqlite3.connect("barcodes.db")
    cr = db.cursor()
    cr.execute("create table if not exists medecine_t (medecine_barcode inetger)")
    cr.execute("insert into medecine_t (medecine_barcode) values(?);" , (x,))
    db.commit()
#------------------------------------------------------------------------------


# ap = argparse.ArgumentParser()
# ap.add_argument("-o" , "--output" ,type = str , default ="bara.csv",help = "path to output CSV file containing barcodes")
# args = vars(ap.parse_args())

#open the output csv file
# csv = open(args["output"] , "w")


class webcam1:
    def __init__(self):
        self.buttonclicked = True
        self.cap = cv2.VideoCapture(0)       #to read barcode or qrcode from video taken from webcam
        self.cap.set(3,640)  #setiing the width of the webcam  where 3 refers to width id
        self.cap.set(4,480)  #setiing the height of the webcam  where 4 refers to height id
        self.found = set()
        while self.buttonclicked == True:
            success , vid = self.cap.read()
            for barcode in (decode(vid)):
                self.mydata = (barcode.data.decode('utf-8'))
                #defining the purple rectangle
                pts = np.array([barcode.polygon],np.int32)
                pts = pts.reshape((-1,1,2))
                cv2.polylines(vid , [pts] , True , (255,0,255) , 5)
                #adding the date and time and the barcode into the csv file
                if self.mydata not in self.found:
                    # csv.write("{} , {}\n".format(datetime.datetime.now() , mydata))
                    # csv.flush()
                    self.found.add(self.mydata)
                    add_to(self.mydata)
            cv2.imshow('result' , vid)
            cv2.waitKey(1)

# cam1 = webcam1()