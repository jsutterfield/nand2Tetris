from symbol_table import SymbolTable

class Parser(object):

    A_CMD = 'A_COMMAND'
    C_CMD = 'C_COMMAND'
    L_CMD = 'L_COMMAND'

    def __init__(self, file_name):
        self.lines = []
        self.current_position = 0
        self.symbol_table = SymbolTable()
        self.readInFile(file_name)
        self.addLabelsToSymbolTable()
        self.substituteVars()

    def readInFile(self, file_name):
        with open (file_name, "r") as fp:
            for line in fp.readlines():
                line = line.strip()
                # skip empty newlines and comments
                if not line or line.startswith("//"):
                    continue
                self.lines.append(line.split()[0])

    def addLabelsToSymbolTable(self):
        line_count = 1
        while (self.hasMoreCommands()):
            self.advance()
            if self.commandType() == Parser.L_CMD:
                # TODO check this, this is wonky
                self.symbol_table.addEntry(self.symbol(), line_count-1)
            else:
                line_count += 1
        # reset current_position after reading
        self.current_position = 0

    def substituteVars(self):
        while (self.hasMoreCommands()):
            self.advance()
            if self.commandType() != Parser.A_CMD:
                continue
            var = self.symbol()
            if var.isdigit():
                continue
            if not self.symbol_table.contains(var):
                self.symbol_table.addEntry(var)
            self.lines[self.current_position-1] = "@{}".format(self.symbol_table.getAddress(var))
        # reset current_position after reading
        self.current_position = 0

    def commandType(self):
        if not self.current_command:
            raise Exception("current_command is empty")

        if self.current_command.startswith("@"):
            return self.A_CMD

        if self.current_command.startswith("("):
            return self.L_CMD

        return self.C_CMD

    def hasMoreCommands(self):
        return self.current_position < len(self.lines)

    def advance(self):
        self.current_command = self.lines[self.current_position]
        self.current_position += 1

    def symbol(self):
        return self.current_command.strip("@()")

    def dest(self):
        if len(self.current_command.split("=")) == 2:
            return self.current_command.split("=")[0]

    def comp(self):
        if len(self.current_command.split(";")) == 2:
            return self.current_command.split(";")[0]
        elif len(self.current_command.split("=")) == 2:
            return self.current_command.split("=")[1]

    def jump(self):
        if len(self.current_command.split(";")) == 2:
            return self.current_command.split(";")[1]
