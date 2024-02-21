

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

registers = [0,0,0,0,0,0,0,0]

def processor(machine_code):
    instructions = parser(machine_code)
    for instruction in instructions: 
        opcode = instruction[:8]
        if opcode == "10000000" or opcode == "11000000":
            print(instruction)
            execute(opcode, instruction, 0)
        else:
            print(instruction)
            execute(opcode, instruction,1)

def parser(assembly):
    instructions = assembly.split('\n')
    return instructions

def execute(opcode,instruction, mode):       # mode 0 --- add/sub
                                             # mode 1 --- mov
    if mode == 0:
        operands = instruction[8:32]
        #dest = operandmap[operands[:8]]
        dest = list(filter(lambda x: operandmap[x] == operands[:8], operandmap))[0]
        op1 = list(filter(lambda x: operandmap[x] == operands[8:16], operandmap))[0]
        op2 = list(filter(lambda x: operandmap[x] == operands[16:24], operandmap))[0]
        
        if opcode == "10000000":
            dest_chunks = [dest[i:i+8] for i in range(0, len(dest), 8)]
            op1_chunks = [op2[i:i+8] for i in range(0, len(op1), 8)] 
            op2_chunks = [op2[i:i+8] for i in range(0, len(op2), 8)] 
            registers[int((''.join(chr(int(chunk, 2)) for chunk in dest_chunks))[1]) - 1] =  registers[int((''.join(chr(int(chunk, 2)) for chunk in op1_chunks))[1])- 1] + registers[int((''.join(chr(int(chunk, 2)) for chunk in op2_chunks))[1])- 1]
            print(registers)

        elif opcode == "11000000":
            dest_chunks = [dest[i:i+8] for i in range(0, len(dest), 8)]
            op1_chunks = [op2[i:i+8] for i in range(0, len(op1), 8)] 
            op2_chunks = [op2[i:i+8] for i in range(0, len(op2), 8)] 
            registers[int((''.join(chr(int(chunk, 2)) for chunk in dest_chunks))[1]) - 1] =  registers[int((''.join(chr(int(chunk, 2)) for chunk in op1_chunks))[1]) - 1] - registers[int((''.join(chr(int(chunk, 2)) for chunk in op2_chunks))[1]) - 1]
            print(registers)


    if mode == 1:
        operands = instruction[8:40]
        dest = list(filter(lambda x: operandmap[x] == operands[:8], operandmap))[0]
        value = instruction[16:40]
        if opcode == "01000000":
            dest_chunks = [dest[i:i+8] for i in range(0, len(dest), 8)]
            value_chunks = [value[i:i+8] for i in range(0, len(value), 8)]
            registers[int((''.join(chr(int(chunk, 2)) for chunk in dest_chunks))[1])-1] = int((''.join(chr(int(chunk, 2)) for chunk in value_chunks))[1]) 
            print(registers)




 
if __name__ == "__main__":
    file = open("bin.txt", "r")
    machine_code = file.read()
    print(registers)
    processor(machine_code)
