from tkinter import *
root = Tk()
root.title("To-Do-List")
root.resizable(False,False)
root.geometry("750x750+0+0")



def q1_correct():
    l2=Label(f1, text="Correct", font="Arial 18 bold", bg="green",fg="black")
    l2.place(x=600,y=150)
    ll2=Label(f1, text="Score: 1", font="Arial 18 bold",fg="black")
    ll2.place(x=600,y=100)

def q1_incorrect():
    l3=Label(f1, text="Wrong", font="Arial 18 bold", bg="red",fg="black")
    l3.place(x=600,y=150)
    ll3=Label(f1, text="Score: 0", font="Arial 18 bold",fg="black")
    ll3.place(x=600,y=100)

def q2_correct():
    l4=Label(f1, text="Correct", font="Arial 18 bold", bg="green",fg="black")
    l4.place(x=600,y=300)
    ll4=Label(f1, text="Score: 1", font="Arial 18 bold",fg="black")
    ll4.place(x=600,y=250)

def q2_incorrect():
    l5=Label(f1, text="Wrong", font="Arial 18 bold", bg="red",fg="black")
    l5.place(x=600,y=300)
    ll5=Label(f1, text="Score: 0", font="Arial 18 bold",fg="black")
    ll5.place(x=600,y=250)

def q3_correct():
    l6=Label(f1, text="Correct", font="Arial 18 bold", bg="green",fg="black")
    l6.place(x=600,y=450)
    ll6=Label(f1, text="Score: 1", font="Arial 18 bold",fg="black")
    ll6.place(x=600,y=400)

def q3_incorrect():
    l7=Label(f1, text="Wrong", font="Arial 18 bold", bg="red",fg="black")
    l7.place(x=600,y=450)
    ll7=Label(f1, text="Score: 0", font="Arial 18 bold",fg="black")
    ll7.place(x=600,y=400)

def q4_correct():
    l8=Label(f1, text="Correct", font="Arial 18 bold", bg="green",fg="black")
    l8.place(x=600,y=600)
    ll8=Label(f1, text="Score: 1", font="Arial 18 bold",fg="black")
    ll8.place(x=600,y=550)

def q4_incorrect():
    l9=Label(f1, text="Wrong", font="Arial 18 bold", bg="red",fg="black")
    l9.place(x=600,y=600)
    ll9=Label(f1, text="Score: 0", font="Arial 18 bold",fg="black")
    ll9.place(x=600,y=550)


#Frame
f1 =Frame(root,width = 1000,height = 1000,bg="grey")
f1.place(x=0,y=0)


#heading
heading=Label(root,text="Quiz-Game",font="boulder 24 bold",fg="black",bg="lightblue").pack()


#Q1
l1=Label(f1, text="Q1. What is the Capital of Uganda ?", font="Arial 14 bold",fg="Black",bg="grey")
l1.place(x=0,y=100)
b1=Button(f1, text="Kampala",font="Arial 12 bold",bg="grey",command=q1_correct)
b1.place(x=0,y=150)
b2=Button(f1, text="Singapur",font="Arial 12 bold",bg="grey",command=q1_incorrect)
b2.place(x=110,y=150)
b3=Button(f1, text="Hongkong",font="Arial 12 bold",bg="grey",command=q1_incorrect)
b3.place(x=222,y=150)

#Q2
l1=Label(f1, text="Q2. How many Vowels are there in English Alphabet ?", font="Arial 14 bold",fg="Black",bg="grey")
l1.place(x=0,y=250)
b1=Button(f1, text="5",font="Arial 12 bold",bg="grey",command=q2_correct)
b1.place(x=0,y=300)
b2=Button(f1, text="6",font="Arial 12 bold",bg="grey",command=q2_incorrect)
b2.place(x=110,y=300)
b3=Button(f1, text="4",font="Arial 12 bold",bg="grey",command=q2_incorrect)
b3.place(x=222,y=300)

#Q3
l1=Label(f1, text="Q3. What is the Output of 4x3 ?", font="Arial 14 bold",fg="Black",bg="grey")
l1.place(x=0,y=400)
b1=Button(f1, text="13",font="Arial 12 bold",bg="grey",command=q3_incorrect)
b1.place(x=0,y=450)
b2=Button(f1, text="12",font="Arial 12 bold",bg="grey",command=q3_correct)
b2.place(x=110,y=450)
b3=Button(f1, text="11",font="Arial 12 bold",bg="grey",command=q3_incorrect)
b3.place(x=222,y=450)

#Q4
l1=Label(f1, text="Q4. What is the total number of Alphabet in English ?", font="Arial 14 bold",fg="Black",bg="grey")
l1.place(x=0,y=550)
b1=Button(f1, text="30",font="Arial 12 bold",bg="grey",command=q4_incorrect)
b1.place(x=0,y=600)
b2=Button(f1, text="27",font="Arial 12 bold",bg="grey",command=q4_incorrect)
b2.place(x=110,y=600)
b3=Button(f1, text="26",font="Arial 12 bold",bg="grey",command=q4_correct)
b3.place(x=222,y=600)


root.mainloop()