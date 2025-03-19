from tkinter import *
from tkinter.ttk import Combobox

from class_calculator import Car, CarCalculator

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
error_label = Label(root, text='', fg='red', wraplength=100)
error_label.grid(row=3, column=1)

def clear_error():
    error_label.config(text='')
def show_error(err_msg: str):
    error_label.config(text=f'Error: {err_msg}')

def calculate():
    clear_error()

    fueltype = fueltype_dropbox.get().lower()

    try: volume = int(volume_entry.get())
    except:
        show_error('volume value must be an integer')
        return

    try: year = int(year_entry.get())
    except:
        show_error('year value must be an integer')
        return

    country = country_dropbox.get()

    try: stake = float(stake_entry.get())
    except:
        show_error('auction stake value must be a real number')
        return

    tmp_car = Car(fueltype, volume, year, country, stake, True)

    res = CarCalculator(tmp_car)

    result_label.config(text='\n'.join(['Results:',
                                         f'Import duty: {res.import_duty}',
                                          f'Excise tax: {res.excise_tax}',
                                                 f'Vat: {res.vat}',
                                        f'Pension fund: {res.pension_fund}']))

result_label = Label(root, text='Result:')
result_label.grid(row=3, column=0)

result_button = Button(root, text='Calculate', command=calculate)
result_button.grid(row=2, column=2, columnspan=2)


# - - - VISUAL SETTINGS - - - - - - - - - - - - - - - - - - - - - - - - - - - 
root.title('CustomsClearance')
root.geometry('550x200')

ROW_GAP = 30
for index in range(10):
    root.grid_rowconfigure(index, minsize=ROW_GAP)

LABEL_WIDTH = 15
USER_INPUT_WIDGET_WIDTH = 20

for widget in root.winfo_children():
        
        if type(widget) in (Label, Button):
            if widget in [result_label, error_label]: continue
            widget.config(width=LABEL_WIDTH)

        elif type(widget) is Entry:
            widget.config(width=USER_INPUT_WIDGET_WIDTH + 3)

        elif type(widget) is Combobox:
            widget.config(width=USER_INPUT_WIDGET_WIDTH)

root.mainloop()
