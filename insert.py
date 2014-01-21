#!/usr/bin/env python

import sys
import os

from pandocfilters import toJSONFilter, CodeBlock, stringify

""" 
Pandoc markdown extension for inserting file contents
into code blocks. Reads the specified files and inserts
them as separate codeblock. Works on the pandoc AST. 
    
Markdown syntax:

[[ filename1 (filename2) ... ]]

Call it as a pandoc filter:

pandoc --filter ./insert.py
    
"""

def build_codeblock(fname):
    """ Construct and return pandoc AST CodeBlock from the 
    specified file. Raise an IOError if the file does not exist.

    """

    try:
        with open(fname) as f:
            raw = f.read().strip()
            code = CodeBlock(['', [], []], raw)
    except IOError:
        msg = "Could not find file '%s' to insert" % fname
        raise IOError(msg)

    return code

    
def insert(key, value, fmt, meta):
    """ Parse Paragraph blocks, checking for the [[ ]] insert
    syntax.

    """

    # source directory for insert files
    if 'dir' in meta:
        idir = meta['dir']['c']
    else:
        idir = '.' 

    if key == 'Para':

        s = stringify(value)

        first = value[0]['c']
        last = value[-1]['c']

        if first.startswith('[[') and last.endswith(']]'):
            
            # remove insert syntax for the cases where
            # there is no space between brackets, eg.
            # [[filename or filename]]
            value[0]['c'] = first[2:]
            value[-1]['c'] = last[:-2]


            contents = []
            for node in value:
                if node['t'] == 'Str' and node['c']:
                    fname = os.path.join(idir, node['c'])
                    code = build_codeblock(fname)
                    contents.append(code)
                        
            return contents


if __name__ == "__main__":
    toJSONFilter(insert)
    
