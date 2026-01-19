from insttohex import insttohex
import sys
stack = []
program = []
for line in program:
    inst = insttohex(line)
    opcode, arg = inst
    if opcode == "0x00":
        break
    elif opcode == "0x01":
        stack.append(int(arg))
    elif opcode == "0x02":
        stack.pop()
    elif opcode == "0x03":
        a = stack.pop()
        b = stack.pop()
        stack.append(a + b)
    elif opcode == "0x04":
        a = stack.pop()
        b = stack.pop()
        stack.append(b - a)
    elif opcode == "0x05":
        print(stack[-1])
