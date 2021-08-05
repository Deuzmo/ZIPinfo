import tkinter as tk


class App(tk.Frame):
    def __init__(self, root, *args, **kwargs):
        tk.Frame.__init__(self, root, *args, **kwargs)
        self.root = root
        self.configure_GUI()
        self.create_widgets()
        

    def configure_GUI(self):
        self.root.title("Find Zip Info")
        self.root.eval('tk::PlaceWindow . center')


    def create_widgets(self):
        text1 = tk.Label(self, text="Find information about a ZIP code from a particular country!")
        text1.pack()

        entry1 = tk.Entry(self, text="Country")
        entry2 = tk.Entry(self, text="ZIP")

        entry1.pack()
        entry2.pack()



if __name__ == "__main__":
    root = tk.Tk()
    root.title("Find Zip Info")
    App(root).pack(side="top", fill="both", expand=True)
    root.mainloop()

