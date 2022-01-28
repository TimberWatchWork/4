import tkinter as tk


def get_winner(a,b,c):
    # Определяем победителя
    m, i, winner = a, 0, ""
    if b > m: m = b
    if c > m: m = c
    if m == a: winner = "Победил кандидат A"; i += 1
    if m == b: winner = "Победил кандидат B"; i += 1
    if m == c: winner = "Победил кандидат C"; i += 1
    if i > 1: winner = "Ничья, победителя нет"
    return winner


def print_result(UI, one, two, three, four, winner):
    # Выводим результаты
    UI.txt.configure(state='normal')
    UI.txt.delete("1.0", "end")
    UI.txt.insert(tk.INSERT, f"{one} \n"
                             f"{two} \n"
                             f"{three} \n"
                             f"{four} \n"
                             f"{winner} \n")
    UI.txt.configure(state='disabled')


def click1(UI):
    method = UI.combo.get()[0]
    winner, a, b, c = "", 0, 0, 0
    # Метод относительного большинства
    if method == "1":
        # Подсчитываем голоса
        a = int(UI.txt1.get()) + int(UI.txt2.get())
        b = int(UI.txt3.get()) + int(UI.txt4.get())
        c = int(UI.txt5.get()) + int(UI.txt6.get())
        # Определяем победителя
        # m, i = a, 0
        # if b > m: m = b
        # if c > m: m = c
        # if m == a: winner = "Победил кандидат A"; i += 1
        # if m == b: winner = "Победил кандидат B"; i += 1
        # if m == c: winner = "Победил кандидат C"; i += 1
        # if i > 1: winner = "Ничья, победителя нет"
        winner = get_winner(a, b, c)
        # Выводим результаты
        # UI.txt.configure(state='normal')
        # UI.txt.delete("1.0", "end")
        # UI.txt.insert(tk.INSERT, f'Подсчёт голосов: \n'
        #                          f"за кандидата А: {a} голосов \n"
        #                          f"за кандидата B: {b} голосов \n"
        #                          f"за кандидата C: {c} голосов \n"
        #                          f"{winner} \n")
        # UI.txt.configure(state='disabled')
        print_result(UI, "Подсчёт голосов:",
                     f"за кандидата А: {a} голосов",
                     f"за кандидата B: {b} голосов",
                     f"за кандидата C: {c} голосов",
                     winner)

    # Метод Кондорсе
    if method in ["2","3","4"]:
        # Подсчет победителей в каждой паре
        ab = int(UI.txt1.get()) + int(UI.txt2.get()) + int(UI.txt5.get())
        ba = int(UI.txt3.get()) + int(UI.txt4.get()) + int(UI.txt6.get())
        ac = int(UI.txt1.get()) + int(UI.txt2.get()) + int(UI.txt3.get())
        ca = int(UI.txt4.get()) + int(UI.txt5.get()) + int(UI.txt6.get())
        bc = int(UI.txt1.get()) + int(UI.txt3.get()) + int(UI.txt4.get())
        cb = int(UI.txt2.get()) + int(UI.txt5.get()) + int(UI.txt6.get())

        if method == "2":
            # Модель Кондорсе: явный победитель
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
            # UI.txt.configure(state='normal')
            # UI.txt.delete("1.0", "end")
            # UI.txt.insert(tk.INSERT, f'Попарное сравнение: \n'
            #                          f"{zab} \n"
            #                          f"{zbc} \n"
            #                          f"{zac} \n"
            #                          f"{winner} \n")
            # UI.txt.configure(state='disabled')

            print_result(UI, "Попарное сравнение:", zab, zbc, zac, winner)

        if method == "3":
            # Модель Кондорсе: Правило Копленда
            if ab > ba: a += 1; b -= 1
            elif ab < ba: a -= 1; b += 1

            if bc > cb: b += 1; c -= 1
            elif bc < cb: b -= 1; c += 1

            if ac > ca: a += 1; c -= 1
            elif ca > ac: a -= 1; c += 1

            winner = get_winner(a,b,c)
            print_result(UI, "Оценка Копленда:",
                         f"A {a}",
                         f"B {b}",
                         f"C {c}",
                         winner)



