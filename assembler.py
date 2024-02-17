import sys

opcodemap={
      "011000010110010001100100" : "10000000",   #ADD 
      "011011010110111101110110" : "01000000",   #mov
      "011100110111010101100010" : "11000000"   #sub

        }

operandmap = {
        "0111001000110001" : "00000001", #{'r1': '0111001000110001'}
        "0111001000110010" : "00000010", #{'r2': '0111001000110010'}
        "0111001000110011" : "00000011", #{'r3': '0111001000110011'}
        "0111001000110100" : "00000100", #{'r4': '0111001000110100'}
        "0111001000110101" : "00000101", #{'r5': '0111001000110101'}
        "0111001000110110" : "00000110", #{'r6': '0111001000110110'}
        "0111001000110111" : "00000111", #{'r7': '0111001000110111'}
        "0111001000111000" : "00001000"  #{'r8': '0111001000111000'}
        }

machine_code = []
final = []

def parser(assembly):
    instructions = assembly.split('\n')
    return instructions

def mapper(machine_code):
    for instruction in machine_code:
        total_buff = ""
        opcode = instruction[:8]
        total_buff = total_buff + opcode
        start = 8
        for i in range((len(instruction)-8)//16 ):
            buffer = instruction[start: start + 16]
            if buffer in operandmap:
                buffer = operandmap[buffer]
                total_buff += buffer
            else:
                total_buff += buffer
            start += 16
        final.append(total_buff)


def assembler(Instructions):
    for instruction in Instructions:
        cleaned = clean_instructions(instruction)
        bit_str = ''.join(format(ord(i), '08b') for i in cleaned)
        opcode = bit_str[:24]
        if len(instruction) != 0:
            if opcode == "011000010110010001100100":
                mapped = opcodemap["011000010110010001100100"] + bit_str[24:]
                machine_code.append(mapped)
            elif opcode == "011011010110111101110110": 
                mapped = opcodemap["011011010110111101110110"] + bit_str[24:]
                machine_code.append(mapped)
            elif opcode == "011100110111010101100010":  
                mapped = opcodemap["011100110111010101100010" ] + bit_str[24:]
                machine_code.append(mapped)
    mapper(machine_code)
 
def clean_instructions(instructions):
    cleaned = instructions.replace(',','')
    cleaned = cleaned.replace(' ', '')
    return cleaned.lower()

if __name__ == "__main__":
    filename = sys.argv[1]
    file = open(filename, "r")
    assembly = file.read()
    parsed = parser(assembly.lower())
    assembler(parsed)
    fileout = open("bin.txt", "w")
    fileout.write('\n'.join(final))
