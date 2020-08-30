HEX_COLOURS = {"AliceBlue": "# f0f8ff", "AntiqueWhite": "#faebd7", "AntiqueWhite1": "#ffefdb",
               "AntiqueWhite2": "#eedfcc", "AntiqueWhite3": "#cdc0b0", "AntiqueWhite4": "#8b8378",
               "BlanchedAlmond": "#ffebcd", "BlueViolet": "#8a2be2", "CadetBlue": "	#5f9ea0",
               "CornflowerBlue": "#6495ed"}

colour = input("Enter a colour: ")

while colour != "":
    # Use "get" method to return None when input is not in the list

    print("{} has colour code: {}".format(colour, HEX_COLOURS.get(colour)))
    colour = input("Enter a colour: ")
