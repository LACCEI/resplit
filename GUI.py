import eel 
from resplit import *
import tkinter 
import tkinter.filedialog as filedialog

eel.init('interface')

@eel.expose
def processing(input_dir: str, output_dir:str, check: bool, task:str, specification):
    automator = PDF_Automator(input_dir, output_dir, "processed_log.csv")
    automator.perform("selection", {"pages": "1, 3-5, 15"})


@eel.expose
def selectFolder():
    root = tkinter.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    directory_path = filedialog.askdirectory()
    return directory_path


eel.start('index.html', size=(1200,800))


