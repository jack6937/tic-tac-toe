from tkinter import *
import tkinter.messagebox

def checked(i) :
      global player
      button = list[i]

      if button["text"] != "     " :
            return
      button["text"] = player 
      button["bg"] = "yellow"

      if player == "X" :
            player = "O"
            button["bg"] = "yellow"
            winner_check()
      else :
            player = "X"
            button["bg"] = "lightgreen"
            winner_check()

window = Tk()
player = "X"
list= []

for i in range(9) :
      b = Button(window, text="     ", command=lambda k=i: checked(k))
      b.grid(row=i//3, column=i%3)
      list.append(b)
      
def winner_check():
       if list[0]["text"] == list[3]["text"] == list[6]["text"] != "     ":
            win()
       elif list[1]["text"] == list[4]["text"] == list[7]["text"] != "     ":
            win()   
       elif list[2]["text"] == list[5]["text"] == list[8]["text"] != "     ":
            win()
       elif list[0]["text"] == list[1]["text"] == list[2]["text"] != "     ":
            win()
       elif list[3]["text"] == list[4]["text"] == list[5]["text"] != "     ":
            win()
       elif list[6]["text"] == list[7]["text"] == list[8]["text"] != "     ":
            win()
       elif list[0]["text"] == list[4]["text"] == list[8]["text"] != "     ":
            win()
       elif list[2]["text"] == list[4]["text"] == list[6]["text"] != "     ":
            win()
       elif list[0]["text"] != "     " and list[1]["text"] != "     " and list[2]["text"] != "     " and list[3]["text"] != "     " and list[4]["text"] != "     "  and list[5]["text"] != "     "  and list[6]["text"] != "     " and list[7]["text"] != "     " and list[8]["text"] != "     ":
            draw()
def draw():
           tkinter.messagebox.showinfo("who is winner?", "draw")
           quit()
def win():
      if player == "X":
            tkinter.messagebox.showinfo("who is winner?", "player 0 win")
            quit()
      else:
            tkinter.messagebox.showinfo("who is winner?", "player X win")
            quit()

window.mainloop()


