import turtle
import pandas as pd

screen =turtle.Screen()
screen.title('Guess States')
image = "India-locator-map-blank.gif" 
screen.addshape(image) #Adding image shape to screen
turtle.shape(image) 

#getting all states
data = pd.read_csv("India-coords.csv")
all_states = data.state.to_list() #Storing all state name to all_state variable
guess_states = [] #Creating a list, List will store all guess states by user
wrong_guess = [] #Creating a list, List will store all WRONG guess states by user

while len(guess_states) < len(all_states):
    # Taking state name from user
    answer_state = screen.textinput(title=f"{len(guess_states)}/{len(all_states)} Guess States", prompt="What's another state name").title()
    print("\nYou Entered state ->",answer_state)

    if answer_state == 'Exit':
        # Using for loop
        # missing_states = []
        # for state in all_states:
        #     missing_states.append(state)

        # Using List comprehension
        missing_states = [state for state in all_states if state not in guess_states]

        #Creating Datatframe of missed states
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("missed_data") #Storing missed states by user in csv file
        break

    #checking user input & states
    if answer_state =="":
        print("PLs enter state")
    #if user guessed correct state then we create a turtle.
    elif answer_state in all_states:
        guess_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data_row = data[data.state == answer_state]#checking if answer_state is equal to state in csv file & storing row in state_data_row
        t.goto(int(state_data_row.x), int(state_data_row.y)) #turtle go to x and y co-ordinates of that row
        t.write(answer_state) #writing answer satate in map
        print("State -> "+answer_state+" corr ->",int(state_data_row.x), ", ",int(state_data_row.y))

    else:
        wrong_guess.append(answer_state)
        print("Wrong guess ->",answer_state)
        print('Your wrong Guess -> ', wrong_guess)
        print('Total Wrong guess  ->',len(wrong_guess))

