from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner


class MyApp(App):
    def build(self):
        # Create the outer layout as a vertical BoxLayout
        outer_layout = BoxLayout(orientation='vertical')

        # Create a horizontal BoxLayout for the header
        header_layout = BoxLayout(orientation='horizontal', padding=10, spacing=10, size_hint_y=None, height=50)

        # Add label and text input fields
        fields = ['UTC', 'MOC', 'MET', 'SLT', 'MJD']
        for field in fields:
            label = Label(text=field, size_hint=(None, None), size=(40, 30))
            header_layout.add_widget(label)
            text_input = TextInput(size_hint=(None, None), size=(100, 30))
            header_layout.add_widget(text_input)

        # Add the dropdown for 'Mode'
        mode_label = Label(text="Mode", size_hint=(None, None), size=(50, 30))
        header_layout.add_widget(mode_label)
        mode_spinner = Spinner(text='Choose', values=('Option 1', 'Option 2'), size_hint=(None, None), size=(100, 30))
        header_layout.add_widget(mode_spinner)

        # Add buttons to the layout
        buttons = ['Log Review', 'Log Entry', 'Log In', 'Log Out', 'B/G Monitor']
        for button_text in buttons:
            button = Button(text=button_text, size_hint=(None, None), size=(120, 30))
            header_layout.add_widget(button)

        # Add the header layout to the top of the outer layout
        outer_layout.add_widget(header_layout)

        # Add an empty widget to fill the remaining space (or you can replace this with more content)
        outer_layout.add_widget(BoxLayout())

        return outer_layout


if __name__ == '__main__':
    MyApp().run()
