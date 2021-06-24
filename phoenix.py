import random
import os
import subprocess

class Phoenix:
    def __init__(self, code, lang):
        self.code = code
        self.lang = lang

    def process_c_cpp(self):
        magicNum = random.randint(1, 100000)

        #create code file
        file = open(str(magicNum) +'.c','w')
        file.write(self.code)
        file.close()

        isCompileSuccess = False
        out = ""
        compiler_used = ""

        #compile code file
        if(self.lang == "C"):
            compiler_used = "gcc "
        else:
            compiler_used = "g++ "

        p = subprocess.Popen(compiler_used+ str(magicNum) +'.c', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        isCompileSuccess = True
        for line in p.stdout.readlines():
            out = out+line.decode("utf-8")
            isCompileSuccess = False
            print(line)
        os.remove(str(magicNum) +'.c')

        if(isCompileSuccess):
        #run
            p = subprocess.Popen('a',stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            for line in p.stdout.readlines():
                out = out+line.decode("utf-8")

        return out

    def process_python(self):
        magicNum = random.randint(1, 100000)

        #create code file
        file = open(str(magicNum) +'.py','w')
        file.write(self.code)
        file.close()

        out = ""

        #run code file
        p = subprocess.Popen("python "+ str(magicNum) +'.py', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        isCompileSuccess = True
        for line in p.stdout.readlines():
            out = out+line.decode("utf-8")
            isCompileSuccess = False
            print(line)
        os.remove(str(magicNum) +'.py')

        return out

    def process_java(self):
        #magicNum = random.randint(1, 100000)

        #create code file
        file = open('Main.java','w')
        file.write(self.code)
        file.close()

        isCompileSuccess = False
        out = ""

        #compile code file

        p = subprocess.Popen("javac Main.java", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        isCompileSuccess = True
        for line in p.stdout.readlines():
            out = out+line.decode("utf-8")
            isCompileSuccess = False
            print(line)
        os.remove('Main.java')

        if(isCompileSuccess):
        #run
            p = subprocess.Popen('java Main',stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            for line in p.stdout.readlines():
                out = out+line.decode("utf-8")

        return out