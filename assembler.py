import sys

opcodemap={
      "011000010110010001100100" : "00000001"   #ADD 
        }

machine_code = []

def parser(assembly):
    instructions = assembly.split('\n')
    return instructions 

def assembler(Instructions):
    for instruction in Instructions:
        cleaned = clean_instructions(instruction)
        bit_str = ''.join(format(ord(i), '08b') for i in cleaned)
        mapped = opcodemap["011000010110010001100100"] + bit_str[24:]
        machine_code.append(mapped)


    

def clean_instructions(instructions):
    cleaned = instructions.replace(',','')
    return cleaned.lower()

if __name__ == "__main__":
    filename = sys.argv[1]
    file = open(filename, "r")
    assembly = file.read()
    parsed = parser(assembly)
    assembler(parsed)
    print(machine_code)
