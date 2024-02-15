import sys

class raju:
    def __init__(self):
        self.registers = [0] * 8    #registers
        #self.registers = [0,0,0,0,0,0,0,0]
        self.memory = [0] * 256     #memory
        self.pc = 0;                #program counter

    #def decode(self, instructions):
     #   parts = instructions.split()
      #  opcodes = parts[0]
       # operands = parts[1:]
        #return opcodes, operands
    def lex(machine_bytes):
        for i 
    def execute_instructions(self, opcodes, operands):
        if opcodes.lower() == "add":
            dest, src1, src2 = operands
            self.registers[int(dest[1])] = self.registers[int(src1[1])] + self.registers[int(src2[1])]

        elif opcodes.lower() == "sub":
            dest, src1, src2 = operands
            self.registers[int(dest[1])] = self.registers[int(src1[1])] - self.registers[int(src2[1])]

        elif opcodes.lower() == "mov":
            dest, immediate = operands
            self.registers[int(dest[1])] = int(immediate)

        self.pc += 1

    def execute(self, machine_code):
        while self.pc < len(machine_code):
            opcodes, operands = self.decode(machine_code[self.pc])
            self.execute_instructions(opcodes, operands)
            print(self.registers)

        



#if __main__ == __init__:

a = raju();

machine_code = ["mov R3, 7","mov R2, 6","mov R0, 5","add R1, R2, R3", "add R2, R1, R3"]

machine_bytes = ["10010110100010100101101000101010100101001010]

a.execute(machine_code)


