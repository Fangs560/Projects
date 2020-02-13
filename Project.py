from tkinter import filedialog
from tkinter import *

root = Tk()
root.title("Attendance Checker")
#Initialized variables
tot_p1=inp_p1=tot_p2=inp_p2=tot_p3=inp_p3=tot_p4=inp_p4=tot_p5=inp_p5=tot_p6=inp_p6=tot_p7=inp_p7=tot_p8=inp_p8=0.0
at_p1=per_p1=at_p2=per_p2=at_p3=per_p3=at_p4=per_p4=at_p5=per_p5=at_p6=per_p6=at_p7=per_p7=at_p8=per_p8=""
'''#Buttons for file saving and/or Opening
def save():
    root.filename =  filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))


save_but=Button(root,text="Save/New",command=save)
save_but.grid(row=4,column=0)

def open():
    root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))

open_but=Button(root,text="Open",command=open)
open_but.grid(row=4,column=1)'''
#Functions for every present button press
def p1():
    global tot_p1,inp_p1,at_p1,per_p1
    tot_p1+=1
    inp_p1+=1
    at_p1=str(int(inp_p1))+"/"+str(int(tot_p1))
    per_p1=float(inp_p1/tot_p1)*100
    p1_lab=Label(root,text=at_p1).grid(row=5,column=3)
    perp1_lab=Label(root,text=str(round(per_p1,2))+"%").grid(row=5,column=4)

def p2():
    global tot_p2,inp_p2,at_p2,per_p2
    tot_p2+=1
    inp_p2+=1
    at_p2=str(int(inp_p2))+"/"+str(int(tot_p2))
    per_p2=float(inp_p2/tot_p2)*100
    p2_lab=Label(root,text=at_p2).grid(row=6,column=3)
    perp2_lab=Label(root,text=str(round(per_p2,2))+"%").grid(row=6,column=4)

def p3():
    global tot_p3,inp_p3,at_p3,per_p3
    tot_p3+=1
    inp_p3+=1
    at_p3=str(int(inp_p3))+"/"+str(int(tot_p3))
    per_p3=float(inp_p3/tot_p3)*100
    p3_lab=Label(root,text=at_p3).grid(row=7,column=3)
    perp3_lab=Label(root,text=str(round(per_p3,2))+"%").grid(row=7,column=4)

def p4():
    global tot_p4,inp_p4,at_p4,per_p4
    tot_p4+=1
    inp_p4+=1
    at_p4=str(int(inp_p4))+"/"+str(int(tot_p4))
    per_p4=float(inp_p4/tot_p4)*100
    p4_lab=Label(root,text=at_p4).grid(row=8,column=3)
    perp4_lab=Label(root,text=str(round(per_p4,2))+"%").grid(row=8,column=4)

def p5():
    global tot_p5,inp_p5,at_p5,per_p5
    tot_p5+=1
    inp_p5+=1
    at_p5=str(int(inp_p5))+"/"+str(int(tot_p5))
    per_p5=float(inp_p5/tot_p5)*100
    p5_lab=Label(root,text=at_p5).grid(row=9,column=3)
    perp5_lab=Label(root,text=str(round(per_p5,2))+"%").grid(row=9,column=4)

def p6():
    global tot_p6,inp_p6,at_p6,per_p6
    tot_p6+=1
    inp_p6+=1
    at_p6=str(int(inp_p6))+"/"+str(int(tot_p6))
    per_p6=float(inp_p6/tot_p6)*100
    p6_lab=Label(root,text=at_p6).grid(row=10,column=3)
    perp6_lab=Label(root,text=str(round(per_p6,2))+"%").grid(row=10,column=4)

def p7():
    global tot_p7,inp_p7,at_p7,per_p7
    tot_p7+=1
    inp_p7+=1
    at_p7=str(int(inp_p7))+"/"+str(int(tot_p7))
    per_p7=float(inp_p7/tot_p7)*100
    p7_lab=Label(root,text=at_p7).grid(row=11,column=3)
    perp7_lab=Label(root,text=str(round(per_p7,2))+"%").grid(row=11,column=4)

def p8():
    global tot_p8,inp_p8,at_p8,per_p8
    tot_p8+=1
    inp_p8+=1
    at_p8=str(int(inp_p8))+"/"+str(int(tot_p8))
    per_p8=float(inp_p8/tot_p8)*100
    p8_lab=Label(root,text=at_p8).grid(row=12,column=3)
    perp8_lab=Label(root,text=str(round(per_p8,2))+"%").grid(row=12,column=4)


#Functions for every Absent button pressed
def a1():
    global tot_p1,inp_p1,at_p1,per_p1
    tot_p1+=1
    at_p1=str(int(inp_p1))+"/"+str(int(tot_p1))
    per_p1=float(inp_p1/tot_p1)*100
    p1_lab=Label(root,text=at_p1).grid(row=5,column=3)
    perp1_lab=Label(root,text=str(round(per_p1,2))+"%").grid(row=5,column=4)

def a2():
    global tot_p2,inp_p2,at_p2,per_p2
    tot_p2+=1
    at_p2=str(int(inp_p2))+"/"+str(int(tot_p2))
    per_p2=float(inp_p2/tot_p2)*100
    p2_lab=Label(root,text=at_p2).grid(row=6,column=3)
    perp2_lab=Label(root,text=str(round(per_p2,2))+"%").grid(row=6,column=4)

