import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_state = data.state.to_list()

guessed_state = []

while len(guessed_state) < 50:

    new_ans_state = screen.textinput(title=f"{len(guessed_state)}/50", prompt="What is the state name?").title()


    if new_ans_state == "Exit":
        missing_state=[]
        for state in all_state:
            if state not in guessed_state:
                missing_state.append(state)
        new_data=pandas.DataFrame(missing_state)
        new_data.to_csv("States_to_learn.csv ")
        break

    if new_ans_state in all_state:
        guessed_state.append(new_ans_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == new_ans_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(new_ans_state)


