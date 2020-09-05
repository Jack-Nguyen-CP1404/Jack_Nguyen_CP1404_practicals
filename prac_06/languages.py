from prac_06.programming_language import ProgrammingLanguage

ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
# Put programming languages in a list
programming_type = [ruby, python, visual_basic]
print(programming_type[2])
print("The dynamically typed languages are:")
# Use
for program in programming_type:
    if program.is_dynamic():
        print(program.programing_name)
