#!/usr/bin/env python
# Add proper metadata to fuzzingbook notebook

"""
usage:

python add-metadata.py A.ipynb > A'.ipynb
"""

import io
import os
import sys

import nbformat

def normalize_notebooks(filename):
    with io.open(filename, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)

    # No cell toolbar for published notebooks
    if 'celltoolbar' in nb.metadata:
        del nb.metadata['celltoolbar']

    # Add bibliography
    if 'ipub' not in nb.metadata:
        nb.metadata['ipub'] = {}
    if 'bibliography' not in nb.metadata['ipub']:
        nb.metadata['ipub']['bibliography'] = 'fuzzingbook.bib'

    # Add table of contents
    nb.metadata['toc'] = {
     "base_numbering": 1,
     "nav_menu": {},
     "number_sections": True,
     "sideBar": True,
     "skip_h1_title": True,
     "title_cell": "",
     "title_sidebar": "Contents",
     "toc_cell": False,
     "toc_position": {},
     "toc_section_display": True,
     "toc_window_display": True
    }
    
    # Write out
    # Include a newline at the end, as Jupyterlab does
    notebook_content = nbformat.writes(nb) + '\n'
    sys.stdout.buffer.write(notebook_content.encode('utf-8'))

    
if __name__ == '__main__':
    notebooks = sys.argv[1:]
    if not notebooks:
        print(__doc__, file=sys.stderr)
        sys.exit(1)
    
    for notebook in notebooks:
        normalize_notebooks(notebook)