import subprocess
import datetime

def Notepad(prompt):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(prompt)
    subprocess.Popen(["notepad.exe", file_name])

    response = "I made a note of that"
    return response