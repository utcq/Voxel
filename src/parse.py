from error import Error


class Parser:
    static = []
    def __init__(self, code: str):
        #Pass in code
        self.code = code
        #Parse code
        self.code = self.Parse(self.code)

    def Parse(self, code: str) -> str:
        #Parse code into normal python
        code = self.ParseInclude(code)
        code = self.ParseImport(code)
        code = self.ParseComments(code)
        code = self.ParseKeyWords(code)
        code = self.ParseEOL(code)
        code = self.Parsenamespace(code)
        code = self.Parsestruct(code)
        code = self.ParseBraces(code)
        code = self.Parsefunctions(code)
        code = self.Parsesammente(code)
        code = self.Parsesi(code)
        code = self.Parseassaje(code)
        code = self.Parseliberu(code)
        code = self.Parsepe(code)
        code = self.Parseautrimenti(code)
        code = self.Parseco(code)
        code = self.Parsede(code)
        code = self.Parsesput(code)
        code = self.Parseturna(code)
        code = self.CleanCode(code)
        code = self.AddEntryPoint(code)
        code = """try:
    from pointers import _
    from pointers import c_malloc as malloc
    from pointers import c_free as free
    from pointers import strcpy, cast
    from pointers import Struct
except:
    pass
""" + code

        #Dump code to file
        with open("output.py", "w") as f:
            f.write(code)
        return code
    def ParseComments(self, code: str) -> str:
        for line in code.splitlines():
            if "//" in line:
                if not self.IsInString("//", line):
                    if list(line)[0] == "/" and list(line)[1] == "/":
                        code = code.replace(line, "")
                    else:
                        newLine = line.partition("//")[0]
                        code = code.replace(line, newLine)
            if "/*" in line or "*/" in line:
                if not self.IsInString("/*", line) or not self.IsInSting("*/", line):
                    if line.startswith("/*") or line.startswith("*/"):
                        code = code.replace("/*", '"""').replace("*/", '"""')
        return code

    def ParseInclude(self, code: str) -> str:
        includeName = ""
        for line in code.splitlines():
            words = line.split()
            for wordNo, word in enumerate(words):
                if words[wordNo] == "from" and not self.IsInString(words[wordNo], line):
                    if words[wordNo + 1]== "native":
                        if words[wordNo + 2] == "fratm":
                            words[wordNo] = f"from {words[wordNo + 3]} import *"
        for line in code.splitlines():
            words = line.split()
            for wordNo, word in enumerate(words):
                if word == "fratm" and not self.IsInString(word, line):
                    includeName = words[wordNo + 1]
                    code = code.replace(line, "")
                    with open(includeName.removesuffix(";") + ".vx", "r") as file:
                        code = file.read() + "\n" + code
        for line in code.splitlines():
            if "from native reference " in line:
                if self.IsInString("from native reference ", line, True):
                    continue
                code = code.replace(line, line.replace("from native reference ", "import "))
                words = line.split()
                newLine = ""
                for wordNo, word in enumerate(words):
                    if words[wordNo] == "from" and not self.IsInString(words[wordNo], line):
                        if words[wordNo + 1] == "native":
                            if words[wordNo + 2] == "reference":
                                words[wordNo] = "import"
                                words[wordNo] = ""
                                words[wordNo + 2] = ""
                                newLine = " ".join(words)
                if newLine != "":
                    code = code.replace(line, newLine)


        return code

    def ParseImport(self, code: str) -> str:
        code = code
        for line in code.splitlines():
            if "include" in line and not self.IsInString("include", line):
                code = code.replace(line, line.replace("include", "import"))
        return code

    def ParseKeyWords(self, code: str) -> str:
        for line in code.splitlines():
            if "this" in line and not self.IsInString("this", line):
                code = code.replace(line, line.replace("this", "self"))
        for line in code.splitlines():
            if "true" in line and not self.IsInString("true", line):
                code = code.replace(line, line.replace("true", "True"))
        for line in code.splitlines():
            if "false" in line and not self.IsInString("false", line):
                code = code.replace(line, line.replace("false", "False"))
        for line in code.splitlines():
            if "null" in line and not self.IsInString("null", line):
                code = code.replace(line, line.replace("null", "None"))
        for line in code.splitlines():
            if "else if" in line and not self.IsInString("else if", line):
                code = code.replace(line, line.replace("else if", "elif"))
        return code

    def ParseEOL(self, code: str) -> str:
        code = "".join([s for s in code.splitlines(True) if s.strip("\r\n")])

        for line in code.splitlines():
            skipLine = False
            for token in ("function","static", "while", "for", "if", "else", "else if", "with", "from", "namespace", '"""', "struct"):
                if token in line and not self.IsInString(token, line):
                    skipLine = True
            if ''.join(line.split()).startswith(("{", "}", "\n", "class")):
                skipLine = True
            elif line.strip() == "":
                skipLine = True
            if skipLine:
                continue
            if ";" in line and not self.IsInString(";", line):
                lineChars = list(line)
                stringCount = 0
                for i in range(len(lineChars)):
                    if lineChars[i] == '"' or lineChars[i] == "'":
                        stringCount += 1
                    if lineChars[i] == ";":
                        if stringCount % 2 == 0:
                            lineChars[i] = "\n"
                            break

            elif line.endswith((":")):
                Error(f"Syntax error in: \n{line}")
            else:
                Error(f"Missing semicolon in: \n{line}")
            if line.endswith((":")):
                Error(f"Syntax error in: \n{line}")

        return code

    def Parsepe(self, code: str) -> str:
        code = code
        for line in code.splitlines():
            if "for" in line and not self.IsInString("for", line):
                code = code.replace(line, line.replace("for", "for"))
        return code


    def Parsenamespace(self, code: str) -> str:
        code = code
        for line in code.splitlines():
            if "namespace" in line and not self.IsInString("namespace", line) and line.split(" ")[0] == "namespace":
                code = code.replace(line, line.replace("namespace", "class"))
            if "::" in line and "-->" in line:
                la = line.split("-->")
                if "std::" in line:
                    ztra = la[0].replace("std::", "")
                else:
                    ztra = la[0].replace("::", ".")
                del la[0]
                new = ztra + "(\n" + str(',\n'.join(la)).strip() + ")"
                code = code.replace(line, new)
        return code

    def Parsestruct(self, code: str) -> str:
        code = code
        for line in code.splitlines():
            if "struct" in line and not self.IsInString("struct", line) and line.split(" ")[0] == "struct":
                NAME = line.split(" ")[1]
                newline = f"class {NAME}(Struct)"
                code = code.replace(line, newline)
        return code





    def Parseliberu(self, code: str) -> str:
        code = code
        for line in code.splitlines():
            if "freev(" in line and not self.IsInString("freev(", line) and ")" in line:
                ne = str("del " + line.replace(")", "").split("(")[1])
                spac = line.split("freev")[0]
                ne = spac + ne
                code = code.replace(line, ne)

        return code


    def Parseassaje(self, code: str) -> str:
        code = code
        for line in code.splitlines():
            if "var " in line and not self.IsInString("var ", line) and "=" in line:
                code = code.replace(line, line.replace("var ", ""))
        return code


    def Parsesi(self, code: str) -> str:
        code = code
        for line in code.splitlines():
            if "if" in line and not self.IsInString("if", line) and ":" in line:
                code = code.replace(line, line.replace("if", "if"))
        return code

    def Parseautrimenti(self, code: str) -> str:
        code = code
        for line in code.splitlines():
            if "else" in line and not self.IsInString("else", line):
                code = code.replace(line, line.replace("else", "else"))
        return code

    def Parseco(self, code: str) -> str:
        code = code
        for line in code.splitlines():
            if "with" in line and not self.IsInString("with", line) and ":" in line:
                code = code.replace(line, line.replace("with", "with"))
        return code

    def Parsede(self, code: str) -> str:
        code = code
        for line in code.splitlines():
            if "from" in line and not self.IsInString("from", line):
                code = code.replace(line, line.replace("from", "from"))
        return code

    def Parseturna(self, code: str) -> str:
        code = code
        for line in code.splitlines():
            if "return" in line and not self.IsInString("return", line):
                code = code.replace(line, line.replace("return", "return"))
        return code



    def ParseBraces(self, code: str) -> str:
        leftBracesAmount = 0
        for line in code.splitlines():
            if "{" in line:
                lineChars = list(line)
                stringCount = 0
                for i in range(len(lineChars)):
                    if lineChars[i] == '"' or lineChars[i] == "'":
                        stringCount += 1
                    if lineChars[i] == "{":
                        if stringCount % 2 == 0 and stringCount != 0:
                            leftBracesAmount += 1
                            break
        rightBracesAmount = 0
        for line in code.splitlines():
            if "}" in line:
                lineChars = list(line)
                stringCount = 0
                for i in range(len(lineChars)):
                    if lineChars[i] == '"' or lineChars[i] == "'":
                        stringCount += 1
                    if lineChars[i] == "}":
                        if stringCount % 2 == 0 and stringCount != 0:
                            rightBracesAmount += 1
                            break

        if leftBracesAmount != rightBracesAmount:
            Error(("Braces amount is not equal"))

        newCode = ""
        splitLines = code.splitlines();
        for line in splitLines:
            if ";" in line and not self.IsInString(";", line):
                lineChars = list(line)
                stringCount = 0
                for i in range(len(lineChars)):
                    if lineChars[i] == '"' or lineChars[i] == "'":
                        stringCount += 1
                    if lineChars[i] == ";":
                        if stringCount % 2 == 0:
                            lineChars[i] = "\n"
                            break
                line = "".join(lineChars)
            if "class" in line:
                if not self.IsInString("class", line):
                    line = line.replace("class", "class")
                    line = "\n"+" ".join(line.split())
            if "function" in line:
                if line.partition("function")[0].count("\"") != 0 and line.partition("function")[0].count("\"") % 2 == 0:
                    words = line.split()
                    for wordNo, word in enumerate(words):
                        if word == "function":
                            speechCount = line.partition("function")[2].count("\"")
                            otherCount = line.partition("function")[2].count("'")
                            if speechCount % 2 == 0 and otherCount % 2 == 0:
                                words[wordNo] = "def"
                                break
                    line = " ".join(words)
            leftBraceExpression = ''.join(line.split())
            if not self.IsInString("{", leftBraceExpression):
                if ''.join(line.split()).startswith(("{")):
                    newCode += ":\n"
            if not self.IsInString("}", line):
                    line = line.replace("}", "#endindent")
            if not self.IsInString("{", line):
                line = line.replace("{", "#startindent")
            line += "\n"
            newCode += line
            line += "\n"

        return newCode

    def Parsefunctions(self, code: str) -> str:
        code = code
        for line in code.splitlines():
            if "function" in line and not self.IsInString("function", line):
                code = code.replace(line, line.replace("function", "def"))
        for line in code.splitlines():
            if "def Start" in line and not self.IsInString("def Start", line):
                code = code.replace(line, line.replace("def Start", "def __init__"))
        for line in code.splitlines():
            if ") is" in line and not self.IsInString(") is", line):
                code = code.replace(line, line.replace(") is", ") ->"))
        for line in code.splitlines():
            if "def" in line:
                if (line.partition("def")[0].strip() == ""):
                    code = code.replace(line, line.replace("(", "("))
        for line in code.splitlines():
            if "static" in line:
                code = code.replace(line, line.replace("static ", ""))
                global static
                nzr = line.split(" ")
                num = nzr.index("def")
                new = nzr[num+1].replace('(', " ").replace(")","").split(" ")[0]

                self.static.append(new)
        return code

    def Parsesammente(self, code: str) -> str:
        code = code
        for line in code.splitlines():
            if "while" in line and not self.IsInString("while", line):
                code = code.replace(line, line.replace("while", "while"))
        return code

    def Parsesput(self, code: str) -> str:
        code = code
        for line in code.splitlines():
            if "printf" in line and not self.IsInString("printf", line):
                code = code.replace(line, line.replace("printf", "print"))
        return code

    def CleanCode(self, code : str) -> str:
        #I'm not going to lie, I made a lot of mistakes. Let's hope these hacks fix it.

        splitLines = code.splitlines()
        for lineNo, line in enumerate(splitLines):
            if line.startswith(":"):
                splitLines[lineNo - 1] = splitLines[lineNo - 1] + ":"
                splitLines[lineNo] = ""
        newCode = ""
        for line in splitLines:
            newCode += line + "\n"
        code = newCode

        splitLines = code.splitlines()
        newCode = ""
        for lineNo, line in enumerate(splitLines):
            i = 0
            indentCount = 0
            while i <= lineNo:
                if "#endindent" in splitLines[i]:
                    if not self.IsInString("#endindent", splitLines[i], True):
                        indentCount -= 1
                elif "#startindent" in splitLines[i] and not self.IsInString("#startindent", splitLines[i], True):
                    if not self.IsInString("#startindent", splitLines[i]):
                        indentCount += 1
                i += 1
            newCode += ("    " * indentCount) + line + "\n"
        code = newCode

        #Remove indent helpers
        newCode = ""
        for line in code.splitlines():
            if "#endindent" in line:
                if not self.IsInString("#endindent", line):
                    line = line.replace(line, "")
            if "#startindent" in line:
                if not self.IsInString("#startindent", line):
                    line = line.replace(line, "")
            newCode += line + "\n"
        code = newCode

        #Tidy code by removing empty lines
        newCode = ""
        for line in code.splitlines():
            if line.strip("\t\r\n") == "":
                line = line.replace(line, line.strip("\t\r\n"))
                newCode += line
            else:
                newCode += line + "\n"
        code = newCode

        code = "\n".join([ll.rstrip() for ll in code.splitlines() if ll.strip()])

        return code

    def AddEntryPoint(self, code: str) -> str:
        code += "\n"
        code += f'''
if __name__ == "__main__":
    main = Main()
'''
        for item in self.static:
            code+=f"    staticmethod(main.{item})\n"
        code += '''    main.Main()'''

        return code

    def IsInString(self, phrase : str, line : str, returnIfMultiple = False) -> bool:
        if not phrase in line:
            return False
        if line.count(phrase) > 1:
            return returnIfMultiple
        leftSide = line.partition(phrase)[0]
        if leftSide.count("\"") > 0:
            if leftSide.count("\"") % 2 == 0:
                return False
            else:
                return True
        if leftSide.count("\'") > 0:
            if leftSide.count("\'") % 2 == 0:
                return False
            else:
                return True
