import winshell

def Recycle():
    winshell.recycle_bin().empty(
        confirm=True, show_progress=False, sound=True
    )
    response = "Recycle Bin Emptied"
    return response