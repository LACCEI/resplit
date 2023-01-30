# Main Resplit file.

import argparse
import tkinter
import pypdf
import re
import os

class PDF_Automator:
    """PDF Automator class"""

    def __init__(self, input_folder: str = "", output_folder: str = "", \
    Resplit_GUI = None):
        self.__GUI_interface = Resplit_GUI
        self.__input_folder = input_folder
        self.__output_folder = output_folder

    def perform(self, task: str, config: dict):
        """
        Specify and run the task to perform in the batch of PDFs.

        Read more about the specific tasks than can be perfomed in the
        documentation. This implementation only allows selection.
        """
        if task == "selection":
            if re.fullmatch( \
            '([0-9]+|[0-9]+-[0-9]+)(, ([0-9]+|[0-9]+-[0-9]+))*', \
            config["pages"]) == None:
                raise Exception("Task: selection. Error: Invalid selection of \
                pages.")
            else:
                self.__task_selection(config["pages"])
        else:
            raise Exception("Invalid tasks in the PDF Automator class.")

    def __task_selection(self, pgs: str):
        """Implementation of the selection task."""
        
        pages = pgs.split(",")
        nums = []
        
        for i in range(len(pages)):
            pages[i] = pages[i].strip()
            if "-" in pages[i]:
                nums_ie = pages[i].split("-")
                index = int(nums_ie[0])
                end = int(nums_ie[1])
                while index <= end:
                    nums.append(index)
                    index += 1
            else:
                nums.append(int(pages[i]))
        
        # Automation task.
        input_files = os.listdir(self.__input_folder)
        for file in input_files:
            if file.endswith(".pdf"):
                reading = pypdf.PdfReader(self.__input_folder + "/" + file)
                writing = pypdf.PdfWriter()
                for pg in nums:
                    if pg <= (len(reading.pages)):
                        writing.add_page(reading.pages[pg - 1])
                    # else:
                    #     FIXME: Add warning when page out of bound.
                    # FIXME: Send update to the GUI.
                writing.write(self.__output_folder + "/" + file)

class Resplit_GUI:
    """Graphical user interface of Resplit."""

    def __init__(self):
        # Creating the window.
        self.__window = tkinter.Tk()
        self.__window.title("Resplit")
        self.__window.geometry("800x600")
        self.__build_ui()
        
        # Create the model.
        self.__model = PDF_Automator("", "", self)

        # Display the window.
        self.__window.mainloop()

    def __build_ui(self):
        # FIXME: GUI incomplete.
        container = tkinter.Frame(self.__window)
        container.grid(padx = 20, pady = 20)
        
        text = tkinter.Label(container, text="LACCEI Resplit Tool")
        text.place(x = 70, y = 90)

# Top-level code.
if __name__ == '__main__':
    gui = Resplit_GUI()