from tkinter import *


def btn_clicked():
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

img0 = PhotoImage(file = f"imageConvertWindow/img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 491, y = 328,
    width = 581,
    height = 131)


canvas.create_rectangle(
    0, 0, 0+313, 0+769,
    fill = "#127264",
    outline = "")


canvas.create_rectangle(
    313, 0, 313+966, 0+103,
    fill = "#127264",
    outline = "")

img1 = PhotoImage(file = f"imageConvertWindow/img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 11, y = 178,
    width = 292,
    height = 88)

img2 = PhotoImage(file = f"imageConvertWindow/img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b2.place(
    x = 11, y = 289,
    width = 292,
    height = 88)

img3 = PhotoImage(file = f"imageConvertWindow/img3.png")
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b3.place(
    x = 11, y = 400,
    width = 292,
    height = 88)

img4 = PhotoImage(file = f"imageConvertWindow/img4.png")
b4 = Button(
    image = img4,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b4.place(
    x = 11, y = 511,
    width = 292,
    height = 88)

img5 = PhotoImage(file = f"imageConvertWindow/img5.png")
b5 = Button(
    image = img5,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b5.place(
    x = 1148, y = 20,
    width = 50,
    height = 50)

img6 = PhotoImage(file = f"imageConvertWindow/img6.png")
b6 = Button(
    image = img6,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b6.place(
    x = 1068, y = 20,
    width = 50,
    height = 50)

img7 = PhotoImage(file = f"imageConvertWindow/img7.png")
b7 = Button(
    image = img7,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b7.place(
    x = 978, y = 20,
    width = 50,
    height = 50)

img8 = PhotoImage(file = f"imageConvertWindow/img8.png")
b8 = Button(
    image = img8,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b8.place(
    x = 1797, y = -272,
    width = 90,
    height = 160)

img9 = PhotoImage(file = f"imageConvertWindow/img9.png")
b9 = Button(
    image = img9,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b9.place(
    x = 1456, y = -229,
    width = 90,
    height = 160)

img10 = PhotoImage(file = f"imageConvertWindow/img10.png")
b10 = Button(
    image = img10,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b10.place(
    x = 1575, y = -251,
    width = 90,
    height = 160)

img11 = PhotoImage(file = f"imageConvertWindow/img11.png")
b11 = Button(
    image = img11,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b11.place(
    x = 491, y = 499,
    width = 581,
    height = 131)

canvas.create_text(
    782.0, 183.5,
    text = "CONVERTIR DOCUMENTOS",
    fill = "#000000",
    font = ("Verdana-Bold", int(40.0)))

canvas.create_text(
    784.5, 274.0,
    text = "Seleccione una opción",
    fill = "#000000",
    font = ("Verdana-Bold", int(24.0)))

window.resizable(False, False)
window.mainloop()