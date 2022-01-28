import tkinter as tk

def click1(UI):
    # res = "Привет {}".format(UI.txt1.get())
    a = int(UI.txt1.get()) + int(UI.txt2.get())
    b = int(UI.txt3.get()) + int(UI.txt4.get())
    c = int(UI.txt5.get()) + int(UI.txt6.get())
    m, i, winner = a, 0, ""
    if b > m:
        m = b
    if c > m:
        m = c
    print('m= ', m)
    if m == a:
        winner = "Победил кандидат A"
        i += 1
    if m == b:
        winner = "Победил кандидат B"
        i += 1
    if m == c:
        winner = "Победил кандидат C"
        i += 1
    print('i= ', i)
    if i > 1:
        winner = "Ничья, победителя нет"
    print('winner= ', winner)

    UI.txt.configure(state='normal')
    UI.txt.delete("1.0", "end")
    UI.txt.insert(tk.INSERT, f'Подсчёт голосов: \n'
                             f"за кандидата А: {a} голосов \n"
                             f"за кандидата B: {b} голосов \n"
                             f"за кандидата C: {c} голосов \n"
                             f"{winner} \n")
    UI.txt.configure(state='disabled')
