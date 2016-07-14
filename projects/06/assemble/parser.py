class Parser(object):

    A_CMD = 'A_COMMAND'
    C_CMD = 'C_COMMAND'
    L_CMD = 'L_COMMAND'

    def __init__(self, file_name):
        self.lines = []
        with open (file_name, "r") as fp:
            for line in fp.readlines():
                line = line.strip()
                if not line or line.startswith("//"):
                    continue
                self.lines.append(line)
        self.current_position = 0

    def commandType(self):
        if not self.current_command:
            raise Exception("current_command is empty")

        if self.current_command.startswith("@"):
            return self.A_CMD

        return self.C_CMD

    def hasMoreCommands(self):
        return self.current_position < len(self.lines)

    def advance(self):
        self.current_command = self.lines[self.current_position]
        self.current_position += 1

    def symbol(self):
        return self.current_command.strip("@R")

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
