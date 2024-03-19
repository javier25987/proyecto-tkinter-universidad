import tkinter as tk 

class root(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('root')
        self.state('zoomed')

        self.imagen = tk.PhotoImage(file='imagen_menu.png')
        self.new_image_1 = self.imagen.subsample(1)
        self.label_img_1 = tk.Label(self, image=self.new_image_1)
        self.label_img_1.pack()

        self.new_image_2 = self.imagen.zoom(1.5)
        self.label_img_2 = tk.Label(self, image=self.new_image_2)
        self.label_img_2.pack()

root = root()
root.mainloop()