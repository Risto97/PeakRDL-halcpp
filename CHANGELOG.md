# V0.3.1

* Fix for when register has sparse fields [c3c1fcd](https://github.com/Risto97/PeakRDL-halcpp/commit/c3c1fcd57d170024843caf99a4c04fcd5e11af60)

# V0.3.0

* Refactor python code, create a class hierarchy before generating CPP files
* Copy base source files into subdirectory include/ of destination directory, generated files are still in destination directory
* Add PeakRDL option --keep-buses which will prevent omitting the addressmaps that do not contain any registers or memories but only other addressmaps, by default they are omitted.

# V0.4.0

* Header-only halcpp files documented
* Python code documented
* HalBaseNode inheriting from systemrdl Node class

# V0.4.1

* halcpp FieldBase class method field_mask() made public and new public method get_width() created
