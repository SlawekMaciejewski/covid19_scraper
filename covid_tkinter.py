import re
import tkinter

import requests


class CovidGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.top_frame = tkinter.Frame(self.main_window, width=400, height=400)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        self.get_www_button = tkinter.Button(self.top_frame, text='Get data(www)', command=self.get_data_from_www)
        self.get_www_button.pack(side='left')

        self.www_info_label = tkinter.Label(self.top_frame, text='From the website "Poland Coronavirus" infected are : ')
        self.www_info_label.pack(side='left')

        self.scraped_data = tkinter.StringVar()
        self.www_scraped_data_label = tkinter.Label(self.top_frame, textvariable=self.scraped_data)
        self.www_scraped_data_label.pack(side='left')

        self.www_info_label2 = tkinter.Label(self.top_frame, text=' persons')
        self.www_info_label2.pack(side='left')

        tkinter.mainloop()

    def get_data_from_www(self):
        page = requests.get('https://www.worldometers.info/coronavirus/country/poland/')
        pattern = r'Poland Coronavirus: (\d,{0,1}\d{0,})'
        obj = re.search(pattern, page.text)
        self.scraped_data.set(obj.group(1))



def get_number_of_infected():
    page = requests.get('https://www.worldometers.info/coronavirus/country/poland/')
    pattern = r'Poland Coronavirus: (\d,{0,1}\d{0,})'
    obj = re.search(pattern, page.text)

    return obj.group(1)


# print(page.text)
# f = open('page.txt', 'w', encoding='utf8')
# f.write(page.text)
if __name__ == '__main__':
    my_covid_gui = CovidGUI()
    print(f'From the website "Poland Coronavirus" : {get_number_of_infected()} persons')

    with open('data.txt', 'r') as f:
        SAVED_DATA = f.readline()

    CURRENT_DATA = get_number_of_infected()

    if SAVED_DATA != CURRENT_DATA:
        with open('data.txt', 'w') as f:
            f.write(str(CURRENT_DATA))
        print(f'New data from file, infected are {CURRENT_DATA} persons')
    else:
        print('No new infected')
