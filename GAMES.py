import tkinter as tk
import os
class ImageSelector(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        # Set window size and background color
        self.geometry("{0}x{1}+0+0".format(self.winfo_screenwidth(), self.winfo_screenheight()))
        self.overrideredirect(True)
        self.config(bg="#000000")
        self.middle_label = tk.Label(self, text="SELECT GAME \nSÉLECTIONNER", bg="#000000", fg="#FFFFFF", font=("Helvetica", 20))
        self.middle_label.pack(side="top", fill="x")
        # Add two images to the window, side by side
        self.image_left = tk.PhotoImage(file="left.png")
        width, height = self.image_left.width(), self.image_left.height()
        if width > height and width > 525:
            new_height = int(height * 525 / width)
            self.image_left = self.image_left.subsample(width // 525, height // new_height)
        elif height > 525:
            new_width = int(width * 525 / height)
            self.image_left = self.image_left.subsample(width // new_width, height // 525)

        self.left_label = tk.Label(self, image=self.image_left, bg="#000000")
        self.left_label.pack(side="left", padx=10)

        self.image_right = tk.PhotoImage(file="right.png")
        width, height = self.image_right.width(), self.image_right.height()
        if width > height and width > 500:
            new_height = int(height * 500 / width)
            self.image_right = self.image_right.subsample(width // 500, height // new_height)
        elif height > 500:
            new_width = int(width * 500 / height)
            self.image_right = self.image_right.subsample(width // new_width, height // 500)

        self.right_label = tk.Label(self, image=self.image_right, bg="#000000")
        self.right_label.pack(side="right", padx=10)

        # Add a text label at the bottom of the window
        self.text_label = tk.Label(self, text="", bg="#000000", fg="#FFFFFF",font=("Helvetica", 10))
        self.text_label.pack(side="bottom", fill="x")

        # Bind left mouse clicks to the images
        self.left_label.bind("<Button-1>", lambda event, image="left": self.on_click(event, image))
        self.right_label.bind("<Button-1>", lambda event, image="right": self.on_click(event, image))

        self.selectable = True

    def on_click(self, event, image):
        if self.selectable:
            if image == "left":
                batch_file = "left.bat"
                os.startfile("left.bat")
            else:
                batch_file = "right.bat"
                os.startfile("right.bat")

            self.run_batch_file(batch_file)
            self.selectable = False
    def run_batch_file(self, file_path):
        
        self.text_label.config(text="Selected")
        self.countdown(20)
        
    def countdown(self, count):
        if count >= 0:
            
            self.text_label.config(text=('NOW BOOTING...\n /\_/\ \n( o.o )\n> ^ <\n\n\n\n\n\n\n CYCLON x ReRave!\n\n\n\n\n\n\n\n\n\nDouble Click Prevention Enabled\n Timeout:{}\n github.com/6745').format(count))
            self.after(1000, lambda: self.countdown(count - 1))
        else:
            self.text_label.config(text="")
            self.selectable = True

selector = ImageSelector()
selector.mainloop()
