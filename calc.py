from tkinter import *
import math

welcome_screen = Tk()

welcome_screen.title("Welcome!")
welwidth = 450
welheight = 550
screenwidth = welcome_screen.winfo_screenwidth()
screenheight = welcome_screen.winfo_screenheight()
welcome_screen.geometry(f"{welwidth}x{welheight}+{math.floor((screenwidth / 2) - (welwidth / 2))}+{math.floor((screenheight / 2) - (welheight / 2) - 30)}")
welcome_screen.config(background='#1f2147')
icon = PhotoImage(file='data/calc.png')
welcome_screen.iconphoto(True, icon)
photo = PhotoImage(file='data/calc300px.png')
welcome_label = Label(welcome_screen, text='WELCOME!\nTo Your Simple\n>> CALCULATOR <<', fg='cyan', bg='black', font=('Impact', 30)).pack(pady=30)
photo_label = Label(welcome_screen, image=photo, bg='#1f2147').pack()


def main_screen():
    welcome_screen.destroy()

    def calculations():
        try:
            if operation.get() == 1:
                x = entry1.get()
                y = entry2.get()
                z = float(x) + float(y)
                resultlabel = Label(window, text=z, font=('Arial', 16), bg='white', fg='black', padx=5, pady=2.4)
                resultlabel.place(x=155, y=373)
                entry1.config(state=DISABLED)
                entry2.config(state=DISABLED)
                window.after(4000,outro_screen)
            elif operation.get() == 2:
                x = entry1.get()
                y = entry2.get()
                z = float(x) - float(y)
                resultlabel = Label(window, text=z, font=('Arial', 16), bg='white', fg='black', padx=5, pady=2.4)
                resultlabel.place(x=155, y=373)
                entry1.config(state=DISABLED)
                entry2.config(state=DISABLED)
                window.after(4000,outro_screen)
            elif operation.get() == 3:
                x = entry1.get()
                y = entry2.get()
                z = float(x) * float(y)
                resultlabel = Label(window, text=z, font=('Arial', 16), bg='white', fg='black', padx=5, pady=2.4)
                resultlabel.place(x=155, y=373)
                entry1.config(state=DISABLED)
                entry2.config(state=DISABLED)
                window.after(4000,outro_screen)
            elif operation.get() == 4:
                x = entry1.get()
                y = entry2.get()
                if y == 0:
                    resultlabel = Label(window, text="Can't Divide by Zero", font=('Arial', 16), bg='white', fg='black', padx=5, pady=2.4)
                    resultlabel.place(x=155, y=373)
                    entry1.config(state=DISABLED)
                    entry2.config(state=DISABLED)
                    window.after(4000,outro_screen)
                else:
                    z = float(x) / float(y)
                    resultlabel = Label(window, text=z, font=('Arial', 16), bg='white', fg='black', padx=5, pady=2.4)
                    resultlabel.place(x=155, y=373)
                    entry1.config(state=DISABLED)
                    entry2.config(state=DISABLED)
                    window.after(4000,outro_screen)
            else:
                resultlabel = Label(window, text='Wrong Input', font=('Arial', 16), bg='white', fg='black', padx=5, pady=2.4)
                resultlabel.place(x=155, y=373)
                entry1.config(state=DISABLED)
                entry2.config(state=DISABLED)
                window.after(4000, outro_screen)
        except ValueError:
            resultlabel = Label(window, text='Wrong Input', font=('Arial', 16), bg='white', fg='black', padx=5, pady=2.4)
            resultlabel.place(x=155, y=373)
            entry1.config(state=DISABLED)
            entry2.config(state=DISABLED)
            window.after(4000, outro_screen)

    window = Tk()
    appwidth = 450
    appheight = 550
    screenwidth = window.winfo_screenwidth()
    screenheight = window.winfo_screenheight()
    window.geometry(f"{appwidth}x{appheight}+{math.floor((screenwidth / 2) - (appwidth / 2))}+{math.floor((screenheight / 2) - (appheight / 2) - 30)}")
    window.title("Calculator")
    icon = PhotoImage(file='data/calc.png')
    window.iconphoto(True, icon)
    window.config(background='#1f2147')
    label = Label(window, text='Calculator', font=('Impact', 28, 'underline'), fg='cyan', bg='black', relief=RAISED, bd=8, padx=20, pady=10).pack(pady=10)
    entryBoxLabel1 = Label(window, text="X:", font=('Arial', 16), bg='black', fg='cyan', padx=5, pady=2.4).place(x=88, y=130)
    entry1 = Entry(window, font=('Consolas', 18), width=7)
    entry1.place(x=118, y=130)
    entryBoxLabel2 = Label(window, text="Y:", font=('Arial', 16), bg='black', fg='cyan', padx=5, pady=2.4).place(x=235, y=130)
    entry2 = Entry(window, font=('Consolas', 18), width=7)
    entry2.place(x=265, y=130)
    entryBoxLabel3 = Label(window, text="The Result is:", font=('Arial', 16), bg='black', fg='cyan', padx=5, pady=2.4).place(x=154, y=340)
    resultLabel2 = Label(window, text='                     ', font=('Arial', 16), bg='white', fg='black', padx=5, pady=2.4).place(x=155, y=373)
    operation = IntVar()
    Radiobutton(window, text='X + Y', font=('Arial', 20), variable=operation, value=1, padx=23, pady=5, compound=LEFT, indicatoron=FALSE, fg='black', bg='cyan').place(x=70, y=190)
    Radiobutton(window, text='X - Y', font=('Arial', 20), variable=operation, value=2, padx=25, pady=5, compound=LEFT, indicatoron=FALSE, fg='black', bg='cyan').place(x=260, y=190)
    Radiobutton(window, text='X x Y', font=('Arial', 20), variable=operation, value=3, padx=25, pady=5, compound=LEFT, indicatoron=FALSE, fg='black', bg='cyan').place(x=70, y=270)
    Radiobutton(window, text='X ÷ Y', font=('Arial', 20), variable=operation, value=4, padx=22, pady=5,  compound=LEFT, indicatoron=FALSE, fg='black', bg='cyan').place(x=260, y=270)
    button = Button(window, text='Calculate', command=calculations, font=('comic sans', 17), fg='#1f2147', bg='black', padx='10', pady='5', activeforeground='cyan', activebackground='black', state=ACTIVE, width=7).place(x=165, y=430)
