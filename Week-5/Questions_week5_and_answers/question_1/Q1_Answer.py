import json


def file_to_dictionary():
    """

    Complete this Function. You must read the District_Locations.txt file and convert it to a dictionary as instructed in
    the Instruction.txt

    Output of this function is given in the Instruction file

    """
    file_location = "District_Locations.txt"
    try:
        with open(file_location, "r+") as fo:
            file_read = fo.read()
            fo.seek(0, 0)
            file = fo.readlines()

        file = file[1:]

        districts = []
        for each_district in file:
            district_split = each_district.split(',')
            for i in range(len(district_split)):
                if "\n" in district_split[i]:
                    district_split[i] = district_split[i][:-1]

            districts.append(district_split)

        geo_dic = {}
        for each in districts:
            longitude = each[1]
            latitude = each[2]

            if not isinstance(longitude, float):
                longitude = float(longitude);
                latitude = float(latitude);

            geo_dic[each[0]] = [longitude, latitude]

        return geo_dic

    except OSError:
        print("Os error!!!")
        return
    except FileNotFoundError:
        print("file not found")
        return


def save(dictionary):
    """
    Used to save dictionary to the folder you don't have to edit this
    :param dictionary: 
    :return: 
    """
    
    try:
        with open("output.json", "w+") as fo:
            json.dump(dictionary, fo)
    except NameError:
        print("Name Error Occurred")
    except OSError:
        print("Something Went Wrong")
    except FileExistsError:
        print("file already exists")


if __name__ == "__main__":
    """
    Used to execute the functions you don't have to change anything here
    """
    result = file_to_dictionary()
    print(result)
    save(result)
