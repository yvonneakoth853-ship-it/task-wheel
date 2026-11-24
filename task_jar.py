import random
import tkinter as tk

tasks = [
    "Do 10 push-ups",
    "Drink a full glass of water",
    "Ride a bicycle",
    "Walk for 30 minutes",
    "Call a friend",
    "Learn a new language",
]
root = tk.Tk()
root.title("Task Jar")
canvas = tk.Canvas(root, width=400, height=500, bg="#fff3b0")
canvas.pack()

#Draw the jar (every piece gets the tag "jar")
canvas.create_rectangle(120, 150, 280, 420, fill="#ffd6f0",
                         outline="#c2185b", width=4, tags="jar")
canvas.create_rectangle(140, 120, 260, 150, fill="#ff4da6",
                        outline="#7b1fa2", width=3, tags="jar")
canvas.create_text(200, 290, text="TASKS", font=("Arial", 22, "bold"),
                   fill="#4a6572", tags="jar")
message = canvas.create_text(200, 40, text="Tap the jar!",
                             font=("Arial", 18), fill="#333", width=360)
shaking = False
note_items = []

def clear_note():
    for item in note_items:
        canvas.delete(item)
    note_items.clear()

def show_note (task):
    paper = canvas.create_rectangle(110, 130, 290, 200, 
                                    fill ="#fff59d", outline="#f9a825", width=2)
    words = canvas.create_text(200, 165, text=task,
                              font=("Arial", 14, "bold"), fill="#333", width=160)
    note_items.extend([paper, words])
    rise()

def rise(step=0):
    if step < 20:
        for item in note_items:
            canvas.move(item, 0, -4)
        root.after(20, rise, step + 1)

def on_tap(event):
    global shaking
    if shaking:
        return
    shaking = True 
    clear_note()
    canvas.itemconfig(message, text="Deciding...")
    shake()

def shake(count=0):
     global shaking
     if count < 12:
            offset = 10 if count %2 == 0 else -10
            canvas.move("jar", offset, 0)
            root.after(50, shake, count +1)
     else:
         canvas.itemconfig(message, text="Your task is...")
         show_note(random.choice(tasks))
         shaking = False
canvas.tag_bind("jar", "<Button-1>", on_tap)

root.mainloop()
    