#    signature = Label(window, font=('Algeria', 18), text='Coded & Designed By: Mohanad Medhat', fg='purple', bg='black')
#    signature.pack(side=BOTTOM)

    def outro_screen():
        window.destroy()
        outro = Tk()
        outro.title("GoodBye!")
        welwidth = 450
        welheight = 550
        screenwidth = outro.winfo_screenwidth()
        screenheight = outro.winfo_screenheight()
        outro.geometry(f"{welwidth}x{welheight}+{math.floor((screenwidth / 2) - (welwidth / 2))}+{math.floor((screenheight / 2) - (welheight / 2) - 30)}")
        outro.config(background='#1f2147')
        icon = PhotoImage(file='data/calc.png')
        outro.iconphoto(True, icon)
        ourto_label = Label(outro, text='THANKS For Using!', fg='cyan', bg='black', font=('Impact', 30), padx=20, pady=5)
        ourto_label.pack(pady=30)
        photo2 = PhotoImage(file='data/heart.png')
        photo2_label = Label(image=photo2, bg='#1f2147')
        photo2_label.image = photo2
        photo2_label.pack(pady=20)
        outro_signature = Label(outro, text='Coded & Designed By\n>> Mohanad Medhat <<', fg='cyan', bg='black', font=('Arial', 20, 'bold'), padx=20)
        outro_signature.pack(side='bottom')

        def ending():
            outro.destroy()

        outro.after(3500, ending)


welcome_screen.after(3000, main_screen)


mainloop()
