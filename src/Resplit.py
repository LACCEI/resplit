# Main Resplit file.

import argparse
import pypdf
import re
import os
import csv

class PDF_Automator:
    """PDF Automator class"""

    def __init__(self, input_dir: str = "", output_dir: str = "", \
    csv_file: str = ""):
        self.__input_dir = input_dir
        self.__output_dir = output_dir
        self.__csv_file = csv_file

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
        processed_pdfs = []
        
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
        input_files = os.listdir(self.__input_dir)
        total_number_files = len (input_files)

        for file in input_files:
            if file.endswith(".pdf"):
                reading = pypdf.PdfReader(self.__input_dir + "/" + file)
                writing = pypdf.PdfWriter()
                for pg in nums:
                    if pg <= (len(reading.pages)):
                        writing.add_page(reading.pages[pg - 1])
                    # else:
                    #     FIXME: Add warning when page out of bound.
                writing.write(self.__output_dir + "/" + file)

                if self.__csv_file != '':
                    processed_pdfs.append(file) 
        
        if self.__csv_file != '':
            self.__write_csv(processed_pdfs)

    def set_csv_file(self, csv_file: str):
        """Set the path to the CSV file where to write the log."""
        self.__csv_file = csv_file

    def dis_csv(self):
        """Disable logging with CSV."""
        self.__csv_file = ''

    def __write_csv(self, files: list):
        """Writting the log of processed files to the CSV file."""
        if self.__csv_file != '':
            # log_file_path = self.__output_dir + self.__csv_file
            log_file_path = self.__csv_file
            if os.path.exists(log_file_path):
                os.remove(log_file_path)
            
            log_file = open(log_file_path, "w")
            output = csv.writer(log_file)
            output.writerow(["File"])
            
            for file in files:
                row = []
                row.append(file)
                output.writerow(row)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog = 'Resplit',
        description= 'Utility function to trim a batch of PDF files.'
    )

    parser.add_argument('input_folder')
    parser.add_argument('output_folder')
    parser.add_argument('selection')
    parser.add_argument('-l', '--log')

    args = parser.parse_args()
    csv_filename = args.log if args.log else ''

    automator = PDF_Automator(
        args.input_folder,
        args.output_folder,
        csv_filename
    )
    automator.perform("selection", {'pages': args.selection})