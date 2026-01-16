# 🔥 Incremental Socket Fuzzer

Incremental Socket Fuzzer is a Python-based fuzzing tool that sends
random data to a TCP service while gradually increasing payload size.

The goal is to identify the input size at which a service crashes.

---

## What This Tool Demonstrates

- How network services handle external input
- Why size limits matter
- How crashes are discovered through fuzzing
- The first step of vulnerability research

---

## Usage

python socket_fuzzer.py <ip> <port> <start_size> <step>

Example  
python socket_fuzzer.py 127.0.0.1 9999 100 100

---

## Notes

- This is not an exploit
- No shellcode, offsets, or memory control
- Use only in lab environments

---

## Final Thought

Fuzzing is about patience, not power.
