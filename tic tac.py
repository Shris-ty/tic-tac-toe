import tkinter as tk
from tkinter import messagebox

root=tk.Tk()
root.geometry("500x500")
root.configure(bg="black")
root.title("tic tac toe")

frame1=tk.Frame(root)
frame1.pack()

clicked=True 
count=0

def reset():
    global b1,b2,b3,b4,b5,b6,b7,b8,b9
    global clicked,count
    clicked=True
    count=0

    frame2=tk.Frame(frame1,bg="white")
    frame2.pack()

    b1=tk.Button(root,text=" ",font="arial 20 bold",bg="grey",width=6,height=3,command=lambda:click(b1))
    b1.place(x=50,y=62)

    b2=tk.Button(root,text=" ",font="arial 20 bold",bg="grey",width=6,height=3,command=lambda:click(b2))
    b2.place(x=200,y=60)

    b3=tk.Button(root,text=" ",font="arial 20 bold",bg="grey",width=6,height=3,command=lambda:click(b3))
    b3.place(x=350,y=60)


    b4=tk.Button(root,text=" ",font="arial 20 bold",bg="grey",width=6,height=3,command=lambda:click(b4))
    b4.place(x=50,y=200)

    b5=tk.Button(root,text=" ",font="arial 20 bold",bg="grey",width=6,height=3,command=lambda:click(b5))
    b5.place(x=200,y=200)

    b6=tk.Button(root,text=" ",font="arial 20 bold",bg="grey",width=6,height=3,command=lambda:click(b6))
    b6.place(x=350,y=200)

    b7=tk.Button(root,text=" ",font="arial 20 bold",bg="grey",width=6,height=3,command=lambda:click(b7))
    b7.place(x=50,y=350)

    b8=tk.Button(root,text=" ",font="arial 20 bold",bg="grey",width=6,height=3,command=lambda:click(b8))
    b8.place(x=200,y=350)

    b9=tk.Button(root,text=" ",font="arial 20 bold",bg="grey",width=6,height=3,command=lambda:click(b9))
    b9.place(x=350,y=350)

def disable_all_buttons():
    b1.config(state="disabled")
    b2.config(state="disabled")
    b3.config(state="disabled")
    b4.config(state="disabled")
    b5.config(state="disabled")
    b6.config(state="disabled")
    b7.config(state="disabled")
    b8.config(state="disabled")
    b9.config(state="disabled")


