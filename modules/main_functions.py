import string
from sympy.solvers import solve
from sympy import Symbol
from sympy import sympify

# The following way of handling import errors is learned here: 
# https://stackoverflow.com/questions/3131217/error-handling-when-importing-modules
try: 
    from modules.dictionary import *    # For running in Jupyter Notebook
except ImportError:
    from dictionary import *    # For running pytest

def clear():
    """Reset all values in the variables dictionary (see dictionary.py) to None; return nothing."""
    for variable in variables.keys():
        variables.update({variable : None})

def replace_punctuation(input_string, filler):
    """Replace punctuations in input_string other than _, -, and + with string specified by the argument, filler; 
    return the resultant string.

    Keyword arguments:
    input_string -- a string of which punctuations are to be replaced
    filler -- a string specifying the content to replace the punctuations with
    """
    output_string = ""
    
    for x in input_string:
        if x == "_" or x == "-" or x == "+":
            pass
        elif x in string.punctuation:
            output_string += filler
            continue
        output_string += x
        
    return output_string

def process_input(input_string):
    """Replace the punctuations in input_string with blank space (calling the replace_punctuation function), 
    set all alphabets in input_string to lower case, and split input_string to a list; 
    return the resultant list.

    Keyword arguments:
    input string -- a string to be processed
    """
    output_list = replace_punctuation(input_string, " ").lower().split()
    return output_list

def update_dictionary_value(input_list):
    """Update the values in the variables dictionary (see dictionary.py) with key-value pairs from input_list;
    return a boolean variable specifying whether the variables dictionary has been changed or not.

    Keyword arguments:
    input_list -- a list containing key-value pairs (even-number indices are keys; odd-number indices are values)
    """
    variable_added = False
    
    for index in range(0, len(input_list), 2):
        add_variable = True
        
        if input_list[index] not in variables.keys():
            
            question = True
            
            while question:
                print("\nThe variable, " + input_list[index] + ", is not in the dictionary.") 
                print("Do you want to add it into the dictionary? [y/n]")
            
                user_input = input('\n\t')
                
                if user_input.lower() == "y":
                    add_variable = True
                    question = False
                
                elif user_input.lower() == "n":
                    add_variable = False
                    question = False
        
        if add_variable:
            variable_added = True
            variables.update({input_list[index] : input_list[index + 1]})
    
    return variable_added
              
def compute(variables, formula, target):
    """Utilizing SymPy's symbolic algebra functions <https://docs.sympy.org/latest/modules>, 
    given the formula and values of all variables, write the target variable as a function of other relevant variables;
    return a string representing the resultant equation.

    Keyword arguments:
    variables -- a dictionary containing variable names (strings) as keys and variable values (floats) as values.
    formula -- a string specifying a formula
    target -- a string specifying the variable to be written as a function of others
    """
    if variables[target] != None:
        return variables[target]
    
    else:        
        for variable in zip(variables.keys(), variables.values()):
            
            if variable[1] != None:
                index = formula.find(variable[0])
                
                if index == 0 or (index > 0 and formula[index - 1] != "_" and not formula[index - 1].isalpha()):
                    formula = formula.replace(variable[0], str(variable[1]))
        
        return solve(sympify(formula), Symbol(target))

def symbolize(equation):
    """Given an equation, replace every replaceable variable name with its symbol as specified by the symbols dictionary 
    (see dictionary.py); return the resultant equation.
    
    Keyword arguments:
    equation -- a string representing the equation of which the variable names are to be replaced by symbols
    """
    for name in symbols:
        equation = equation.replace(name, symbols[name])
        
    return equation

def print_dictionary(input_dictionary):
    """Print out the dictionary with each line having a key-value pair; return nothing.

    Keyword arguments:
    input_dictionary -- a dictionary to be printed
    """
    for key in input_dictionary.keys():
        print(key + " : " + str(input_dictionary[key]))