def a3():
    global tot_p3,inp_p3,at_p3,per_p3
    tot_p3+=1
    at_p3=str(int(inp_p3))+"/"+str(int(tot_p3))
    per_p3=float(inp_p3/tot_p3)*100
    p3_lab=Label(root,text=at_p3).grid(row=7,column=3)
    perp3_lab=Label(root,text=str(round(per_p3,2))+"%").grid(row=7,column=4)

def a4():
    global tot_p4,inp_p4,at_p4,per_p4
    tot_p4+=1
    at_p4=str(int(inp_p4))+"/"+str(int(tot_p4))
    per_p4=float(inp_p4/tot_p4)*100
    p4_lab=Label(root,text=at_p4).grid(row=8,column=3)
    perp4_lab=Label(root,text=str(round(per_p4,2))+"%").grid(row=8,column=4)

def a5():
    global tot_p5,inp_p5,at_p5,per_p5
    tot_p5+=1
    at_p5=str(int(inp_p5))+"/"+str(int(tot_p5))
    per_p5=float(inp_p5/tot_p5)*100
    p5_lab=Label(root,text=at_p5).grid(row=9,column=3)
    perp5_lab=Label(root,text=str(round(per_p5,2))+"%").grid(row=9,column=4)

def a6():
    global tot_p6,inp_p6,at_p6,per_p6
    tot_p6+=1
    at_p6=str(int(inp_p6))+"/"+str(int(tot_p6))
    per_p6=float(inp_p6/tot_p6)*100
    p6_lab=Label(root,text=at_p6).grid(row=10,column=3)
    perp6_lab=Label(root,text=str(round(per_p6,2))+"%").grid(row=10,column=4)

def a7():
    global tot_p7,inp_p7,at_p7,per_p7
    tot_p7+=1
    at_p7=str(int(inp_p7))+"/"+str(int(tot_p7))
    per_p7=float(inp_p7/tot_p7)*100
    p7_lab=Label(root,text=at_p7).grid(row=11,column=3)
    perp7_lab=Label(root,text=str(round(per_p7,2))+"%").grid(row=11,column=4)

def a8():
    global tot_p8,inp_p8,at_p8,per_p8
    tot_p8+=1
    at_p8=str(int(inp_p8))+"/"+str(int(tot_p8))
    per_p8=float(inp_p8/tot_p8)*100
    p8_lab=Label(root,text=at_p8).grid(row=12,column=3)
    perp8_lab=Label(root,text=str(round(per_p8,2))+"%").grid(row=12,column=4)
    
#Labels for name, reg.no, branch and section
name_lab=Label(root,text="Name:").grid(row=0,column=0)
reg_lab=Label(root,text="Reg No.:").grid(row=1,column=0)
branch_lab=Label(root,text="Branch:").grid(row=2,column=0)
sec_lab=Label(root,text="Section:").grid(row=3,column=0)
per_lab=Label(root,text="Percentage").grid(row=4,column=4)
count_lab=Label(root,text="Classes Attended").grid(row=4,column=3)

#Entry boxes for  name, reg.no, branch and section
name_inp=Entry(root).grid(row=0,column=1)
reg_inp=Entry(root).grid(row=1,column=1)
branch_inp=Entry(root).grid(row=2,column=1)
sec_inp=Entry(root).grid(row=3,column=1)

#Subject Labels
sub_1=Label(root,text="Design and Analysis of Algorithms").grid(row=5,column=0)
sub_2=Label(root,text="Advanced Programming Practices").grid(row=6,column=0)
sub_3=Label(root,text="Computer Communications").grid(row=7,column=0)
sub_4=Label(root,text="Probability and Queueing Theory").grid(row=8,column=0)
sub_5=Label(root,text="Creative and Critical Thinking Skills").grid(row=9,column=0)
sub_6=Label(root,text="Environmental Science").grid(row=10,column=0)
sub_7=Label(root,text="Operating Systems").grid(row=11,column=0)
sub_8=Label(root,text="Software Engineering and Project Management").grid(row=12,column=0)

#Present Buttons
p1_but=Button(root,text="Present",command=p1).grid(row=5,column=1)
p2_but=Button(root,text="Present",command=p2).grid(row=6,column=1)
p3_but=Button(root,text="Present",command=p3).grid(row=7,column=1)
p4_but=Button(root,text="Present",command=p4).grid(row=8,column=1)
p5_but=Button(root,text="Present",command=p5).grid(row=9,column=1)
p6_but=Button(root,text="Present",command=p6).grid(row=10,column=1)
p7_but=Button(root,text="Present",command=p7).grid(row=11,column=1)
p8_but=Button(root,text="Present",command=p8).grid(row=12,column=1)

#Absent Buttons
a1_but=Button(root,text="Absent",command=a1).grid(row=5,column=2)
a2_but=Button(root,text="Absent",command=a2).grid(row=6,column=2)
a3_but=Button(root,text="Absent",command=a3).grid(row=7,column=2)
a4_but=Button(root,text="Absent",command=a4).grid(row=8,column=2)
a5_but=Button(root,text="Absent",command=a5).grid(row=9,column=2)
a6_but=Button(root,text="Absent",command=a6).grid(row=10,column=2)
a7_but=Button(root,text="Absent",command=a7).grid(row=11,column=2)
a8_but=Button(root,text="Absent",command=a8).grid(row=12,column=2)











    

