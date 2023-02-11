from tkinter import *
from tkinter import messagebox

player = "X"
game_over = False

def check_for_winner():
    global game_over
    winner = None
    if (button1["text"] == button2["text"] == button3["text"] != " ") or \
        (button4["text"] == button5["text"] == button6["text"] != " ") or \
        (button7["text"] == button8["text"] == button9["text"] != " ") or \
        (button1["text"] == button4["text"] == button7["text"] != " ") or \
        (button2["text"] == button5["text"] == button8["text"] != " ") or \
        (button3["text"] == button6["text"] == button9["text"] != " ") or \
        (button1["text"] == button5["text"] == button9["text"] != " ") or \
        (button3["text"] == button5["text"] == button7["text"] != " "):
        winner = player
        game_over = True
        messagebox.showinfo("Gagnant", f"Le joueur {winner} a gagné!")
    elif " " not in [button1["text"], button2["text"], button3["text"], button4["text"], button5["text"], button6["text"], button7["text"], button8["text"], button9["text"]]:
        game_over = True
        messagebox.showinfo("Match nul", "Match nul!")

def button_click(button):
    global player
    global game_over
    if button["text"] == " " and not game_over:
        button["text"] = player
        check_for_winner()
        if player == "X":
            player = "O"
        else:
            player = "X"

def reset_game():
    global player
    global game_over
    player = "X"
    game_over = False
    button1["text"] = " "
    button2["text"] = " "
    button3["text"] = " "
    button4["text"] = " "
    button5["text"] = " "
    button6["text"] = " "
    button7["text"] = " "
    button8["text"] = " "
    button9["text"] = " "

root = Tk()
root.title("Tic Tac Toe")

button1 = Button(root, text=" ", width=5, height=2, font=("Arial", 20), command=lambda: button_click(button1))
button2 = Button(root, text=" ", width=5, height=2, font=("Arial", 20), command=lambda: button_click(button2))
button3 = Button(root, text=" ", width=5, height=2, font=("Arial", 20), command=lambda:   button_click(button3))
button4 = Button(root, text=" ", width=5, height=2, font=("Arial", 20), command=lambda: button_click(button4))
button5 = Button(root, text=" ", width=5, height=2, font=("Arial", 20), command=lambda: button_click(button5))
button6 = Button(root, text=" ", width=5, height=2, font=("Arial", 20), command=lambda: button_click(button6))
button7 = Button(root, text=" ", width=5, height=2, font=("Arial", 20), command=lambda: button_click(button7))
button8 = Button(root, text=" ", width=5, height=2, font=("Arial", 20), command=lambda: button_click(button8))
button9 = Button(root, text=" ", width=5, height=2, font=("Arial", 20), command=lambda: button_click(button9))
reset_button = Button(root, text="réset", width=6, height=1, font=("Arial", 12), command=reset_game)

button1.grid(row=0, column=0)
button2.grid(row=0, column=1)
button3.grid(row=0, column=2)
button4.grid(row=1, column=0)
button5.grid(row=1, column=1)
button6.grid(row=1, column=2)
button7.grid(row=2, column=0)
button8.grid(row=2, column=1)
button9.grid(row=2, column=2)
reset_button.grid(row=3, column=1)

root.mainloop()

