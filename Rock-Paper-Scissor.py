import tkinter as tk
import random

def play_game(user_choice):
    choices = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(choices)
    
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Paper' and computer_choice == 'Rock') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper'):
        result = "You win!"
    else:
        result = "You lose!"
    
    # Update the result label
    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")

# Create the main window
root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("400x300")
root.configure(bg='#f5f5f5')

# Create a main frame to hold the buttons and result label
main_frame = tk.Frame(root, bg='#f5f5f5')
main_frame.pack(pady=20)

# Create and place buttons for Rock, Paper, and Scissors
button_font = ('Arial', 14, 'bold')
button_width = 12
button_height = 2

rock_button = tk.Button(main_frame, text="Rock", width=button_width, height=button_height, font=button_font, bg='#e57373', fg='white', command=lambda: play_game('Rock'))
rock_button.grid(row=0, column=0, padx=10, pady=10)

paper_button = tk.Button(main_frame, text="Paper", width=button_width, height=button_height, font=button_font, bg='#64b5f6', fg='white', command=lambda: play_game('Paper'))
paper_button.grid(row=0, column=1, padx=10, pady=10)

scissors_button = tk.Button(main_frame, text="Scissors", width=button_width, height=button_height, font=button_font, bg='#81c784', fg='white', command=lambda: play_game('Scissors'))
scissors_button.grid(row=0, column=2, padx=10, pady=10)

# Create a label to display the result
result_label = tk.Label(root, text="", font=('Arial', 16, 'bold'), bg='#f5f5f5')
result_label.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
