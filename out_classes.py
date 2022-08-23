from tkinter import *
import sqlite3
from tkinter import messagebox
import cv2
import numpy as np
from pyzbar.pyzbar import decode
from datetime import datetime





class medecine_class:
    def __init__(self):
        self.db = sqlite3.connect("pharmacy.db")
        self.cr = self.db.cursor()
        self.cr.execute("create table if not exists medecine_t (medecine_name text, medecine_barcode integer , medecine_expdate date, medecine_cost float , medecine_quantity integer , medecine_contradictions text )")
        today = datetime.today()
        x = today.timetuple()
        self.curr_date_list = (x[1] , x[0])
    def addmedecine_info(self, a , b , c , d , e , f):
        self.db = sqlite3.connect("pharmacy.db")
        self.cr = self.db.cursor()
        self.cr.execute("create table if not exists medecine_t (medecine_name text, medecine_barcode integer, medecine_expdate date, medecine_cost float , medecine_quantity integer , medecine_contradictions text)")
        self.cr.execute("insert into medecine_t (medecine_name, medecine_barcode, medecine_expdate , medecine_cost, medecine_quantity , medecine_contradictions ) values (?,?,?,?,?,?)" , (a , b , c , d , e , f))
        self.db.commit()
        self.db.close()

    def searchformedecine(self,x):
        self.db = sqlite3.connect("pharmacy.db")
        self.cr = self.db.cursor()
        self.r = self.cr.execute("select * from medecine_t where medecine_name = ?" , (x,))
        self.mednamerec = self.r.fetchall() #a tuple of the returned values
        if self.mednamerec == []:
            messagebox.showinfo("INFO" , "This medicine cannot be found")
        else:
            self.sumofdublicates = 0
            count = 0
            for record in self.mednamerec:
                count+=1
                if count > 0:
                    self.sumofdublicates += record[4]
                else:
                    self.sumofdublicates = record[4]
                self.db.commit()     
        return self.mednamerec , self.sumofdublicates
    def searchformedecine_bybar(self,x):
        self.db = sqlite3.connect("pharmacy.db")
        self.cr = self.db.cursor()
        self.r = self.cr.execute("select * from medecine_t where medecine_barcode = ?" , (x,))
        self.medbarrec = self.r.fetchall() #a tuple of the returned values
        if self.medbarrec == []:
            messagebox.showinfo("INFO" , "This medicine cannot be found")
        else:
            self.sumofdublicates = 0
            count = 0
            for record in self.medbarrec:
                count+=1
                if count > 0:
                    self.sumofdublicates += record[4]
                else:
                    self.sumofdublicates = record[4]
                self.db.commit()
        return self.medbarrec , self.sumofdublicates
    def remove_medecine(self , x):
        self.db = sqlite3.connect("pharmacy.db")
        self.cr = self.db.cursor()
        self.cr.execute("delete from medecine_t where medecine_name = ?" , (x,))
        self.db.commit()
        self.db.close()
    def remove_medecine_bybar(self , x):
        self.db = sqlite3.connect("pharmacy.db")
        self.cr = self.db.cursor()
        self.cr.execute("delete from medecine_t where medecine_barcode = ?" , (x,))
        self.db.commit()
        self.db.close()
    def count_medicines(self):
        self.db = sqlite3.connect("pharmacy.db")
        self.cr = self.db.cursor()
        self.cr.execute("select medecine_name from medecine_t")
        self.db.commit()
        return len(self.cr.fetchall())
    #gets all medicine's contradictions 
    def get_contradictions(self):
        r = self.cr.execute("select medecine_contradictions from medecine_t")
        records = r.fetchall()
        list_of_diseases = []
        for k,record in enumerate(records):
            if record[0] == 'Null' or record[0] == 'No' or record[0] == '':
                continue
            else:
                list_of_diseases.append(record[0])
                list_of_diseases  = sorted(set(list_of_diseases))  #to remove the duplicates and sort func to sort it alphabitically
        return list_of_diseases
    #gets contradiction for a spacefic medicine according to its barcode
    def get_spacefic_contra(self , x):
        r = self.cr.execute("select medecine_contradictions from medecine_t where medecine_barcode = ?" ,(x,))
        return r.fetchone()
    def exp_years(self):
        db = sqlite3.connect("pharmacy.db")
        cr = db.cursor()
        self.result_list =[]
        for date in cr.execute("SELECT medecine_expdate , medecine_name from medecine_t"): 
            self.result = [date[0][6],date[0][0:4] ,date[1]]
            self.result[0] = int(self.result[0])
            self.result[1] = int(self.result[1])
            self.result_list.append(self.result)
        self.yeardiff_list = []
        self.year_month_diff = []
        for k,result in enumerate(self.result_list):
            x = [result[1] - self.curr_date_list[1] ,self.result_list[k][2]]
            self.yeardiff_list.append(x)
            self.year_month_diff.append(x[0]*12)    
        db.commit()
        db.close()
        return self.yeardiff_list
    def exp_monthes(self):
        self.final_result_all = []
        k = 0
        for k,year in enumerate(self.year_month_diff):
            self.final_result_all.append([year + self.result_list[k][0] , self.result_list[k][2]])
        return self.final_result_all

