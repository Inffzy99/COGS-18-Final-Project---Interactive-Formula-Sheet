from main_functions import *
from dictionary import *

def test_answer():
        
    # testing replace_punctuation function
    assert replace_punctuation("Hello !?~ world", "-") == "Hello --- world"
    assert replace_punctuation("___Hello!@#$%^&*( world!@#$%^&*()", "") == "___Hello world"
    
    # testing process_input function
    assert process_input("Hello world") == ["hello", "world"]
    assert process_input("Hello_world1 Hello_world2") == ["hello_world1", "hello_world2"]
    
    # testing update_dictionary_value and clear function
    input_list1 = ["wavelength", 2, "angle_of_bright_fringes", 5]
    update_dictionary_value(input_list1)
    assert variables["wavelength"] == 2
    assert variables["angle_of_bright_fringes"] == 5
    clear()
    assert variables["wavelength"] == None
    assert variables["angle_of_bright_fringes"] == None
    
    # testing compute function
    formula1 = "slit_spacing * sin(angle_of_bright_fringes) - order_of_diffraction * wavelength"
    formula2 = "position_of_bright_fringes - screen_distance * tan(angle_of_bright_fringes)"
    target1 = "slit_spacing"
    target2 = "angle_of_bright_fringes"
    assert str(compute(variables, formula1, target1)[0]) == "order_of_diffraction*wavelength/sin(angle_of_bright_fringes)"
    assert str(compute(variables, formula2, target2)[0]) == "atan(position_of_bright_fringes/screen_distance)"
    
    # testing symbolize function
    assert symbolize("change_in_position_of_bright_fringes - wavelength * screen_distance / slit_spacing") == str(chr(916)) + "y - " + str(chr(955)) + " * L / d" 
    assert symbolize("slit_spacing * sin(angle_of_bright_fringes) - order_of_diffraction * wavelength") == "d * sin(" + str(chr(952)) + "_m) - m * " + str(chr(955))
    
    # testing scan_command function
    assert scan_command("what pass_list#clear2restart!quit?") == 0
    assert scan_command("what pass_list#clear2restart?") == 1
    assert scan_command("what pass_list#clear2?") == 2
    assert scan_command("what pass_list#?") == 2
    assert scan_command("what pass_?") == 3
    assert scan_command("what ?") == -1