import eel 
from resplitclass import *
import tkinter 
import tkinter.filedialog as filedialog

eel.init('.')

@eel.expose
def processing(input_dir: str, output_dir:str, check: bool, task:str, specification, name: str):
    automator = PDF_Automator(input_dir, output_dir, name, eel.updateProcessBar) #generates csv file when passed the name or ' '
    automator.perform("selection", {"pages": "1, 3-5, 15"})

@eel.expose
def selectFolder():
    root = tkinter.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    directory_path = filedialog.askdirectory()
    return directory_path

eel.start('index.html', size=(350, 400))