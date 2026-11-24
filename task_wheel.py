import math
import random
import tkinter as tk

tasks = ["Do 10 push-ups", "Drink a full glass of water", "Ride a bicycle", "Walk for 30 minutes", "Call a friend", "Learn a new language"]
colors = ["#ff6b6b", "#feca57", "#48dbfb", "#1dd1a1", "#ff9ff3", "#a29bfe"]

root = tk.Tk()
root.title("Task Wheel")
canvas = tk.Canvas(root, width = 500, height=560, bg="#fff3b0")
canvas.pack()

cx,cy, radius = 250, 300, 200
angle = 0
spinning = False
speed = 0

title = canvas.create_text(250, 45, text="Tap to spin!", font=("Arial", 28, "bold"), fill="#d63384")

def draw_wheel():
    canvas.delete("wheel")
    slice_size = 360 / len(tasks)
    for i, task in enumerate(tasks):
        start = angle + i * slice_size
        canvas.create_arc(cx - radius, cy - radius, cx + radius, cy + radius, start=start, extent=slice_size, fill=colors[i % len(colors)], outline="white", width=3, tags="wheel")
        middle = math.radians(start + slice_size / 2)
        x = cx + radius * 0.62 * math.cos(middle)
        y = cy - radius * 0.62 * math.sin(middle)
        canvas.create_text(x, y, text=task, font=("Arial", 10, "bold"), fill="white", width=90, tags="wheel")
    canvas.tag_raise("pointer")

def spin():
    global angle, speed, spinning
    angle = (angle + speed) % 360
    draw_wheel()
    speed = speed * 0.97
    if speed > 0.3:
        root.after(30, spin)
    else:
        spinning = False
        canvas.itemconfig(title, text="Tap to spin!")

def on_tap(event):
    global spinning, speed
    if spinning:
        return
    spinning = True
    speed = random.uniform(25, 40)
    canvas.itemconfig(title, text="On the go...")
    spin()

draw_wheel()
canvas.create_polygon(cx - 15, cy - radius - 25, cx + 15, cy - radius - 25, cx, cy - radius + 10, fill="#333", tags="pointer")
canvas.bind("<Button-1>", on_tap)

root.mainloop()
