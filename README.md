# CPU Simulator 🧠💾

A Python-based CPU simulator built for the Codecademy Computer Architecture Portfolio Project.  
This simulator mimics the behavior of a simplified MIPS processor, executing instructions from a file, simulating memory access, and optionally handling cache.

## 📂 Features

- 32 general-purpose registers
- Memory read/write via simulated memory bus
- Instruction fetch, decode, and execute stages
- Support for inline comments (`;`)
- Simulated CACHE instruction (enable/disable/flush)

## 🛠 Supported Instructions

| Instruction | Description |
|------------|-------------|
| `ADD`      | `Rd ← Rs + Rt` |
| `ADDI`     | `Rt ← Rs + immediate` |
| `SUB`      | `Rd ← Rs - Rt` |
| `SLT`      | `Rd ← 1 if Rs < Rt else 0` |
| `BNE`      | Branch if `Rs ≠ Rt` |
| `J`        | Jump to instruction at index |
| `JAL`      | Jump and store return address in `R7` |
| `LW`       | Load word from memory |
| `SW`       | Store word to memory |
| `CACHE`    | `0 = Off`, `1 = On`, `2 = Flush` |
| `HALT`     | Stop execution |

## 🚀 How to Run

```bash
python cpu_simulator.py instructions.txt memory.txt

📄 Example: instructions.txt
ADDI R1, R0, 10      ; Set R1 = 10
ADDI R2, R0, 20      ; Set R2 = 20
SLT R3, R1, R2       ; R3 = 1
BNE R1, R2, 2        ; Branch if not equal
ADDI R4, R0, 99      ; Skipped if branch taken
HALT

🧠 Example: memory.txt
0 0
4 100
8 200

📦 File Structure
├── cpu_simulator.py      # main logic
├── instructions.txt      # sample instruction input
├── memory.txt            # initial memory values
└── README.md             # this file

👨‍💻 Author
Built by Frederico Beckedorff
Part of the Codecademy Computer Science Path

Feel free to fork, contribute, or use it as a learning tool! 🚀