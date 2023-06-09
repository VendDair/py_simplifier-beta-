import os
import sys
class Compile:
    def __init__(self, input_file, output_file) -> None:
        self.input = input_file
        self.output = output_file

    def run_code(self):
        os.system("python3 " + self.output)

    def main(self):
        with open(self.input, "r") as f:
            lines = f.readlines()

        # loop through each line
        for i, line in enumerate(lines):
            # remove any leading or trailing spaces or newlines
            line = line.rstrip()
            # split the line into words
            words = line.split()
            # loop through each word
            for j, word in enumerate(words):
                # check if words is imp to replace to import
                if word == "imp":
                    words[j] = "import"

                # check word inp to replace to input
                # elif word == "inp":
                #     words[j] = "input"

                # check word *: to replace to :
                elif word.endswith(":+"):
                    words[j] = "".join(words[j].split("+"))
                # check word init* to replace to __init__
                elif word == "init+":
                    words[j] = "def __init__"
                elif word == "re+":
                    words[j] = "return"

                # elif word == "cl+":
                #     words[j] = "class"

                elif word == "fun":
                    words[j] = "def"
                elif word == "--":
                    words[j] = "#"

                # elif word == "true":
                #     words[j] = "True"

                elif word == "ifname+":
                    words[j] = 'if __name__ = "__main__"'
                elif word == "open+":
                    words[j] = "with open"
                elif word == "if+":
                    words[j] = "elif"
                elif word == "br+":
                    words[j] = "break"
                elif word == "imp_tmp+":
                    words[j] = "import sys\nimport os\nsys.path.append(os.path.abspath('tmp'))"
                
                # check if the word ends with ":"
                elif word.endswith(":"):
                    if word.startswith('("'):
                        # print(word)
                        continue
                    # remove the ":" and add " ="
                    words[j] = word[:-1] + " ="
                    
            # add leading spaces to preserve the indentation
            new_line = " " * (len(line) - len(line.lstrip())) + " ".join(words)

            # posediting some words
            # editing prl word
            if "prl" in new_line and not "#" in new_line:
                # print(new_line)
                new_line = new_line.replace("prl", "print(")
                new_line = new_line + " )"
                # new_line = new_line.replace("# print", "kek")
            # editing inp
            if "inp" in new_line and "#" in new_line:
                # print(new_line)
                new_line = new_line.replace("inp", "input(")
                new_line = new_line + " )"
            # editing () in line with def
            if "def" in new_line and "(" in new_line and ")" in new_line and not "#" in new_line:
                new_line = new_line + ":"
            if "def" in new_line and not "(" in new_line and not ")" in new_line and not "#" in new_line:
                # new_line = new_line.replace(":", "():")
                new_line = new_line + "():"
            
            # editing true to True
            if "true" in new_line and not "#" in new_line:
                # print(new_line)
                new_line = new_line.replace("true", "True")
            # editing with open to add ()
            if "with open" in new_line and "as" in new_line and '"' in new_line and not "#" in new_line:
                # print(new_line)
                new_line = new_line.replace("open", "open(").replace("as", ") as")
                new_line = new_line + ":"
            if "if" in new_line and "=" in new_line and not "!" in new_line and not "<" in new_line and not ">" in new_line and not "#" in new_line:
                new_line = new_line.replace("=", "==")
                new_line = new_line + ":"
            if "if" in new_line and "=" in new_line and "!" in new_line and not "#" in new_line:
                new_line = new_line + ":"
            if "if" in new_line and "=" in new_line and "<" in new_line and not "#" in new_line:
                new_line = new_line + ":"
            if "if" in new_line and "=" in new_line and ">" in new_line and not "#" in new_line:
                new_line = new_line + ":"
            if "for" in new_line and "in" in new_line and not "#" in new_line:
                new_line = new_line + ":"
            # if "==" in new_line:
            #     new_line = new_line + ":"

            if "cl+" in new_line and not "#" in new_line:
                new_line = new_line.replace("cl+", "class ")
                new_line = new_line + ":"

            if "compile" in new_line and not "#" in new_line:
                    output = new_line.replace("compile ", "")
                    input_compile = output
                    # output = words[j + 1]
                    if output.endswith("psp") and not "#" in new_line:
                        output = output.split("/")
                        output = output[-1]
                        output = output.split("psp")
                        output = output[0] + "py"
                        output = "tmp/" + output
                        if "tmp" not in os.listdir("."):
                            os.system("mkdir tmp")
                        os.system(f"python3 compile.py {input_compile} {output} compile")
                        new_line = ""
                    else:
                        pass

            # test for init+    
            # if "__init__" in new_line and "def" in new_line:
            #     new_line = new_line + ":"

            # replace the original line with the modified line
            lines[i] = new_line

        # join the modified lines into a string
        new_text = "\n".join(lines)

        # write the new text to a file
        with open(self.output, "w") as f:
            f.write(new_text)


# translator = Compile("input.prb", "output.py")
# translator = Compile("pyautogui.prb", "output.py")
# translator.main()
# translator.run_code()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 compile.py input_file output_file run/compile")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        if sys.argv[3] == "run":
            translator = Compile(input_file, output_file)
            translator.main()
            translator.run_code()
        elif sys.argv[3] == "compile":
            translator = Compile(input_file, output_file)
            translator.main()