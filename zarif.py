import webbrowser
import tkinter as tk

# webbrowser.open('http://net-informations.com', new=2)


# config
root = tk.Tk()
root.title("GameOpen")
root.geometry("320x320+150+150")
root.configure(background="#000000")

# defines
def car():
    webbrowser.open('https://www.roblox.com/games/654732683/New-Limited-Car-Crushers-2', new=2)


def arsenal():
    webbrowser.open('https://www.roblox.com/games/286090429/Arsenal', new=2)


def doors():
    webbrowser.open('https://www.roblox.com/games/6516141723/DOORS', new=2)


def dor_but_good():
    webbrowser.open('https://www.roblox.com/games/10704934612/DOORS-But-Bad', new=2)


# buttons,etc
text1 = tk.Label(root, text='Select game').grid(row=0, column=0)
btn1 = tk.Button(root, text="Car crushers", command=car).grid(row=1, column=2,columnspan=2, sticky='we')
btn2 = tk.Button(root, text="Arsenal", command=arsenal).grid(row=2, column=2, columnspan=2, sticky='we')
btn3 = tk.Button(root, text='doors', command=doors).grid(row=3, column=2, columnspan=2, sticky='we')
btn4 = tk.Button(root, text='doors but good', command=dor_but_good).grid(row=4, column=2, columnspan=2, sticky='we')
if __name__ == '__main__':
    root.mainloop()
