def get_option(prompt, options):
    while True:
        try:
            option: int = int(input(prompt))
            if option in options:
                return option
            else:
                print(f"Invalid option. Please choose between {min(options)} and {max(options)}.")
        except ValueError:
            print("Please enter a valid number.")

def menu():
    resolution_options = {
        1: "60% (recommended)",
        2: "70%",
        3: "80%",
        4: "90%",
        5: "100%"
    }

    redimension_options = {
        1: "0%",
        2: "5%",
        3: "10%",
        4: "15%",
        5: "20%",
        6: "25%",
        7: "30%",
        8: "35%",
        9: "40%",
        10: "45%",
        11: "50%"
    }

    convert_options = {
        1: "Yes",
        2: "No"
    }

    resolution_prompt = "\n".join([f"{key} - {value}" for key, value in resolution_options.items()]) + "\nOption: "
    resolution = get_option(f"\nChoose the quantity that you want to reduce the resolution of the photos:\n\n{resolution_prompt}", resolution_options.keys())

    redimension_prompt = "\n".join([f"{key} - {value}" for key, value in redimension_options.items()]) + "\nOption: "
    redimention = get_option(f"\nChoose the quantity that you want to redimension the photos:\n\n{redimension_prompt}", redimension_options.keys())

    convert_prompt = "\n".join([f"{key} - {value}" for key, value in convert_options.items()]) + "\nOption: "
    convert = get_option(f"\nDo you want to convert the photo(s) to jpg?\n\n{convert_prompt}", convert_options.keys())

    return resolution, redimention, convert
