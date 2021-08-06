import tkinter as tk
from tkinter.constants import RIDGE
import tkinter.ttk as ttk
from countrylist import supported_countries, get_country_code
from APIcalls import findby_country_and_zip


class App(tk.Frame):
    def __init__(self, root, countries, *args, **kwargs):
        tk.Frame.__init__(self, root, *args, **kwargs)
        self.root = root
        self.configure_GUI()
        self.set_country_list(countries)
        self.create_widgets()
        

    def configure_GUI(self):
        self.root.title("Find Zip Info")
        self.root.eval('tk::PlaceWindow . center')


    def create_widgets(self):
        self.result_frame = tk.Frame(self, borderwidth=3, relief=tk.GROOVE)
        self.text1 = tk.Label(self, text="Find information about a ZIP code from a particular country!")
        self.text2 = tk.Label(self, text="Select country: ")
        self.text3 = tk.Label(self, text="Enter ZIP code:")
        
    
        self.countryvar = tk.StringVar(self, "United States")
        self.countrybox = ttk.Combobox(self, textvariable= self.countryvar, width = 25)
        self.countrybox['values'] = self.supported_countries
        self.countrybox.state(["readonly"])

        self.ZIP_var = tk.StringVar(self, "")
        self.ZIP_entry = tk.Entry(self, textvariable= self.ZIP_var, width = 15)

        self.submit_btn = tk.Button(self, text="Find!", command=self.output_result, width=14, 
            pady=2, foreground='dark green', activeforeground="dark green",
             font = "Arial 12 bold", borderwidth=4)

        self.result_string = tk.StringVar(self.result_frame, "")
        self.result_label = tk.Label(self.result_frame, textvariable=self.result_string, 
                                    font=('Arial 11'), width=40, height=8, wraplength=400)

        self.text1.grid(row = 0, column = 0, columnspan=2, pady=15)
        self.text2.grid(row = 1, column = 0)
        self.text3.grid(row = 1, column = 1)
        self.countrybox.grid(row = 2, column = 0, padx=10, pady=5)
        self.ZIP_entry.grid(row = 2, column = 1, padx=10, pady=5)
        self.submit_btn.grid(row=3, column = 0, columnspan=2)

        self.result_frame.grid(row=4, column= 0, columnspan=2, rowspan=2, padx=10, pady=10)
        self.result_label.grid(row=4, column= 0, columnspan=2, rowspan=2)

    def set_country_list(self, countries):
        self.supported_countries = [*supported_countries]

    def output_result(self):
        result = findby_country_and_zip(
            get_country_code(self.countryvar.get()), self.ZIP_var.get())

        if (len(result) > 1):
            self.result_string.set("The code {} points to the city of {} "
             "located in the state of {}.\n\nlatitude: {}       longitude: {}".format(
                 self.ZIP_var.get(), result["places"][0]["place name"], 
                 result["places"][0]["state"], result["places"][0]["latitude"], 
                 result["places"][0]["longitude"]))
        else:
            self.result_string.set(result["error"])
         

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Find Zip Info")
    App(root, supported_countries, borderwidth=3, relief=tk.RIDGE).pack(
            expand=True, side="top", fill="both", padx=1, pady=1)
    root.mainloop()

