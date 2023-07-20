
# V0.3.0

* Refactor python code, create a class hierarchy before generating CPP files
* Copy base source files into subdirectory include/ of destination directory, generated files are still in destination directory
* Add PeakRDL option --keep-buses which will prevent omitting the addressmaps that do not contain any registers or memories but only other addressmaps, by default they are omitted.
