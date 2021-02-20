import json


def file_to_dictionary():
    """

    Complete this Function. You must read the District_Locations.txt file and convert it to a dictionary as instructed in
    the Instruction.txt

    Output of this function is given in the Instruction file

    """

    return;


def save(dictionary):
    try:
        with open("output.json", "w+") as fo:
            json.dump(dictionary, fo)
    except NameError:
        print("Name Error Occurred")
    except OSError:
        print("Something Went Wrong")


if __name__ == "__main__":
    result = file_to_dictionary()
    print(result)
    save(result)
