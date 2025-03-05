#imoort Libraries
from tkinter import *
from tkinter import messagebox
# Make Tic_Tac_Toe class 
class Tic_Tac_Toe:
    def __init__(self, root):
        self.root = root  # Main Window
        self.root.title("Tic Tac Toe") # Set The Title
        self.current_player = "X" # Initialize Current Player When You start game 
        self.board = [""] * 9 # Make 9 empty game board
        self.buttons = [] #list of hold button widgets
        self.create_buttons() # Call method to create buttons
    # Make create_buttons Method
    def create_buttons(self):
        for i in range(9): # loop from 0 to 8
            button = Button(self.root, text="", font="Arial 20", width=5, height=5, bg="orange" , fg="black" ,  command=lambda i=i: self.make_move(i)) #create button
            button.grid(row=i // 3, column=i % 3) # Arrange button in fgrid
            self.buttons.append(button) # Add button to the List
    # Make make_move Method 
    def make_move(self, index):
        if self.board[index] == "": # Check if the index in board is empty
            self.board[index] = self.current_player # Make the player begain to play
            self.buttons[index].config(text=self.current_player) # Update the button text
            if self.check_winner(): # Check the player is winner
                messagebox.showinfo("Congratulations", f"Player {self.current_player} is Winner!") #show the winner message
                self.reset_game() # reset the empty board again !
            elif "" not in self.board: # the boards are full
                messagebox.showinfo("Hard Luck!", "It is a Tie!") # show the tie message
                self.reset_game() # reset the empty board again !
            else: 
                # switch players
                self.current_player = "O" if self.current_player == "X" else "X"
    # Make check_winner Method
    def check_winner(self):
        win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)] #Defining the Winning buttons
        for a, b, c in win_conditions: # loop through winning buttons
            if self.board[a] == self.board[b] == self.board[c] != "":
                return True # return true if winning condtion is met
        return False # return false if no winner

    def reset_game(self): 
        self.board = [""] * 9 #clear the board
        for button in self.buttons: #loop  for clean board
            button.config(text="")
        self.current_player = "X" #reset current player to "X"
# Main Execution block
if __name__ == "__main__":
    root = Tk() #create main window
    game = Tic_Tac_Toe(root) # instantiate the tictactoe class
    root.mainloop() # run the event