def won():
    global winner
    winner=False

    if b1["text"] =="X" and b2["text"]=="X" and b3["text"]=="X":
        b1.config(bg="blue")
        b2.config(bg="blue")
        b3.config(bg="blue")
        winner=True
        messagebox.showinfo("win","player1 is winner.....!")
        disable_all_buttons()



    elif b4["text"] =="X" and b5["text"]=="X" and b6["text"]=="X":
        b4.config(bg="blue")
        b5.config(bg="blue")
        b6.config(bg="blue")
        winner=True
        messagebox.showinfo("win","player1 is winner.....!")
        disable_all_buttons()


    elif b7["text"] =="X" and b8["text"]=="X" and b9["text"]=="X":
        b7.config(bg="blue")
        b8.config(bg="blue")
        b9.config(bg="blue")
        winner=True
        messagebox.showinfo("win","player1 is winner.....!")
        disable_all_buttons()    

    elif b1["text"] =="X" and b4["text"]=="X" and b7["text"]=="X":
        b1.config(bg="blue")
        b4.config(bg="blue")
        b7.config(bg="blue")
        winner=True
        messagebox.showinfo("win","player1 is winner.....!")
        disable_all_buttons()


    elif b2["text"] =="X" and b5["text"]=="X" and b8["text"]=="X":
        b2.config(bg="blue")
        b5.config(bg="blue")
        b8.config(bg="blue")
        winner=True
        messagebox.showinfo("win","player1 is winner.....!")
        disable_all_buttons()   

    elif b3["text"] =="X" and b6["text"]=="X" and b9["text"]=="X":
        b3.config(bg="blue")
        b6.config(bg="blue")
        b9.config(bg="blue")
        winner=True
        messagebox.showinfo("win","player1 is winner.....!")
        disable_all_buttons()


    elif b1["text"] =="X" and b5["text"]=="X" and b9["text"]=="X":
        b1.config(bg="blue")
        b5.config(bg="blue")
        b9.config(bg="blue")
        winner=True
        messagebox.showinfo("win","player1 is winner.....!")
        disable_all_buttons()    


    elif b3["text"] =="X" and b5["text"]=="X" and b7["text"]=="X":
        b3.config(bg="blue")
        b5.config(bg="blue")
        b7.config(bg="blue")
        winner=True
        messagebox.showinfo("win","player1 is winner.....!")
        disable_all_buttons()   

    elif b1["text"] =="0" and b2["text"]=="0" and b3["text"]=="0":
        b1.config(bg="blue")
        b2.config(bg="blue")
        b3.config(bg="blue")
        winner=True
        messagebox.showinfo("win","player2 is winner.....!")
        disable_all_buttons()



    elif b4["text"] =="0" and b5["text"]=="0" and b6["text"]=="0":
        b4.config(bg="blue")
        b5.config(bg="blue")
        b6.config(bg="blue")
        winner=True
        messagebox.showinfo("win","player2 is winner.....!")
        disable_all_buttons()


    elif b7["text"] =="0" and b8["text"]=="0" and b9["text"]=="0":
        b7.config(bg="blue")
        b8.config(bg="blue")
        b9.config(bg="blue")
        winner=True
        messagebox.showinfo("win","player2 is winner.....!")
        disable_all_buttons()    

    elif b1["text"] =="0" and b4["text"]=="0" and b7["text"]=="0":
        b1.config(bg="blue")
        b4.config(bg="blue")
        b7.config(bg="blue")
        winner=True
        messagebox.showinfo("win","player2 is winner.....!")
        disable_all_buttons()


    elif b2["text"] =="0" and b5["text"]=="0" and b8["text"]=="0":
        b2.config(bg="blue")
        b5.config(bg="blue")
        b8.config(bg="blue")
        winner=True
        messagebox.showinfo("win","player2 is winner.....!")
        disable_all_buttons()   

    elif b3["text"] =="0" and b6["text"]=="0" and b9["text"]=="0":
        b3.config(bg="blue")
        b6.config(bg="blue")
        b9.config(bg="blue")
        winner=True
        messagebox.showinfo("win","player2 is winner.....!")
        disable_all_buttons()


    elif b1["text"] =="0" and b5["text"]=="0" and b9["text"]=="0":
        b1.config(bg="blue")
        b5.config(bg="blue")
        b9.config(bg="blue")
        winner=True
        messagebox.showinfo("win","player2 is winner.....!")
        disable_all_buttons()    


    elif b3["text"] =="0" and b5["text"]=="0" and b7["text"]=="0":
        b4.config(bg="blue")
        b5.config(bg="blue")
        b6.config(bg="blue")
        winner=True
        messagebox.showinfo("win","player2 is winner.....!")
        disable_all_buttons()   

    if count==9 and winner == False:
        messagebox.showinfo("tic tac toe","ITS A TIE")
        
     
def click(b):
    global clicked,count
    
    if b["text"] == " " and clicked==True:
        b["text"]="X"
        clicked=False
        count+=1
        won()
      
    elif b["text"] ==" " and clicked==False:
        b["text"]="0"
        clicked=True
        count+=1
        won()

    else:
        messagebox.showerror("ERROR","Select another box which is empty")
    
l1=tk.Label(frame1,text="tic tac toe",font="arial 20 bold",fg="yellow",bg="blue")
l1.pack()

frame2=tk.Frame(frame1,bg="white")
frame2.pack()

b1=tk.Button(root,text=" ",font="arial 20 bold",bg="grey",width=6,height=3,command=lambda:click(b1))
b1.place(x=50,y=62)

b2=tk.Button(root,text=" ",font="arial 20 bold",bg="grey",width=6,height=3,command=lambda:click(b2))
b2.place(x=200,y=60)

b3=tk.Button(root,text=" ",font="arial 20 bold",bg="grey",width=6,height=3,command=lambda:click(b3))
b3.place(x=350,y=60)


b4=tk.Button(root,text=" ",font="arial 20 bold",bg="grey",width=6,height=3,command=lambda:click(b4))
b4.place(x=50,y=200)

b5=tk.Button(root,text=" ",font="arial 20 bold",bg="grey",width=6,height=3,command=lambda:click(b5))
b5.place(x=200,y=200)

b6=tk.Button(root,text=" ",font="arial 20 bold",bg="grey",width=6,height=3,command=lambda:click(b6))
b6.place(x=350,y=200)

b7=tk.Button(root,text=" ",font="arial 20 bold",bg="grey",width=6,height=3,command=lambda:click(b7))
b7.place(x=50,y=350)

b8=tk.Button(root,text=" ",font="arial 20 bold",bg="grey",width=6,height=3,command=lambda:click(b8))
b8.place(x=200,y=350)

b9=tk.Button(root,text=" ",font="arial 20 bold",bg="grey",width=6,height=3,command=lambda:click(b9))
b9.place(x=350,y=350)

button=tk.Button(root,text="reset",font="arial 15 bold",command=reset,bg="white",fg="red")
button.place(x=10,y=10)

root.mainloop()
