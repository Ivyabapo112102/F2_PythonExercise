def decToBinary(dec):
    return bin(dec)[2:]
def binaryToN(bin_str, type):
    if type == 'decimal':
        return int(bin_str, 2)
    elif type == 'octal':
        return oct(int(bin_str, 2))[2:]
    elif type == 'hexadecimal':
        return hex(int(bin_str, 2))[2:]
    else:
        return "Invalid type"
def decToOctal(dec):
    return oct(dec)[2:]
def decToHex(dec):
    return hex(dec)[2:]
def main():
    decimal_number = int(input("Enter a decimal number: "))
    binary_number = decToBinary(decimal_number)
    print(f"Binary: {binary_number}")
    octal_number = decToOctal(decimal_number)
    print(f"Octal: {octal_number}")
    hexadecimal_number = decToHex(decimal_number)
    print(f"Hexadecimal: {hexadecimal_number}")
    binary_to_decimal = binaryToN(binary_number, 'decimal')
    print(f"Binary to Decimal: {binary_to_decimal}")
    binary_to_octal = binaryToN(binary_number, 'octal')
    print(f"Binary to Octal: {binary_to_octal}")
    binary_to_hexadecimal = binaryToN(binary_number, 'hexadecimal')
    print(f"Binary to Hexadecimal: {binary_to_hexadecimal}")

if __name__ == "__main__":
    main()
