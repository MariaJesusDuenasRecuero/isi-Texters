from tkinter import *

from click import command


def convertir():
    window.withdraw()
    Convertwindow = Tk()

    Convertwindow.geometry("1279x769")
    Convertwindow.configure(bg = "#ffffff")
    Convertcanvas = Canvas(
        Convertwindow,
        bg = "#ffffff",
        height = 769,
        width = 1279,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    Convertcanvas.place(x = 0, y = 0)

    Convertimg0 = PhotoImage(file = f"imageConvertWindow/img0.png")
    Convertb0 = Button(
        image = Convertimg0,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked,
        relief = "flat")

    Convertb0.place(
        x = 491, y = 328,
        width = 581,
        height = 131)


    Convertcanvas.create_rectangle(
        0, 0, 0+313, 0+769,
        fill = "#127264",
        outline = "")


    Convertcanvas.create_rectangle(
        313, 0, 313+966, 0+103,
        fill = "#127264",
        outline = "")

    Convertimg1 = PhotoImage(file = f"imageConvertWindow/img1.png")
    Convertb1 = Button(
        image = Convertimg1,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked,
        relief = "flat")

    Convertb1.place(
        x = 11, y = 178,
        width = 292,
        height = 88)

    Convertimg2 = PhotoImage(file = f"imageConvertWindow/img2.png")
    Convertb2 = Button(
        image = Convertimg2,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked,
        relief = "flat")

    Convertb2.place(
        x = 11, y = 289,
        width = 292,
        height = 88)

    Convertimg3 = PhotoImage(file = f"imageConvertWindow/img3.png")
    Convertb3 = Button(
        image = Convertimg3,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked,
        relief = "flat")

    Convertb3.place(
        x = 11, y = 400,
        width = 292,
        height = 88)

    Convertimg4 = PhotoImage(file = f"imageConvertWindow/img4.png")
    Convertb4 = Button(
        image = Convertimg4,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked,
        relief = "flat")

    Convertb4.place(
        x = 11, y = 511,
        width = 292,
        height = 88)

    Convertimg5 = PhotoImage(file = f"imageConvertWindow/img5.png")
    Convertb5 = Button(
        image = Convertimg5,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked,
        relief = "flat")

    Convertb5.place(
        x = 1148, y = 20,
        width = 50,
        height = 50)

    Convertimg6 = PhotoImage(file = f"imageConvertWindow/img6.png")
    Convertb6 = Button(
        image = Convertimg6,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked,
        relief = "flat")

    Convertb6.place(
        x = 1068, y = 20,
        width = 50,
        height = 50)

    Convertimg7 = PhotoImage(file = f"imageConvertWindow/img7.png")
    Convertb7 = Button(
        image = Convertimg7,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked,
        relief = "flat")

    Convertb7.place(
        x = 978, y = 20,
        width = 50,
        height = 50)

    Convertimg8 = PhotoImage(file = f"imageConvertWindow/img8.png")
    Convertb8 = Button(
        image = Convertimg8,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked,
        relief = "flat")

    Convertb8.place(
        x = 1797, y = -272,
        width = 90,
        height = 160)

    Convertimg9 = PhotoImage(file = f"imageConvertWindow/img9.png")
    Convertb9 = Button(
        image = Convertimg9,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked,
        relief = "flat")

    Convertb9.place(
        x = 1456, y = -229,
        width = 90,
        height = 160)

    Convertimg10 = PhotoImage(file = f"imageConvertWindow/img10.png")
    Convertb10 = Button(
        image = Convertimg10,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked,
        relief = "flat")

    Convertb10.place(
        x = 1575, y = -251,
        width = 90,
        height = 160)

    Convertimg11 = PhotoImage(file = f"imageConvertWindow/img11.png")
    Convertb11 = Button(
        image = Convertimg11,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked,
        relief = "flat")

    Convertb11.place(
        x = 491, y = 499,
        width = 581,
        height = 131)

    Convertcanvas.create_text(
        782.0, 183.5,
        text = "CONVERTIR DOCUMENTOS",
        fill = "#000000",
        font = ("Verdana-Bold", int(40.0)))

    Convertcanvas.create_text(
        784.5, 274.0,
        text = "Seleccione una opción",
        fill = "#000000",
        font = ("Verdana-Bold", int(24.0)))

    Convertwindow.resizable(False, False)

def btn_clicked(): #borrar cuando esten todas las ventanas implementadas
    print("Button Clicked")


window = Tk()

window.geometry("1279x769")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 769,
    width = 1279,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)


canvas.create_rectangle(
    0, 0, 0+313, 0+769,
    fill = "#127264",
    outline = "")


canvas.create_rectangle(
    313, 0, 313+966, 0+103,
    fill = "#127264",
    outline = "")

img0 = PhotoImage(file = f"imageMainWindow/img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = convertir,
    relief = "flat")

b0.place(
    x = 11, y = 178,
    width = 292,
    height = 88)

img1 = PhotoImage(file = f"imageMainWindow/img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    relief = "flat")

b1.place(
    x = 11, y = 289,
    width = 292,
    height = 88)

img2 = PhotoImage(file = f"imageMainWindow/img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    relief = "flat")

b2.place(
    x = 11, y = 400,
    width = 292,
    height = 88)

img3 = PhotoImage(file = f"imageMainWindow/img3.png")
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    relief = "flat")

b3.place(
    x = 11, y = 511,
    width = 292,
    height = 88)

img4 = PhotoImage(file = f"imageMainWindow/img4.png")
b4 = Button(
    image = img4,
    borderwidth = 0,
    highlightthickness = 0,
    relief = "flat")

b4.place(
    x = 1148, y = 20,
    width = 50,
    height = 50)

img5 = PhotoImage(file = f"imageMainWindow/img5.png")
b5 = Button(
    image = img5,
    borderwidth = 0,
    highlightthickness = 0,
    relief = "flat")

b5.place(
    x = 1068, y = 20,
    width = 50,
    height = 50)

img6 = PhotoImage(file = f"imageMainWindow/img6.png")
b6 = Button(
    image = img6,
    borderwidth = 0,
    highlightthickness = 0,
    relief = "flat")

b6.place(
    x = 978, y = 20,
    width = 50,
    height = 50)

window.resizable(False, False)
window.mainloop()



