from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Create a handle_greet function to change text Label."""
        print('greet')
        print("test")
        # Change text label
        # self.root.ids.output_label.text = "Hello "
        self.root.ids.output_label.text = "Hello " + self.root.ids.input_name.text

    def handle_clear_data(self):
        """Create a clear data even handler to clear input and output to blank."""
        self.root.ids.output_label.text = ""
        self.root.ids.input_name.text = ""


BoxLayoutDemo().run()
