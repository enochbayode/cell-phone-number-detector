import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import time

gui = tk.Tk()
gui.geometry('1200x705')
gui.title("Phone Number App")
#gui.resizable(0,0)

# F1 is the top frame
F1 = tk.Frame(gui)
F1.grid()

#creating the background image
image = Image.open("Phone number detector.jpg")
photo = ImageTk.PhotoImage(image)
lbl = ttk.Label(F1, image=photo)
lbl.grid()

def Enter():

    mat = r.get()
    
    if mat == 1:

        #conditional statements for telephone numbers in the format of 090.../081.../070... etc
        Tel = num.get() #getting the value of num by using the .get() method 
        list(Tel) # Turning Tel into a list
        len(Tel)  # counting Tel using len()
        x = len(Tel) # assigning the numbers of Tel to the variable x
        x = 11 # giving the x a value which is equal to len(Tel)

                
        if x == len(Tel): # conditional statement for len(Tel) to be eqaul to the value of x

            if Tel[:4] == "0803" or Tel[:4] == "0703" or Tel[:4] == "0903" or Tel[:4] == "0806" or Tel[:4] == "0706"\
                or Tel[:4] == "0813" or Tel[:4] == "0810" or Tel[:4] == "0814" or Tel[:4] == "0816" or Tel[:4] == "0906" :
                lbl1 = tk.Label(F1,text="This is a MTN NG number",bg='yellow',fg='blue',width=40,
                                 font=('monotype corsiva',30,'bold')) # conditional statement for MTN NG
                lbl1.place(x=250, y=600)
                
            elif Tel[:4] == "0705" or Tel[:4] == "0905" or Tel[:4] == "0807" or Tel[:4] == "0815" \
                or Tel[:4] == "0811" or Tel[:4] == "0905" or Tel[:4] == "0805":
                lbl2 = tk.Label(F1,text="This is a Glo NG number",bg='green',fg='white',width=40,
                               font=('monotype corsiva',30,'bold'))   # conditional statement for glo NG
                lbl2.place(x=250, y=600)
                  
            elif Tel[:4] == "0909" or Tel[:4] == "0817" or Tel[:4] == "0818" or Tel[:4] == "0908" or Tel[:4] == "0809" :
                lbl3 = tk.Label(F1,text="This is an Etisalat NG number",bg='green',fg='white',width=40,
                               font=('monotype corsiva',30,'bold')) # conditional statement for Etisalat NG
                lbl3.place(x=250, y=600)
                
            elif Tel[:4] == "0902" or Tel[:4] == "0701" or Tel[:4] == "0808" or Tel[:4] == "0812" \
                or Tel[:4] == "0802" or Tel[:4] == "0708" or Tel[:4] == "0907":
                lbl4 = tk.Label(F1,text="This is an Airtel NG number",bg='red',fg='white',width=40,
                               font=('monotype corsiva',30,'bold')) # conditional statement for Airtel NG
                lbl4.place(x=250, y=600)
                
            elif Tel[:4] == "0819" or Tel[:5] == "07028" or Tel[:5] == "07029" :
                lbl5 = tk.Label(F1,text="This is Starcomm NG number",bg='blue',fg='yellow',width=40,
                               font=('monotype corsiva',30,'bold')) # conditional statement for Starcomm
                lbl5.place(x=250, y=600)

            elif Tel[:4] == "0709" or Tel[:5] == "07029" :
                lbl6 = tk.Label(F1,text="This is a Multilink NG number",bg='indigo',fg='white',width=40,
                               font=('monotype corsiva',30,'bold')) # conditional statement for Multilink
                lbl6.place(x=250, y=600)

            elif Tel[:4] == "0704" or Tel[:5] == "07025" or Tel[:5] == "07026" :
                lbl7 = tk.Label(F1,text="This is a Visafone NG number",bg='pink',fg='white',width=40,
                               font=('monotype corsiva',30,'bold'))# conditional statement for Visafone
                lbl7.place(x=250, y=600)

            elif Tel[:4] == "0707" :
                lbl8 = tk.Label(F1,text="This is a Zoom mobile NG number",bg='indigo',fg='blue',width=40,
                               font=('monotype corsiva',30,'bold')) # conditional statement for Zoom mobile
                lbl8.place(x=250, y=600)

            elif Tel[:4] == "0804" :
                lbl9 = tk.Label(F1,text="This is a MTEL NG number",bg='lightgreen',fg='white',width=40,
                               font=('monotype corsiva',30,'bold'))  # conditional statement for MTEL
                lbl9.place(x=250, y=600)

            elif len(Tel[:4]) == 0:
                lbl12 = tk.Label(F1,text="The textbox is still empty",bg='lightgreen',fg='white',width=40,
                               font=('monotype corsiva',30,'bold'))  # conditional statement for MTEL
                lbl12.place(x=250, y=600)


            else:
                lbl10 = tk.Label(F1,text="Invalid phone number",bg='red',fg='white',width=40,
                              font=('monotype corsiva',30,'bold'))
                lbl10.place(x=250, y=600)

        else:
            lbl11 = tk.Label(F1,text="Phone number is greater than or less than 11",bg='red',fg='white',width=40,
                              font=('monotype corsiva',30,'bold'))
            lbl11.place(x=250, y=600)

    elif mat == 2:

        # conditional statements for telephone numbers in the format of +23490.../+23481... etc
        Tel = num.get() #getting the value of num by using the .get() method 
        list(Tel) # Turning Tel into a list
        len(Tel) # counting Tel using len()
        g = len(Tel) # assigning the numbers of Tel to the variable g
        g = 14 # giving the g a value which is equal to len(Tel)


        if g == len(Tel): # conditional statement for len(Tel) to be eqaul to the value of g

           if Tel[:7] == "+234803" or Tel[:7] == "+234703" or Tel[:7] == "+234903" or Tel[:7] == "+234806"\
              or Tel[:7] == "+234706" or Tel[:7] == "+234813" or Tel[:7] == "+234810"\
              or Tel[:7] == "+234814" or Tel[:7] == "+234816" :
              lbl1 = tk.Label(F1,text="This is a MTN NG number",bg='yellow',fg='blue',width=40,
                                 font=('monotype corsiva',30,'bold')) # conditional statement for MTN NG
              lbl1.place(x=250, y=600)   
              
            
           elif Tel[:7] == "+234705" or Tel[:7] == "+234905" or Tel[:7] == "+234807" or Tel[:7] == "+234815" \
              or Tel[:7] == "+234811" or Tel[:7] == "+234905" or Tel[:7] == "+234805":
              lbl2 = tk.Label(F1,text="This is a Glo NG number",bg='green',fg='white',width=40,
                               font=('monotype corsiva',30,'bold'))   # conditional statement for glo NG
              lbl2.place(x=250, y=600)
            
           elif Tel[:7] == "+234909" or Tel[:7] == "+234817" or Tel[:7] == "+234818" or Tel[:7] == "+234908" \
              or Tel[:7] == "+234809" :
              lbl3 = tk.Label(F1,text="This is an Etisalat NG number",bg='green',fg='white',width=40,
                               font=('monotype corsiva',30,'bold')) # conditional statement for Etisalat NG
              lbl3.place(x=250, y=600)
            
           elif Tel[:7] == "+234902" or Tel[:7] == "+234701" or Tel[:7] == "+234808" or Tel[:7] == "+234812" \
              or Tel[:7] == "+234802" or Tel[:7] == "+234708" or Tel[:7] == "+234907":
              lbl4 = tk.Label(F1,text="This is an Airtel NG number",bg='red',fg='white',width=40,
                               font=('monotype corsiva',30,'bold')) # conditional statement for Airtel NG
              lbl4.place(x=250, y=600)

           elif Tel[:7] == "+234819" or Tel[:8] == "+2347028" or Tel[:8] == "+2347029":
               lbl5 = tk.Label(F1,text="This is Starcomm NG number",bg='blue',fg='yellow',width=40,
                               font=('monotype corsiva',30,'bold')) # conditional statement for Starcomm
               lbl5.place(x=250, y=600)
              
           elif Tel[:7] == "+234709" or Tel[:8] == "+2347029" :
               lbl6 = tk.Label(F1,text="This is a Multilink NG number",bg='indigo',fg='white',width=40,
                               font=('monotype corsiva',30,'bold')) # conditional statement for Multilink
               lbl6.place(x=250, y=600)

           elif Tel[:7] == "+234704" or Tel[:8] == "+2347025" or Tel[:8] == "+2347026" :
               lbl7 = tk.Label(F1,text="This is a Visafone NG number",bg='pink',fg='white',width=40,
                               font=('monotype corsiva',30,'bold'))# conditional statement for Visafone
               lbl7.place(x=250, y=600)

           elif Tel[:7] == "+234707" :
               lbl8 = tk.Label(F1,text="This is a Zoom mobile NG number",bg='indigo',fg='blue',width=40,
                               font=('monotype corsiva',30,'bold')) # conditional statement for Zoom mobile
               lbl8.place(x=250, y=600)

           elif Tel[:7] == "+234804" :
              lbl9 = tk.Label(F1,text="This is a MTEL NG number",bg='lightgreen',fg='white',width=40,
                               font=('monotype corsiva',30,'bold'))  # conditional statement for MTEL
              lbl9.place(x=250, y=600)

           else:
               lbl10 = tk.Label(F1,text="Invalid phone number",bg='red',fg='white',width=40,
                              font=('monotype corsiva',30,'bold'))
               lbl10.place(x=250, y=600)

        else:
            lbl11 = tk.Label(F1,text="Phone number is greater than or less than 14",bg='red',fg='white',width=40,
                              font=('monotype corsiva',30,'bold'))
            lbl11.place(x=250, y=600)

