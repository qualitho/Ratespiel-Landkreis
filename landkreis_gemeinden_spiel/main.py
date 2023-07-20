import turtle, pandas as pn

gemeinden_df = pn.read_csv("gemeinden.csv")
gemeinden_list = gemeinden_df.state.to_list()
x_cord_list = gemeinden_df.x.to_list()
y_cord_list = gemeinden_df.y.to_list()
erratene_gemeinden_list = []
anzahl_gemeinden = len(gemeinden_list)

with open("high_score.txt") as file:
    high_score = int(file.readline())
print(high_score)

punktezahl = 0

screen = turtle.Screen()
screen.setup(width=1330, height=750)
screen.bgpic("karte_landkreis_aschaffenburg.gif")
screen.title("Ratespiel Gemeinden - Landkreis Aschaffenburg")
writer = turtle.Turtle()
writer.color("white")
writer.penup()
writer.hideturtle()

game_on = True


def punktezahl_gueltig():
    return punktezahl <= anzahl_gemeinden


def schreibe_high_score(neuer_punktestand):
    global high_score
    if neuer_punktestand > high_score:
        high_score = neuer_punktestand


while game_on:

    eingabe = screen.textinput(title=f"Punktestand: {punktezahl}/{anzahl_gemeinden}",
                               prompt="Rate eine Gemeinde:").title()

    if eingabe in gemeinden_list and eingabe not in erratene_gemeinden_list and punktezahl_gueltig():
        index = gemeinden_list.index(eingabe)
        writer.goto(x_cord_list[index], y_cord_list[index])
        writer.write(gemeinden_list[index])
        erratene_gemeinden_list.append(eingabe)
        punktezahl += 1
        schreibe_high_score(punktezahl)

    else:
        writer.goto(-200, 0)
        writer.write(f"GAME OVER - Finaler Punktestand: {punktezahl}/{anzahl_gemeinden}", font=("arial", 20, "bold"))
        writer.goto(-100, -100)
        writer.write(f"High Score: {high_score}", font=("arial", 20, "bold"))
        with open("high_score.txt", "w") as file:
            file.write(str(high_score))
        game_on = False

turtle.mainloop()
