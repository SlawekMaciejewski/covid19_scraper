import re
import tkinter
import tkinter.messagebox

import requests


class CovidGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title('Information about people infected with the COVID in Poland')
        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        self.current_data = 0
        self.saved_data = 0

        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        self.get_www_button = tkinter.Button(self.top_frame, text='Get data(www)', command=self.show_data_from_www,
                                             relief=tkinter.GROOVE, borderwidth=5)
        self.get_www_button.pack(side='left')

        self.www_info_label = tkinter.Label(self.top_frame,
                                            text='From the website "Poland Coronavirus" infected are : ')
        self.www_info_label.pack(side='left')

        self.scraped_data = tkinter.StringVar()
        self.www_scraped_data_label = tkinter.Label(self.top_frame, textvariable=self.scraped_data)
        self.www_scraped_data_label.pack(side='left')

        self.www_info_label2 = tkinter.Label(self.top_frame, text=' people')
        self.www_info_label2.pack(side='left')

        self.get_file_button = tkinter.Button(self.mid_frame, text='Get data(file)', command=self.show_data_from_file,
                                              relief=tkinter.GROOVE, borderwidth=5)
        self.get_file_button.pack(side='left')

        self.file_info_label = tkinter.Label(self.mid_frame,
                                             text='Last data from file, infected are: ')
        self.file_info_label.pack(side='left')

        self.read_data_from_file = tkinter.StringVar()
        self.read_data_file_label = tkinter.Label(self.mid_frame, textvariable=self.read_data_from_file)
        self.read_data_file_label.pack(side='left')

        self.file_info_label2 = tkinter.Label(self.mid_frame, text=' people')
        self.file_info_label2.pack(side='left')

        self.save_file_button = tkinter.Button(self.bottom_frame, text='Save data(www) to file',
                                               command=self.save_data_to_file, relief=tkinter.GROOVE, borderwidth=5)
        self.save_file_button.pack(side='left')

        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy,
                                          relief=tkinter.GROOVE, borderwidth=5)
        self.quit_button.pack(side='left')

        tkinter.mainloop()

    def get_data_from_www(self):
        page = requests.get('https://www.worldometers.info/coronavirus/country/poland/')
        pattern = r'Poland Coronavirus: (\d,{0,1}\d{0,})'
        obj = re.search(pattern, page.text)
        return obj.group(1)

    def show_data_from_www(self):
        self.scraped_data.set(self.get_data_from_www())

    def get_data_from_file(self):
        with open('data.txt', 'r') as f:
            self.saved_data = f.readline()
        return self.saved_data

    def show_data_from_file(self):
        self.read_data_from_file.set(self.get_data_from_file())

    def save_data_to_file(self):
        self.current_data = self.get_data_from_www()
        self.saved_data = self.get_data_from_file()
        if self.saved_data != self.current_data:
            with open('data.txt', 'w') as f:
                f.write(self.current_data)
        else:
            tkinter.messagebox.showinfo('Information', 'No new infected')


if __name__ == '__main__':
    my_covid_gui = CovidGUI()
