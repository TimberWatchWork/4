import tkinter as tk


def click1(UI):
    method = UI.combo.get()[0]
    winner = ""
    # Метод относительного большинства
    if method == "1":
        # Подсчитываем голоса
        a = int(UI.txt1.get()) + int(UI.txt2.get())
        b = int(UI.txt3.get()) + int(UI.txt4.get())
        c = int(UI.txt5.get()) + int(UI.txt6.get())
        # Определяем победителя
        m, i = a, 0
        if b > m: m = b
        if c > m: m = c
        if m == a: winner = "Победил кандидат A"; i += 1
        if m == b: winner = "Победил кандидат B"; i += 1
        if m == c: winner = "Победил кандидат C"; i += 1
        if i > 1: winner = "Ничья, победителя нет"
        # Выводим результаты
        UI.txt.configure(state='normal')
        UI.txt.delete("1.0", "end")
        UI.txt.insert(tk.INSERT, f'Подсчёт голосов: \n'
                                 f"за кандидата А: {a} голосов \n"
                                 f"за кандидата B: {b} голосов \n"
                                 f"за кандидата C: {c} голосов \n"
                                 f"{winner} \n")
        UI.txt.configure(state='disabled')

    # Метод Кондорсе
    if method == "2":
        # Подсчет победителей в каждой паре
        ab = int(UI.txt1.get()) + int(UI.txt2.get()) + int(UI.txt5.get())
        ba = int(UI.txt3.get()) + int(UI.txt4.get()) + int(UI.txt5.get())
        ac = int(UI.txt1.get()) + int(UI.txt2.get()) + int(UI.txt3.get())
        ca = int(UI.txt4.get()) + int(UI.txt5.get()) + int(UI.txt6.get())
        bc = int(UI.txt1.get()) + int(UI.txt3.get()) + int(UI.txt4.get())
        cb = int(UI.txt2.get()) + int(UI.txt5.get()) + int(UI.txt6.get())

        if ab > ba: zab = "A "+str(ab)+" > B "+str(ba)
        elif ab == ba: zab = "A "+str(ab)+" = B "+str(ba)
        else: zab = "B "+str(ba)+" > A "+str(ab)

        if bc > cb: zbc = "B "+str(bc)+" > C "+str(cb)
        elif bc == cb: zbc = "B "+str(bc)+" = C "+str(cb)
        else: zbc = "C "+str(cb)+" > B "+str(bc)

        if ac > ca: zac = "A "+str(ac)+" > C "+str(ca)
        elif ac == ca: zac = "A "+str(ac)+" = C "+str(ca)
        else: zac = "C "+str(ca)+" > A "+str(ac)

        if (ab > ba) & (ac > ca): winner = "Победил кандидат A"
        elif (ba > ab) & (bc > cb): winner = "Победил кандидат B"
        elif (cb > bc) & (ca > ac): winner = "Победил кандидат C"
        else: winner = "Ничья, победителя нет"
        # Выводим результаты
        UI.txt.configure(state='normal')
        UI.txt.delete("1.0", "end")
        UI.txt.insert(tk.INSERT, f'Попарное сравнение: \n'
                                 f"{zab} \n"
                                 f"{zbc} \n"
                                 f"{zac} \n"
                                 f"{winner} \n")
        UI.txt.configure(state='disabled')

