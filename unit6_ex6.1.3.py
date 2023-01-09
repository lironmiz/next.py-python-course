# exercise 6.1.3 from unit 6
'''
In this exercise you will create basic graphics in Python, by exploring a module from the Python standard library.
You must write a program that creates a window that looks like this.

The software window in which the text is written: what's my favorite video?
And below the text there is a button with the text: click to find out!
The window must include two elements: text (with a question of your choice)
and a button.
When the user clicks the button, the bottom of the screen should open and
display an image that is actually an answer to the question. for example:

The software window from the previous step after clicking where you see the
text + the button and added the image from the favorite video which is actually
the answer to the question.
In our case, when you click on the button, a picture of our favorite video
appears - one that appears in the next.py course, of course...

Guidelines:
Read online documentation about a built-in module called tkinter
and use it to solve the task.
'''

import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.image_hidden = True

    def create_widgets(self):
        self.question = tk.Label(self, text=" what's my in favorite video?")
        self.question.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

        self.show = tk.Button(self, text="SHOW IMAGE",
                              fg="blue", command=self.toggle_image)
        self.show.pack(side="bottom")

        self.image = tk.PhotoImage(file="favVideo.png")
        self.lable_image = tk.Label(
            self, image=self.image, width=500, height=500)

    def toggle_image(self):
        if self.image_hidden:
            self.lable_image.pack()
        else:
            self.lable_image.pack_forget()
        self.image_hidden = not self.image_hidden


def main():
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()


if __name__ == "__main__":
    main()
