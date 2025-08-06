#!/usr/bin/env python

import sys
import os
sys.path.append('.')

# Import the write_cmn function directly
from PyVelest import main

# Create a simple test without the interactive prompt
def test_write_cmn():
    # Create a mock input dictionary with the parameters from par.dat
    input_dic = {
        'olat': '72',
        'olon': '-126.0',
        'icoordsystem': '0',
        'zshift': '0.0',
        'itrial': '0',
        'ztrial': '0.0',
        'ised': '0',
        'neqs': '50',
        'nshot': '0',
        'rotate': '0.0',
        'isingle': '0',
        'iresolcalc': '0',
        'dmax': '300.0',
        'itopo': '0',
        'zmin': '0.01',
        'veladj': '0.20',
        'zadj': '5.00',
        'lowveloclay': '0',
        'nsp': '1',
        'swtfac': '1.00',
        'vpvs': '1.73',
        'nmod': '1',
        'othet': '0.01',
        'xythet': '0.01',
        'zthet': '0.01',
        'vthet': '1.00',
        'stathet': '0.01',
        'nsinv': '1',
        'nshcor': '0',
        'nshfix': '0',
        'iuseelev': '1',
        'iusestacorr': '1',
        'iturbo': '1',
        'icnvout': '1',
        'istaout': '1',
        'ismpout': '0',
        'irayout': '0',
        'idrvout': '0',
        'ialeout': '0',
        'idspout': '0',
        'irflout': '0',
        'irfrout': '0',
        'iresout': '0',
        'delmin': '0.01',
        'ittmax': '3',
        'invertratio': '1',
        'Modelfile': './velinp/Kusur.mod',
        'Stationfile': './velinp/station.sta',
        'Seismofile': 'None',
        'RegionNamesfile': 'None',
        'Region_coorfile': 'None',
        'Topo_data_1file': 'None',
        'Topo_data_2file': 'None',
        'EQ_datafile': './velinp/data.cnv',
        'Shot_datafile': 'None',
        'Main_printoutfile': './velout/velest.out',
        'Single_ev_locfile': 'None',
        'Final_hypfile': './velout/final_loc.cnv',
        'Station_corrfile': './velout/stations_corr.sta',
        'Summary_cardsfile': 'None',
        'Raypointsfile': 'None',
        'Derivativesfile': 'None',
        'ALEsfile': 'None',
        'Dirichlet_sprfile': 'None',
        'Reflection_pntfile': 'None',
        'Refraction_pntfile': 'None',
        'Residualsfile': 'None'
    }
    
    # Create a mock main instance
    start = main.__new__(main)
    start.velmod_name = 'Kusur.mod'
    
    # Test the write_cmn function
    try:
        start.write_cmn(input_dic, 'test_velest.cmn', 'Kusur')
        print("write_cmn() completed successfully")
        
        # Check if test_velest.cmn was created
        if os.path.exists('test_velest.cmn'):
            print("test_velest.cmn file was created")
            
            # Read and check the iusestacorr value
            with open('test_velest.cmn', 'r') as f:
                lines = f.readlines()
            
            for i, line in enumerate(lines):
                if 'iusestacorr' in line:
                    print("Line {}: {}".format(i+1, line.strip()))
                if 'nsinv   nshcor   nshfix     iuseelev    iusestacorr' in line:
                    print("Line {}: {}".format(i+1, line.strip()))
                    if i+1 < len(lines):
                        print("Line {}: {}".format(i+2, lines[i+1].strip()))
        else:
            print("test_velest.cmn file was NOT created")
            
    except Exception as e:
        print("Error in write_cmn(): {}".format(e))
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_write_cmn() 