try:
    from termcolor import colored
except ImportError:
    colored = None

class OptionalArgument:
    """optional arguments implementation:
    -u ( --underscore ) which prints '^' under the matching text
    -c ( --color ) which highlight matching text 
    -m ( --machine ) which generate machine-readable output
                  format: file_name:no_line:start_pos:matched_text"""

    def __init__(self, file, line, line_num):
        self.file = file
        self.line = line
        self.line_num = line_num

    def printline(self):
        """
        If given regular expression matches to any string then it prints the line, line number and file name.
        """
        print(f"{self.line}  ||  line number: {self.line_num}  ||  file name: {self.file} ")

    def underscore_option(self, start, end):
        """
        If you give underscore option(-u, --underscore), then it prints '^' under the matching text
        """
        self.printline()

        for j in range(0, start):
            print(" ", end="")
        for j in range(start, end):
            print("^", end="")
        print()

    def color_option(self, matched_string): 
        """
        If you give color option(-c, --color), then it highlight matching text 
        """
        replaced_line = self.line.replace(matched_string, colored(matched_string, "white", "on_blue"))
        print( f"line: {replaced_line}  ||  line number: {self.line_num}  ||  file name: {self.file} ")


    def machine_option(self,start, matched_string):
        """ If you give machine option(-m, --machine) then output will generate machine-readable output in
                  format: file_name:no_line:start_pos:matched_text
        """
        print(f"{self.file}:{self.line_num}:{start}:{matched_string}")


if __name__ == "main":
    pass