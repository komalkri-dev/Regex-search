##About this Script:
-------------------------------------------------------------------------------------------
This script searches for lines matching regular expression -r (--regex) in file/s -f (--files) with some optional arguments
optional parameters:
    -u ( --underscore ) which prints '^' under the matching text
    -c ( --color ) which highlight matching text 
    -m ( --machine ) which generate machine-readable output 
                     format: file_name:no_line:start_pos:matched_text

####Note:
These are mutually exclusive paramters:
So you cannot two optional parameter together.
#################################################################################################

##How to run the script:
-------------------------------------------------------------------------------------------
copy the regex_script.py, optional_argument.py and the files to search regular expression in same folder.
Then run,
python <regex_script.py> -f <file> -r <regular expression>
In case of multiple files, run:
python <regex_script.py> -f <file1> <file2> <file3> <filen> -r <regular expression>

####With optional parameter:
python <regex_script.py> -f <file1> <file2> <file3> <filen> -r <regular expression> -c
#################################################################################################
