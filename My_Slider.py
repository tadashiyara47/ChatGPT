import tkinter as tk

class MySlider(tk.Canvas):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        
        self.configure(bg="black", height=100, width=400, highlightthickness=0)
        self.create_line(50, 50, 350, 50, fill="yellow", width=20, capstyle="round")
        self.create_text(50, 75, text="-10", fill="white")
        self.create_text(350, 75, text="+10", fill="white")
        self.create_text(200, 75, text="0", fill="white")
        
        self.slider = self.create_rectangle(195, 25, 205, 75, fill="red")
        self.bind("<Button-1>", self.move_slider)
        self.bind("<B1-Motion>", self.move_slider)
        self.bind("<ButtonRelease-1>", self.release_slider)
        
        NUM_MARKINGS = 9
        MARKING_LENGTH = 10
        MARKING_SPACING = 20
        SLIDER_X = 200
        SLIDER_Y = 50
        
        for i in range(NUM_MARKINGS):
            x = SLIDER_X + i * MARKING_SPACING
            y1 = SLIDER_Y - MARKING_LENGTH/2
            y2 = SLIDER_Y + MARKING_LENGTH/2
            self.create_line(x, y1, x, y2, fill="white")
            
        for i in range(-NUM_MARKINGS, 0):
            x = SLIDER_X + i * MARKING_SPACING
            y1 = SLIDER_Y - MARKING_LENGTH/2
            y2 = SLIDER_Y + MARKING_LENGTH/2
            self.create_line(x, y1, x, y2, fill="white")
        
        self.x = 200
        self.y = 50
        self.vx = 0
        self.vy = 0
        
        self.update()
        
    def move_slider(self, event):
        x = self.canvasx(event.x)
        if x < 95:
            x = 95
        elif x > 305:
            x = 305
        self.coords(self.slider, x-5, 25, x+5, 75)
        self.x = x
        
    def release_slider(self, event):
        target_x = 200
        duration = 1000 # in milliseconds
        
        dx = target_x - self.x
        dt = duration / 1000 # convert milliseconds to seconds
        
        self.vx = dx / dt / 10
        self.vy = 0
        
        self.update_position()
        
    def update_position(self):
        self.x += self.vx
        self.y += self.vy
        
        if abs(self.x - 200) <= 1:
            self.x = 200
            self.vx = 0
        else:
            self.vx *= 0.95
            
        self.coords(self.slider, self.x-5, 25, self.x+5, 75)
        
        if self.vx != 0:
            self.after(10, self.update_position)
        else:
            self.vx = - (self.x - 200) / 20
            self.update_slowdown()
            
    def update_slowdown(self):
        self.x += self.vx
        self.vx *= 0.95
        
        if abs(self.x - 200) <= 1:
            self.x = 200
            self.vx = 0
