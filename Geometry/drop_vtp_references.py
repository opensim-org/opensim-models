#!/usr/bin/env python3

# replaces any references to vtp files in the opensim-models
# repository with references to obj files (e.g. <mesh_file>mesh.vtp</mesh_file> --> <mesh_file>mesh.obj</mesh_file>
# must be ran from the root of opensim-models

import glob
import re

patterns = [re.compile(s) for s in [
    r'(?<=<mesh_file>)(.+?)\.vtp',
    r'(?<=<geometry_file>)(.+?)\.vtp',
    r'(?<=addDisplayGeometry\(")(.+?)\.vtp',
]]
glob_patterns = ['**/*.osim', '**/*.cpp']

for p in glob_patterns:
    for f in glob.glob(p, recursive=True):
        with open(f, 'r') as fd:
            content = fd.read()

        new_content = content
        for pattern in patterns:
            new_content = re.sub(pattern, r'\1.obj', new_content)
    
        if new_content != content:
            with open(f, 'w') as fd:
                fd.write(new_content)

