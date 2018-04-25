import sys
import fileinput
with fileinput.FileInput(sys.argv[1], inplace=True) as file:
    for line in file:
        print(line.replace("<?xml version=\"1.0\" encoding=\"UTF-8\" ?><svg xmlns=\"http://www.w3.org/2000/svg\" version=\"1.1\">", "<?xml version=\"1.0\" encoding=\"UTF-8\" ?><svg  width=\"100%\" height=\"100%\" viewBox=\"0 0 2000 2000\"  xmlns=\"http://www.w3.org/2000/svg\" version=\"1.1\">"), end="")
