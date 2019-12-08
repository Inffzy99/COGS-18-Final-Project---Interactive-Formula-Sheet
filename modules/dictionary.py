symbols = {"wavelength" : str(chr(955)), 
           "angle_of_bright_fringes" : str(chr(952)) + "_m", 
           "change_in_position_of_bright_fringes" : str(chr(916)) + "y",
           "position_of_bright_fringes" : "y_m",
           "order_of_diffraction" : "m", 
           "slit_spacing" : "d",
           "screen_distance" : "L"}

variables = {"wavelength" : None,
             "angle_of_bright_fringes" : None, 
             "change_in_position_of_bright_fringes" : None,
             "position_of_bright_fringes" : None,
             "order_of_diffraction" : None, 
             "slit_spacing" : None,
             "screen_distance" : None}

formulae = ["angle_of_bright_fringes - order_of_diffraction * wavelength / slit_spacing",
            "position_of_bright_fringes - order_of_diffraction * wavelength * screen_distance / slit_spacing",
            "change_in_position_of_bright_fringes - wavelength * screen_distance / slit_spacing",
            "slit_spacing * sin(angle_of_bright_fringes) - order_of_diffraction * wavelength",
            "position_of_bright_fringes - screen_distance * tan(angle_of_bright_fringes)"]