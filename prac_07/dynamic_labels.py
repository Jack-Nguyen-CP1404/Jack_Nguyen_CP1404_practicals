from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """Dynamically create labels from a list"""

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        # Create a list of data
        self.names = ["Joe", "Luke", "Gabby", "Abby"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        for name in self.names:
            label_name = Label(text=name, id=name)
            self.root.ids.name_box.add_widget(label_name)


DynamicLabelsApp().run()
