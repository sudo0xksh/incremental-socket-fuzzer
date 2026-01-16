# 🔥 Incremental Socket Fuzzer

Incremental Socket Fuzzer is a Python-based tool that sends
random payloads of increasing size to a TCP service
until the service crashes or stops responding.

This tool is designed for learning how crashes happen,
not for exploitation.

---

## What This Tool Does

- Connects to a TCP service
- Sends random data
- Increases payload size step by step
- Stops when the target crashes
- Reports the payload size that caused the crash

Slow pressure.
Clear feedback.
Simple logic.

---

## Why This Exists

Because buffer overflows and crashes don’t happen magically.
They happen when software receives more input than it can handle.

This tool helps you **see that breaking point**.

---

## Usage

Run the script after updating target IP and port  
python socket_fuzzer.py

Make sure the service:
- Is running in a lab
- Is intentionally vulnerable
- Is monitored for crashes

---

## Important Notes

- This is NOT an exploit
- No offsets or shellcode
- Just fuzzing behaviour
- Intended only for controlled environments

---

## Final Thought

Crash first.
Understand later.
That’s how vulnerability research begins.
