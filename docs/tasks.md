# Resplit Tasks
The architecture overview explains that the application has a model that can perform tasks in a given batch of PDFs. This document details those tasks and how to call them in the PDF Automator class method `perform()`.

## List of Tasks
### 1. Select
This operation takes the batch of PDFs and, given a selection, produces an output batch with the specified pages of each PDF. For example, if you only want pages 1, 3, 4, and 5 of every PDF, this operation takes the input batch and produces a PDF for every input file with those pages. Note that if the selection has a page number that does not exist in the input file, the method omits that page. It may also produce a warning.

The "perform()" method will expect a dictionary with a single value, pages.

```python
config = {
    "pages": "1, 3-5"
}
```

Pages must be a string with comma-separate values (only numbers) of the pages to select or a range specified with a dash.

Example:
```python
input_dir = "./in"
output_dir = "./out"
automator = PDF_Automator(input_dir, output_dir)

config = {
    "pages": "1, 3-5"
}

automator.perform("selection", config)
```