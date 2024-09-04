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

        # Add another BoxLayout for the data table
        table_box = BoxLayout(orientation='vertical', padding=10, size_hint=(1, 0.8))

        # Load the CSV data into a pandas DataFrame (example file path, adjust as needed)
        try:
            df = pd.read_csv('sample_data.csv')
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
