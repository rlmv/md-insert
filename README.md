

Pandoc Markdown extension for inserting file contents into code blocks. Inserts the specified files as codeblocks, one codeblock per file. Built to keep external source code synced with embedded versions in lecture notes.

Install the filter script onto the system:
   
    python setup.py install
    
Markdown syntax extension:
  
    [[ filename1 (filename2) ... ]]

Called as a Pandoc filter:

    pandoc --filter md_insert.py	

To include source files from a directory other than the current directory we use a Pandoc metadata argument:
   
    pandoc --filter md_insert.py --metadata dir=target_dir

We also support syntax highlighting through another metadata flag:
   
    pandoc --filter md_insert.py --metadata lang=javascript

Requires the Python `pandocfilters` package:

    pip install pandocfilters
    