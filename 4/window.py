from tkinter import *
from tkinter import ttk

from systems import *



# Окно
window = Tk()
window.title("Коллективные решения")
window.geometry('500x250')
# Вкладки
tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab4 = ttk.Frame(tab_control)
tab5 = ttk.Frame(tab_control)
tab_control.add(tab1, text='1 Относительное большинство')
tab_control.add(tab2, text='2.1 Кондорсе')
tab_control.add(tab3, text='2.2 Копленд')
tab_control.add(tab4, text='2.3 Симпсон')
tab_control.add(tab5, text='3 Борд')

# Относительное большинство
lbl = Label(tab1, text="Привет", padx=10, pady=5, width=50)
lbl.grid(column=0, row=0)
txt = Entry(tab1, width=5)
txt.grid(column=1, row=0, padx=5)
btn = Button(tab1, text="Клик!", command=clicked)
btn.grid(column=2, row=1, padx=5)

# Кондорсе
# Копленд
# Симпсон
# Борд

tab_control.pack(expand=1, fill='both')
window.mainloop()