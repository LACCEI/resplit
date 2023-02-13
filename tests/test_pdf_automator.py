# Testing the functionalities of the PDF Automator class.
import sys
sys.path.append("../")
from resplit import PDF_Automator

intput_dir = "input_dir"
output_dir = "output_dir"

automator = PDF_Automator(intput_dir, output_dir, "processed_log.csv")
automator.perform("selection", {"pages": "1, 3-5, 15"})