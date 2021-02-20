import json


def file_to_dictionary():
    file_name = open('District_Locations.txt')
    files = file_name.readlines()
    files = files[1:]
    districts = {}
    for line in files:
        print(line)
        if line == "District,Long,Lat":
            continue
        else:
            s = []
            s = line.split(",")
            district = s[0]
            long = s[1]
            s[2] = s[2].strip("\n")
            lat = s[2]
            districts[district] = long, lat

    return districts;


def save(dictionary):
    try:
        with open("output.json", "w+") as fo:
            json.dump(dictionary, fo)
    except NameError:
        print("Name Error Occurred")
    except OSError:
        print("Something Went Wrong")


if __name__ == "_main_":
    result = file_to_dictionary()
    print(result)
    save(result)