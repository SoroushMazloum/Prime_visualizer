import tkinter as tk

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def mark_primes():
    root = tk.Tk()
    width, height = root.winfo_screenwidth(), root.winfo_screenheight()
    canvas = tk.Canvas(root, width=width, height=height, bg="black")
    canvas.pack()

    for y in range(height):
        for x in range(width):
            pixel_num = y * width + x
            if is_prime(pixel_num):
                canvas.create_rectangle(x, y, x + 2, y + 2, fill="white" )
                canvas.pack()

    root.mainloop()

mark_primes()