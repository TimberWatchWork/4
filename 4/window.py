from tkinter import *
from tkinter import ttk, scrolledtext
from systems import *


class MakeUI(Frame):

    def __init__(self, *args, **kwargs):

        # Heritage
        Frame.__init__(self, width=500, height=250, *args, **kwargs)
        self.pack(expand=1, fill='both')

        # Вкладки
        self.tab_control = ttk.Notebook(self)
        self.tab1 = ttk.Frame(self.tab_control)
        self.tab2 = ttk.Frame(self.tab_control)
        self.tab3 = ttk.Frame(self.tab_control)
        self.tab4 = ttk.Frame(self.tab_control)
        self.tab5 = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab1, text='1 Относительное большинство')
        self.tab_control.add(self.tab2, text='2.1 Кондорсе')
        self.tab_control.add(self.tab3, text='2.2 Копленд')
        self.tab_control.add(self.tab4, text='2.3 Симпсон')
        self.tab_control.add(self.tab5, text='3 Борд')

        # Относительное большинство
        var1 = IntVar()
        var2 = IntVar()
        var3 = IntVar()
        var4 = IntVar()
        var5 = IntVar()
        var6 = IntVar()
        var1.set(0), var2.set(0), var3.set(0), var4.set(0), var5.set(0), var6.set(0)
        self.lbl1 = Label(self.tab1, text="A > B > C", padx=10, pady=5, width=10)
        self.lbl1.grid(column=0, row=0)
        self.txt1 = Spinbox(self.tab1, width=5, from_=0, to=1000, textvariable=var1)
        self.txt1.grid(column=1, row=0, padx=5)
        self.lbl2 = Label(self.tab1, text="A > C > B", padx=10, pady=5, width=10)
        self.lbl2.grid(column=0, row=1)
        self.txt2 = Spinbox(self.tab1, width=5, from_=0, to=1000, textvariable=var2)
        self.txt2.grid(column=1, row=1, padx=5)
        self.lbl3 = Label(self.tab1, text="B > A > C", padx=10, pady=5, width=10)
        self.lbl3.grid(column=0, row=2)
        self.txt3 = Spinbox(self.tab1, width=5, from_=0, to=1000, textvariable=var3)
        self.txt3.grid(column=1, row=2, padx=5)
        self.lbl4 = Label(self.tab1, text="B > C > A", padx=10, pady=5, width=10)
        self.lbl4.grid(column=0, row=3)
        self.txt4 = Spinbox(self.tab1, width=5, from_=0, to=1000, textvariable=var4)
        self.txt4.grid(column=1, row=3, padx=5)
        self.lbl5 = Label(self.tab1, text="C > A > B", padx=10, pady=5, width=10)
        self.lbl5.grid(column=0, row=4)
        self.txt5 = Spinbox(self.tab1, width=5, from_=0, to=1000, textvariable=var5)
        self.txt5.grid(column=1, row=4, padx=5)
        self.lbl6 = Label(self.tab1, text="C > B > A", padx=10, pady=5, width=10)
        self.lbl6.grid(column=0, row=5)
        self.txt6 = Spinbox(self.tab1, width=5, from_=0, to=1000, textvariable=var6)
        self.txt6.grid(column=1, row=5, padx=5)

        # self.combo = Combobox(self.tab1)
        # self.combo['values'] = (1, 2, 3, 4, 5)
        # self.combo.current(0)  # установите вариант по умолчанию
        # self.combo.grid(column=0, row=6)

        self.btn = Button(self.tab1, text="Подсчёт", command=self.clicked)
        self.btn.grid(column=2, row=6, padx=5)

        self.txt = scrolledtext.ScrolledText(self.tab1, width=40, height=10, state='disabled')
        self.txt.grid(column=2, row=0, rowspan=6)

        self.tab_control.pack(expand=1, fill='both')

    def clicked(self):
        click1(self)


def main():
    window = Tk()
    MakeUI()
    window.title("Коллективные решения")
    window.geometry('500x250')
    window.mainloop()


if __name__ == '__main__':
    main()
