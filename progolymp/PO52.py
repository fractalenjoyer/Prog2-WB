
def get_bin(string):
    binary = 0
    for c in string:
        binary = binary * 2 + (not c in "aeiouy")
    return binary


def get_count(binary, length):
    count = 0
    for i in range(length-3):
        testval = (binary >> i) & 0b111
        if testval == 0b101:
            count += 2**(length - i - 3)
        elif testval == 0b011:
            count += 2**(length - 3)
    return count

inval = "jogurtkaka"
print(2**len(inval) - 1 - get_count(get_bin(inval), len(inval)))