#-------Radio button to check the format of the numbers---------
info_header = tk.Label(F1,text='Instruction',
                bg='red',font=('times new roman',13,'bold'))
info_header.place(x=10,y=115)

info = tk.Label(F1,text='Choose the format of the phone number\nyou want to enter in the textbox',
                bg='yellow',font=('times new roman',10,'bold'))
info.place(x=10,y=142)

r = tk.IntVar()#using the method IntVar() to get an integer variable

radiobtn1 = tk.Radiobutton(F1,text='080.., 081.., 090..',variable=r,value=1,indicator=0)
radiobtn1.place(x=10,y=185)

radiobtn2 = tk.Radiobutton(F1,text='+234....',variable=r,value=2,indicator=0,width=12)
radiobtn2.place(x=10,y=215)
#--------------------------------------------------------------------

label = tk.Label(F1,text='Enter your phone number in the box below',bg='yellow',
                 font=('times new roman',15,'bold'))
label.place(x=450, y=350)

num = tk.StringVar() #getting the phone number by usihg string variable
Entry = ttk.Entry(F1,textvariable=num,width=22,
                  font=('monotype corsiva',25,'bold'))
Entry.place(x=452, y=380)

Enter_btn = ttk.Button(F1,text='PRESS ENTER',command=Enter)
Enter_btn.place(x=580,y=440)

gui.mainloop()



