from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty


class DynamicNameDisplay(App):
    status_text = StringProperty()

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.names = {"Bob Brown": "20", "Cat Cyan": "30", "Oren Ochre": "40"}

    def build(self):
        self.title = 'Dynamic name display'
        self.root = Builder.load_file('dynamic_name_display.kv')
        self.create_widget()
        return self.root

    def create_widget(self):
        for name in self.names:
            button = Button(text=name, id=name)
            button.bind(on_release=self.press_entry)
            self.root.ids.entries_box.add_widget(button)

    def press_entry(self, instance):
        # get name (dictionary key) from the id of Button we clicked on
        name = instance.id  # or name = instance.text
        # update status text
        self.status_text = "{}'s age is {}".format(name, self.names[name])

    def clear_all(self):

        self.root.ids.entries_box.clear_widgets()


DynamicNameDisplay().run()
