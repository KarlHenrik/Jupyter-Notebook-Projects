import os

directory = os.fsencode(b"_build/features")

badGuy1 = "![png](C%3A/Users/KarlH/Dropbox/GitHubRepositories/Jupyter-Notebook-Projects/_build/"
badGuy2 = "C:\\Users\\KarlH\\Dropbox\\GitHubRepositories\\Jupyter-Notebook-Projects\\content\\"

for subdir, dirs, files in os.walk(directory):
    for file in files:
        #print os.path.join(subdir, file)
        if file.endswith(b".md"):
            myfile = os.path.join(subdir, file)

            with open(myfile, "r") as f:
                lines = f.readlines()
            with open(myfile, "w") as f:
                for line in lines:
                    if (badGuy1 in line):
                        f.write(line.replace(badGuy1, "![png](../../"))
                        print("BG1")
                    elif (badGuy2 in line):
                        f.write(line.replace(badGuy2, ""))
                        print("BG2")
                    else:
                        f.write(line)
            continue
        else:
            continue
print("Finished")
