import turtle

# Funktion, die das Herz mit Text zeichnet
def zeichne_herz(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()

    # Herz zeichnen
    pen.color("red", "pink")
    pen.begin_fill()

    pen.setheading(140)
    pen.forward(180)
    pen.circle(-90, 200)
    pen.left(120)
    pen.circle(-90, 200)
    pen.forward(180)

    pen.end_fill()

    # Text über dem Herz anzeigen
    pen.penup()
    pen.goto(x, y + 120)
    pen.color("black")
    pen.write("Du bist süß", align="center", font=("Lucida Handwriting", 20, "bold"))

    pen.setheading(0)  # Ausrichtung zurücksetzen

# Fenster einrichten
window = turtle.Screen()
window.bgcolor("black")
window.title("Klicke, um ein Herz zu zeichnen 💖")

# Turtle konfigurieren
pen = turtle.Turtle()
pen.speed(2)
pen.hideturtle
# Wenn mit der Maus geklickt wird, Herz mit Text zeichnen
window.onclick(zeichne_herz)

# Fenster offen halten
window.mainloop()