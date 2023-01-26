# Architecture Overview
As Resplit is a simple application for completing a single task, its internal architecture is also simple. Its architectural pattern is model-view-controller but all in a single file. It is flexible enough to add other types of tasks (not only splitting PDFs) in the model space. Yet, it would require significant changes in the controller and view spaces (the GUI specifically).

![Diagram for the conceptual design.](imgs/conceptual-design.svg)

The important (and still simple) part is the PDF Automator, which performs the instructed task in a batch of given files. The PDF Representation, although designed here, is substituted by objects from the [PyPDF2](https://pypi.org/project/PyPDF2/) library.