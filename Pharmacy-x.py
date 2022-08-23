from tkinter import *
import sqlite3
from datetime import datetime
from fpdf import FPDF
from tkinter import messagebox
#importing patientclass which contains patient tables and medecine_class for medecine tables and webcam class to scan barcodes
from out_classes import patient_class ,medecine_class,webcam , order








class signinwindow:
    def __init__(self,master):
        self.master = master
#properties of signinwindow:
        self.master.geometry('500x400')
        self.master.title('login window')
        self.master.resizable(False , False)
#widgets:
    #Labels:
        #username_label
        self.username_lb = Label(self.master ,text = 'Username :')
        self.username_lb.place(x = 120 , y = 40)
        #password_label
        self.password_lb = Label(self.master ,text = 'Password :')
        self.password_lb.place(x = 120 , y = 80)
    #entry:
        #username_entry
        self.var1 = StringVar()
        self.username_ent = Entry(self.master , textvariable=self.var1 )
        self.username_ent.place(x = 190 , y = 40)
        #password_entry
        self.var2 = StringVar()
        self.password_ent = Entry(self.master , textvariable=self.var2 , show = '*')
        self.password_ent.place(x = 190 , y = 80)
    #buttons:
        #buttons (signin , signup)
        self.signin_bt = Button(self.master , text = 'Sign in' , command = self.signin_bt_function)
        self.signin_bt.place(x = 280 , y = 130)
        self.signup_bt = Button(self.master , text = 'Sign up' , command = self.signup_bt_function)
        self.signup_bt.place(x = 190 , y = 130)
#functions(signin_bt_function,signup_bt_function):
    def signin_bt_function(self):
        db = sqlite3.connect("pharmacy.db")
        cr = db.cursor()        
        cr.execute("CREATE TABLE IF NOT EXISTS logadmin_t (admin_username text , admin_password text , admin_email text)")
        if self.var1.get() =="" or self.var2.get() =="":
            messagebox.showerror("Error signing in" , "All fields are required")
        else:
            cr.execute("select * from logadmin_t where admin_username = ? and admin_password = ?" , (self.var1.get(),self.var2.get()))
            row = cr.fetchone()
            if row == None:
                messagebox.showerror("Error signing in" , "Username or Password are Wrong")
            else:
                self.master.destroy()    
                self.root3 = Tk()
                mainwindow(self.root3)

    def signup_bt_function(self):           
        self.root2 = Toplevel()
        signupwindow(self.root2)




class signupwindow:
    def __init__ (self,master1):
        self.master1 = master1
    #properties
        self.master1.geometry('500x500')
        self.master1.title("Sign up Window")
    #Widgets
        #labels:
        #enter_username_label
        self.enter_username_lb = Label(self.master1 ,text = 'Enter Username :')
        self.enter_username_lb.place(x = 99 , y = 40)
        #enter_password_label
        self.enter_password_lb = Label(self.master1 ,text = 'Enter Password :')
        self.enter_password_lb.place(x = 100 , y = 80)
        #enter_emailaddress_label
        self.enter_password_lb = Label(self.master1 ,text = 'Enter Email Address:')
        self.enter_password_lb.place(x = 79 , y = 120)

        #entry boxes:
        #enter_username_entry
        self.username_txtvar = StringVar()
        self.enter_username_ent = Entry(self.master1 , textvariable=self.username_txtvar )
        self.enter_username_ent.place(x = 190 , y = 40)
        #enter_password_entry
        self.password_txtvar = StringVar()
        self.enter_password_ent = Entry(self.master1 , textvariable=self.password_txtvar , show = '*')
        self.enter_password_ent.place(x = 190 , y = 80)
        #enter_emailaddress_entry
        self.email_txtvar = StringVar()
        self.enter_emailaddress_ent = Entry(self.master1 , textvariable=self.email_txtvar)
        self.enter_emailaddress_ent.place(x = 190 , y = 120)

        #buttons (submit , backtosignin_bt)
        self.submit_bt = Button(self.master1 , text = 'Submit' , command = self.submit_bt_function)
        self.submit_bt.place(x = 270 , y = 150)
        self.backtosignin_bt = Button(self.master1 , text = 'Back To sign in' , command = self.backtosignin_bt_function)
        self.backtosignin_bt.place(x = 150 , y = 150)
    #Functions of buttons(Backtosignin_function , submit_info_function)
    def backtosignin_bt_function(self):
        self.master1.destroy()
    def submit_bt_function(self):
        db = sqlite3.connect("pharmacy.db")
        cr = db.cursor()        
        cr.execute("CREATE TABLE IF NOT EXISTS logadmin_t (admin_username text , admin_password text , admin_email text)")
        #if the user left an empty fields
        if self.username_txtvar.get() =="" or self.password_txtvar.get() =="" or self.email_txtvar.get() =="":
            messagebox.showerror("Error" , "All Feilds are required to submit !")
        else:
            self.talk_submit_lb = Label(self.master1 ,text = 'You have successfully registered' , fg = "green")
            self.talk1_submit_lb = Label(self.master1 ,text = 'username has been taken' , fg = "red")
            cr.execute("select * from logadmin_t where admin_username  = ? " , (self.username_txtvar.get() , ))
            row = cr.fetchone()
            if row == None:
                cr.execute("insert into logadmin_t(admin_username , admin_password , admin_email) values(?,?,?)" , (self.username_txtvar.get() ,self.password_txtvar.get() , self.email_txtvar.get()))
                db.commit()
                self.enter_username_ent.delete(0,END)
                self.enter_password_ent.delete(0,END)
                self.enter_emailaddress_ent.delete(0,END)
                self.talk_submit_lb.place(x = 140 , y = 180)
            else:
                self.talk1_submit_lb.place(x = 140 , y = 180 )




