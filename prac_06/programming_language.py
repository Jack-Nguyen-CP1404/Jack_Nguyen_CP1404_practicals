class ProgrammingLanguage:
    """Define a class  for programing language"""

    def __init__(self, programing_name, typing, reflection, year):
        self.programing_name = programing_name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(self.programing_name, self.typing,
                                                                           self.reflection, self.year)

    def is_dynamic(self):
        """Determine if a programming language is dynamically typed"""
        return self.typing == "Dynamic"
