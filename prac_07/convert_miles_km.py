"""Create class"""
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.app import StringProperty

MILES_TO_KM = 1.609


class MilesToKMConversion(App):
    message = StringProperty()

    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (500, 300)
        self.title = "Miles to Km conversion"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_convert_miles_km(self):
        """Convert miles to km."""
        value = self.get_valid_miles()
        print(value)
        result = value * MILES_TO_KM
        self.root.ids.output_number.text = str(result)

    def handle_increment(self, increment):
        """"Increment value of input number and calculate new value"""
        # new_input_number = float(self.root.ids.input_number.text) + increment
        new_input_number = self.get_valid_miles() + increment
        self.root.ids.input_number.text = str(new_input_number)
        self.handle_convert_miles_km()

    def get_valid_miles(self):
        """Get text input from input entry widget, convert to float and return 0 if invalid number entered"""
        try:
            value = float(self.root.ids.input_number.text)
            return value
        except ValueError:
            return 0


MilesToKMConversion().run()
