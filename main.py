from tkinter import *
from tkinter.ttk import Combobox

root = Tk()

# - - - VOLUME - - - - - - - - - - - - - - - - - - - - - - - - - - - 
volume_label = Label(root, text='Volume:')
volume_entry = Entry(root)

volume_label.grid(row=0, column=0)
volume_entry.grid(row=0, column=1)


# - - - YEAR - - - - - - - - - - - - - - - - - - - - - - - - - - - 
year_label = Label(root, text='Year:')
year_entry = Entry(root)

year_label.grid(row=0, column=2)
year_entry.grid(row=0, column=3)


# - - - FUEL TYPE - - - - - - - - - - - - - - - - - - - - - - - - - - - 
fuel_types = ['Diesel', 'Gasoline', 'Electro']

fueltype_label = Label(root, text='Fuel type:')
fueltype_dropbox = Combobox(root, state='readonly', values=fuel_types)

fueltype_dropbox.set(fuel_types[0])
fueltype_label  .grid(row=1, column=0)
fueltype_dropbox.grid(row=1, column=1)


# - - - COUNTRY - - - - - - - - - - - - - - - - - - - - - - - - - - - 
countries = ['EU', 'US', 'UK']

country_lable = Label(root, text='Country:')
country_dropbox = Combobox(root, state='readonly', values=countries)

country_dropbox.set(countries[0])
country_lable  .grid(row=1, column=2)
country_dropbox.grid(row=1, column=3)


# - - - AUCTION STAKE - - - - - - - - - - - - - - - - - - - - - - - - - - - 
stake_label = Label(root, text='Auction stake:')
stake_entry = Entry(root)

stake_label.grid(row=2, column=0)
stake_entry.grid(row=2, column=1)


# - - - RESULT CALCULATION - - - - - - - - - - - - - - - - - - - - - - - - - - - 
result_label = Label(root, text='Result:')
result_button = Button(root, text='Calculate', command=...)

result_button.grid(row=3, column=0)
result_label.grid(row=3, column=1)


# - - - VISUAL SETTINGS - - - - - - - - - - - - - - - - - - - - - - - - - - - 
root.title('CustomsClearance')
root.geometry('550x200')

ROW_GAP = 30
for row_index in range(10):
    root.grid_rowconfigure(row_index, minsize=ROW_GAP)

LABEL_WIDTH = 15
USER_INPUT_WIDGET_WIDTH = 20

for widget in root.winfo_children():
        
        if isinstance(widget, (Label, Button)):
            widget.config(width=LABEL_WIDTH)

        if isinstance(widget, Entry):
            widget.config(width=USER_INPUT_WIDGET_WIDTH + 3)

        if isinstance(widget, Combobox):
            widget.config(width=USER_INPUT_WIDGET_WIDTH)

root.mainloop()
