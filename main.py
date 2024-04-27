from tkinter import *
from tkinter import messagebox
import sounddevice as sound
from scipy.io.wavfile import write
import time


root = Tk()
root.geometry("350x450")
root.title("Voice Recorder")
root.iconbitmap("icon.ico")
root.resizable(False,False)
root.configure(bg="#4a4a4a")

def start_rec():
    freq = 44100
    dur = int(rec_time.get())
    recording = sound.rec(dur*freq,samplerate = freq,channels = 2)
    try:
        temp = int(rec_time.get())
    except:
        print("plese type right value")
    while temp>0:
        root.update()
        time.sleep(1)
        temp -= 1
        if (temp == 0):
            messagebox.showinfo("Time","times up")
        Label(text=f"{str(temp)}",font="16",width=4,fg="white",bg="#4a4a4a").place(relx=0.12,rely=0.8)

    sound.wait()
    file = filename.get()
    write(f"{file}.wav",freq,recording)


filename=StringVar()
entry=Entry(root,textvariable=filename,width=12,font="arial 16").place(relx=0.3,rely=0.3)
filename.set("recording")
Label(text="Set name of rec",font="18",bg="#4a4a4a",fg="white").place(relx=0.3,rely=0.4)

rec_time = StringVar()
inp = Entry(root,textvariable=rec_time,font="bold 24", width=15).place(relx=0.12,rely=0.5)
Label(text="Enter Time in sec [for recording]",font="bold 16",bg="#4a4a4a",fg="white").place(relx=0.1,rely=0.62)
Button(root,font="20",text="Start Rec", bg="red",fg="white",border=0,command=start_rec).place(relx=0.35,rely=0.7)


root.mainloop()