from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('scores.kv')
        return self.root

    def score_evaluation(self):
        """Create a handle_greet function to change text Label."""
        print('greet')
        print("test")
        # Change text label
        # self.root.ids.output_label.text = "Hello "
        score = self.root.ids.input_score.text
        if 0 <= int(score) < 50:
            self.root.ids.output_label.text = "Fail"
        elif 50 <= int(score) < 75:
            self.root.ids.output_label.text = "Credit"
        elif 75 <= int(score) < 85:
            self.root.ids.output_label.text = "Distinction"
        elif 85 <= int(score) <= 100:
            self.root.ids.output_label.text = "HD"
        else:
            self.root.ids.output_label.text = "Invalid score"

    def handle_clear_data(self):
        """Create a clear data even handler to clear input and output to blank."""
        self.root.ids.output_label.text = ""
        self.root.ids.input_score.text = ""


BoxLayoutDemo().run()