class mainwindow(patient_class , medecine_class , webcam , order):
    def __init__ (self,master):
        self.master = master
    #properties:
        self.master.geometry('1000x500')
        self.master.resizable(False , False)
        self.master.title('Pharmacy-X')
        self.master.config(bg = 'white')
    #Widgets:
        # Frames
        #Buttons frame 
        self.buttons_frame = Frame(self.master , width = 600 , height = 250 , bg = '#407280' , bd = 8 , relief = RIDGE )
        self.buttons_frame.place(x = 0 , y = 0 )
        #Payment_frame
        self.payment_frame = Frame(self.master,width = 600 , height = 250 , bg = '#407280' , bd = 8 , relief = RIDGE )
        self.payment_frame.place(x =0  , y = 252)
        #Textscreen Frame
        self.textscreen_frame = Frame(self.master,width = 397 , height = 185 , bg = 'white' ,bd = 4, relief = RIDGE )
        self.textscreen_frame.place(x = 602 , y = 108)
        #Dashboard_Frame
        self.dashboard_frame = Frame(self.master,width = 400 , height = 220 , bg = '#407280' , bd = 8 , relief = RIDGE )
        self.dashboard_frame.place(x = 602 , y = 300)

        #Labels :
        #patient phone number
        self.patient_phonenumber_lb = Label(self.payment_frame ,text = 'Enter the patient\'s Phone Number:' ,  bg = '#407280' , fg = 'white' , font = 10)
        self.patient_phonenumber_lb.place(x = 0 , y = 62)
        #medecine barcode
        self.medecine_barcode_lb = Label(self.payment_frame ,text = 'Enter the medecine\'s Barcode:' ,  bg = '#407280' , fg = 'white' , font = 10)
        self.medecine_barcode_lb.place(x = 0 ,y = 15)
        #medical_history label
        self.medical_history_lb =  Label(self.payment_frame ,text = 'Choose from these medical issues if patient suffers from' ,  bg = '#407280' , fg = 'white' , font = 10)
        self.medical_history_lb.place(x = 0, y = 113)
        #label the big title of the window
        self.bigtitle_lb = Label(self.master , text = "Pharmacy-X Management System" , bd = 13 , relief = RIDGE , bg = 'white'  , fg ="darkblue" , font = ('times new roman' , 50 , 'bold') , padx = 2 ,pady = 2 )
        self.bigtitle_lb.pack(side = TOP , fill =X)
        #dashboard patient count lb
        x = self.count_patients()
        self.patient_count_lb = Label(self.dashboard_frame , text = f"The no. of patient's \n registered in \nthe pharmacy is :\n {x} " , bg = '#003f5c' ,width = 20 , height = 5, fg = 'white' , relief = RAISED , bd = 5 , font = ('Helvetica', 11, 'bold'))
        self.patient_count_lb.place(x = 0 , y = 0)
        y = self.count_medicines()
        self.medicines_count_lb = Label(self.dashboard_frame , text = f"The no. of Medincins \n Stored in \nthe pharmacy is :\n {y} " , bg = 'green' ,width = 20 , height = 5, fg = 'white' , relief = RAISED , bd = 5 , font = ('Helvetica', 11, 'bold'))
        self.medicines_count_lb.place(x = 191 , y = 0)
        #quantity of medecine to pay
        self.medecine_quantity_lb = Label(self.payment_frame , text = "Q " , bg = '#407280' , fg = 'white' , font = 10).place(x = 408 , y = 15)
        #dashboard medecine exp date cound and view
        

        #Entry Boxes:
        #search for patient entry box
        self.var1 = IntVar()
        self.var1.set("")
        self.searchforpatient_ent = Entry(self.buttons_frame , textvariable = self.var1 ,  width = 16 , font= 25)
        self.searchforpatient_ent.place(x =52 ,y = 170 )
        #search for medecine entry Box:
        self.var2 = StringVar()
        self.searchformedecine_ent = Entry(self.buttons_frame  , textvariable = self.var2 ,  width = 16 , font= 25)
        self.searchformedecine_ent.place(x =302 ,y = 170 )
        #medecine barcode entry box
        self.var3 = IntVar()
        self.var3.set("")
        self.medecinebarcode_ent = Entry(self.payment_frame ,  textvariable = self.var3 ,  width = 16 , font= 25)
        self.medecinebarcode_ent.place(x =220 ,y = 15 )
        #add_patient phonenumber entry box:
        self.var4 = IntVar()
        self.var4.set("")
        self.patient_phonenumber_ent = Entry(self.payment_frame ,  textvariable = self.var4 ,  width = 16 , font= 25)
        self.patient_phonenumber_ent.place(x =250 ,y = 65 )
        #add_medicine's payment quantity
        self.var7 = IntVar()
        self.var7.set(1.0)
        self.medecines_pay_quantity_ent = Entry(self.payment_frame ,  textvariable = self.var7 ,  width = 3 , font= 25)
        self.medecines_pay_quantity_ent.place(x =425 ,y = 15 )
        #expiary year entery box
        self.var6 = StringVar()
        self.var6.set("<=YY")
        self.exp_year_ent = Entry(self.dashboard_frame , textvariable = self.var6 , width = 5 , font = 25 )
        self.exp_year_ent.place(x = 333 , y = 135)
        #expiary month entery box
        self.var5 = StringVar()
        self.var5.set("<=MM")
        self.exp_month_ent = Entry(self.dashboard_frame , textvariable = self.var5 , width = 5 , font = 25 )
        self.exp_month_ent.place(x = 333, y = 102)
        #option menues
        #medical_history opm:
        self.lisofdis = self.get_contradictions()
        self.lisofdis.append("*Nothing From Above*")
        self.patient_medical_history_opm = StringVar()
        self.patient_medical_history = OptionMenu(self.payment_frame ,self.patient_medical_history_opm,*self.lisofdis)
        self.patient_medical_history.place(x = 400 ,y = 115)
        self.patient_medical_history_opm.set("Choose")

        #buttons :
        #add or remove patient_button
        self.add_remove_patient_bt = Button(self.buttons_frame ,height = 2 , width = 20 ,  text = "Add patient To The Sys" , bg = 'gray'  , fg = 'white' , relief = RAISED , bd = 5 , command = self.addorremovepat_bt_function)
        self.add_remove_patient_bt.place(x = 50 , y = 112)
        #add or remove medicine button :
        self.add_remove_medecine_bt = Button(self.buttons_frame ,height = 2 , width = 20 , text = "Add Medicine To The Sys" , bg = 'gray' , fg = 'white' , relief = RAISED , bd = 5 , command = self.addorremovemed_bt_function)
        self.add_remove_medecine_bt.place(x = 300 , y = 112)
        #search for patient button:
        self.searchforpatient_bt = Button(self.buttons_frame ,height = 1 , width = 9 , text = "Search" , bg = 'gray' , fg = 'white'  , relief = RAISED , bd = 5 , command = self.searchphonepatient_bt_function)
        self.searchforpatient_bt.place(x = 50 , y = 195)
        #remove patient button
        self.removepatient_bt = Button(self.buttons_frame ,height = 1 , width = 9 , text = "Remove" , bg = 'gray' , fg = 'white'  , relief = RAISED , bd = 5  , command = self.remove_patient_bt_function)
        self.removepatient_bt.place(x = 130 , y = 195)
        #search for medecine button:
        self.searchformedecine_bt = Button(self.buttons_frame ,height = 1 , width = 9 , text = "Search" , bg = 'gray' , fg = 'white'  , relief = RAISED , bd = 5 , command = self.searchbarmedecine_bt_function)
        self.searchformedecine_bt.place(x = 300 , y = 195)
        #remove medecine button:
        self.removemedecine_bt = Button(self.buttons_frame ,height = 1 , width = 9 , text = "Remove" , bg = 'gray' , fg = 'white'  , relief = RAISED , bd = 5  , command = self.remove_medecine_bt_function)
        self.removemedecine_bt.place(x = 380 , y = 195)
        #add medecine for payment button:
        self.add_medecineforpayment_bt = Button(self.payment_frame ,height = 2 , width = 17, text = "Place an Order" , bg = 'gray' , fg = 'white'  , relief = RAISED , command = self.add_medecineforpayment_bt_function)
        self.add_medecineforpayment_bt.place(x = 165 , y = 170)
        #make_payment button:
        self.make_payment_bt = Button(self.payment_frame ,height = 2 , width = 17  ,text = "Make a bill" , bg = 'black' , fg = 'white' , relief = RAISED ,command = self.make_payment_bt_function)
        self.make_payment_bt.place(x =320, y = 170)
        #scan barcode button at buttons frame
        self.scanforbarcode_bt = Button(self.buttons_frame ,text = "Scan" , bg = "gray" , relief=  RIDGE , command = self.from_scan_to_ent)
        self.scanforbarcode_bt.place(x = 453 , y = 169)
        #scan barcode button at payment frame
        self.scanforbarcode_bt = Button(self.payment_frame ,text = "Scan" , bg = "gray" , relief=  RIDGE , command = self.from_scan_to_ent_2)
        self.scanforbarcode_bt.place(x = 370 , y = 15)
        #CLEAR TEXTSCREEN_BT
        self.cleartextscreen_bt = Button(self.textscreen_frame, bg = "gray" , text = "Clear" , relief= RIDGE , command = self.clear_screen_bt_function)
        self.cleartextscreen_bt.place(x = 0 , y = 160)
        #Refresh Mainwindow bt
        self.refresh_bt = Button(self.dashboard_frame , text = "Refresh" , command = self.refresh_bt_function , bg = "green" , fg = 'white')
        self.refresh_bt.place(x = 332 ,y = 170)
        #print bill BT
        self.save_bt = Button(self.textscreen_frame , text = "Print"  , command = self.print_bt_func  ,bg = "gray" , fg = "black" , relief = RIDGE )
        self.save_bt.place(x = 50 , y = 160)
        #mediines exp year BT
        self.medicine_exp_bt = Button(self.dashboard_frame , text = "search expiry Year" , fg = "white" , bg = 'red' , relief = RAISED , bd = 4 , font = ('Helvetica', 11, 'bold') ,width = 17 , height = 4, command = self.medecine_expyear_print_bt)
        self.medicine_exp_bt.place(x = 0 , y = 100)
        #mediines exp month BT
        self.medicine_exp_bt = Button(self.dashboard_frame , text = "search expiry Month" , fg = "white" , bg = 'red' , relief = RAISED , bd = 4 , font = ('Helvetica', 11, 'bold') ,width = 17 , height = 4, command = self.medecine_expmonth_print_bt)
        self.medicine_exp_bt.place(x = 167 , y = 100)
        # #Text area 
        self.textarea = Text(self.textscreen_frame , height = 10, width = 55 , state = 'normal' , font = ("Helvetica", 10, "bold") )
        self.textarea.place(x = 0, y = 0)
    #funcions:  
    def addorremovepat_bt_function(self):
        self.root4 = Toplevel()
        add_remvove_patient_window(self.root4)
    def addorremovemed_bt_function(self):
        self.root5 = Toplevel()
        add_remvove_medecine_window(self.root5)
    def searchbarmedecine_bt_function(self):
        self.medbarcode = self.searchformedecine_ent.get()
        if self.medbarcode.isalpha():
            #using the inherited function from class medecine
            self.foundmedecine = self.searchformedecine(self.medbarcode)
            for x in range(len(self.foundmedecine[0])):
                self.textarea.insert(END,f"Name:     {self.foundmedecine[0][x][0]}\n")
                self.textarea.insert(END,f"Barcode :   {self.foundmedecine[0][x][1]}\n")
                self.textarea.insert(END,f"Expiary Date :   {self.foundmedecine[0][x][2]}\n")
                self.textarea.insert(END,f"Cost :   {self.foundmedecine[0][x][3]}\n")
                self.textarea.insert(END,f"Quantity :       {self.foundmedecine[0][x][4]}\n")
                self.textarea.insert(END,f"Contradictions :   {self.foundmedecine[0][x][5]}\n =================================\n")
            self.textarea.insert(END,f"   *Total Quantity of {self.foundmedecine[0][0][0]} ,      is : {self.foundmedecine[1]}*")
            self.searchformedecine_ent.delete(0,END)

        elif self.medbarcode.isnumeric():
            self.foundmedecine = self.searchformedecine_bybar(self.medbarcode)
            for x in range(len(self.foundmedecine[0])):
                self.textarea.insert(END,f"Name:     {self.foundmedecine[0][x][0]}\n")
                self.textarea.insert(END,f"Barcode :   {self.foundmedecine[0][x][1]}\n")
                self.textarea.insert(END,f"Expiary Date :   {self.foundmedecine[0][x][2]}\n")
                self.textarea.insert(END,f"Cost :   {self.foundmedecine[0][x][3]}\n")
                self.textarea.insert(END,f"Quantity :       {self.foundmedecine[0][x][4]}\n")
                self.textarea.insert(END,f"Contradictions :   {self.foundmedecine[0][x][5]}\n =================================\n")
            self.textarea.insert(END,f"   *Total Quantity of {self.foundmedecine[0][0][0]} is :  {self.foundmedecine[1]}*")
            self.searchformedecine_ent.delete(0,END)

        else:
            #using the inherited function from class medecine
            self.foundmedecine = self.searchformedecine(self.medbarcode)
            for x in range(len(self.foundmedecine[0])):
                self.textarea.insert(END,f"Name:     {self.foundmedecine[0][x][0]}\n")
                self.textarea.insert(END,f"Barcode :   {self.foundmedecine[0][x][1]}\n")
                self.textarea.insert(END,f"Expiary Date :   {self.foundmedecine[0][x][2]}\n")
                self.textarea.insert(END,f"Cost :   {self.foundmedecine[0][x][3]}\n")
                self.textarea.insert(END,f"Quantity :       {self.foundmedecine[0][x][4]}\n")
                self.textarea.insert(END,f"Contradictions :   {self.foundmedecine[0][x][5]}\n =================================\n")
            self.textarea.insert(END,f"   *Total Quantity of {self.foundmedecine[0][0][0]} ,      is : {self.foundmedecine[1]}*")
            self.searchformedecine_ent.delete(0,END)
        # talklabel1 = Label(self.textscreen_frame , text = f"Medicine's Name is : {self.foundmedecine[0]}\nMedecine's Barcode is: {self.foundmedecine[1]}\nExpiary Date : {self.foundmedecine[2]} \nCost : {self.foundmedecine[3]}\nQunatity : {self.foundmedecine[4]} \nContradictions : {self.foundmedecine[5]} " , bg = 'white' , bd  = 0)
        # talklabel1.pack()
    def searchphonepatient_bt_function(self):
        self.medbarcode = self.searchforpatient_ent.get()
        #using the inherited function from class medecine
        self.foundmedecine = self.searchforpatient(self.medbarcode)
        self.textarea.insert(END,f"Name:     {self.foundmedecine[0]}\n")
        self.textarea.insert(END,f"Phone Number :   {self.foundmedecine[1]}\n")
        self.textarea.insert(END,f"Gender :   {self.foundmedecine[2]}\n")
        self.textarea.insert(END,f"Age :   {self.foundmedecine[3]}\n")
        self.searchforpatient_ent.delete(0,END)
    def remove_patient_bt_function(self):
        self.remove_patients(self.searchforpatient_ent.get())
        self.textarea.insert(END,f"The Patient with phonenumber{self.searchforpatient_ent.get()} ,\nHas been removed succesfully ")
    def remove_medecine_bt_function(self):
        x = self.searchformedecine_ent.get()
        if x.isalpha():    
            self.remove_medecine(x)
            self.textarea.insert(END,f"{self.searchformedecine_ent.get()} Has been removed succesfully " )
        elif x.isnumeric():
            self.remove_medecine_bybar(x)
            self.textarea.insert(END,f"Medicine With barcode : {self.searchformedecine_ent.get()} Has been removed succesfully " )
        else:
            self.remove_medecine(x)
            self.textarea.insert(END,f"{self.searchformedecine_ent.get()} Has been removed succesfully " )
    def make_payment_bt_function(self):
        self.ret = self.get_billinfo(self.patient_phonenumber_ent.get())
        self.textarea.insert(END,f"-Patient Name:  {self.ret[0][0][0]}\n") #contsatnt
        for self.i in range(len(self.ret[0])):
            self.textarea.insert(END,f"\n-Medicine Name :  {self.ret[0][self.i][1]}\n")
            self.textarea.insert(END , f"-Medicine Quantity :  {self.ret[0][self.i][3]}\n")
            self.textarea.insert(END,f" -Cost per one :  {self.ret[0][self.i][2]}\n------------------------------------------------")
            if self.patient_medical_history_opm.get() == self.ret[0][self.i][4] and self.patient_medical_history_opm.get() != "" and self.patient_medical_history_opm.get() != "None" and self.patient_medical_history_opm.get() != None:
                self.textarea.insert(END, f"\n-becarefull : {self.ret[0][self.i][1]} Medicine \n contradicts With {self.ret[0][self.i][4]} Patients\n")        
        self.textarea.insert(END,f"\n**The Total cost is  :   {self.ret[1]}**\n")#constant
        self.update_medecinetable(self.barcode)
        # self.update_medecinetable(self.record[3] , self.barcode)
        self.delete_all()
    def add_medecineforpayment_bt_function(self):
        self.barcode = self.medecinebarcode_ent.get()
        phonenumber = self.patient_phonenumber_ent.get()
        medical_history = self.patient_medical_history_opm.get()
        #A condition to compare patient's medical history with the medicine's contradicts
        if medical_history in self.get_spacefic_contra(self.barcode):
            check = messagebox.askquestion("Becarfull" , f"This medicine contradicts with {medical_history} Patients\nWould You Like to Continue?")
            if check == "no":
                return
        medecine_quantity = self.medecines_pay_quantity_ent.get()
        self.addmedtobill(self.barcode , medecine_quantity ,  phonenumber , medical_history)
        self.medecinebarcode_ent.delete(0,END)
    def refresh_bt_function(self):
        self.master.destroy() #destroy the old window   
        y = Tk()  #instantiate an object from Tk class to give a window
        mainwindow(y)   # assign the tk object to as an attribute to the main window class in order to give the window all the mainwindow funcs atributes....
    def print_bt_func(self):
        pdf = FPDF('P' ,'mm' , (100 ,125))
        pdf.add_page()
        pdf.set_font("Arial", size = 10)
        self.x = self.textarea.get(1.0 , END).splitlines()
        pdf.cell(200,10 , txt = '---------------------------------------------------', ln = 1, align = 'L')
        for self.line in self.x :
            pdf.cell(200, 10, txt = self.line, ln = 1, align = 'L')
        pdf.cell(200,10 , txt = '---------------------------------------------------', ln = 1, align = 'L')
        pdf.output("bill.pdf")
    def from_scan_to_ent(self):
        self.ret = self.scan()
        self.searchformedecine_ent.insert(0,self.ret)
    def from_scan_to_ent_2(self):
        self.ret1 = self.scan()
        self.medecinebarcode_ent.insert(0,self.ret1)
    def clear_screen_bt_function(self):
        self.textarea.delete(1.0,END)
    def medecine_expyear_print_bt(self):
        today = datetime.today()
        z = today.timetuple()
        self.curr_date_list = (z[1] , z[0])
        for year in self.exp_years():
            if year[0] <=int(self.var6.get()):
                self.textarea.insert(END,f"Name :    {year[1]}")
                self.textarea.insert(END,f"  ,    Remained Years :    {year[0]}\n")
        self.exp_year_ent.delete(0,END)
    def medecine_expmonth_print_bt(self):
        today = datetime.today()
        z = today.timetuple()
        self.curr_date_list = (z[1] , z[0])
        self.exp_years()
        for month in self.exp_monthes():
            if month[0] <= int(self.var5.get()):
                self.textarea.insert(END,f"Name :    {month[1]}")
                self.textarea.insert(END,f"  ,    Remained Months :    {month[0]}\n")
        self.exp_month_ent.delete(0,END)




