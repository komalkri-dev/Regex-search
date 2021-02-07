## About this Script:
---
> This script searches for lines matching regular expression -r (--regex) in file/s -f (--files) with some optional arguments  

Optional parameters:  
- -u ( --underscore ) which prints '^' under the matching text  
- -c ( --color ) which highlight matching text   
- -m ( --machine ) which generate machine-readable output in format: `file_name:no_line:start_pos:matched_text`  

#### Note:
- These are mutually exclusive paramters, so you cannot use two optional parameter together.

## How to run the script:
---
Copy the regex_script.py, optional_argument.py and the files to search regular expression in same folder.  
Then use this:
```bash
python regex_script.py -f [file] -r [regular expression]
```

In case of multiple files, use this:
```bash
python regex_script.py -f [file1] [file2] [file3] [filen] -r [regular expression]
```

With optional parameter:
```bash
python regex_script.py -f [file1] [file2] -r [regular expression] -c
```
---