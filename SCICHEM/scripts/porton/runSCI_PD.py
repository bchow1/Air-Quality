# -*- coding: utf-8 -*-
"""
Created on Fri May 05 10:43:45 2017

@author: Biswanath
"""

import os
import sys
import pandas as pd

sys.path.append("E:\\Air-Quality\\SCICHEM\\scripts")
import SciProject

def rdSamLocs(samLocFile):
    # Could not read with header=3 as it is taking 3rd non comment line
    samLocs = pd.read_table(samLocFile,header=None,skiprows=3,names=['x','y'])
    xMin,xMax =  samLocs['x'].min(), samLocs['x'].max()
    yMin,yMax =  samLocs['y'].min(), samLocs['y'].max()
    samLocs.plot(x='x',y='y',style='*',xlim=[xMin,xMax],ylim=[yMin,yMax])
    return (xMin,xMax,yMin,yMax)
        
# Main Program
if __name__ == '__main__':
  
  prjName  = 'P1'
  metFiles = ['P1.sfc']
  samLocFile  = 'P1_dos_samplers.txt'
  (xMin,xMax,yMin,yMax)  = rdSamLocs(samLocFile)
  
  mySCIprj = SciProject.SCIproject(prjName,metFiles=metFiles)
  mySCIprj.inp['domain']['xmin'] = xMin
  mySCIprj.inp['domain']['xmax'] = xMax
  mySCIprj.inp['domain']['ymin'] = yMin
  mySCIprj.inp['domain']['ymax'] = xMax
  mySCIprj.wrtNml()
  
  '''
  print 'Project Name = ',mySCIprj.name
  print 'Material density = ',mySCIprj.inp['matdef']['density']
  #print mySCIprj.wrtNml('random_seed')
  print mySCIprj.nmlVal('density',value=1.3)
  #mySCIprj.wrtNml('dens
  '''
 