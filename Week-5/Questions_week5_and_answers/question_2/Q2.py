def create_tree():
    leaf_height = 15
    stump_height = 5
    stump_thickness = 5

    length_line = 2 * leaf_height - 1
    lines = []

    for i1 in range(leaf_height):
        line_string = ''
        num_stars = 2 * i1 + 1

        line_string += ' ' * ((length_line - num_stars) // 2)
        line_string += '*' * num_stars
        line_string += ' ' * ((length_line - num_stars) // 2)

        lines.append(line_string)

    for i2 in range(stump_height):
        line_string = ''

        line_string += ' ' * ((length_line - stump_thickness) // 2)
        line_string += '*' * stump_thickness
        line_string += ' ' * ((length_line - stump_thickness) // 2)

        lines.append(line_string)

    for each in lines:
        print(each)

    for index in range(len(lines)):
        lines[index] = lines[index] + '\n'

    with open('output_Q2.txt', 'w+') as fileObject:
        for each_line in lines:
            fileObject.write(each_line)


if __name__ == "__main__":
    create_tree()
