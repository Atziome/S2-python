import tkinter as tk

CANVAS_WIDTH, CANVAS_HEIGHT = 600, 600

root = tk.Tk()

canvas =tk.Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT)

# Début de votre code
y0 = 100
x = CANVAS_WIDTH - 100
y1 = CANVAS_HEIGHT / 2
canvas.create_line(x,y0,x,y1)
canvas.create_oval(x - 50, y0 + 50, x + 50, y0 - 50)
canvas.create_oval(x - 50, y1 + 50, x + 50, y1 - 50)
canvas.create_oval((x-50,(y1+y0)/2+50,x+50,(y1+y0)/2-50))
    
# Fin de votre code

canvas.grid(row=1, column=1)
root.mainloop()
