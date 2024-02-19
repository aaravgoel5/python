def rgb_to_hex(rgb):


    if len(rgb) != 3 or any(not isinstance(val, int) or val < 0 or val > 255 for val in rgb):

        print("Only put three integers between 0 and 255")

        return None





    hex_value = "#{:02X}{:02X}{:02X}".format(*rgb)

    return hex_value



while True:


        r = int(input("Enter the red value (0-255): "))

        g = int(input("Enter the green value (0-255): "))

        b = int(input("Enter the blue value (0-255): "))


        hex_color = rgb_to_hex([r, g, b])

        if hex_color:

            print(f"HEX: {hex_color}")

        choice = input("Do you want to convert more values? (yes/no): ")

        if choice == 'no':

            break
