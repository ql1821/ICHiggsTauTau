from WMCore.Configuration import Configuration
config=Configuration()
config.section_('General')
config.General.transferOutputs = True
config.General.workArea='Nov19_MC_74X'
config.section_('JobType')
config.JobType.psetName = '/afs/cern.ch/work/a/adewit/private/CMSSW_7_4_15_patch1/src/UserCode/ICHiggsTauTau/test/higgstautau_cfg_74X_Nov15.py'
config.JobType.pluginName = 'Analysis'
config.JobType.outputFiles = ['EventTree.root']
#config.JobType.inputFiles = ['Summer15_V5_MC.db']
config.JobType.pyCfgParams = ['release=7412MINIAOD','isData=0','doHT=0','globalTag=74X_mcRun2_asymptotic_v2']
config.section_('Data')
#config.Data.inputDataset = 'DUMMY'
config.Data.unitsPerJob = 1
config.Data.splitting = 'FileBased'
config.Data.publication = False
config.Data.outLFNDirBase='/store/user/adewit/Nov19_MC_74X/'
config.section_('User')
config.section_('Site')
config.Site.whitelist = ['T2_UK_London_IC', 'T2_CH_CERN', 'T2_FR_GRIF_LLR', 'T2_UK_SGrid_Bristol', 'T3_US_FNALLPC', 'T2_DE_DESY', 'T2_IT_Bari', 'T2_BE_IIHE', 'T2_US_UCSD', 'T2_US_MIT', 'T2_IT_Pisa', 'T2_US_Wisconsin', 'T2_US_Florida', 'T2_IT_Rome', 'T2_RU_JINR','T2_FR_GRIF_IRFU','T2_ES_IFCA','T2_DE_RWTH']
config.Site.storageSite = 'T2_UK_London_IC'

if __name__ == '__main__':

    from CRABAPI.RawCommand import crabCommand
    from httplib import HTTPException

    # We want to put all the CRAB project directories from the tasks we submit here into one common directory.
    # That's why we need to set this parameter (here or above in the configuration file, it does not matter, we will not overwrite it).

    def submit(config):
        try:
            crabCommand('submit', config = config)
        except HTTPException, hte:
            print hte.headers

    #############################################################################################
    ## From now on that's what users should modify: this is the a-la-CRAB2 configuration part. ##
    #############################################################################################

    tasks=list()

