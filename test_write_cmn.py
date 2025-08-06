#!/usr/bin/env python

import sys
import os
sys.path.append('.')

from PyVelest import main

# Create a main instance
start = main()

# Set the project name to avoid interactive prompt
start.project_nm = 'Kusur'

# Read parameters
start.read_par()

print("Parameters read successfully:")
print("iusestacorr: {}".format(start.input_dic.get('iusestacorr', 'NOT FOUND')))
print("nsinv: {}".format(start.input_dic.get('nsinv', 'NOT FOUND')))

# Try to write the control file
try:
    start.write_par()
    print("write_par() completed successfully")
    
    # Check if velest.cmn was created
    if os.path.exists('velest.cmn'):
        print("velest.cmn file was created")
        
        # Read and check the iusestacorr value
        with open('velest.cmn', 'r') as f:
            lines = f.readlines()
        
        for i, line in enumerate(lines):
            if 'iusestacorr' in line:
                print("Line {}: {}".format(i+1, line.strip()))
            if 'nsinv   nshcor   nshfix     iuseelev    iusestacorr' in line:
                print("Line {}: {}".format(i+1, line.strip()))
                if i+1 < len(lines):
                    print("Line {}: {}".format(i+2, lines[i+1].strip()))
    else:
        print("velest.cmn file was NOT created")
        
except Exception as e:
    print("Error in write_par(): {}".format(e))
    import traceback
    traceback.print_exc() 