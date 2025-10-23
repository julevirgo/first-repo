import turtle

# Fenster einrichten
window = turtle.Screen()
window.bgcolor("white")
window.title("Ein Herz mit Turtle")

# Turtle konfigurieren
pen = turtle.Turtle()
pen.fillcolor("red")
pen.speed(2)

# Herz zeichnen
pen.begin_fill()
pen.left(140)
pen.forward(180)
pen.circle(-90, 200)
pen.left(120)
pen.circle(-90, 200)
pen.forward(180)
pen.end_fill()

# Fenster offen halten
pen.hideturtle()
window.mainloop()