#Signal samples
    tasks.append(('GluGluHToTauTau_M-120','/GluGluHToTauTau_M120_13TeV_powheg_pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
    tasks.append(('GluGluHToTauTau_M-125','/GluGluHToTauTau_M125_13TeV_powheg_pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
    tasks.append(('GluGluHToTauTau_M-130','/GluGluHToTauTau_M130_13TeV_powheg_pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
    tasks.append(('VBFHToTauTau_M-120','/VBFHToTauTau_M120_13TeV_powheg_pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
    tasks.append(('VBFHToTauTau_M-125','/VBFHToTauTau_M125_13TeV_powheg_pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
    tasks.append(('VBFHToTauTau_M-130','/VBFHToTauTau_M130_13TeV_powheg_pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
    tasks.append(('SUSYGluGluToHToTauTau_M-80','/SUSYGluGluToHToTauTau_M-80_TuneCUETP8M1_13TeV-pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
    tasks.append(('SUSYGluGluToHToTauTau_M-90','/SUSYGluGluToHToTauTau_M-90_TuneCUETP8M1_13TeV-pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
    tasks.append(('SUSYGluGluToHToTauTau_M-100','/SUSYGluGluToHToTauTau_M-100_TuneCUETP8M1_13TeV-pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
    tasks.append(('SUSYGluGluToHToTauTau_M-110','/SUSYGluGluToHToTauTau_M-110_TuneCUETP8M1_13TeV-pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
    tasks.append(('SUSYGluGluToHToTauTau_M-120','/SUSYGluGluToHToTauTau_M-120_TuneCUETP8M1_13TeV-pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
    tasks.append(('SUSYGluGluToHToTauTau_M-130','/SUSYGluGluToHToTauTau_M-130_TuneCUETP8M1_13TeV-pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
    tasks.append(('SUSYGluGluToHToTauTau_M-140','/SUSYGluGluToHToTauTau_M-140_TuneCUETP8M1_13TeV-pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
    tasks.append(('SUSYGluGluToHToTauTau_M-500','/SUSYGluGluToHToTauTau_M-500_TuneCUETP8M1_13TeV-pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
    tasks.append(('SUSYGluGluToHToTauTau_M-180','/SUSYGluGluToHToTauTau_M-180_TuneCUETP8M1_13TeV-pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
    tasks.append(('SUSYGluGluToHToTauTau_M-200','/SUSYGluGluToHToTauTau_M-200_TuneCUETP8M1_13TeV-pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
    tasks.append(('SUSYGluGluToHToTauTau_M-250','/SUSYGluGluToHToTauTau_M-250_TuneCUETP8M1_13TeV-pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
    tasks.append(('SUSYGluGluToHToTauTau_M-300','/SUSYGluGluToHToTauTau_M-300_TuneCUETP8M1_13TeV-pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
    tasks.append(('SUSYGluGluToHToTauTau_M-350','/SUSYGluGluToHToTauTau_M-350_TuneCUETP8M1_13TeV-pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
    tasks.append(('SUSYGluGluToHToTauTau_M-400','/SUSYGluGluToHToTauTau_M-400_TuneCUETP8M1_13TeV-pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
    tasks.append(('SUSYGluGluToHToTauTau_M-450','/SUSYGluGluToHToTauTau_M-450_TuneCUETP8M1_13TeV-pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
    tasks.append(('SUSYGluGluToHToTauTau_M-600','/SUSYGluGluToHToTauTau_M-600_TuneCUETP8M1_13TeV-pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
    tasks.append(('SUSYGluGluToHToTauTau_M-800','/SUSYGluGluToHToTauTau_M-800_TuneCUETP8M1_13TeV-pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
    tasks.append(('SUSYGluGluToHToTauTau_M-700','/SUSYGluGluToHToTauTau_M-700_TuneCUETP8M1_13TeV-pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v4/MINIAODSIM'))
    tasks.append(('SUSYGluGluToHToTauTau_M-900','/SUSYGluGluToHToTauTau_M-900_TuneCUETP8M1_13TeV-pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
    tasks.append(('SUSYGluGluToHToTauTau_M-1200','/SUSYGluGluToHToTauTau_M-1200_TuneCUETP8M1_13TeV-pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
    tasks.append(('SUSYGluGluToHToTauTau_M-1400','/SUSYGluGluToHToTauTau_M-1400_TuneCUETP8M1_13TeV-pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
    tasks.append(('SUSYGluGluToHToTauTau_M-1600','/SUSYGluGluToHToTauTau_M-1600_TuneCUETP8M1_13TeV-pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
    tasks.append(('SUSYGluGluToHToTauTau_M-1800','/SUSYGluGluToHToTauTau_M-1800_TuneCUETP8M1_13TeV-pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
    tasks.append(('SUSYGluGluToHToTauTau_M-2000','/SUSYGluGluToHToTauTau_M-2000_TuneCUETP8M1_13TeV-pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
    tasks.append(('SUSYGluGluToHToTauTau_M-2300','/SUSYGluGluToHToTauTau_M-2300_TuneCUETP8M1_13TeV-pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
    tasks.append(('SUSYGluGluToHToTauTau_M-2900','/SUSYGluGluToHToTauTau_M-2900_TuneCUETP8M1_13TeV-pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
    tasks.append(('SUSYGluGluToHToTauTau_M-1000','/SUSYGluGluToHToTauTau_M-1000_TuneCUETP8M1_13TeV-pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
    tasks.append(('SUSYGluGluToHToTauTau_M-160','/SUSYGluGluToHToTauTau_M-160_TuneCUETP8M1_13TeV-pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
    tasks.append(('SUSYGluGluToHToTauTau_M-1500','/SUSYGluGluToHToTauTau_M-1500_TuneCUETP8M1_13TeV-pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
    tasks.append(('SUSYGluGluToHToTauTau_M-2600','/SUSYGluGluToHToTauTau_M-2600_TuneCUETP8M1_13TeV-pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM')) 
    tasks.append(('SUSYGluGluToHToTauTau_M-3200','/SUSYGluGluToHToTauTau_M-3200_TuneCUETP8M1_13TeV-pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM')) 
    tasks.append(('SUSYGluGluToBBHToTauTau_M-80','/SUSYGluGluToBBHToTauTau_M-80_TuneCUETP8M1_13TeV-pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
    tasks.append(('SUSYGluGluToBBHToTauTau_M-90','/SUSYGluGluToBBHToTauTau_M-90_TuneCUETP8M1_13TeV-pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
    tasks.append(('SUSYGluGluToBBHToTauTau_M-100','/SUSYGluGluToBBHToTauTau_M-100_TuneCUETP8M1_13TeV-pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
    tasks.append(('SUSYGluGluToBBHToTauTau_M-110','/SUSYGluGluToBBHToTauTau_M-110_TuneCUETP8M1_13TeV-pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
    tasks.append(('SUSYGluGluToBBHToTauTau_M-120','/SUSYGluGluToBBHToTauTau_M-120_TuneCUETP8M1_13TeV-pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
    tasks.append(('SUSYGluGluToBBHToTauTau_M-130','/SUSYGluGluToBBHToTauTau_M-130_TuneCUETP8M1_13TeV-pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
    tasks.append(('SUSYGluGluToBBHToTauTau_M-140','/SUSYGluGluToBBHToTauTau_M-140_TuneCUETP8M1_13TeV-pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
    tasks.append(('SUSYGluGluToBBHToTauTau_M-500','/SUSYGluGluToBBHToTauTau_M-500_TuneCUETP8M1_13TeV-pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
    tasks.append(('SUSYGluGluToBBHToTauTau_M-1000','/SUSYGluGluToBBHToTauTau_M-1000_TuneCUETP8M1_13TeV-pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
    tasks.append(('SUSYGluGluToBBHToTauTau_M-180','/SUSYGluGluToBBHToTauTau_M-180_TuneCUETP8M1_13TeV-pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
    tasks.append(('SUSYGluGluToBBHToTauTau_M-200','/SUSYGluGluToBBHToTauTau_M-200_TuneCUETP8M1_13TeV-pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
    tasks.append(('SUSYGluGluToBBHToTauTau_M-250','/SUSYGluGluToBBHToTauTau_M-250_TuneCUETP8M1_13TeV-pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
    tasks.append(('SUSYGluGluToBBHToTauTau_M-300','/SUSYGluGluToBBHToTauTau_M-300_TuneCUETP8M1_13TeV-pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
    tasks.append(('SUSYGluGluToBBHToTauTau_M-350','/SUSYGluGluToBBHToTauTau_M-350_TuneCUETP8M1_13TeV-pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
    tasks.append(('SUSYGluGluToBBHToTauTau_M-400','/SUSYGluGluToBBHToTauTau_M-400_TuneCUETP8M1_13TeV-pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
    tasks.append(('SUSYGluGluToBBHToTauTau_M-450','/SUSYGluGluToBBHToTauTau_M-450_TuneCUETP8M1_13TeV-pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
    tasks.append(('SUSYGluGluToBBHToTauTau_M-600','/SUSYGluGluToBBHToTauTau_M-600_TuneCUETP8M1_13TeV-pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
    tasks.append(('SUSYGluGluToBBHToTauTau_M-700','/SUSYGluGluToBBHToTauTau_M-700_TuneCUETP8M1_13TeV-pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
    tasks.append(('SUSYGluGluToBBHToTauTau_M-800','/SUSYGluGluToBBHToTauTau_M-800_TuneCUETP8M1_13TeV-pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
    tasks.append(('SUSYGluGluToBBHToTauTau_M-900','/SUSYGluGluToBBHToTauTau_M-900_TuneCUETP8M1_13TeV-pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
    tasks.append(('SUSYGluGluToBBHToTauTau_M-1200','/SUSYGluGluToBBHToTauTau_M-1200_TuneCUETP8M1_13TeV-pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
    tasks.append(('SUSYGluGluToBBHToTauTau_M-1400','/SUSYGluGluToBBHToTauTau_M-1400_TuneCUETP8M1_13TeV-pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
    tasks.append(('SUSYGluGluToBBHToTauTau_M-1500','/SUSYGluGluToBBHToTauTau_M-1500_TuneCUETP8M1_13TeV-pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
    tasks.append(('SUSYGluGluToBBHToTauTau_M-1600','/SUSYGluGluToBBHToTauTau_M-1600_TuneCUETP8M1_13TeV-pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
    tasks.append(('SUSYGluGluToBBHToTauTau_M-1800','/SUSYGluGluToBBHToTauTau_M-1800_TuneCUETP8M1_13TeV-pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
    tasks.append(('SUSYGluGluToBBHToTauTau_M-2000','/SUSYGluGluToBBHToTauTau_M-2000_TuneCUETP8M1_13TeV-pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
    tasks.append(('SUSYGluGluToBBHToTauTau_M-2300','/SUSYGluGluToBBHToTauTau_M-2300_TuneCUETP8M1_13TeV-pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
    tasks.append(('SUSYGluGluToBBHToTauTau_M-2600','/SUSYGluGluToBBHToTauTau_M-2600_TuneCUETP8M1_13TeV-pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
    tasks.append(('SUSYGluGluToBBHToTauTau_M-2900','/SUSYGluGluToBBHToTauTau_M-2900_TuneCUETP8M1_13TeV-pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
    tasks.append(('SUSYGluGluToBBHToTauTau_M-3200','/SUSYGluGluToBBHToTauTau_M-3200_TuneCUETP8M1_13TeV-pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
    tasks.append(('SUSYGluGluToBBHToTauTau_M-160','/SUSYGluGluToBBHToTauTau_M-160_TuneCUETP8M1_13TeV-pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
#    tasks.append(('WJetsToLNu','/WJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
#    tasks.append(('DYJetsToLL','/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
#    tasks.append(('DYJetsToLL10-50','/DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM'))
#    tasks.append(('TTJets','/TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v3/MINIAODSIM'))
    tasks.append(('ZZTo2L2Nu','/ZZTo2L2Nu_13TeV_powheg_pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v2/MINIAODSIM'))
    tasks.append(('WZTo3LNu','/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
    tasks.append(('WZTo1L3Nu','/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
    tasks.append(('T-t','/ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
    tasks.append(('Tbar-t','/ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
    tasks.append(('WZTo1L1Nu2Q','/WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
    tasks.append(('WZTo2L2Q','/WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
    tasks.append(('ZZTo2L2Q','/ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
    tasks.append(('VVTo2L2Nu','/VVTo2L2Nu_13TeV_amcatnloFXFX_madspin_pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
    tasks.append(('WZJetsTo3LNu','/WZJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
    tasks.append(('WWTo1L1Nu2Q','/WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
    tasks.append(('ZZTo4L','/ZZTo4L_13TeV-amcatnloFXFX-pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
   # tasks.append(('WWinclusive','/WW_TuneCUETP8M1_13TeV-pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
   # tasks.append(('WZinclusive','/WZ_TuneCUETP8M1_13TeV-pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
   # tasks.append(('ZZinclusive','/ZZ_TuneCUETP8M1_13TeV-pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
#    tasks.append(('QCDFlat','/QCD_Pt-15to7000_TuneCUETP8M1_Flat_13TeV_pythia8/RunIISpring15DR74-Asympt35nsRaw_MCRUN2_74_V9-v3/MINIAODSIM'))
#    tasks.append(('QCDMuEnr','/QCD_Pt-20toInf_MuEnrichedPt15_TuneCUETP8M1_13TeV_pythia8/RunIISpring15DR74-Asympt35ns_MCRUN2_74_V9-v1/MINIAODSIM'))
    tasks.append(('T-tW','/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v2/MINIAODSIM'))
    tasks.append(('Tbar-tW','/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
   # tasks.append(('TT','/TT_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
    tasks.append(('TT-ext','/TT_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2_ext3-v1/MINIAODSIM'))
    tasks.append(('WWTo2L2Nu', '/WWTo2L2Nu_13TeV-powheg/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
    tasks.append(('WWToLNuQQ', '/WWToLNuQQ_13TeV-powheg/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
#    tasks.append(('ZZTo4L','/ZZTo4L_13TeV_powheg_pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v2/MINIAODSIM'))
    tasks.append(('QCD_Ht100to200','/QCD_HT100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
    tasks.append(('QCD_Ht200to300','/QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
    tasks.append(('QCD_Ht300to500','/QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
    tasks.append(('QCD_Ht500to700','/QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
    tasks.append(('QCD_Ht700to1000','/QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
    tasks.append(('QCD_Ht1000to1500','/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
    tasks.append(('QCD_Ht1500to2000','/QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
    tasks.append(('QCD_Ht2000toInf','/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
    tasks.append(('GluGluToRadionToHHTo2B2Tau_M-250','/GluGluToRadionToHHTo2B2Tau_M-250_narrow_13TeV-madgraph/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
    tasks.append(('GluGluToRadionToHHTo2B2Tau_M-260','/GluGluToRadionToHHTo2B2Tau_M-260_narrow_13TeV-madgraph/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
    tasks.append(('GluGluToRadionToHHTo2B2Tau_M-270','/GluGluToRadionToHHTo2B2Tau_M-270_narrow_13TeV-madgraph/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
    tasks.append(('GluGluToRadionToHHTo2B2Tau_M-280','/GluGluToRadionToHHTo2B2Tau_M-280_narrow_13TeV-madgraph/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
    tasks.append(('GluGluToRadionToHHTo2B2Tau_M-300','/GluGluToRadionToHHTo2B2Tau_M-300_narrow_13TeV-madgraph/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
    tasks.append(('GluGluToRadionToHHTo2B2Tau_M-320','/GluGluToRadionToHHTo2B2Tau_M-320_narrow_13TeV-madgraph/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
    tasks.append(('GluGluToRadionToHHTo2B2Tau_M-340','/GluGluToRadionToHHTo2B2Tau_M-340_narrow_13TeV-madgraph/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v2/MINIAODSIM'))
    tasks.append(('GluGluToRadionToHHTo2B2Tau_M-350','/GluGluToRadionToHHTo2B2Tau_M-350_narrow_13TeV-madgraph/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v2/MINIAODSIM'))
    tasks.append(('GluGluToRadionToHHTo2B2Tau_M-400','/GluGluToRadionToHHTo2B2Tau_M-400_narrow_13TeV-madgraph/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
    tasks.append(('GluGluToRadionToHHTo2B2Tau_M-450','/GluGluToRadionToHHTo2B2Tau_M-450_narrow_13TeV-madgraph/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v2/MINIAODSIM'))
    tasks.append(('GluGluToRadionToHHTo2B2Tau_M-500','/GluGluToRadionToHHTo2B2Tau_M-500_narrow_13TeV-madgraph/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
    tasks.append(('GluGluToRadionToHHTo2B2Tau_M-550','/GluGluToRadionToHHTo2B2Tau_M-550_narrow_13TeV-madgraph/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
    tasks.append(('GluGluToRadionToHHTo2B2Tau_M-600','/GluGluToRadionToHHTo2B2Tau_M-600_narrow_13TeV-madgraph/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
    tasks.append(('GluGluToRadionToHHTo2B2Tau_M-650','/GluGluToRadionToHHTo2B2Tau_M-650_narrow_13TeV-madgraph/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v2/MINIAODSIM'))
    tasks.append(('GluGluToRadionToHHTo2B2Tau_M-700','/GluGluToRadionToHHTo2B2Tau_M-700_narrow_13TeV-madgraph/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
    tasks.append(('GluGluToRadionToHHTo2B2Tau_M-800','/GluGluToRadionToHHTo2B2Tau_M-800_narrow_13TeV-madgraph/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))
    tasks.append(('GluGluToRadionToHHTo2B2Tau_M-900','/GluGluToRadionToHHTo2B2Tau_M-900_narrow_13TeV-madgraph/RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2-v1/MINIAODSIM'))


#
    for task in tasks:
        print task[0]
        config.General.requestName = task[0]
        config.Data.inputDataset = task[1]
        submit(config)



