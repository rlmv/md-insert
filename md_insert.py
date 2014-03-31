#!/usr/bin/env python

import sys
import os

from pandocfilters import toJSONFilter, CodeBlock

def read_file(fname):

    try:
        with open(fname) as f:
            raw = f.read().strip()
    except IOError:
        msg = "Could not find file '%s' to insert" % fname
        raise IOError(msg)
        
    return raw
    

def insert(key, value, fmt, meta):

    # source directory for insert files
    if 'dir' in meta:
        idir = meta['dir']['c']
    else:
        idir = '.' 

    if key == 'CodeBlock':
        
        code = []

        # each key-value pair:
        for attr in value[0][2]: 
            if 'insert' == attr[0].lower():
                fname = os.path.join(idir, attr[1])
                code.append(read_file(fname))

        return CodeBlock(value[0], '\n\n'.join(code))
        
if __name__ == "__main__":
    toJSONFilter(insert)
    
