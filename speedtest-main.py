import speedtest
from tkinter import *
from tkinter import ttk
from threading import Thread
root = Tk()
root.title('Internet Speedtest by AliFGT')
root.geometry("600x660")
main_bg = '#100D12'
f = "Helvetica"
root.config(bg=main_bg)
root.resizable(False, False)
tab = ttk.Notebook()
tab.pack(side=TOP)
welcome = Frame(root, width=600, height=655, bd=0, border=0, borderwidth=0, bg=main_bg)
welcome.pack()
welcome.pack_propagate(0)
test_frame = Frame(root, width=600, height=655, bd=0, border=0, borderwidth=0, bg=main_bg)
test_frame.pack()
test_frame.pack_propagate(0)
test_frame.grid_propagate(0)
tab.add(welcome, text="Welcome, Getting started")
tab.add(test_frame, text="Internet Speed test")

def go():
    tab.select(1)

def test_now():
    test.pack_forget()
    frame = LabelFrame(test_frame, text="Your internet results", bg=main_bg, fg='white')
    frame.grid(pady=50)
    calc = Label(frame, text="Calculating now, please wait")
    calc.pack()
    prog = ttk.Progressbar(frame, mode='determinate')
    prog.pack()
    Thread(target=prog.start()).start()
    inter = speedtest.Speedtest()
    upload = int(inter.upload() / 1024 / 1024)
    download = int(inter.download() / 1024 / 1024)
    ping = inter.results.ping
    best = inter.get_best_server()
    Label(frame, text=f"Your internet results is:\nUpload speed: {upload} Mbit\\s\n"+
        f"Download speed: {download} Mbit\\s\nPing result: {int(ping)} ms\n"+
        f"Best server: {best['host']} Located in: {best['country']}").pack()
    prog.stop()

tr7ib = Label(welcome, text="Welcome to Speedtest Application!", bg=main_bg, fg='white',
    font=(f, 20))
tr7ib.grid(sticky=N, padx=40, pady=10)
infos = Label(welcome, text="You can navigate between the pages using menu\n"+
    "Or Go to Internet Speed test tab from here:", font=(
        f, 13), bg=main_bg, fg="white").grid(pady=(180, 0))
navigate = Button(welcome, text="Navigate", font=(f, 15), command=go).grid(pady=35)

tr7ib = Label(test_frame, text="Welcome to Speedtest tab!", bg=main_bg, fg='white',
    font=(f, 20)).grid(sticky=N, padx=90, pady=10)
test = Button(test_frame, text="Go test your internet", font=(f, 17),
    command=Thread(target=test_now).start)
test.pack(pady=100)

root.mainloop()