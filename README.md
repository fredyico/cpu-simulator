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

📦 File Structure
├── cpu_simulator.py      # main logic
├── instructions.txt      # sample instruction input
├── memory.txt            # initial memory values
└── README.md             # this file

👨‍💻 Author
Built by Frederico Beckedorff
Part of the Codecademy Computer Science Path