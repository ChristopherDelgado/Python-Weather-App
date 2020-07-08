# import tkinter to be used as the GUI
# import api_access for it's methods

import tkinter as tk
import api_access as open_weather_map


class Frame:
    def __init__(self, root):
        # set the default values for the frame's widgets
        self.root = root
        self.entry = None
        self.button = None
        self.output_text = None
        self.redo_button = None
        # set the properties of the frame
        self.root.title("Weather")
        self.root.geometry("300x130")
        self.root.resizable(0, 0)
        self.root.pack_propagate(0)
        photo = tk.PhotoImage(file='Assets\\icon.png')
        self.root.iconphoto(False, photo)

    def input(self):
        # creating the input section
        self.entry = tk.Entry(self.root)
        self.entry.pack()
        self.button = tk.Button(self.root, text='Enter', command=self.enter)
        self.button.pack()
        self.root.mainloop()

    def output(self, data):
        # destroy the input section
        self.entry.destroy()
        self.button.destroy()
        # retrieve the output string
        data_string = self.get_data(data)
        # create the output text widget
        self.output_text = tk.Text(self.root, height=6, width=30)
        self.output_text.insert(tk.END, data_string)
        self.output_text.config(state='disabled')
        self.output_text.pack()
        # create the reset button
        self.redo_button = tk.Button(self.root, text='Reset', command=self.reset)
        self.redo_button.pack()

    def reset(self):
        # destroy the output section and bring back the input section
        self.output_text.destroy()
        self.redo_button.destroy()
        self.input()

    def enter(self):
        # get input from the textbox
        m_input = self.entry.get()
        # Check if the input contains a state and handle accordingly
        if ',' in m_input:
            temp_list = m_input.split(',')
            city = temp_list[0]
            state = temp_list[1].upper().strip()
            data = open_weather_map.get_weather(city, state)
        else:
            city = m_input
            state = "N/A"
            data = open_weather_map.get_weather(m_input, None)
        # if api_access finds the city it should return a list
        if data is not None:
            data.update({'city': city})
            data.update({'state': state})
            self.output(data)
        else:
            self.button.config(text='Try Again')

    # this function creates and returns the output for the city given
    def get_data(self, list) -> str:
        string = ('City: ' + list['city'] + '\nState: ' + list['state'] + '\nTemperature: ' + str(
            list['temp']) + '\nHumidity: ' + str(
            list['humidity'])
                  + '\nDescription: ' + str(list['description']) +
                  "\nTime: " + str(list['time']))
        return string