class add_remvove_patient_window(patient_class) :
    def __init__(self,master):
        self.master = master
    #properties:
        self.master.geometry("500x500")
        self.master.resizable(False , False)
    #Widgets:
        #labels
        self.patient_name_lb = Label(self.master , text = "Enter the Patient's name:",font = ('bold' , 10))
        self.patient_name_lb.place(x = 0 , y = 20)
        self.patient_phonenumber_lb = Label(self.master , text = "Enter the Patient's phone number:",font = ('bold' , 10))
        self.patient_phonenumber_lb.place(x = 0 , y = 70)
        self.patient_age_lb = Label(self.master , text = "Enter the Patient's Age:",font = ('bold' , 10))
        self.patient_age_lb.place(x = 0 , y = 120)
        self.patient_gender_lb = Label(self.master , text = "Choose the Patient's gender:",font = ('bold' , 10))
        self.patient_gender_lb.place(x = 0 , y = 170)

        #Entry boxes:
        #patient_name_ent
        self.v1 = StringVar()
        self.patient_name_ent = Entry(self.master ,textvariable=self.v1 , relief = RIDGE , bd =3 , font = 30)
        self.patient_name_ent.place(x = 150 , y = 20)
        #patient_phonenumber_ent
        self.v2 = IntVar()
        self.v2.set("")
        self.patient_phonenumber_ent = Entry(self.master ,textvariable=self.v2 , relief = RIDGE , bd = 3 , font=  30)
        self.patient_phonenumber_ent.place(x = 200 , y = 70)
        #patient_age_ent
        self.v3 = IntVar()
        self.v3.set("")
        self.patient_age_ent = Entry(self.master ,textvariable=self.v3 , relief = RIDGE , bd = 3 , font=  30)
        self.patient_age_ent.place(x = 160 , y = 120)
    
        #dropdown menus:
        self.v4 = StringVar() 
        self.v4.set("Choose gender")
        self.patient_gender_optionmenu = OptionMenu(self.master ,self.v4 , "Male" , "Female")
        self.patient_gender_optionmenu.place(x = 172 , y = 164)

        #buttons
        self.add_patient_data_bt = Button(self.master , text = "Add"  , bd = 4 , relief = RAISED , width = 10 , command  = self.getfromENTandsendtoDB_bt_funcion )
        self.add_patient_data_bt.place(x = 200 , y = 225)


    #funcions:
    def getfromENTandsendtoDB_bt_funcion(self):
        name = self.v1.get()
        phonenumber = self.patient_phonenumber_ent.get()
        age = self.v3.get()
        gender  = self.v4.get()
        self.addpatient_info(name, phonenumber, gender, age)
        confirmlabel = Label(self.master , text ="Patient have been added succefully" , fg = "green" )
        confirmlabel.place(x =160 , y = 280 )
        self.patient_name_ent.delete(0,END)
        self.patient_phonenumber_ent.delete(0,END)
        self.patient_age_ent.delete(0,END)
        



