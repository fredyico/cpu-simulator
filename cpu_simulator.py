import sys

# === Instruction Class ===
class Instruction:
    def __init__(self, opcode, operands):
        self.opcode = opcode.upper()
        self.operands = operands

# === MemoryBus Class ===
class MemoryBus:
    def __init__(self, memory_file):
        self.memory = {}
        self.load_memory(memory_file)

    def load_memory(self, filename):
        try:
            with open(filename, 'r') as f:
                for line in f:
                    if line.strip():
                        address, value = map(int, line.strip().split())
                        self.memory[address] = value
        except FileNotFoundError:
            print(f"Memory file '{filename}' not found.")

    def read(self, address):
        return self.memory.get(address, 0)

    def write(self, address, value):
        self.memory[address] = value

# === CPU Class ===
class CPU:
    def __init__(self, memory_bus):
        self.registers = [0] * 32  # 32 general-purpose registers
        self.memory_bus = memory_bus
        self.instructions = []
        self.pc = 0
        self.running = True
        self.cache_enabled = False


    def load_instructions(self, filename):
        try:
            with open(filename, 'r') as f:
                for line in f:
                    if line.strip():
                        line = line.strip()
                        if ';' in line:
                            line = line.split(';')[0].strip()  # Remove everything after ';'

                        if not line:
                            continue  # Skip empty/comment-only lines

                        parts = line.split()
                        opcode = parts[0]
                        operands = [p.strip(',') for p in parts[1:]]
                        self.instructions.append(Instruction(opcode, operands))
        except FileNotFoundError:
            print(f"Instruction file '{filename}' not found.")

    def execute(self):
        while self.running and self.pc < len(self.instructions):
            instr = self.instructions[self.pc]
            print(f"[PC={self.pc}] Executing: {instr.opcode} {', '.join(instr.operands)}")
            self.run_instruction(instr)
            self.pc += 1

    # Print state after HALT or end
        print("\n[CPU] Execution completed.")
        print("[CPU] Final Register States:")
        for i, val in enumerate(self.registers):
            print(f"R{i}: {val}")
        print("\n[CPU] Final Memory State:")
        for addr in sorted(self.memory_bus.memory.keys()):
            print(f"MEM[{addr}] = {self.memory_bus.memory[addr]}")


    def run_instruction(self, instr):
        if instr.opcode == 'ADD':
            rd, rs, rt = map(self.get_register_index, instr.operands)
            self.registers[rd] = self.registers[rs] + self.registers[rt]
        elif instr.opcode == 'SUB':
            rd, rs, rt = map(self.get_register_index, instr.operands)
            self.registers[rd] = self.registers[rs] - self.registers[rt]
        elif instr.opcode == 'ADDI':
            rt, rs, imm = instr.operands
            rt = self.get_register_index(rt)
            rs = self.get_register_index(rs)
            self.registers[rt] = self.registers[rs] + int(imm)
        elif instr.opcode == 'LW':
            rt, offset_rs = instr.operands
            rt = self.get_register_index(rt)
            offset, rs = offset_rs.replace(')', '').split('(')
            rs = self.get_register_index(rs)
            address = self.registers[rs] + int(offset)
            self.registers[rt] = self.memory_bus.read(address)
        elif instr.opcode == 'SW':
            rt, offset_rs = instr.operands
            rt = self.get_register_index(rt)
            offset, rs = offset_rs.replace(')', '').split('(')
            rs = self.get_register_index(rs)
            address = self.registers[rs] + int(offset)
            self.memory_bus.write(address, self.registers[rt])
        elif instr.opcode == 'SLT':
            rd, rs, rt = map(self.get_register_index, instr.operands)
            self.registers[rd] = 1 if self.registers[rs] < self.registers[rt] else 0
        elif instr.opcode == 'BNE':
            rs, rt, offset = instr.operands
            rs = self.get_register_index(rs)
            rt = self.get_register_index(rt)
            offset = int(offset)
            if self.registers[rs] != self.registers[rt]:
                print(f"[BNE] Branching from PC={self.pc} to PC={(self.pc + 1) + offset}")
                self.pc = (self.pc + 1) + offset - 1  # subtract 1 to neutralize the main loop's pc += 1
        elif instr.opcode == 'J':
            target = int(instr.operands[0])
            print(f"[J] Jumping to PC={target}")
            self.pc = target - 1  # -1 to cancel out pc += 1 after execution
        elif instr.opcode == 'JAL':
            target = int(instr.operands[0])
            self.registers[7] = self.pc + 1  # R7 gets return address (next instruction index)
            print(f"[JAL] Saving return address {self.pc + 1} in R7 and jumping to PC={target}")
            self.pc = target - 1
        elif instr.opcode == 'CACHE':
            code = int(instr.operands[0])
            if code == 0:
                self.cache_enabled = False
                print("[CACHE] Cache disabled.")
            elif code == 1:
                self.cache_enabled = True
                print("[CACHE] Cache enabled.")
            elif code == 2:
                print("[CACHE] Cache flushed.")
            else:
                print(f"[CACHE] Unknown cache code: {code}")


        elif instr.opcode == 'HALT':
            print("[CPU] HALT encountered. Stopping execution.")
            self.running = False        
        else:
            print(f"[ERROR] Unknown instruction: {instr.opcode}")

    def get_register_index(self, reg):
        return int(reg.replace('R', ''))

# === Main Entry Point ===
def run_simulator(instruction_file, memory_file):
    memory_bus = MemoryBus(memory_file)
    cpu = CPU(memory_bus)
    cpu.load_instructions(instruction_file)
    cpu.execute()

# === Uncomment to Run ===
if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python cpu_simulator.py <instructions.txt> <memory.txt>")
    else:
        run_simulator(sys.argv[1], sys.argv[2])
