# -*- coding: utf-8 -*-
"""
SCIproject class to initialize and update input namelist files
"""
class SCIproject(object) :

    def __init__(self,name='scipuff',metFiles=None):
        self.name = name
        self.metFiles  = metFiles
        self.setMetString()
        self.initInp()  
        self.initMsc()
        self.initScn()
         
    def nmlFiles(self):
        return ('inp','msc','scn')
        
    def initInp(self):
        # Initialize the namelists for inp file
        self.inp = {}
        for nml in ['ctrl','time1','time2','flags','domain','options','matdef']:
            self.inp.update({nml:{}})
            if nml == 'ctrl':
                self.inp[nml].update({'restart':"F",'file_rst':"''",'path_rst':"''",'time_rst':0.0})
            if nml == 'time1':
                self.inp[nml].update({'year_start':2000,'month_start':1,'day_start':1,'tstart':0.0})
                self.inp[nml].update({'tzone':16.0,'local':"F"})
            if nml == 'time2':
                self.inp[nml].update({'year_end':2000,'month_end':1,'day_end':1,'tend':0.5})
                self.inp[nml].update({'tend_hr':0.5,'delt':60.,'dt_save':60.})
            if nml == 'flags':
                self.inp[nml].update({'title':"''",'create':'T','audit_class':'Unclassified'})
                self.inp[nml].update({'audit_analyst':"''",'dynamic':"F",'dense_gas':"F",'static':'T'})
                self.inp[nml].update({'hazarea':"Off",'run_mode':0})
                #self.inp[nml].update({'prjeffect':0})
            if nml == 'domain':
                self.inp[nml].update({'cmap':"'CARTESIAN'",'xmin':0.,'xmax':1.})
                self.inp[nml].update({'ymin':0.,'ymax':1.,'zmax':2500.})
                self.inp[nml].update({'vres':1.e36,'hres':1.e36,'utm_zone':12})
                self.inp[nml].update({'xref':0.,'yref':0.,'lon0':-112.994,'lat0':40.08413})
            if nml == 'options':
                self.inp[nml].update({'t_avg':1.e36,'cmin':1e-20,'lsplitz':"F",'delmin':1.e36})
                self.inp[nml].update({'wwtrop':0.01,'epstrop':4e-04,'sltrop':10.0,'uu_calm':0.25})
                self.inp[nml].update({'sl_calm':1000.0,'nzbl':11,'mgrd':2,'z_dosage':0.0e0})
                self.inp[nml].update({'smpfile':"''",'dt_smp':1.e36,'substrate_type':0})
            if nml == 'matdef':
                self.inp[nml].update({'class':"'gas'",'mname':"'tracer'",'units':"'kg'",'file_name':"''"})
                self.inp[nml].update({'file_path':"''",'group_deposition':"F",'group_dose':"F",'multi_comp':"F"})
                self.inp[nml].update({'conc_min':0.e0,'decay_amp':0.e0,'decay_min':0.e0})
                self.inp[nml].update({'density':1.2,'gas_deposition':0.e+0})
                self.inp[nml].update({'effectclass':0,'effectavail':0})
        return
                
    def initMsc(self):
        # Initialize the msc namelist for msc file and set metfile value
        self.msc = {}
        nml = 'met'
        self.msc.update({nml:{}})
        self.msc[nml].update({'met_type':"'obs'",'bl_type':"'oper'",'ensm_type':"'oper3.1'",'uu_ensm':0.0})
        self.msc[nml].update({'sl_ensm':100000.0,'zimin':50.0,'zimax':1000.000,'hconst':0.0})
        self.msc[nml].update({'hdiur':50.0,'h_cnp':-1.00,'alpha_cnp':0.000e+00,'zruf':1.000e-02})
        self.msc[nml].update({'sl_haz':100000.0,'albedo':0.3,'bowen':4.0,'cloud_cover':5.001e-02})
        self.msc[nml].update({'local_met':"F",'nearest_sfc':65535,'nearest_prf':65535,'lmc_ua':"F",'alpha_max':1.0})
        self.msc[nml].update({'alpha_min':1.0e-03,'max_iter_ac':200,'ac_eps':1.0e-02,'max_iter':100})
        self.msc[nml].update({'p_eps':1.0e-05,'nzb':23})
        zb  = '50.0,150.0,261.4300,385.4140,523.1650,675.9950,845.3170,1032.650,\n'
        zb += ' '*7 + '1239.620,1467.990,1719.600,1996.440,2300.620,2634.360,3000.000,3400.000,\n'
        zb += ' '*7 + '3892.620,4503.540,5266.700,6227.120,7444.830,9000.000,11000.00,177*0.0'
        self.msc[nml].update({'zb':zb})
        self.msc[nml].update({'file_ter':'','lout_mc':"F",'lout_met':"F",'tout_met':-1.e36})
        self.msc[nml].update({'lout_3d':"F",'lout_2d':"F",'pr_type':'NONE','tbin_met':60.00000e+00})
        self.msc[nml].update({'i_wet':2,'dt_swift':1.e36,'mctype':0,'lformat':"F"})
        return
        
    def setMetString(self):
        self.metString = None
        if self.metFiles is None:
          return
        if len(self.metFiles) > 0:
            metString = '   %1d '%len(self.metFiles)
            for metFile in self.metFiles:
                metString += '@%03d%s'%(len(metFile),metFile.strip())
            print 'metString = ',metString
            self.metString = metString
        return
        
    def initScn(self):
        # Initialize the namelist scn for scn file
        self.scn = {}
        nml = 'scn'
        self.scn.update({nml:{}})
        self.scn[nml].update({'relname':"''",'reldisplay':"'<empty>'",'trel':0.0})
        self.scn[nml].update({'xrel':2.137133,'yrel':-5.5464860e-02,'zrel':1.0})
        self.scn[nml].update({'cmass':33.0,'subgroup':1,'sigx':0.10,'sigy':0.10})
        self.scn[nml].update({'sigz':0.10,'wmom':0.0,'buoy':0.0})
        self.scn[nml].update({'lognorm_mmd':-1.e36,'lognorm_sigma':-1.e36})
        self.scn[nml].update({'slurry_fraction':-1.e36,'number_random':-65535})
        self.scn[nml].update({'random_spread':-1.e36,'random_seed':-65535})
        self.scn[nml].update({'horiz_uncertainty':-1.e36,'vert_uncertainty':-1.e36})
        self.scn[nml].update({'relstatus':1,'reltyp':"'C'",'relmat':"'tracer'",'tdur':0.25})
        return
        
    def nmlVal(self,nml,value=None):
        # Get the namelist variable value if input value is none, otherwise set
        # the value to the input argument
        nameList = None
        foundNml = False
        for nmlFile in self.nmlFiles():
            #print '\n',nmlFile
            for nameList in getattr(self,nmlFile).iterkeys():
                if nml in getattr(self,nmlFile)[nameList]:
                    foundNml = True
                    #print nmlFile,nameList,getattr(self,nmlFile)[nameList][nml]
                    if value is None:
                        value = getattr(self,nmlFile)[nameList][nml]
                    else:
                        nmlFileVal = getattr(self,nmlFile)
                        nmlFileVal[nameList][nml] = value
                        setattr(self,nmlFile,nmlFileVal)                    
                    break
            if foundNml:
                break                    
        return (nmlFile,nameList,value)
    
    def wrtNml(self,nml=None):
        # Write all nmlFiles if nml is none, otherwise write specific nmlFile
        # which contains nml
        if nml is None:
            nmlFiles = self.nmlFiles()
        else:
            nmlFiles = None
            foundNml = False
            for nmlFile in self.nmlFiles():
                for nameList in getattr(self,nmlFile).iterkeys():
                    if nml in getattr(self,nmlFile)[nameList]:
                        foundNml = True
                        nmlFiles = [nmlFile]
                        break
                if foundNml:
                    break
        
        # List of all namelist files
        print nmlFiles
        if nmlFiles is not None:
            for nmlFile in nmlFiles:
                fileNml = open(self.name + '.' + nmlFile,'w')
                for nameList in getattr(self,nmlFile).iterkeys():
                   # Get list of namelist in nmlFile
                   # print nameList
                   fileNml.write('&%s\n'%nameList)
                   for nmlVal in getattr(self,nmlFile)[nameList]:
                       # Get the value of namelist variable
                       #print nmlVal
                       fileNml.write('  %s = %s,\n'%(nmlVal,getattr(self,nmlFile)[nameList][nmlVal]))
                   fileNml.write('/\n')
                   if nameList == 'met' and self.metString is not None:
                       fileNml.write('%s\n'%self.metString)
                fileNml.close()
        return