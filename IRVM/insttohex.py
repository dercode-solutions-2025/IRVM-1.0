def insttohex(line):
	commands = {
	"HALT": "0x00",
	"PUSH": "0x01",
	"POP": "0x02",
	"ADD": "0x03",
	"SUB": "0x04",
	"PRINT": "0x05",
	}
	return [commands.get(line.upper().split(maxsplit=1)[0]), line.split(maxsplit=1)[1] if len(line.split(maxsplit=1)) == 2 else None]
