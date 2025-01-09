
from config.choices import type_choices

def choices_project_type():
    """
    This function is to show the choices of the project type
    """
    global type_choices
    # -> show the choices list with number before to input the choice
    print ("Please select the type of the project")
    for i, answer_choice in enumerate(type_choices):
        print ("{} - {}".format(i + 1, answer_choice))

    # -> get the choice
    choice = input("Please select the type of the project: ")
    choice = int(choice) - 1

    # -> Validate the choice
    if choice < 0 or choice >= len(type_choices):
        print ("The choice is not valid")
        return choices_project_type()
    
    return {
        "index": choice,
        "value": type_choices[choice]
    }