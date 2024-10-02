from tkinter import *
import random
import tkinter.messagebox as tsmg

root = Tk()
root.geometry("600x600")  # Increased window size
root.title("GUI of Game")
# root.wm_iconbitmap("1.ico")
root.config(bg="yellow")

# Mapping choices to their names
choices = {1: "Stone", 2: "Paper", 3: "Scissors"}
choicesss = list(choices.keys())  # List of numerical choices

# Initialize scores
player_score = 0
computer_score = 0

# Create a frame for the rules
rules_frame = Frame(root, bg="black")
rules_frame.pack(side=LEFT, fill=Y, padx=4, pady=4)

# Display the rules
rules_text = """\
A] The responsive code is:\n\n
   1 - for Stone\n
   2 - for Paper\n
   3 - for Scissors\n
   4 -  Type 'exit' to end the game\n
"""
rules_label = Label(rules_frame, text=rules_text, font="lucida 10 bold", bg="black", fg="white", anchor='w')
rules_label.pack(anchor='nw', padx=6, pady=6)

heading = Label(text="Welcome to Stone Paper Scissors GAME", bg="black", fg="red", font="lucida 12 bold")
heading.pack(fill=X)

player1 = Label(text="Enter the code (1 for Stone, 2 for Paper, 3 for Scissors): ", fg="orange", bg="black", font="lucida 8 bold")
player1.pack(anchor='w', padx=6, pady=6, fill=X)
player1_var = StringVar()
player1_new = Entry(textvariable=player1_var)
player1_new.pack()

# Create a frame for the Text widget and Scrollbar
frame = Frame(root)
frame.pack(pady=10)

# Create a Text widget for displaying game results
text_area = Text(frame, width=60, height=20, bg="black", fg="white", font="lucida 10")  # Increased size
text_area.pack(side=LEFT)

# Create a Scrollbar
scrollbar = Scrollbar(frame, command=text_area.yview)
scrollbar.pack(side=RIGHT, fill=Y)

# Configure the Text widget to work with the Scrollbar
text_area.config(yscrollcommand=scrollbar.set,height=40,width=120)

# Score display
score_label = Label(text=f"Player Score: {player_score}   Computer Score: {computer_score}", bg="yellow", fg="blue", font="lucida 10 bold")
score_label.pack(pady=10)

def update_score():
    """Update the score display."""
    score_label.config(text=f"Player Score: {player_score}   Computer Score: {computer_score}")

def announce_winner():
    """Announce the winner before exiting."""
    if player_score > computer_score:
        winner_message = "Congratulations! You are the winner!"
    elif computer_score > player_score:
        winner_message = "Computer is the winner! Better luck next time."
    else:
        winner_message = "It's a tie! Well played by both!"
    
    tsmg.showinfo("Game Over", winner_message)
    root.destroy()

def somthing():
    global player_score, computer_score
    computer_choice = random.choice(choicesss)
    player_choice = player1_var.get()

    # Mapping numerical choices to their string representation
    computer_choice_str = choices[computer_choice]
    
    result_message = ""

    if player_choice == "exit":
        announce_winner()  # Announce the winner before exiting
        return
    
    try:
        player_choice_num = int(player_choice)
    except ValueError:
        result_message = f"Your input '{player_choice}' is not valid. Please enter 1, 2, or 3.\n"
        tsmg.showwarning("Incorrect value", "Please enter the correct value")
        text_area.insert(END, result_message)
        text_area.see(END)  # Scroll to the end
        return

    if player_choice_num not in choices:
        result_message = f"Your input '{player_choice}' is not valid. Please enter 1, 2, or 3.\n"
        tsmg.showwarning("Incorrect value", "Please enter the correct value")
        text_area.insert(END, result_message)
        text_area.see(END)  # Scroll to the end
        return

    player_choice_str = choices[player_choice_num]

    if player_choice_num == computer_choice:
        result_message = f"It's a tie! You both selected {player_choice_str}.\n\n"
    elif (player_choice_num == 1 and computer_choice == 2) or \
         (player_choice_num == 2 and computer_choice == 3) or \
         (player_choice_num == 3 and computer_choice == 1):
        result_message = f"Computer wins! Computer selected {computer_choice_str} and you selected {player_choice_str}.\n\n"
        computer_score += 1
    else:
        result_message = f"You win! You selected {player_choice_str} and computer selected {computer_choice_str}.\n\n"
        player_score += 1

    # Insert the result message into the Text widget
    text_area.insert(END, result_message)
    text_area.see(END)  # Scroll to the end
    
    # Update the scores display
    update_score()

but1 = Button(root, text="Play", command=somthing)
but1.pack(pady=4)

root.mainloop()