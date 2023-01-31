import tkinter
from tkinter import ttk
from PIL import ImageTk, Image  

#Player class for storing progress
class Player:
  click_count = 0
  level = 1
  money = 0
  xp_goal = 10

  def registerClick(self, buttonPressed):
    self.click_count += 1

    if (self.click_count >= self.xp_goal):
      self.level += 1
      self.click_count = 0
      self.xp_goal = (self.level * 5) * self.level

#Create player
player = Player()

#Create library of Zack Lee evolutions
evolutions = ["ZackLee-Baby.webp", "ZackLee-Kid.png", "ZackLee-Teen.webp", "ZackLee-Adult.webp", "ZackLee-Trained.jpg", "ZackLee-God.png", "ZackLee-Real.png"]
evolutionTitles = ["Baby", "Kid", "Teen", "Adult", "Trained", "God", "Real"]

#Create fullscreen TK window
window = tkinter.Tk()
window.geometry("%dx%d" % (window.winfo_screenwidth(), window.winfo_screenheight()))
window.title("Zack Lee Clicker Game")

#Create title
title = tkinter.Label(text="Zack Lee Clicker Game", fg="blue", bg="white")
title.pack(padx=30, pady=30)

#Display level and click requirement
level = tkinter.Label(text="Level: " + str(player.level) + ", Click Goal: " + str(player.xp_goal), fg="black", bg="white")
level.pack(padx=10, pady=10)

#Create button and add style
style = ttk.Style()
style.map("C.TButton",
    foreground=[('pressed', 'red'), ('active', 'black')],
    background=[('pressed', 'yellow'), ('active', 'white')]
    )

button = ttk.Button(window, text="\n\n Click to start your Zack Lee Journey \n\n", style="C.TButton", width=70)
button.pack(padx=10, pady=10)

#Display current zack lee evolution title
current = tkinter.Label(text="You are currentely: " + evolutionTitles[player.click_count] + " Zack Lee", fg="black", bg="white")
current.pack(padx=10, pady=10)

#Put up starting image of Zack Lee
zackImage = ImageTk.PhotoImage(Image.open("Zack_lee_Evolutions/" + evolutions[player.level - 1]))

zackLabel = tkinter.Label(image=zackImage)
zackLabel.place(x=850, y=350)

prev_level = player.level
#Resgister button click input
def onClick(event):
  global zackImage
  global zackLabel
  global prev_level

  player.registerClick(button)
  button.configure(text= "\n\n" + str(player.click_count) + "\n\n")

  if (player.level != prev_level):
    level.configure(text="Level: " + str(player.level) + ", Click Goal: " + str(player.xp_goal))
    current.configure(text="You are currently: " + evolutionTitles[player.level - 1] + " Zack Lee")

    zackImage = ImageTk.PhotoImage(Image.open("Zack_lee_Evolutions/" + evolutions[player.level - 1]))
    zackLabel = tkinter.Label(image=zackImage)
    zackLabel.place(x=850, y=350)

    prev_level = player.level

button.bind("<ButtonRelease-1>", onClick)
window.mainloop()
