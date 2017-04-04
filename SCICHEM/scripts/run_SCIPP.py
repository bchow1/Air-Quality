import os
import sys
import shutil
import subprocess
import fileinput
import numpy as np
import matplotlib.pyplot as plt

def mainProg():
  # Set SCIpp path
  baseDir = "E:\\APIOilSpill\\SCICHEM_3.1_161013\\export"

  binDir      = baseDir + "\\Win64"
  #iniFile     = baseDir  + "\\scipuff.ini"
  iniFile     =  "..\\scipuff.ini"
  env         = os.environ.copy()
  env["PATH"] = "%s;%s" % (binDir,env["PATH"])
  scipp       = os.path.join(binDir,'scipp.exe')
  print 'Using scipp from ',binDir
  print scipp
 
  for prjName in ['Scen01']:
    runSCIPP(env,scipp,prjName,iniFile)
    
def runSCIPP(env,scipp,prjName,iniFile):
  
  global timeList

  #-- Run scipp fo project
  print 'Running scipp on project ',prjName

  # Initial call to get the list of available times
  outFile = prjName + '_scipp' + '.out'    
  crtOut(scipp,env,iniFile,prjName,'0',outFile,rmOut=False)
 
  timeLStart = 9999
  timeList   = []
  for line in fileinput.input('scipp.output'):
    if 'Available Field Times' in line:
      timeLStart = fileinput.lineno() + 1
      print timeLStart
    if fileinput.lineno() > timeLStart:
      if len(line.strip()) == 0:
        print 'Break'
        break      
      timeList.append(line.split('(')[1].split(')')[0].strip())
  fileinput.close()
  os.remove('scipp.output')    
  print timeList

  # Main loop for all times and components
  for tNo,tString in enumerate(timeList):
    for comp in ['AR1','AR2','AR9']:
      for ht in [0.,10.,100.]:
          outFile = prjName + '_%s_%d_%dm.out'%(comp,tNo,ht)
          crtOut(scipp,env,iniFile,prjName,tString,outFile,comp=comp,ht=ht)
          conc = np.loadtxt(outFile,skiprows=14,usecols=(0,1,2,3))
          print 'Time,comp,lon,lat,ht,meanC,maxC ='
          print tString,comp,conc[0,0],conc[0,1],ht,conc[0,2],conc[:,2].max()
          fig = plt.figure()
          plt.clf()
          fig.hold(True)
          plt.plot(conc[:,2])
          plt.xlabel('Sampler')
          plt.ylabel('Conc(ppm)')
          plt.title('Concentration of %s at %s and height %dm '%(comp,tString,ht))
          plt.hold(False)
          plt.savefig(outFile.replace('.out','.png'))
          #plt.show()
          
  return
  

def crtOut(scipp,env,iniFile,prjName,tString,outFile,rmOut=True,comp='AR1',ht=10.):
        
  
    inSCIpp = open('scipp.input','w') 
    inSCIpp.write('%s\n'%iniFile)
    inSCIpp.write('KE\n%s\n'%prjName)
    
    
    # Surface Concentration
    inSCIpp.write('Concentration \nComponents \n%s \n'%comp)
    inSCIpp.write('Horizontal \nMean \n')
    inSCIpp.write('%s\n'%tString)
    inSCIpp.write(' \n \n')   # Slice lower left and upper right points.
    inSCIpp.write(' %d\n'%ht) # Slice height 
    inSCIpp.write('CG \n-1 \ngrid400.sam\n')
    inSCIpp.write('%s\n'%outFile)    
    inSCIpp.close()
    
    if os.path.exists(outFile):
      os.remove(outFile)
    
    scipp_inp = open('scipp.input','r')
    scipp_out = open('scipp.output','w')
    scipp_err = open('scipp.error','w')
    h = subprocess.Popen(scipp, env=env, bufsize=0, shell=False,stdin=scipp_inp, stdout=scipp_out,stderr=scipp_err)
    h.communicate()
    scipp_inp.close()
    scipp_out.close()
    scipp_err.close()
        
    # Cleanup
    os.remove('scipp.input')
    if rmOut:
      os.remove('scipp.output')
    os.remove('scipp.error')
           
if __name__ == '__main__':
    mainProg() 
