import os
os.system('cls')
from tkinter import *


# ---------------------------- CONSTANTS ------------------------------- #
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer=None
# ---------------------------- TIMER RESET ------------------------------- # 
def timer_cancel():
    t.after_cancel(timer)
    canvas.itemconfig(text_timer,text="00:00")
    l.config(text="Timer",font=("Courier",40,"bold"),fg="#9bdeac",bg="#f7f5dd")
    lt.config(text="")
    global reps
    reps=0


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def Timer():
    global reps
    
    reps+=1
    work_sec=WORK_MIN *60
    short_break_sec=SHORT_BREAK_MIN *60
    long_break_sec=LONG_BREAK_MIN *60

    if reps%8==0:
        
        count_down( long_break_sec)
        l.config(text="Break",font=("Courier",40,"bold"),fg="red")


    elif reps%2==0:
        count_down( short_break_sec)
        l.config(text="Break",font=("Courier",40,"bold"),fg="pink")


    else:
        count_down(work_sec)
        l.config(text="Work",font=("Courier",40,"bold"),fg="green")
       

            




# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(seconds):
    c_minute=seconds//60
    c_seconds=int(seconds%60)
    if seconds>=0:
        canvas.itemconfig(text_timer,text=f"{c_minute:02d}:{c_seconds:02d}")
        global timer
        timer=t.after(1000,count_down,seconds-1)
    else:
        Timer()
        mark=""
        ws=reps//2
        for i in range(ws):
            mark=mark+"✔"


            lt.config(text=mark,font=("Courier",25,"bold"),fg="#9bdeac",highlightthickness=0,bg="#f7f5dd")
            

        

# ---------------------------- UI SETUP ------------------------------- #


t=Tk()
t.title("Pomodoro App -(By Rachit Mishra)")
t.geometry("500x600")
l=Label(t,text="Timer",font=("Courier",40,"bold"),fg="#9bdeac",bg="#f7f5dd")
l.grid(row=0,column=1)
t.config(padx=100,pady=50,bg="#f7f5dd")







canvas=Canvas(width=200,height=224,bg="#f7f5dd",highlightthickness=0)
img=PhotoImage(file="D:\\Programming\\programming\\python\\PYTHON BASIC\\tomato.png")
canvas.create_image(100,112,image=img)
canvas.grid(row=1,column=1,pady=40)
text_timer=canvas.create_text(103,130,text=f"00:00",fill="white",font=("Courier",35,"bold"))





bs=Button(t,text="Start",highlightthickness=0,command=Timer)
bs.grid(row=10,column=0)

lt=Label(t,text="✔",font=("Courier",25,"bold"),fg="#9bdeac",highlightthickness=0,bg="#f7f5dd")
lt.grid(row=15,column=1)

br=Button(t,text="Reset",highlightthickness=0,command=timer_cancel)
br.grid(row=10,column=2)



t.mainloop()















