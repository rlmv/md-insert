

Pandoc Markdown extension for inserting file contents into code blocks. Inserts the specified files as codeblocks, one codeblock per file. Built to keep external source code synced with embedded versions in lecture notes.
    
Markdown syntax:
 
	[[ filename1 (filename2) ... ]]

Called as a pandoc filter:

     pandoc --filter ./insert.py	

Requires the Python pandocfilters package:

	 pip install pandocfilters
    