import tkinter
import asyncio
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

def TranslateLinkToZackTitle(link):
  split1 = link.split("-")
  split2 = split1[1].split(".")
  return split2[0]

#Create library of Zack Lee evolutions
evolutions = ["ZackLee-Baby.webp", "ZackLee-Kid.png", "ZackLee-Teen.webp", "ZackLee-RedGlasses.jpg", "ZackLee-RizzGod.webp", "ZackLee-Trained.jpg", "ZackLee-Insane.jpeg", "ZackLee-God.png", "ZackLee-BabyEater.jpg", "ZackLee-Real.png"]

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

#Create button style
style = ttk.Style()
style.map("C.TButton",
    foreground=[('pressed', 'red'), ('active', 'black')],
    background=[('pressed', 'yellow'), ('active', 'white')]
    )

#Resgister button with click input and style
def onClick():
  global zackImage
  global zackLabel
  global prev_level

  player.registerClick(button)
  button.configure(text= "\n\n" + str(player.click_count) + "\n\n")

  if player.level != prev_level:
    level.configure(text="Level: " + str(player.level) + ", Click Goal: " + str(player.xp_goal))
    current.configure(text="You are currently: " + TranslateLinkToZackTitle(evolutions[player.level - 1]) + " Zack Lee")

    zackImage = ImageTk.PhotoImage(Image.open("Zack_lee_Evolutions/" + evolutions[player.level - 1]))
    zackLabel = tkinter.Label(image=zackImage)
    zackLabel.place(x=850, y=350)

    prev_level = player.level

button = ttk.Button(window, text="\n\n Click to start your Zack Lee Journey \n\n", style="C.TButton", width=70, command=onClick)
button.pack(padx=10, pady=10)

#Display current zack lee evolution title
current = tkinter.Label(text="You are currentely: " + TranslateLinkToZackTitle(evolutions[player.level - 1]) + " Zack Lee", fg="black", bg="white")
current.pack(padx=10, pady=10)

#Put up starting image of Zack Lee
zackImage = ImageTk.PhotoImage(Image.open("Zack_lee_Evolutions/" + evolutions[player.level - 1]))

zackLabel = tkinter.Label(image=zackImage)
zackLabel.place(x=850, y=350)

prev_level = player.level

#Autoclicking check loop
elapsed = 0
async def registerAutoClick():
  global elapsed
  
  while (True):
    elapsed += 1
    if auto_click.get() and elapsed > 100 / player.xp_goal:
      onClick()
      elapsed = 0

    window.update()
    await asyncio.sleep(0.001)

#Checkbox
auto_click = tkinter.BooleanVar()
c1 = tkinter.Checkbutton(window, text='AutoClick',variable=auto_click, onvalue=True, offvalue=False)
c1.pack()

asyncio.run(registerAutoClick())
