import sys
import random

# check if filename is supplied as a command line argument
if sys.argv[1:]:
    filename = sys.argv[1]
else:
    filename = input("What is the name of the file? (extension included): ")

try:
    file = open(filename)
except (FileNotFoundError, IOError):
    print("File doesn't exist!")
    exit()

# pega o numero de linhas
num_lines = sum(1 for line in file if line.rstrip())

# gera um numero aletório dentro da quantidade de linhas
random_line = random.randint(0, num_lines)

# mover o indicador de posição do arquivo para o início.
file.seek(0)

for i, line in enumerate(file):
    if i == random_line:
        print(line.rstrip())  # rstrip remove espaços em branco
        break