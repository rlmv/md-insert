

Pandoc Markdown extension for inserting file contents into code blocks. Reads the specified files and inserts them as separate codeblock. Works on the Pandoc AST. 
    
Markdown syntax:
 
	[[ filename1 (filename2) ... ]]

Call it as a pandoc filter:

     pandoc --filter ./insert.py	

Requires the Python pandocfilters package:

	 pip install pandocfilters
    