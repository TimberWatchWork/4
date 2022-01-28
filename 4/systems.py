import tkinter as tk


def get_winner(a, b, c):
    # Определяем победителя
    m, i, winner = a, 0, ""
    if b > m: m = b
    if c > m: m = c
    if m == a: winner = "Победил кандидат A"; i += 1
    if m == b: winner = "Победил кандидат B"; i += 1
    if m == c: winner = "Победил кандидат C"; i += 1
    if i > 1: winner = "Ничья, победителя нет"
    return winner


def print_result(UI, title, one, two, three, four, winner):
    # Выводим результаты
    UI.txt.configure(state='normal')
    UI.txt.delete("1.0", "end")
    UI.txt.insert(tk.INSERT, f"{title} \n"
                             "\n"
                             f"{one} \n"
                             f"{two} \n"
                             f"{three} \n"
                             f"{four} \n"
                             "\n"
                             f"{winner} \n")
    UI.txt.configure(state='disabled')


def click1(UI):
    method = UI.combo.get()[0]
    winner, a, b, c = "", 0, 0, 0

    # Модель относительного большинства
    if method == "1":
        # Подсчитываем голоса
        a = int(UI.txt1.get()) + int(UI.txt2.get())
        b = int(UI.txt3.get()) + int(UI.txt4.get())
        c = int(UI.txt5.get()) + int(UI.txt6.get())

        winner = get_winner(a, b, c)
        print_result(UI,
                     "Модель относительного большинства",
                     "Подсчёт голосов:",
                     f"за кандидата А: {a} голосов",
                     f"за кандидата B: {b} голосов",
                     f"за кандидата C: {c} голосов",
                     winner)

    # Модель Кондорсе
    if method in ["2", "3", "4"]:
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

            print_result(UI, "Модель Кондорсе: явный победитель", "Попарное сравнение:", zab, zbc, zac, winner)

        if method == "3":
            # Модель Кондорсе: Правило Копленда
            # Считаем оценки Копленда
            if ab > ba: a += 1; b -= 1
            elif ab < ba: a -= 1; b += 1

            if bc > cb: b += 1; c -= 1
            elif bc < cb: b -= 1; c += 1

            if ac > ca: a += 1; c -= 1
            elif ca > ac: a -= 1; c += 1

            winner = get_winner(a, b, c)
            print_result(UI,
                         "Модель Кондорсе: Правило Копленда",
                         "Оценка Копленда:",
                         f"A {a}",
                         f"B {b}",
                         f"C {c}",
                         winner)

        if method == "4":
            # Модель Кондорсе: Правило Симпсона
            # Считаем оценки Симпсона
            if ab < ac: a = ab
            else: a = ac

            if ba < bc: b = ba
            else: b = bc

            if ca < cb: c = ca
            else: c = cb

            winner = get_winner(a, b, c)
            print_result(UI,
                         "Модель Кондорсе: Правило Симпсона",
                         "Победы в парах и оценка Симпсона:",
                         f"A {ab}, {ac}; оценка: {a}",
                         f"B {ba}, {bc}; оценка: {b}",
                         f"C {ca}, {cb}; оценка: {c}",
                         winner)

    if method == "5":
        # Модель Борда
        a = 2 * int(UI.txt1.get()) + 2 * int(UI.txt2.get()) + int(UI.txt3.get()) + int(UI.txt5.get())
        b = 2 * int(UI.txt3.get()) + 2 * int(UI.txt4.get()) + int(UI.txt1.get()) + int(UI.txt6.get())
        c = 2 * int(UI.txt5.get()) + 2 * int(UI.txt6.get()) + int(UI.txt2.get()) + int(UI.txt4.get())

        winner = get_winner(a, b, c)
        print_result(UI,
                     "Модель Борда",
                     "Сумма очков:",
                     f"A {a}",
                     f"B {b}",
                     f"C {c}",
                     winner)
