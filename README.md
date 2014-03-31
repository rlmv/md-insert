
Pandoc Markdown extension for inserting file contents into code blocks. Inserts the specified files into the codeblock. Built to keep external source code synced with embedded versions in lecture notes.

Requires the Python `pandocfilters` package:

    pip install pandocfilters

Install the filter script onto the system:
   
    python setup.py install
    
Markdown syntax extension:
  
    ``` { insert=FILENAME }
    ```	

Pandoc supports code highlighting with classes:
      
    ``` { insert=FILENAME .javascript }
    ```

Called as a Pandoc filter:

    pandoc --filter md_insert.py	

To include source files from a directory other than the current directory we use a Pandoc metadata argument:
   
    pandoc --filter md_insert.py --metadata dir=target_dir
    
