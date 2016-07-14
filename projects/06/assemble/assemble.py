from parser import Parser
from code import Code
import sys

def assemble(asm_file):
    parser = Parser(asm_file)
    fp_out = open("{}.hack".format(asm_file), "w")
    while (parser.hasMoreCommands()):
        parser.advance()
        if parser.commandType() == Parser.L_CMD:
            continue;
 
        if parser.commandType() == Parser.A_CMD:
            out_line = "0{:015b}".format(int(parser.symbol()))
        else:
            comp = Code.comp(parser.comp())
            dest = Code.dest(parser.dest())
            jump = Code.jump(parser.jump())
            out_line = "111%s%s%s" % (comp, dest, jump)
        fp_out.write("{}\n".format(out_line))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise Exception("Must pass a .asm file to assemble!")
    assemble(sys.argv[1])