import pandas as pd
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.uix.widget import Widget

class MyApp(App):
    def build(self):
        # Set the window to open in full screen
        Window.maximize()

        # Create the outer layout as a vertical BoxLayout
        outer_layout = BoxLayout(orientation='vertical')

        # Create a horizontal BoxLayout for the header
        header_layout = BoxLayout(orientation='horizontal', padding=10, spacing=10, size_hint_y=None, height=50)

        # Add label and text input fields, and make them resizable
        fields = ['UTC', 'MOC', 'MET', 'SLT', 'MJD']
        for field in fields:
            label = Label(text=field, size_hint=(None, None), size=(40, 30))
            header_layout.add_widget(label)
            text_input = TextInput(size_hint_x=0.1, height=30)  # Resize based on the available space
            header_layout.add_widget(text_input)

        # Add the dropdown for 'Mode' and ensure it resizes properly
        mode_label = Label(text="Mode", size_hint_x=0.05, height=30)  # Mode label with size_hint_x=0.15
        header_layout.add_widget(mode_label)
        mode_spinner = Spinner(text='Choose', values=('Option 1', 'Option 2'), size_hint_x=0.10, height=20)
        header_layout.add_widget(mode_spinner)

        # Add an empty widget with size_hint_x=0.05 for spacing on the right
        header_layout.add_widget(Widget(size_hint_x=0.05))

        # Add buttons to the same header row, making them resizable
        buttons = ['Log Review', 'Log Entry', 'Log In', 'Log Out', 'B/G Monitor']
        for button_text in buttons:
            button = Button(text=button_text, size_hint_x=0.1, height=30)  # Ensure buttons resize based on space
            header_layout.add_widget(button)

        # Add the header layout to the top of the outer layout
        outer_layout.add_widget(header_layout)

        # Add another BoxLayout for the data table
        table_box = BoxLayout(orientation='vertical', size_hint=(1, 0.8), padding=10)

        # Load the CSV data into a pandas DataFrame (example file path, adjust as needed)
        try:
            df = pd.read_csv('../sample_data.csv')
        except Exception as e:
            print(f"Error loading CSV: {e}")
            return outer_layout

        # Create a ScrollView to make the table scrollable
        scroll_view = ScrollView(size_hint=(1, None), size=(Window.width, 300))

        # Create a GridLayout to display the CSV data as a table
        table_layout = GridLayout(cols=len(df.columns), size_hint_y=None)
        table_layout.bind(minimum_height=table_layout.setter('height'))

        # Add headers
        for column in df.columns:
            header = Label(text=column, size_hint_y=None, height=30)
            table_layout.add_widget(header)

        # Add data rows
        for index, row in df.iterrows():
            for value in row:
                label = Label(text=str(value), size_hint_y=None, height=30)
                table_layout.add_widget(label)

        # Add the table layout to the scroll view
        scroll_view.add_widget(table_layout)

        # Add the scroll view to the table box layout
        table_box.add_widget(scroll_view)

        # Add the table box layout to the outer layout
        outer_layout.add_widget(table_box)

        return outer_layout


if __name__ == '__main__':
    MyApp().run()