def scan_command(input_string):
    """Scan user input and execute special commands, if there's any contained in the input; 
    return an int representing action to be taken by the caller of this function.
    
    Return value interpretation:
    0 -- quit, end the program
    1 -- restart from the very beginning of the program
    2 -- restart from the beginning of the current functionality in the program
    3 -- pass, skip the current functionality and proceed to the next
    -1 -- no special commands recognized
    (see launch_formula_sheet() for application of this function)
    
    Keyword arguments:
    input_string -- a string representing commands input by user
    """
    if input_string.lower().find("quit") >= 0:
        print("\nQuitting Interactive Formula Sheet.")
        return 0
            
    elif input_string.lower().find("restart") >= 0:
        print("\nRestarting Interactive Formula Sheet.")
        return 1
        
    elif input_string.lower().find("clear") >= 0:
        print("\nClearing variable values in dictionary.")
        clear()
        return 2
            
    elif input_string.lower().find("list") >= 0:
        print("\nSYMBOLS: ")
        print_dictionary(symbols)
    
        print("\nVARIABLES: ")
        print_dictionary(variables)
    
        print("\nFORMULAE: ")
        for formula in formulae:
            print(formula + " = 0")
        return 2
    
    elif input_string.lower().find("pass") >= 0:
        return 3
    
    else:
        return -1

def launch_formula_sheet():
    """Launch the Interactive Formula Sheet; return nothing.
    
    launch_formula_sheet() is consisted of 1 while loop that contains 2 while loops. 
    The outer while loop has formula_sheet_on as condition; the inner while loops have question1 and question2 as conditions.
    These conditions change according to user inputs.
    """

    formula_sheet_on = True
    
    while formula_sheet_on:
        
        question1 = True
        question2 = True
    
        while question1:
        
            print("\nWhat variables do you know?")
            print("(Format your answer as: <variable name 1> : <value 1> ; <variable name 2> : <value 2> ... )")
            print("\n  Or you can enter one of these special commands:")
            print("\n  list    -- see all information in the dictionary")
            print("  pass    -- skip to next question")
            print("  clear   -- set all values in the dictionary to none")
            print("  restart -- start from beginning of program")
            print("  quit    -- exit program")
 
            # Scan user input. Execute the special commands if the user input contains any.
            user_input = input('\n\t')
            scan_result = scan_command(user_input.lower())
            
            if scan_result == 0:    
                question2 = False
                formula_sheet_on = False
                break
            
            elif scan_result == 1 or scan_result == 2:
                continue
        
            elif scan_result == 3: 
                break
            
            # If the user input does not contain any special commands, 
            # then assume the user input contains information on updating the variables dictionary (see dictionary.py).
            else:
                known_variables = process_input(user_input)
                
                if len(known_variables) < 2 or (len(known_variables) % 2 != 0):
                    print("Please re-enter your input.")
                    continue
                    
                elif update_dictionary_value(known_variables):
                    question1 = False
            
        while question2:
        
            print("\nWhat variable do you want to solve for?")
            print("\n  Or you can enter one of these special commands:")
            print("\n  list    -- see all information in the dictionary")
            print("  pass    -- skip to next question")
            print("  clear   -- set all values in the dictionary to none")
            print("  restart -- start from beginning of program")
            print("  quit    -- exit program")
            
            # Scan user input. Execute the special commands if the user input contains any.
            user_input = input('\n\t')
            scan_result = scan_command(user_input.lower())
        
            if scan_result == 0:
                formula_sheet_on = False
                break
            
            elif scan_result == 1 or scan_result == 3:
                break
            
            elif scan_result == 2:
                continue
        
            # If the user input does not contain any special commands, 
            # then assume the user input is providing the target variable to be written as functions of other variables.
            else:
                target_variable = process_input(user_input)[0]
                target_variable_found = False
                
                for formula in formulae:
                    index = formula.find(target_variable)
                    
                    if index == 0 or (index > 0 and formula[index - 1] != "_" and not formula[index - 1].isalpha()):
                        target_variable_found = True
                        compute_result = compute(variables, formula, target_variable)
                        
                        if type(compute_result) == list:
                            compute_result = str(compute_result[0])
                
                        output = target_variable + " = " + compute_result
                
                        print("\n" + output)
                        print("\n" + symbolize(output))
            
                       
                if not target_variable_found:
                    print("\nTarget variable, " + target_variable + ", is not found in the dictionary.")
                
                question2 = False