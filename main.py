from turtle import Turtle, Screen
import pandas

turtle = Turtle()
screen = Screen()
screen.title("US STATE GAME")
screen.bgpic("./Day_25_csv_file_&_pandas/final_game/blank_states_img.gif")

data = pandas.read_csv("./Day_25_csv_file_&_pandas/final_game/50_states.csv")
all_states = data.state.str.title().to_list()  # Convert to lowercase and remove extra spaces
guesses_states= []

while len(guesses_states) < 50:
    answer_state = screen.textinput(f"{len(guesses_states)}/50 states", "What's another state's name?").title()
    print(answer_state) 


    if answer_state == "Exit":  #if user want to exit
#using lis comprehension to make the below code shorter 
        missing_states= [state for state in all_states if state not in guesses_states]
    #     missing_states= []
    #     for states in all_states:
    #         if states not in guesses_states:
    #             missing_states.append(states)

        print(missing_states)
        print(len(missing_states))

        left_states= pandas.DataFrame(missing_states)
        left_states.to_csv(("./Day_25_csv_file_&_pandas/final_game/left_out_states.csv"))
        break

    if answer_state in all_states:  # Convert input to lowercase and remove extra spaces
        guesses_states.append(answer_state)
        t = Turtle()
        t.color("black")
        t.penup() 
        t.hideturtle()
        row_data = data[data.state == answer_state]  # Convert state names for comparison
        t.goto(int(row_data.x), int(row_data.y))
        t.write(answer_state)

screen.exitonclick()