class add_remvove_medecine_window(mainwindow):#to inherit from medecine_class , main window together as mainwindow class already inherited from medecine_class
    def __init__(self,master):
        self.master = master
    #properties:
        self.master.geometry("500x500")
        self.master.resizable(False , False)
        
    #Widgets:
        #labels
        self.medecine_name_lb = Label(self.master , text = "Enter the Medecine's name:",font = ('bold' , 10))
        self.medecine_name_lb.place(x = 0 , y = 20)
        self.medecine_barcode_lb = Label(self.master , text = "Enter the Medecine's barcode :",font = ('bold' , 10))
        self.medecine_barcode_lb.place(x = 0 , y = 70)
        self.medecine_expdate_lb = Label(self.master , text = "Enter the Medecine's expiary Date:",font = ('bold' , 10))
        self.medecine_expdate_lb.place(x = 0 , y = 120)
        self.medecine_cost_lb = Label(self.master , text = "Enter the Medecine's Cost:",font = ('bold' , 10))
        self.medecine_cost_lb.place(x = 0 , y = 170)
        self.medecine_quantity_lb = Label(self.master , text = "Enter the Medecine's quantity:",font = ('bold' , 10))
        self.medecine_quantity_lb.place(x = 0 , y = 220)
        self.medecine_contradictions_lb = Label(self.master , text = "Enter the Medecine's contradictions:",font = ('bold' , 10))
        self.medecine_contradictions_lb.place(x = 0 , y = 270)
        

        #Entry boxes:
        #medecine_name_ent
        self.medecine_name_ent = Entry(self.master , relief = RIDGE , bd = 3 , font = 30)
        self.medecine_name_ent.place(x = 180 , y = 20)
        #medecine_barcode_ent
        self.medecine_barcode_ent = Entry(self.master , relief = RIDGE , bd = 3 , font=  30)
        self.medecine_barcode_ent.place(x = 180, y = 70)
        #medecine_expiary date_ent
        self.medecine_expdate_ent = Entry(self.master , relief = RIDGE , bd = 3 , font=  30)
        self.medecine_expdate_ent.place(x = 210 , y = 120)
        self.medecine_expdate_ent.insert(0 , "Y0000-M00")
        #medecine cost
        self.medecine_cost_ent = Entry(self.master , relief = RIDGE , bd = 3 , font=  30)
        self.medecine_cost_ent.place(x = 180 , y = 170)
        #medecine quantity
        self.medecine_quantity_ent = Entry(self.master , relief = RIDGE , bd = 3 , font=  30)
        self.medecine_quantity_ent.place(x = 180 , y = 220)
        #medecine contradictions
        self.medecine_contradictions_ent = Entry(self.master , relief = RIDGE , bd = 3 , font=  30)
        self.medecine_contradictions_ent.place(x = 220 , y = 270)
        self.medecine_contradictions_ent.insert(0, "if no leave empty")

        #buttons
        self.add_medecine_data_bt = Button(self.master , text = "Add"  , bd = 4 , relief = RAISED , width = 10 , command = self.add_medecineinfo_bt_functions )
        self.add_medecine_data_bt.place(x = 200 , y = 300)
        #class scan and add bt
        self.scanforbarcode2_bt = Button(self.master , text = "Scan" ,bd = 4 ,  relief = RIDGE , bg = "gray" ,command =self.from_scan_to_ent )
        self.scanforbarcode2_bt.place(x = 380 , y = 70)
        
    #functions
    def add_medecineinfo_bt_functions(self):
        name = self.medecine_name_ent.get()
        barcode = self.medecine_barcode_ent.get()
        expiarydate = self.medecine_expdate_ent.get()
        cost = self.medecine_cost_ent.get()
        quantity = self.medecine_quantity_ent.get()
        if self.medecine_contradictions_ent.get() == "if no leave empty": #to prevent adding the default text if there is no contradictions to the DB
            contradictions = " "
        else:
            contradictions = self.medecine_contradictions_ent.get()
        if expiarydate == " " or expiarydate == "NULL" or len(expiarydate) !=7 or expiarydate == "Y0000-M00":
            messagebox.showerror("Validation Error !","Please enter a valid Date")
        else: 
            self.addmedecine_info(name,barcode,expiarydate,cost,quantity,contradictions)
            confirmlabel = Label(self.master , text ="Medecine have been added succefully" , fg = "green" )
            confirmlabel.place(x =190 , y = 340 )
            self.medecine_name_ent.delete(0,END)
            self.medecine_barcode_ent.delete(0,END)
            self.medecine_expdate_ent.delete(0,END)
            self.medecine_cost_ent.delete(0,END)
            self.medecine_quantity_ent.delete(0,END)
            self.medecine_contradictions_ent.delete(0,END)
        
        #inherting it from maincwindow class and from webcam class which is inherited by mainwindow class
    def from_scan_to_ent(self):
        self.ret = self.scan()
        self.medecine_barcode_ent.insert(0,self.ret)









# db.commit()
# db.close()

def main():
    root1 = Tk()
    app = signinwindow(root1)
    root1.mainloop()
if __name__ == '__main__':
    main()