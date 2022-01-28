from tkinter import *
from tkinter import scrolledtext
from tkinter.ttk import Combobox
from systems import *


class MakeUI(Frame):

    def __init__(self, *args, **kwargs):

        # Heritage
        Frame.__init__(self, width=500, height=250, *args, **kwargs)
        self.pack(expand=1, fill='both')

        var1 = IntVar()
        var2 = IntVar()
        var3 = IntVar()
        var4 = IntVar()
        var5 = IntVar()
        var6 = IntVar()
        var1.set(0), var2.set(0), var3.set(0), var4.set(0), var5.set(0), var6.set(0)

        self.lbl = Label(self, text=" Выберите модель: ", padx=10, pady=10, width=15)
        self.lbl.grid(column=0, row=0, columnspan=2)
        self.combo = Combobox(self, width=40)
        self.combo['values'] = ("1  Модель относительного большинства",
                                "2  Модель Кондорсе: явный победитель",
                                "3  Модель Кондорсе: Правило Копленда",
                                "4  Модель Кондорсе: Правило Симпсона",
                                "5  Модель Борда")
        self.combo.current(0)  # установите вариант по умолчанию
        self.combo.grid(column=2, row=0)

        self.lbl = Label(self, text="Альтернативы:", padx=15, pady=5, width=10)
        self.lbl.grid(column=0, row=1)
        self.lbl = Label(self, text="Голоса:", padx=10, pady=5, width=10)
        self.lbl.grid(column=1, row=1)
        self.lbl = Label(self, text="Результат:", padx=10, pady=5, width=10)
        self.lbl.grid(column=2, row=1)

        self.lbl1 = Label(self, text="A > B > C", padx=10, pady=5, width=10)
        self.lbl1.grid(column=0, row=2)
        self.txt1 = Spinbox(self, width=5, from_=0, to=1000, textvariable=var1)
        self.txt1.grid(column=1, row=2, padx=5)
        self.lbl2 = Label(self, text="A > C > B", padx=10, pady=5, width=10)
        self.lbl2.grid(column=0, row=3)
        self.txt2 = Spinbox(self, width=5, from_=0, to=1000, textvariable=var2)
        self.txt2.grid(column=1, row=3, padx=5)
        self.lbl3 = Label(self, text="B > A > C", padx=10, pady=5, width=10)
        self.lbl3.grid(column=0, row=4)
        self.txt3 = Spinbox(self, width=5, from_=0, to=1000, textvariable=var3)
        self.txt3.grid(column=1, row=4, padx=5)
        self.lbl4 = Label(self, text="B > C > A", padx=10, pady=5, width=10)
        self.lbl4.grid(column=0, row=5)
        self.txt4 = Spinbox(self, width=5, from_=0, to=1000, textvariable=var4)
        self.txt4.grid(column=1, row=5, padx=5)
        self.lbl5 = Label(self, text="C > A > B", padx=10, pady=5, width=10)
        self.lbl5.grid(column=0, row=6)
        self.txt5 = Spinbox(self, width=5, from_=0, to=1000, textvariable=var5)
        self.txt5.grid(column=1, row=6, padx=5)
        self.lbl6 = Label(self, text="C > B > A", padx=10, pady=5, width=10)
        self.lbl6.grid(column=0, row=7)
        self.txt6 = Spinbox(self, width=5, from_=0, to=1000, textvariable=var6)
        self.txt6.grid(column=1, row=7, padx=5)

        self.btn = Button(self, text="Подсчёт", command=self.clicked)
        self.btn.grid(column=2, row=8, padx=5)

        self.txt = scrolledtext.ScrolledText(self, width=40, height=10, state='disabled')
        self.txt.grid(column=2, row=2, rowspan=6, padx=5)

    def clicked(self):
        click1(self)


def main():
    window = Tk()
    MakeUI()
    window.title("Модели принятия коллективных решений")
    window.geometry('550x275')
    window.resizable(width=False, height=False)
    window.mainloop()


if __name__ == '__main__':
    main()
