def part_of_the_common(a,b):
    common = []
    for element in a:
        if element in b:
            common.append(element)
    return common
