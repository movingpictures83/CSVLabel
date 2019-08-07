# CSVLabel
# Language: Python
# Input: TXT (keyword, value pairs)
# Output: CSV (labeled)
# Tested with: PluMA 1.0, Python 3.6

PluMA plugin to take a CSV file and label each row (the first row is assumed to be a header, and labeled with "").

The input TXT file is a list of keyword, value pairs.  Two keywords should be supplied:

inputfile: The name of the CSV input file
label: The label to use for each row

The output CSV file will contain an additional entry at the beginning of each row.  For the first, it will be the
empty string ("") as specified above.  The rest will have the user-supplied label in the input TXT file.

