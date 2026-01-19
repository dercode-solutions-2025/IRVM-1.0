from insttohex import *
import sys
stack = []
inst = insttohex()
math = []
if inst[0] == "0x00":
  sys.exit()
elif inst[0] == "0x01":
  stack.add(inst[1])
elif inst[0] == "0x02":
  stack.pop(stack[-1])
elif inst[0] == "0x03":
  sum(math.append(stack[-2:]))
  math = []
elif inst[0] == "0x04":
  stack.add(stack[-1] - stack[-2])
elif inst[0] == "0x05":
  print(stack[-1])
