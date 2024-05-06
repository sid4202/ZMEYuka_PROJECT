txtName = "input.txt"

def getMazeMatrix():
    with open(txtName, "r") as f: file = f.read()
    return [[file.replace("\n", "")[j+i*len(file.split("\n")[0])] for j in range(len(file.split("\n")[0]))] for i in range(len(file)//len(file.split("\n")[0]))]