class patient_class:
    def __init__(self):
        self.db = sqlite3.connect("pharmacy.db")
        self.cr = self.db.cursor()
        self.cr.execute("create table if not exists patient_t (patient_name text, patient_phonenumber  integer PRIMARY KEY, patient_age integer , patient_gender text )")
    def addpatient_info(self , a , b , c , d):
        self.db = sqlite3.connect("pharmacy.db")
        self.cr = self.db.cursor()
        self.cr.execute("create table if not exists patient_t (patient_name text, patient_phonenumber  integer PRIMARY KEY ,    patient_age integer , patient_gender text )")
        self.cr.execute("insert into patient_t (patient_name , patient_phonenumber , patient_age , patient_gender) values(?,?,?,?)" , (a ,b ,c , d))
        self.db.commit()
        self.db.close()
    def searchforpatient(self,x):
        self.db = sqlite3.connect("pharmacy.db")
        self.cr = self.db.cursor()
        r = self.cr.execute("select * from patient_t where patient_phonenumber = ? " , (x,))
        self.patnamerec = r.fetchone()
        if self.patnamerec ==None:
            messagebox.showinfo("Info" , "This patient Cannot be Found")
        else:
            self.db.commit()
            self.db.close()
            return self.patnamerec
    def remove_patients(self , x):
        self.db = sqlite3.connect("pharmacy.db")
        self.cr = self.db.cursor()
        self.cr.execute("delete from patient_t where patient_phonenumber = ?" , (x,))
        self.db.commit()
        self.db.close()
    def count_patients(self):
        self.db = sqlite3.connect("pharmacy.db")
        self.cr = self.db.cursor()
        self.cr.execute("select patient_name from patient_t")
        self.db.commit()
        return len(self.cr.fetchall())




class webcam:
    # def __init__(self):
    def scan(self):
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
                    # self.add_to(self.mydata)
                    return self.mydata
                    
            cv2.imshow('result' , vid)
            cv2.waitKey(1)

    # def add_to(self,x):  
    #     db = sqlite3.connect("barcodes.db")
    #     cr = db.cursor()
    #     cr.execute("create table if not exists medecine_t (medecine_barcode inetger)")
    #     cr.execute("insert into medecine_t (medecine_barcode) values(?);" , (x,))
    #     db.commit()


class order():
    def __init__(self):
        self.db = sqlite3.connect("pharmacy.db")
        self.cr = self.db.cursor()
        self.cr.execute("create table if not exists order_t (order_id integer IDENTITY(1,1) primary key, order_quantity integer , patient_phonenumber integer ,medecine_barcode integer , patient_medical_issue text , foreign key(patient_phonenumber) references patient_t(patient_phonenumber) , foreign key (medecine_barcode) references medecine_t (medecine_barcode))")
        self.db.commit()

        #function adds the payment info into order_t
    def addmedtobill(self , x , t , y , z ):
        self.db = sqlite3.connect("pharmacy.db")
        self.cr = self.db.cursor()
        self.cr.execute("create table if not exists order_t (order_id integer primary key AUTOINCREMENT , order_quantity integer, patient_phonenumber integer ,medecine_barcode integer , patient_medical_issue text , foreign key(patient_phonenumber) references patient_t(patient_phonenumber) )")
        self.cr.execute("insert into order_t (medecine_barcode ,order_quantity, patient_phonenumber , patient_medical_issue) values (?,?,?,?)" , (x,t,y,z))
        self.db.commit()
        #function gets the info from the order_t and joins it with medecine table and patient_t in order to make a full bill
    def get_billinfo(self , phone):
        self.db = sqlite3.connect("pharmacy.db")
        self.cr = self.db.cursor()
        self.cr.execute("create table if not exists order_t (order_id integer primary key AUTOINCREMENT ,order_cost float, order_quantity integer , patient_phonenumber integer ,medecine_barcode integer , patient_medical_issue text , foreign key(patient_phonenumber) references patient_t(patient_phonenumber) )")
        x = self.cr.execute("select patient_name ,  medecine_name , medecine_cost  ,order_quantity , medecine_contradictions from patient_t , medecine_t , order_t where patient_t.patient_phonenumber = order_t.patient_phonenumber and  medecine_t.medecine_barcode = order_t.medecine_barcode  and patient_t.patient_phonenumber = ?",(phone, ))  ###############
        records = list(set(x.fetchall()))
        self.db.commit()
        costofall = 0
        for self.record in records:
            costofall+=self.record[2] *self.record[3]
        return records , costofall

    #function to update the quantity of a certain medicine after a payment order  
    def update_medecinetable(self,y):
        self.cr.execute(f"update medecine_t set medecine_quantity  = medecine_quantity - {self.record[3]}  where medecine_barcode = ? ",(y,))
        self.db.commit()
    # function to remove all the data from order  to make it ready for a new paymernt order
    def delete_all(self):
        self.cr.execute("delete from order_t;")
        self.db.commit()

class payment_history:
    def __init__ (self):
        self.db = sqlite3.connect("pharmacy.db")
        self.cr = self.db.cursor()
        self.cr.execute("create table if not exists payment_history_t ( payment_date datetime , foreign key (order_id) references order_t (order_id))")
        self.db.commit()
    
    def get_from_order(self):
        self.db = sqlite3.connect("pharmacy.db")
        self.cr = self.db.cursor()
        self.cr.execute("create table if not exists payment_history_t ( payment_date datetime , foreign key (order_id) references order_t (order_id))")
        self.cr.execute("insert into payment_history_t (payment_date) values()")
        self.db.commit()


