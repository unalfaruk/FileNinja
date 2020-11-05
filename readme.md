# FileNinja v.0.1
## File Splitter and Joiner

This is a Python script using for splitting a file and joining chunks into a file.

* Dependencies: Python 3.x

### Notes to Who Wants to Use
It is just a simple script, I have prepared it for my specific need and generalized it later for others. So, there may be many bugs etc.

### Usage
1. JOINNING
> python3 fileNinja.py join <input_directory> <output_path>

> python3 fileNinja.py join ./test_dir/ ./test_dir/output.ext

2. SPLITTING
> python3 fileNinja.py split <input_file> <output_directory> <chunk_size_MB>

> python3 fileNinja.py split ./example.txt ./test_dir 1

### To-Do
1. argparse need to be improved.
* Some parameters (chunk size, output path) should be optional by giving them default value.
2. Usage by "import <module_name>" scenarios should be tested/verified

