import os

directory = os.fsencode("_build/features/notebooks")

skurk1 = "ï¿½"

for filename in os.listdir(directory):
    if filename.endswith(b".md"):
        myfile = os.path.join(directory, filename)

        with open(myfile, "r") as f:
            lines = f.readlines()
            for line in lines:
                if (skurk1 in line):
                    print(myfile, "\n", line)
        continue
    else:
        continue
