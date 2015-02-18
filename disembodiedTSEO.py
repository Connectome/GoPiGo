# GoPiGo Connectome
# Written by Timothy Busbice, Gabriel Garrett, Geoffrey Churchill (c) 2014, in Python 2.7
# The GoPiGo Connectome uses a Postsynaptic dictionary based on the C Elegans Connectome Model
# This application can be ran on the Raspberry Pi GoPiGo robot with a Sonar that represents Nose Touch when activated
# To run standalone without a GoPiGo robot, simply comment out the sections with Start and End comments 

#TIME STATE EXPERIMENTAL OPTIMIZATION
## Start Comment
#from gopigo import *
## End Comment
import time
import copy
# The postsynaptic dictionary contains the accumulated weighted values as the
# connectome is executed
postsynaptic = {}

global thisState
global nextState
thisState = 0 
nextState = 1

# The Threshold is the maximum sccumulated value that must be exceeded before
# the Neurite will fire
threshold = 30

# Accumulators are used to decide the value to send to the Left and Right motors
# of the GoPiGo robot
accumleft = 0
accumright = 0

# Used to remove from Axon firing since muscles cannot fire.
muscles = ['MVU', 'MVL', 'MDL', 'MVR', 'MDR']

# Used to accumulate muscle weighted values in body muscles 07-23 = worm locomotion
musDleft = ['MDL07', 'MDL08', 'MDL09', 'MDL10', 'MDL11', 'MDL12', 'MDL13', 'MDL14', 'MDL15', 'MDL16', 'MDL17', 'MDL18', 'MDL19', 'MDL20', 'MDL21', 'MDL22', 'MDL23']
musVleft = ['MVL07', 'MVL08', 'MVL09', 'MVL10', 'MVL11', 'MVL12', 'MVL13', 'MVL14', 'MVL15', 'MVL16', 'MVL17', 'MVL18', 'MVL19', 'MVL20', 'MVL21', 'MVL22', 'MVL23']
musDright = ['MDR07', 'MDR08', 'MDR09', 'MDR10', 'MDR11', 'MDR12', 'MDR13', 'MDR14', 'MDR15', 'MDR16', 'MDR17', 'MDR18', 'MDR19', 'MDR20', 'MDL21', 'MDR22', 'MDR23']
musVright = ['MVR07', 'MVR08', 'MVR09', 'MVR10', 'MVR11', 'MVR12', 'MVR13', 'MVR14', 'MVR15', 'MVR16', 'MVR17', 'MVR18', 'MVR19', 'MVR20', 'MVL21', 'MVR22', 'MVR23']

# This is the full C Elegans Connectome as expresed in the form of the Presynatptic
# neurite and the postsynaptic neurites
# postsynaptic['ADAR'][nextState] = (2 + postsynaptic['ADAR'][thisState])
# arr=postsynaptic['AIBR'] potential optimization

def ADAL():
        postsynaptic['ADAR'][nextState] += 2
        postsynaptic['ADFL'][nextState] += 1
        postsynaptic['AIBL'][nextState] += 1
        postsynaptic['AIBR'][nextState] += 2
        postsynaptic['ASHL'][nextState] += 1
        postsynaptic['AVAR'][nextState] += 2
        postsynaptic['AVBL'][nextState] += 4
        postsynaptic['AVBR'][nextState] += 7
        postsynaptic['AVDL'][nextState] += 1
        postsynaptic['AVDR'][nextState] += 2
        postsynaptic['AVEL'][nextState] += 1
        postsynaptic['AVJR'][nextState] += 5
        postsynaptic['FLPR'][nextState] += 1
        postsynaptic['PVQL'][nextState] += 1
        postsynaptic['RICL'][nextState] += 1
        postsynaptic['RICR'][nextState] += 1
        postsynaptic['RIML'][nextState] += 3
        postsynaptic['RIPL'][nextState] += 1
        postsynaptic['SMDVR'][nextState] += 2

def ADAR():
        postsynaptic['ADAL'][nextState] += 1
        postsynaptic['ADFR'][nextState] += 1
        postsynaptic['AIBL'][nextState] += 1
        postsynaptic['AIBR'][nextState] += 1
        postsynaptic['ASHR'][nextState] += 1
        postsynaptic['AVAL'][nextState] += 1
        postsynaptic['AVBL'][nextState] += 1
        postsynaptic['AVBR'][nextState] += 5
        postsynaptic['AVDL'][nextState] += 2
        postsynaptic['AVEL'][nextState] += 1
        postsynaptic['AVJL'][nextState] += 3
        postsynaptic['PVQR'][nextState] += 1
        postsynaptic['RICL'][nextState] += 1
        postsynaptic['RIMR'][nextState] += 5
        postsynaptic['RIPR'][nextState] += 1
        postsynaptic['RIVR'][nextState] += 1
        postsynaptic['SMDVL'][nextState] += 2

def ADEL():
        postsynaptic['ADAL'][nextState] += 1
        postsynaptic['ADER'][nextState] += 1
        postsynaptic['AINL'][nextState] += 1
        postsynaptic['AVAL'][nextState] += 2
        postsynaptic['AVAR'][nextState] += 3
        postsynaptic['AVEL'][nextState] += 1
        postsynaptic['AVKR'][nextState] += 1
        postsynaptic['AVL'][nextState] += 1
        postsynaptic['BDUL'][nextState] += 1
        postsynaptic['CEPDL'][nextState] += 1
        postsynaptic['FLPL'][nextState] += 1
        postsynaptic['IL1L'][nextState] += 1
        postsynaptic['IL2L'][nextState] += 1
        postsynaptic['MDL05'][nextState] += 1
        postsynaptic['OLLL'][nextState] += 1
        postsynaptic['RIAL'][nextState] += 1
        postsynaptic['RIFL'][nextState] += 1
        postsynaptic['RIGL'][nextState] += 5
        postsynaptic['RIGR'][nextState] += 3
        postsynaptic['RIH'][nextState] += 2
        postsynaptic['RIVL'][nextState] += 1
        postsynaptic['RIVR'][nextState] += 1
        postsynaptic['RMDL'][nextState] += 2
        postsynaptic['RMGL'][nextState] += 1
        postsynaptic['RMHL'][nextState] += 1
        postsynaptic['SIADR'][nextState] += 1
        postsynaptic['SIBDR'][nextState] += 1
        postsynaptic['SMBDR'][nextState] += 1
        postsynaptic['URBL'][nextState] += 1

def ADER():
        postsynaptic['ADAR'][nextState] += 1
        postsynaptic['ADEL'][nextState] += 2
        postsynaptic['ALA'][nextState] += 1
        postsynaptic['AVAL'][nextState] += 5
        postsynaptic['AVAR'][nextState] += 1
        postsynaptic['AVDR'][nextState] += 2
        postsynaptic['AVER'][nextState] += 1
        postsynaptic['AVJR'][nextState] += 1
        postsynaptic['AVKL'][nextState] += 2
        postsynaptic['AVKR'][nextState] += 1
        postsynaptic['CEPDR'][nextState] += 1
        postsynaptic['FLPL'][nextState] += 1
        postsynaptic['FLPR'][nextState] += 1
        postsynaptic['OLLR'][nextState] += 2
        postsynaptic['PVR'][nextState] += 1
        postsynaptic['RIGL'][nextState] += 7
        postsynaptic['RIGR'][nextState] += 4
        postsynaptic['RIH'][nextState] += 1
        postsynaptic['RMDR'][nextState] += 2
        postsynaptic['SAAVR'][nextState] += 1

def ADFL():
        postsynaptic['ADAL'][nextState] += 2
        postsynaptic['AIZL'][nextState] += 12
        postsynaptic['AUAL'][nextState] += 5
        postsynaptic['OLQVL'][nextState] += 1
        postsynaptic['RIAL'][nextState] += 15
        postsynaptic['RIGL'][nextState] += 1
        postsynaptic['RIR'][nextState] += 2
        postsynaptic['SMBVL'][nextState] += 2
        #print (postsynaptic['ADAL'][nextState])

def ADFR():
        postsynaptic['ADAR'][nextState] += 2
        postsynaptic['AIAR'][nextState] += 1
        postsynaptic['AIYR'][nextState] += 1
        postsynaptic['AIZR'][nextState] += 8
        postsynaptic['ASHR'][nextState] += 1
        postsynaptic['AUAR'][nextState] += 4
        postsynaptic['AWBR'][nextState] += 1
        postsynaptic['PVPR'][nextState] += 1
        postsynaptic['RIAR'][nextState] += 16
        postsynaptic['RIGR'][nextState] += 3
        postsynaptic['RIR'][nextState] += 3
        postsynaptic['SMBDR'][nextState] += 1
        postsynaptic['SMBVR'][nextState] += 2
        postsynaptic['URXR'][nextState] += 1

def ADLL():
        postsynaptic['ADLR'][nextState] += 1
        postsynaptic['AIAL'][nextState] += 6
        postsynaptic['AIBL'][nextState] += 7
        postsynaptic['AIBR'][nextState] += 1
        postsynaptic['ALA'][nextState] += 2
        postsynaptic['ASER'][nextState] += 3
        postsynaptic['ASHL'][nextState] += 2
        postsynaptic['AVAL'][nextState] += 2
        postsynaptic['AVAR'][nextState] += 3
        postsynaptic['AVBL'][nextState] += 2
        postsynaptic['AVDL'][nextState] += 1
        postsynaptic['AVDR'][nextState] += 4
        postsynaptic['AVDR'][nextState] += 1
        postsynaptic['AVJL'][nextState] += 1
        postsynaptic['AVJR'][nextState] += 3
        postsynaptic['AWBL'][nextState] += 2
        postsynaptic['OLQVL'][nextState] += 2
        postsynaptic['RIPL'][nextState] += 1
        postsynaptic['RMGL'][nextState] += 1

def ADLR():
        postsynaptic['ADLL'][nextState] += 1
        postsynaptic['AIAR'][nextState] += 10
        postsynaptic['AIBR'][nextState] += 10
        postsynaptic['ASER'][nextState] += 1
        postsynaptic['ASHR'][nextState] += 3
        postsynaptic['AVAR'][nextState] += 2
        postsynaptic['AVBL'][nextState] += 1
        postsynaptic['AVBR'][nextState] += 2
        postsynaptic['AVDL'][nextState] += 5
        postsynaptic['AVDR'][nextState] += 2
        postsynaptic['AVJR'][nextState] += 1
        postsynaptic['AWCR'][nextState] += 3
        postsynaptic['OLLR'][nextState] += 1
        postsynaptic['PVCL'][nextState] += 1
        postsynaptic['RICL'][nextState] += 1
        postsynaptic['RICR'][nextState] += 1

def AFDL():
        postsynaptic['AFDR'][nextState] += 1
        postsynaptic['AIBL'][nextState] += 1
        postsynaptic['AINR'][nextState] += 1
        postsynaptic['AIYL'][nextState] += 7

def AFDR():
        postsynaptic['AFDL'][nextState] += 1
        postsynaptic['AIBR'][nextState] += 1
        postsynaptic['AIYR'][nextState] += 13
        postsynaptic['ASER'][nextState] += 1
                   
def AIAL():
        postsynaptic['ADAL'][nextState] += 1
        postsynaptic['AIAR'][nextState] += 1
        postsynaptic['AIBL'][nextState] += 10
        postsynaptic['AIML'][nextState] += 2
        postsynaptic['AIZL'][nextState] += 1
        postsynaptic['ASER'][nextState] += 3
        postsynaptic['ASGL'][nextState] += 1
        postsynaptic['ASHL'][nextState] += 1
        postsynaptic['ASIL'][nextState] += 2
        postsynaptic['ASKL'][nextState] += 3
        postsynaptic['AWAL'][nextState] += 1
        postsynaptic['AWCR'][nextState] += 1
        postsynaptic['HSNL'][nextState] += 1
        postsynaptic['RIFL'][nextState] += 1
        postsynaptic['RMGL'][nextState] += 1

def AIAR():
        postsynaptic['ADAR'][nextState] += 1
        postsynaptic['ADFR'][nextState] += 1
        postsynaptic['ADLR'][nextState] += 2
        postsynaptic['AIAL'][nextState] += 1
        postsynaptic['AIBR'][nextState] += 14
        postsynaptic['AIZR'][nextState] += 1
        postsynaptic['ASER'][nextState] += 1
        postsynaptic['ASGR'][nextState] += 1
        postsynaptic['ASIR'][nextState] += 2
        postsynaptic['AWAR'][nextState] += 2
        postsynaptic['AWCL'][nextState] += 1
        postsynaptic['AWCR'][nextState] += 3
        postsynaptic['RIFR'][nextState] += 2

def AIBL():
        postsynaptic['AFDL'][nextState] += 1
        postsynaptic['AIYL'][nextState] += 1
        postsynaptic['ASER'][nextState] += 1
        postsynaptic['AVAL'][nextState] += 2
        postsynaptic['AVBL'][nextState] += 5
        postsynaptic['DVC'][nextState] += 1
        postsynaptic['FLPL'][nextState] += 1
        postsynaptic['PVT'][nextState] += 1
        postsynaptic['RIBR'][nextState] += 4
        postsynaptic['RIFL'][nextState] += 1
        postsynaptic['RIGR'][nextState] += 1
        postsynaptic['RIGR'][nextState] += 3
        postsynaptic['RIML'][nextState] += 2
        postsynaptic['RIMR'][nextState] += 13
        postsynaptic['RIMR'][nextState] += 1
        postsynaptic['RIVL'][nextState] += 1
        postsynaptic['SAADL'][nextState] += 2
        postsynaptic['SAADR'][nextState] += 2
        postsynaptic['SMDDR'][nextState] += 4

def AIBR():
        postsynaptic['AFDR'][nextState] += 1
        postsynaptic['AVAR'][nextState] += 1
        postsynaptic['AVBR'][nextState] += 3
        postsynaptic['AVEL'][nextState] += 1
        postsynaptic['DB1'][nextState] += 1
        postsynaptic['DVC'][nextState] += 2
        postsynaptic['PVT'][nextState] += 1
        postsynaptic['RIAL'][nextState] += 1
        postsynaptic['RIBL'][nextState] += 4
        postsynaptic['RIGL'][nextState] += 3
        postsynaptic['RIML'][nextState] += 16
        postsynaptic['RIML'][nextState] += 1
        postsynaptic['RIMR'][nextState] += 1
        postsynaptic['RIS'][nextState] += 1
        postsynaptic['RIVR'][nextState] += 1
        postsynaptic['SAADL'][nextState] += 1
        postsynaptic['SMDDL'][nextState] += 3
        postsynaptic['SMDVL'][nextState] += 1
        postsynaptic['VB1'][nextState] += 3

def AIML():
        postsynaptic['AIAL'][nextState] += 5
        postsynaptic['ALML'][nextState] += 1
        postsynaptic['ASGL'][nextState] += 2
        postsynaptic['ASKL'][nextState] += 2
        postsynaptic['AVBR'][nextState] += 2
        postsynaptic['AVDL'][nextState] += 1
        postsynaptic['AVDR'][nextState] += 1
        postsynaptic['AVER'][nextState] += 1
        postsynaptic['AVFL'][nextState] += 4
        postsynaptic['AVFR'][nextState] += 1
        postsynaptic['AVHL'][nextState] += 2
        postsynaptic['AVHR'][nextState] += 1
        postsynaptic['AVJL'][nextState] += 1
        postsynaptic['PVQL'][nextState] += 1
        postsynaptic['RIFL'][nextState] += 1
        postsynaptic['SIBDR'][nextState] += 1
        postsynaptic['SMBVL'][nextState] += 1

def AIMR():
        postsynaptic['AIAR'][nextState] += 5
        postsynaptic['ASGR'][nextState] += 2
        postsynaptic['ASJR'][nextState] += 2
        postsynaptic['ASKR'][nextState] += 3
        postsynaptic['AVDR'][nextState] += 1
        postsynaptic['AVFL'][nextState] += 1
        postsynaptic['AVFR'][nextState] += 1
        postsynaptic['HSNL'][nextState] += 1
        postsynaptic['HSNR'][nextState] += 2
        postsynaptic['OLQDR'][nextState] += 1
        postsynaptic['PVNR'][nextState] += 1
        postsynaptic['RIFR'][nextState] += 1
        postsynaptic['RMGR'][nextState] += 1

def AINL():
        postsynaptic['ADEL'][nextState] += 1
        postsynaptic['AFDR'][nextState] += 5
        postsynaptic['AINR'][nextState] += 2
        postsynaptic['ASEL'][nextState] += 3
        postsynaptic['ASGR'][nextState] += 2
        postsynaptic['AUAR'][nextState] += 2
        postsynaptic['BAGL'][nextState] += 3
        postsynaptic['RIBL'][nextState] += 1
        postsynaptic['RIBR'][nextState] += 2

def AINR():
        postsynaptic['AFDL'][nextState] += 4
        postsynaptic['AFDR'][nextState] += 1
        postsynaptic['AIAL'][nextState] += 2
        postsynaptic['AIBL'][nextState] += 2
        postsynaptic['AINL'][nextState] += 2
        postsynaptic['ASEL'][nextState] += 1
        postsynaptic['ASER'][nextState] += 1
        postsynaptic['ASGL'][nextState] += 1
        postsynaptic['AUAL'][nextState] += 1
        postsynaptic['AUAR'][nextState] += 1
        postsynaptic['BAGR'][nextState] += 3
        postsynaptic['RIBL'][nextState] += 2
        postsynaptic['RID'][nextState] += 1

def AIYL():
        postsynaptic['AIYR'][nextState] += 1
        postsynaptic['AIZL'][nextState] += 13
        postsynaptic['AWAL'][nextState] += 3
        postsynaptic['AWCL'][nextState] += 1
        postsynaptic['AWCR'][nextState] += 1
        postsynaptic['HSNR'][nextState] += 1
        postsynaptic['RIAL'][nextState] += 7
        postsynaptic['RIBL'][nextState] += 4
        postsynaptic['RIML'][nextState] += 1

def AIYR():
        postsynaptic['ADFR'][nextState] += 1
        postsynaptic['AIYL'][nextState] += 1
        postsynaptic['AIZR'][nextState] += 8
        postsynaptic['AWAR'][nextState] += 1
        postsynaptic['HSNL'][nextState] += 1
        postsynaptic['RIAR'][nextState] += 6
        postsynaptic['RIBR'][nextState] += 2
        postsynaptic['RIMR'][nextState] += 1

def AIZL():
        postsynaptic['AIAL'][nextState] += 3
        postsynaptic['AIBL'][nextState] += 2
        postsynaptic['AIBR'][nextState] += 8
        postsynaptic['AIZR'][nextState] += 2
        postsynaptic['ASEL'][nextState] += 1
        postsynaptic['ASGL'][nextState] += 1
        postsynaptic['ASHL'][nextState] += 1
        postsynaptic['AVER'][nextState] += 5
        postsynaptic['DVA'][nextState] += 1
        postsynaptic['RIAL'][nextState] += 8
        postsynaptic['RIGL'][nextState] += 1
        postsynaptic['RIML'][nextState] += 4
        postsynaptic['SMBDL'][nextState] += 9
        postsynaptic['SMBVL'][nextState] += 7
        postsynaptic['VB2'][nextState] += 1

def AIZR():
        postsynaptic['AIAR'][nextState] += 1
        postsynaptic['AIBL'][nextState] += 8
        postsynaptic['AIBR'][nextState] += 1
        postsynaptic['AIZL'][nextState] += 2
        postsynaptic['ASGR'][nextState] += 1
        postsynaptic['ASHR'][nextState] += 1
        postsynaptic['AVEL'][nextState] += 4
        postsynaptic['AVER'][nextState] += 1
        postsynaptic['AWAR'][nextState] += 1
        postsynaptic['DVA'][nextState] += 1
        postsynaptic['RIAR'][nextState] += 7
        postsynaptic['RIMR'][nextState] += 4
        postsynaptic['SMBDR'][nextState] += 5
        postsynaptic['SMBVR'][nextState] += 3
        postsynaptic['SMDDR'][nextState] += 1

def ALA():
        postsynaptic['ADEL'][nextState] += 1
        postsynaptic['AVAL'][nextState] += 1
        postsynaptic['AVEL'][nextState] += 2
        postsynaptic['AVER'][nextState] += 1
        postsynaptic['RID'][nextState] += 1
        postsynaptic['RMDR'][nextState] += 1

def ALML():
        postsynaptic['AVDR'][nextState] += 1
        postsynaptic['AVEL'][nextState] += 1
        postsynaptic['AVM'][nextState] += 1
        postsynaptic['BDUL'][nextState] += 6
        postsynaptic['CEPDL'][nextState] += 3
        postsynaptic['CEPVL'][nextState] += 2
        postsynaptic['PVCL'][nextState] += 2
        postsynaptic['PVCR'][nextState] += 1
        postsynaptic['PVR'][nextState] += 1
        postsynaptic['RMDDR'][nextState] += 1
        postsynaptic['RMGL'][nextState] += 1
        postsynaptic['SDQL'][nextState] += 1

def ALMR():
        postsynaptic['AVM'][nextState] += 1
        postsynaptic['BDUR'][nextState] += 5
        postsynaptic['CEPDR'][nextState] += 1
        postsynaptic['CEPVR'][nextState] += 1
        postsynaptic['PVCR'][nextState] += 3
        postsynaptic['RMDDL'][nextState] += 1
        postsynaptic['SIADL'][nextState] += 1

def ALNL():
        postsynaptic['SAAVL'][nextState] += 3
        postsynaptic['SMBDR'][nextState] += 2
        postsynaptic['SMBDR'][nextState] += 1
        postsynaptic['SMDVL'][nextState] += 1

def ALNR():
        postsynaptic['ADER'][nextState] += 1
        postsynaptic['RMHR'][nextState] += 1
        postsynaptic['SAAVR'][nextState] += 2
        postsynaptic['SMBDL'][nextState] += 2
        postsynaptic['SMDDR'][nextState] += 1
        postsynaptic['SMDVL'][nextState] += 1

def AQR():
        postsynaptic['AVAL'][nextState] += 1
        postsynaptic['AVAR'][nextState] += 3
        postsynaptic['AVBL'][nextState] += 3
        postsynaptic['AVBL'][nextState] += 1
        postsynaptic['AVBR'][nextState] += 4
        postsynaptic['AVDL'][nextState] += 1
        postsynaptic['AVDR'][nextState] += 1
        postsynaptic['AVJL'][nextState] += 1
        postsynaptic['AVKL'][nextState] += 2
        postsynaptic['AVKR'][nextState] += 1
        postsynaptic['BAGL'][nextState] += 2
        postsynaptic['BAGR'][nextState] += 2
        postsynaptic['PVCR'][nextState] += 2
        postsynaptic['PVPL'][nextState] += 1
        postsynaptic['PVPL'][nextState] += 7
        postsynaptic['PVPR'][nextState] += 9
        postsynaptic['RIAL'][nextState] += 3
        postsynaptic['RIAR'][nextState] += 1
        postsynaptic['RIGL'][nextState] += 2
        postsynaptic['RIGR'][nextState] += 1
        postsynaptic['URXL'][nextState] += 1

def AS1():
        postsynaptic['AVAL'][nextState] += 3
        postsynaptic['AVAR'][nextState] += 2
        postsynaptic['DA1'][nextState] += 2
        postsynaptic['MDL05'][nextState] += 3
        postsynaptic['MDL08'][nextState] += 3
        postsynaptic['MDR05'][nextState] += 3
        postsynaptic['MDR08'][nextState] += 4
        postsynaptic['VA3'][nextState] += 1
        postsynaptic['VD1'][nextState] += 5
        postsynaptic['VD2'][nextState] += 1

def AS2():
        postsynaptic['DA2'][nextState] += 1
        postsynaptic['DB1'][nextState] += 1
        postsynaptic['DD1'][nextState] += 1
        postsynaptic['MDL07'][nextState] += 3
        postsynaptic['MDL08'][nextState] += 2
        postsynaptic['MDR07'][nextState] += 3
        postsynaptic['MDR08'][nextState] += 3
        postsynaptic['VA4'][nextState] += 2
        postsynaptic['VD2'][nextState] += 10

def AS3():
        postsynaptic['AVAL'][nextState] += 2
        postsynaptic['AVAR'][nextState] += 1
        postsynaptic['DA2'][nextState] += 1
        postsynaptic['DA3'][nextState] += 1
        postsynaptic['DD1'][nextState] += 1
        postsynaptic['MDL09'][nextState] += 3
        postsynaptic['MDL10'][nextState] += 3
        postsynaptic['MDR09'][nextState] += 3
        postsynaptic['MDR10'][nextState] += 3
        postsynaptic['VA5'][nextState] += 2
        postsynaptic['VD2'][nextState] += 1
        postsynaptic['VD3'][nextState] += 15

def AS4():
        postsynaptic['AS5'][nextState] += 1
        postsynaptic['DA3'][nextState] += 1
        postsynaptic['MDL11'][nextState] += 2
        postsynaptic['MDL12'][nextState] += 2
        postsynaptic['MDR11'][nextState] += 3
        postsynaptic['MDR12'][nextState] += 2
        postsynaptic['VD4'][nextState] += 11

def AS5():
        postsynaptic['AVAL'][nextState] += 1
        postsynaptic['AVAR'][nextState] += 1
        postsynaptic['DD2'][nextState] += 1
        postsynaptic['MDL11'][nextState] += 2
        postsynaptic['MDL14'][nextState] += 3
        postsynaptic['MDR11'][nextState] += 2
        postsynaptic['MDR14'][nextState] += 3
        postsynaptic['VA7'][nextState] += 1
        postsynaptic['VD5'][nextState] += 9

def AS6():
        postsynaptic['AVAL'][nextState] += 1
        postsynaptic['AVAR'][nextState] += 1
        postsynaptic['AVBR'][nextState] += 1
        postsynaptic['DA5'][nextState] += 2
        postsynaptic['MDL13'][nextState] += 3
        postsynaptic['MDL14'][nextState] += 2
        postsynaptic['MDR13'][nextState] += 3
        postsynaptic['MDR14'][nextState] += 2
        postsynaptic['VA8'][nextState] += 1
        postsynaptic['VD6'][nextState] += 13

def AS7():
        postsynaptic['AVAL'][nextState] += 6
        postsynaptic['AVAR'][nextState] += 5
        postsynaptic['AVBL'][nextState] += 2
        postsynaptic['AVBR'][nextState] += 2
        postsynaptic['MDL13'][nextState] += 2
        postsynaptic['MDL16'][nextState] += 3
        postsynaptic['MDR13'][nextState] += 2
        postsynaptic['MDR16'][nextState] += 3

def AS8():
        postsynaptic['AVAL'][nextState] += 4
        postsynaptic['AVAR'][nextState] += 3
        postsynaptic['MDL15'][nextState] += 2
        postsynaptic['MDL18'][nextState] += 3
        postsynaptic['MDR15'][nextState] += 2
        postsynaptic['MDR18'][nextState] += 3

def AS9():
        postsynaptic['AVAL'][nextState] += 4
        postsynaptic['AVAR'][nextState] += 2
        postsynaptic['DVB'][nextState] += 7
        postsynaptic['MDL17'][nextState] += 2
        postsynaptic['MDL20'][nextState] += 3
        postsynaptic['MDR17'][nextState] += 2
        postsynaptic['MDR20'][nextState] += 3

def AS10():
        postsynaptic['AVAL'][nextState] += 1
        postsynaptic['AVAR'][nextState] += 1
        postsynaptic['MDL19'][nextState] += 3
        postsynaptic['MDL20'][nextState] += 2
        postsynaptic['MDR19'][nextState] += 3
        postsynaptic['MDR20'][nextState] += 2

def AS11():
        postsynaptic['MDL21'][nextState] += 1
        postsynaptic['MDL22'][nextState] += 1
        postsynaptic['MDL23'][nextState] += 1
        postsynaptic['MDL24'][nextState] += 1
        postsynaptic['MDR21'][nextState] += 1
        postsynaptic['MDR22'][nextState] += 1
        postsynaptic['MDR23'][nextState] += 1
        postsynaptic['MDR24'][nextState] += 1
        postsynaptic['PDA'][nextState] += 1
        postsynaptic['PDB'][nextState] += 1
        postsynaptic['PDB'][nextState] += 2
        postsynaptic['VD13'][nextState] += 2

def ASEL():
        postsynaptic['ADFR'][nextState] += 1
        postsynaptic['AIAL'][nextState] += 3
        postsynaptic['AIBL'][nextState] += 7
        postsynaptic['AIBR'][nextState] += 2
        postsynaptic['AIYL'][nextState] += 13
        postsynaptic['AIYR'][nextState] += 6
        postsynaptic['AWCL'][nextState] += 4
        postsynaptic['AWCR'][nextState] += 1
        postsynaptic['RIAR'][nextState] += 1

def ASER():
        postsynaptic['AFDL'][nextState] += 1
        postsynaptic['AFDR'][nextState] += 2
        postsynaptic['AIAL'][nextState] += 1
        postsynaptic['AIAR'][nextState] += 3
        postsynaptic['AIBL'][nextState] += 2
        postsynaptic['AIBR'][nextState] += 10
        postsynaptic['AIYL'][nextState] += 2
        postsynaptic['AIYR'][nextState] += 14
        postsynaptic['AWAR'][nextState] += 1
        postsynaptic['AWCL'][nextState] += 1
        postsynaptic['AWCR'][nextState] += 1

def ASGL():
        postsynaptic['AIAL'][nextState] += 9
        postsynaptic['AIBL'][nextState] += 3
        postsynaptic['AINR'][nextState] += 2
        postsynaptic['AIZL'][nextState] += 1
        postsynaptic['ASKL'][nextState] += 1

def ASGR():
        postsynaptic['AIAR'][nextState] += 10
        postsynaptic['AIBR'][nextState] += 2
        postsynaptic['AINL'][nextState] += 1
        postsynaptic['AIYR'][nextState] += 1
        postsynaptic['AIZR'][nextState] += 1

def ASHL():
        postsynaptic['ADAL'][nextState] += 2
        postsynaptic['ADFL'][nextState] += 3
        postsynaptic['AIAL'][nextState] += 7
        postsynaptic['AIBL'][nextState] += 5
        postsynaptic['AIZL'][nextState] += 1
        postsynaptic['ASHR'][nextState] += 1
        postsynaptic['ASKL'][nextState] += 1
        postsynaptic['AVAL'][nextState] += 2
        postsynaptic['AVBL'][nextState] += 6
        postsynaptic['AVDL'][nextState] += 2
        postsynaptic['AVDR'][nextState] += 2
        postsynaptic['RIAL'][nextState] += 4
        postsynaptic['RICL'][nextState] += 2
        postsynaptic['RIML'][nextState] += 1
        postsynaptic['RIPL'][nextState] += 1
        postsynaptic['RMGL'][nextState] += 1

def ASHR():
        postsynaptic['ADAR'][nextState] += 3
        postsynaptic['ADFR'][nextState] += 2
        postsynaptic['AIAR'][nextState] += 10
        postsynaptic['AIBR'][nextState] += 3
        postsynaptic['AIZR'][nextState] += 1
        postsynaptic['ASHL'][nextState] += 1
        postsynaptic['ASKR'][nextState] += 1
        postsynaptic['AVAR'][nextState] += 5
        postsynaptic['AVBR'][nextState] += 3
        postsynaptic['AVDL'][nextState] += 5
        postsynaptic['AVDR'][nextState] += 1
        postsynaptic['AVER'][nextState] += 3
        postsynaptic['HSNR'][nextState] += 1
        postsynaptic['PVPR'][nextState] += 1
        postsynaptic['RIAR'][nextState] += 2
        postsynaptic['RICR'][nextState] += 2
        postsynaptic['RMGR'][nextState] += 2
        postsynaptic['RMGR'][nextState] += 1

def ASIL():
        postsynaptic['AIAL'][nextState] += 2
        postsynaptic['AIBL'][nextState] += 1
        postsynaptic['AIYL'][nextState] += 2
        postsynaptic['AIZL'][nextState] += 1
        postsynaptic['ASER'][nextState] += 1
        postsynaptic['ASIR'][nextState] += 1
        postsynaptic['ASKL'][nextState] += 2
        postsynaptic['AWCL'][nextState] += 1
        postsynaptic['AWCR'][nextState] += 1
        postsynaptic['RIBL'][nextState] += 1

def ASIR():
        postsynaptic['AIAL'][nextState] += 1
        postsynaptic['AIAR'][nextState] += 3
        postsynaptic['AIAR'][nextState] += 2
        postsynaptic['AIBR'][nextState] += 1
        postsynaptic['ASEL'][nextState] += 2
        postsynaptic['ASHR'][nextState] += 1
        postsynaptic['ASIL'][nextState] += 1
        postsynaptic['AWCL'][nextState] += 1
        postsynaptic['AWCR'][nextState] += 1

def ASJL():
        postsynaptic['ASJR'][nextState] += 1
        postsynaptic['ASKL'][nextState] += 4
        postsynaptic['HSNL'][nextState] += 1
        postsynaptic['HSNR'][nextState] += 1
        postsynaptic['PVQL'][nextState] += 14

def ASJR():
        postsynaptic['ASJL'][nextState] += 1
        postsynaptic['ASKR'][nextState] += 4
        postsynaptic['HSNR'][nextState] += 1
        postsynaptic['PVQR'][nextState] += 13

def ASKL():
        postsynaptic['AIAL'][nextState] += 11
        postsynaptic['AIBL'][nextState] += 2
        postsynaptic['AIML'][nextState] += 2
        postsynaptic['ASKR'][nextState] += 1
        postsynaptic['PVQL'][nextState] += 5
        postsynaptic['RMGL'][nextState] += 1

def ASKR():
        postsynaptic['AIAR'][nextState] += 11
        postsynaptic['AIMR'][nextState] += 1
        postsynaptic['ASHR'][nextState] += 1
        postsynaptic['ASKL'][nextState] += 1
        postsynaptic['AWAR'][nextState] += 1
        postsynaptic['CEPVR'][nextState] += 1
        postsynaptic['PVQR'][nextState] += 4
        postsynaptic['RIFR'][nextState] += 1
        postsynaptic['RMGR'][nextState] += 1

def AUAL():
        postsynaptic['AINR'][nextState] += 1
        postsynaptic['AUAR'][nextState] += 1
        postsynaptic['AVAL'][nextState] += 3
        postsynaptic['AVDR'][nextState] += 1
        postsynaptic['AVEL'][nextState] += 3
        postsynaptic['AWBL'][nextState] += 1
        postsynaptic['RIAL'][nextState] += 5
        postsynaptic['RIBL'][nextState] += 9

def AUAR():
        postsynaptic['AINL'][nextState] += 1
        postsynaptic['AIYR'][nextState] += 1
        postsynaptic['AUAL'][nextState] += 1
        postsynaptic['AVAR'][nextState] += 1
        postsynaptic['AVER'][nextState] += 4
        postsynaptic['AWBR'][nextState] += 1
        postsynaptic['RIAR'][nextState] += 6
        postsynaptic['RIBR'][nextState] += 13
        postsynaptic['URXR'][nextState] += 1

def AVAL():
        postsynaptic['AS1'][nextState] += 3
        postsynaptic['AS10'][nextState] += 3
        postsynaptic['AS11'][nextState] += 4
        postsynaptic['AS2'][nextState] += 1
        postsynaptic['AS3'][nextState] += 3
        postsynaptic['AS4'][nextState] += 1
        postsynaptic['AS5'][nextState] += 4
        postsynaptic['AS6'][nextState] += 1
        postsynaptic['AS7'][nextState] += 14
        postsynaptic['AS8'][nextState] += 9
        postsynaptic['AS9'][nextState] += 12
        postsynaptic['AVAR'][nextState] += 7
        postsynaptic['AVBR'][nextState] += 1
        postsynaptic['AVDL'][nextState] += 1
        postsynaptic['AVHL'][nextState] += 1
        postsynaptic['AVJL'][nextState] += 2
        postsynaptic['DA1'][nextState] += 4
        postsynaptic['DA2'][nextState] += 4
        postsynaptic['DA3'][nextState] += 6
        postsynaptic['DA4'][nextState] += 10
        postsynaptic['DA5'][nextState] += 8
        postsynaptic['DA6'][nextState] += 21
        postsynaptic['DA7'][nextState] += 4
        postsynaptic['DA8'][nextState] += 4
        postsynaptic['DA9'][nextState] += 3
        postsynaptic['DB5'][nextState] += 2
        postsynaptic['DB6'][nextState] += 4
        postsynaptic['FLPL'][nextState] += 1
        postsynaptic['LUAL'][nextState] += 2
        postsynaptic['PVCL'][nextState] += 12
        postsynaptic['PVCR'][nextState] += 11
        postsynaptic['PVPL'][nextState] += 1
        postsynaptic['RIMR'][nextState] += 3
        postsynaptic['SABD'][nextState] += 4
        postsynaptic['SABVR'][nextState] += 1
        postsynaptic['SDQR'][nextState] += 1
        postsynaptic['URYDL'][nextState] += 1
        postsynaptic['URYVR'][nextState] += 1
        postsynaptic['VA1'][nextState] += 3
        postsynaptic['VA10'][nextState] += 6
        postsynaptic['VA11'][nextState] += 7
        postsynaptic['VA12'][nextState] += 2
        postsynaptic['VA2'][nextState] += 5
        postsynaptic['VA3'][nextState] += 3
        postsynaptic['VA4'][nextState] += 3
        postsynaptic['VA5'][nextState] += 8
        postsynaptic['VA6'][nextState] += 10
        postsynaptic['VA7'][nextState] += 2
        postsynaptic['VA8'][nextState] += 19
        postsynaptic['VA9'][nextState] += 8
        postsynaptic['VB9'][nextState] += 5

def AVAR():
        postsynaptic['ADER'][nextState] += 1
        postsynaptic['AS1'][nextState] += 3
        postsynaptic['AS10'][nextState] += 2
        postsynaptic['AS11'][nextState] += 6
        postsynaptic['AS2'][nextState] += 2
        postsynaptic['AS3'][nextState] += 2
        postsynaptic['AS4'][nextState] += 1
        postsynaptic['AS5'][nextState] += 2
        postsynaptic['AS6'][nextState] += 3
        postsynaptic['AS7'][nextState] += 8
        postsynaptic['AS8'][nextState] += 9
        postsynaptic['AS9'][nextState] += 6
        postsynaptic['AVAL'][nextState] += 6
        postsynaptic['AVBL'][nextState] += 1
        postsynaptic['AVDL'][nextState] += 1
        postsynaptic['AVDR'][nextState] += 2
        postsynaptic['AVEL'][nextState] += 2
        postsynaptic['AVER'][nextState] += 2
        postsynaptic['DA1'][nextState] += 8
        postsynaptic['DA2'][nextState] += 4
        postsynaptic['DA3'][nextState] += 5
        postsynaptic['DA4'][nextState] += 8
        postsynaptic['DA5'][nextState] += 7
        postsynaptic['DA6'][nextState] += 13
        postsynaptic['DA7'][nextState] += 3
        postsynaptic['DA8'][nextState] += 9
        postsynaptic['DA9'][nextState] += 2
        postsynaptic['DB3'][nextState] += 1
        postsynaptic['DB5'][nextState] += 3
        postsynaptic['DB6'][nextState] += 5
        postsynaptic['LUAL'][nextState] += 1
        postsynaptic['LUAR'][nextState] += 3
        postsynaptic['PDEL'][nextState] += 1
        postsynaptic['PDER'][nextState] += 1
        postsynaptic['PVCL'][nextState] += 7
        postsynaptic['PVCR'][nextState] += 8
        postsynaptic['RIGL'][nextState] += 1
        postsynaptic['RIML'][nextState] += 2
        postsynaptic['RIMR'][nextState] += 1
        postsynaptic['SABD'][nextState] += 1
        postsynaptic['SABVL'][nextState] += 6
        postsynaptic['SABVR'][nextState] += 1
        postsynaptic['URYDR'][nextState] += 1
        postsynaptic['URYVL'][nextState] += 1
        postsynaptic['VA10'][nextState] += 5
        postsynaptic['VA11'][nextState] += 15
        postsynaptic['VA12'][nextState] += 1
        postsynaptic['VA2'][nextState] += 2
        postsynaptic['VA3'][nextState] += 7
        postsynaptic['VA4'][nextState] += 5
        postsynaptic['VA5'][nextState] += 4
        postsynaptic['VA6'][nextState] += 5
        postsynaptic['VA7'][nextState] += 4
        postsynaptic['VA8'][nextState] += 16
        postsynaptic['VB9'][nextState] += 10
        postsynaptic['VD13'][nextState] += 2

def AVBL():
        postsynaptic['AQR'][nextState] += 1
        postsynaptic['AS10'][nextState] += 1
        postsynaptic['AS3'][nextState] += 1
        postsynaptic['AS4'][nextState] += 1
        postsynaptic['AS5'][nextState] += 1
        postsynaptic['AS6'][nextState] += 1
        postsynaptic['AS7'][nextState] += 2
        postsynaptic['AS9'][nextState] += 1
        postsynaptic['AVAL'][nextState] += 7
        postsynaptic['AVAR'][nextState] += 7
        postsynaptic['AVBR'][nextState] += 4
        postsynaptic['AVDL'][nextState] += 1
        postsynaptic['AVDR'][nextState] += 2
        postsynaptic['AVEL'][nextState] += 1
        postsynaptic['AVER'][nextState] += 2
        postsynaptic['AVL'][nextState] += 1
        postsynaptic['DB3'][nextState] += 1
        postsynaptic['DB4'][nextState] += 1
        postsynaptic['DB5'][nextState] += 1
        postsynaptic['DB6'][nextState] += 2
        postsynaptic['DB7'][nextState] += 2
        postsynaptic['DVA'][nextState] += 1
        postsynaptic['PVNR'][nextState] += 1
        postsynaptic['RIBL'][nextState] += 1
        postsynaptic['RIBR'][nextState] += 1
        postsynaptic['RID'][nextState] += 1
        postsynaptic['SDQR'][nextState] += 1
        postsynaptic['SIBVL'][nextState] += 1
        postsynaptic['VA10'][nextState] += 1
        postsynaptic['VA2'][nextState] += 1
        postsynaptic['VA7'][nextState] += 1
        postsynaptic['VB1'][nextState] += 1
        postsynaptic['VB10'][nextState] += 2
        postsynaptic['VB11'][nextState] += 2
        postsynaptic['VB2'][nextState] += 4
        postsynaptic['VB4'][nextState] += 1
        postsynaptic['VB5'][nextState] += 1
        postsynaptic['VB6'][nextState] += 1
        postsynaptic['VB7'][nextState] += 2
        postsynaptic['VB8'][nextState] += 7
        postsynaptic['VB9'][nextState] += 1
        postsynaptic['VC3'][nextState] += 1

def AVBR():
        postsynaptic['AS1'][nextState] += 1
        postsynaptic['AS10'][nextState] += 1
        postsynaptic['AS3'][nextState] += 1
        postsynaptic['AS4'][nextState] += 1
        postsynaptic['AS5'][nextState] += 1
        postsynaptic['AS6'][nextState] += 2
        postsynaptic['AS7'][nextState] += 3
        postsynaptic['AVAL'][nextState] += 6
        postsynaptic['AVAR'][nextState] += 7
        postsynaptic['AVBL'][nextState] += 4
        postsynaptic['DA5'][nextState] += 1
        postsynaptic['DB1'][nextState] += 3
        postsynaptic['DB2'][nextState] += 1
        postsynaptic['DB3'][nextState] += 1
        postsynaptic['DB4'][nextState] += 1
        postsynaptic['DB5'][nextState] += 1
        postsynaptic['DB6'][nextState] += 1
        postsynaptic['DB7'][nextState] += 1
        postsynaptic['DD1'][nextState] += 1
        postsynaptic['DVA'][nextState] += 1
        postsynaptic['HSNR'][nextState] += 1
        postsynaptic['PVNL'][nextState] += 2
        postsynaptic['RIBL'][nextState] += 1
        postsynaptic['RIBR'][nextState] += 1
        postsynaptic['RID'][nextState] += 2
        postsynaptic['SIBVL'][nextState] += 1
        postsynaptic['VA4'][nextState] += 1
        postsynaptic['VA8'][nextState] += 1
        postsynaptic['VA9'][nextState] += 2
        postsynaptic['VB10'][nextState] += 1
        postsynaptic['VB11'][nextState] += 1
        postsynaptic['VB2'][nextState] += 1
        postsynaptic['VB3'][nextState] += 1
        postsynaptic['VB4'][nextState] += 1
        postsynaptic['VB6'][nextState] += 2
        postsynaptic['VB7'][nextState] += 2
        postsynaptic['VB8'][nextState] += 3
        postsynaptic['VB9'][nextState] += 6
        postsynaptic['VD10'][nextState] += 1
        postsynaptic['VD3'][nextState] += 1

def AVDL():
        postsynaptic['ADAR'][nextState] += 2
        postsynaptic['AS1'][nextState] += 1
        postsynaptic['AS10'][nextState] += 1
        postsynaptic['AS11'][nextState] += 2
        postsynaptic['AS4'][nextState] += 1
        postsynaptic['AS5'][nextState] += 1
        postsynaptic['AVAL'][nextState] += 13
        postsynaptic['AVAR'][nextState] += 19
        postsynaptic['AVM'][nextState] += 2
        postsynaptic['DA1'][nextState] += 1
        postsynaptic['DA2'][nextState] += 1
        postsynaptic['DA3'][nextState] += 4
        postsynaptic['DA4'][nextState] += 1
        postsynaptic['DA5'][nextState] += 1
        postsynaptic['DA8'][nextState] += 1
        postsynaptic['FLPL'][nextState] += 1
        postsynaptic['FLPR'][nextState] += 1
        postsynaptic['LUAL'][nextState] += 1
        postsynaptic['PVCL'][nextState] += 1
        postsynaptic['SABD'][nextState] += 1
        postsynaptic['SABVL'][nextState] += 1
        postsynaptic['SABVR'][nextState] += 1
        postsynaptic['VA5'][nextState] += 1

def AVDR():
        postsynaptic['ADAL'][nextState] += 2
        postsynaptic['ADLL'][nextState] += 1
        postsynaptic['AS10'][nextState] += 1
        postsynaptic['AS5'][nextState] += 1
        postsynaptic['AVAL'][nextState] += 16
        postsynaptic['AVAR'][nextState] += 15
        postsynaptic['AVBL'][nextState] += 1
        postsynaptic['AVDL'][nextState] += 2
        postsynaptic['AVJL'][nextState] += 2
        postsynaptic['DA1'][nextState] += 2
        postsynaptic['DA2'][nextState] += 1
        postsynaptic['DA3'][nextState] += 1
        postsynaptic['DA4'][nextState] += 1
        postsynaptic['DA5'][nextState] += 2
        postsynaptic['DA8'][nextState] += 1
        postsynaptic['DA9'][nextState] += 1
        postsynaptic['DB4'][nextState] += 1
        postsynaptic['DVC'][nextState] += 1
        postsynaptic['FLPR'][nextState] += 1
        postsynaptic['LUAL'][nextState] += 2
        postsynaptic['PQR'][nextState] += 1
        postsynaptic['SABD'][nextState] += 1
        postsynaptic['SABVL'][nextState] += 3
        postsynaptic['SABVR'][nextState] += 1
        postsynaptic['VA11'][nextState] += 1
        postsynaptic['VA2'][nextState] += 1
        postsynaptic['VA3'][nextState] += 2
        postsynaptic['VA6'][nextState] += 1

def AVEL():
        postsynaptic['AS1'][nextState] += 1
        postsynaptic['AVAL'][nextState] += 12
        postsynaptic['AVAR'][nextState] += 7
        postsynaptic['AVER'][nextState] += 1
        postsynaptic['DA1'][nextState] += 5
        postsynaptic['DA2'][nextState] += 1
        postsynaptic['DA3'][nextState] += 3
        postsynaptic['DA4'][nextState] += 1
        postsynaptic['PVCR'][nextState] += 1
        postsynaptic['PVT'][nextState] += 1
        postsynaptic['RIML'][nextState] += 2
        postsynaptic['RIMR'][nextState] += 3
        postsynaptic['RMDVR'][nextState] += 1
        postsynaptic['RMEV'][nextState] += 1
        postsynaptic['SABD'][nextState] += 6
        postsynaptic['SABVL'][nextState] += 7
        postsynaptic['SABVR'][nextState] += 3
        postsynaptic['VA1'][nextState] += 5
        postsynaptic['VA3'][nextState] += 3
        postsynaptic['VD2'][nextState] += 1
        postsynaptic['VD3'][nextState] += 1

def AVER():
        postsynaptic['AS1'][nextState] += 3
        postsynaptic['AS2'][nextState] += 2
        postsynaptic['AS3'][nextState] += 1
        postsynaptic['AVAL'][nextState] += 7
        postsynaptic['AVAR'][nextState] += 16
        postsynaptic['AVDR'][nextState] += 1
        postsynaptic['AVEL'][nextState] += 1
        postsynaptic['DA1'][nextState] += 5
        postsynaptic['DA2'][nextState] += 3
        postsynaptic['DA3'][nextState] += 1
        postsynaptic['DB3'][nextState] += 1
        postsynaptic['RIML'][nextState] += 3
        postsynaptic['RIMR'][nextState] += 2
        postsynaptic['RMDVL'][nextState] += 1
        postsynaptic['RMDVR'][nextState] += 1
        postsynaptic['RMEV'][nextState] += 1
        postsynaptic['SABD'][nextState] += 2
        postsynaptic['SABVL'][nextState] += 3
        postsynaptic['SABVR'][nextState] += 3
        postsynaptic['VA1'][nextState] += 1
        postsynaptic['VA2'][nextState] += 1
        postsynaptic['VA3'][nextState] += 2
        postsynaptic['VA4'][nextState] += 1
        postsynaptic['VA5'][nextState] += 1

def AVFL():
        postsynaptic['AVBL'][nextState] += 1
        postsynaptic['AVBR'][nextState] += 2
        postsynaptic['AVFR'][nextState] += 30
        postsynaptic['AVG'][nextState] += 1
        postsynaptic['AVHL'][nextState] += 4
        postsynaptic['AVHR'][nextState] += 7
        postsynaptic['AVJL'][nextState] += 1
        postsynaptic['AVJR'][nextState] += 1
        postsynaptic['AVL'][nextState] += 1
        postsynaptic['HSNL'][nextState] += 1
        postsynaptic['MVL11'][nextState] += 1
        postsynaptic['MVL12'][nextState] += 1
        postsynaptic['PDER'][nextState] += 1
        postsynaptic['PVNL'][nextState] += 2
        postsynaptic['PVQL'][nextState] += 1
        postsynaptic['PVQR'][nextState] += 2
        postsynaptic['VB1'][nextState] += 1

def AVFR():
        postsynaptic['ASJL'][nextState] += 1
        postsynaptic['ASKL'][nextState] += 1
        postsynaptic['AVBL'][nextState] += 1
        postsynaptic['AVBR'][nextState] += 5
        postsynaptic['AVFL'][nextState] += 24
        postsynaptic['AVHL'][nextState] += 4
        postsynaptic['AVHR'][nextState] += 2
        postsynaptic['AVJL'][nextState] += 1
        postsynaptic['AVJR'][nextState] += 1
        postsynaptic['HSNR'][nextState] += 1
        postsynaptic['MVL14'][nextState] += 2
        postsynaptic['MVR14'][nextState] += 2
        postsynaptic['PVQL'][nextState] += 1
        postsynaptic['VC4'][nextState] += 1
        postsynaptic['VD11'][nextState] += 1

def AVG():
        postsynaptic['AVAR'][nextState] += 3
        postsynaptic['AVBL'][nextState] += 1
        postsynaptic['AVBR'][nextState] += 2
        postsynaptic['AVDR'][nextState] += 1
        postsynaptic['AVEL'][nextState] += 1
        postsynaptic['AVER'][nextState] += 1
        postsynaptic['AVFL'][nextState] += 1
        postsynaptic['AVJL'][nextState] += 1
        postsynaptic['AVL'][nextState] += 1
        postsynaptic['DA8'][nextState] += 1
        postsynaptic['PHAL'][nextState] += 2
        postsynaptic['PVCL'][nextState] += 1
        postsynaptic['PVNR'][nextState] += 1
        postsynaptic['PVPR'][nextState] += 1
        postsynaptic['PVQR'][nextState] += 1
        postsynaptic['PVT'][nextState] += 1
        postsynaptic['RIFL'][nextState] += 1
        postsynaptic['RIFR'][nextState] += 1
        postsynaptic['VA11'][nextState] += 1

def AVHL():
        postsynaptic['ADFR'][nextState] += 3
        postsynaptic['AVBL'][nextState] += 1
        postsynaptic['AVBR'][nextState] += 1
        postsynaptic['AVDL'][nextState] += 1
        postsynaptic['AVFL'][nextState] += 1
        postsynaptic['AVFL'][nextState] += 2
        postsynaptic['AVFR'][nextState] += 5
        postsynaptic['AVHR'][nextState] += 2
        postsynaptic['AVJL'][nextState] += 1
        postsynaptic['AWBR'][nextState] += 1
        postsynaptic['PHBR'][nextState] += 1
        postsynaptic['PVPR'][nextState] += 2
        postsynaptic['PVQL'][nextState] += 1
        postsynaptic['PVQR'][nextState] += 2
        postsynaptic['RIMR'][nextState] += 1
        postsynaptic['RIR'][nextState] += 3
        postsynaptic['SMBDR'][nextState] += 1
        postsynaptic['SMBVR'][nextState] += 1
        postsynaptic['VD1'][nextState] += 1

def AVHR():
        postsynaptic['ADLL'][nextState] += 1
        postsynaptic['ADLR'][nextState] += 2
        postsynaptic['AQR'][nextState] += 2
        postsynaptic['AVBL'][nextState] += 2
        postsynaptic['AVBR'][nextState] += 1
        postsynaptic['AVDR'][nextState] += 1
        postsynaptic['AVFL'][nextState] += 1
        postsynaptic['AVFR'][nextState] += 2
        postsynaptic['AVHL'][nextState] += 2
        postsynaptic['AVJR'][nextState] += 4
        postsynaptic['PVNL'][nextState] += 1
        postsynaptic['PVPL'][nextState] += 3
        postsynaptic['RIGL'][nextState] += 1
        postsynaptic['RIR'][nextState] += 4
        postsynaptic['SMBDL'][nextState] += 1
        postsynaptic['SMBVL'][nextState] += 1

def AVJL():
        postsynaptic['AVAL'][nextState] += 2
        postsynaptic['AVAR'][nextState] += 1
        postsynaptic['AVBL'][nextState] += 1
        postsynaptic['AVBR'][nextState] += 4
        postsynaptic['AVDL'][nextState] += 1
        postsynaptic['AVDR'][nextState] += 2
        postsynaptic['AVEL'][nextState] += 1
        postsynaptic['AVFR'][nextState] += 1
        postsynaptic['AVHL'][nextState] += 2
        postsynaptic['AVJR'][nextState] += 4
        postsynaptic['HSNR'][nextState] += 1
        postsynaptic['PLMR'][nextState] += 2
        postsynaptic['PVCL'][nextState] += 2
        postsynaptic['PVCR'][nextState] += 5
        postsynaptic['PVNR'][nextState] += 1
        postsynaptic['RIFR'][nextState] += 1
        postsynaptic['RIS'][nextState] += 2

def AVJR():
        postsynaptic['AVAL'][nextState] += 1
        postsynaptic['AVAR'][nextState] += 1
        postsynaptic['AVBL'][nextState] += 3
        postsynaptic['AVBR'][nextState] += 1
        postsynaptic['AVDL'][nextState] += 1
        postsynaptic['AVDR'][nextState] += 3
        postsynaptic['AVER'][nextState] += 3
        postsynaptic['AVJL'][nextState] += 5
        postsynaptic['PVCL'][nextState] += 3
        postsynaptic['PVCR'][nextState] += 4
        postsynaptic['PVQR'][nextState] += 1
        postsynaptic['SABVL'][nextState] += 1

def AVKL():
        postsynaptic['ADER'][nextState] += 1
        postsynaptic['AQR'][nextState] += 2
        postsynaptic['AVBL'][nextState] += 1
        postsynaptic['AVEL'][nextState] += 2
        postsynaptic['AVER'][nextState] += 1
        postsynaptic['AVKR'][nextState] += 2
        postsynaptic['AVM'][nextState] += 1
        postsynaptic['DVA'][nextState] += 1
        postsynaptic['PDEL'][nextState] += 3
        postsynaptic['PDER'][nextState] += 1
        postsynaptic['PVM'][nextState] += 1
        postsynaptic['PVPL'][nextState] += 1
        postsynaptic['PVPR'][nextState] += 1
        postsynaptic['PVT'][nextState] += 2
        postsynaptic['RICL'][nextState] += 1
        postsynaptic['RICR'][nextState] += 1
        postsynaptic['RIGL'][nextState] += 1
        postsynaptic['RIML'][nextState] += 2
        postsynaptic['RIMR'][nextState] += 1
        postsynaptic['RMFR'][nextState] += 1
        postsynaptic['SAADR'][nextState] += 1
        postsynaptic['SIAVR'][nextState] += 1
        postsynaptic['SMBDL'][nextState] += 1
        postsynaptic['SMBDR'][nextState] += 1
        postsynaptic['SMBVR'][nextState] += 1
        postsynaptic['SMDDR'][nextState] += 1
        postsynaptic['VB1'][nextState] += 4
        postsynaptic['VB10'][nextState] += 1

def AVKR():
        postsynaptic['ADEL'][nextState] += 1
        postsynaptic['AQR'][nextState] += 1
        postsynaptic['AVKL'][nextState] += 2
        postsynaptic['BDUL'][nextState] += 1
        postsynaptic['MVL10'][nextState] += 1
        postsynaptic['PVPL'][nextState] += 6
        postsynaptic['PVQL'][nextState] += 1
        postsynaptic['RICL'][nextState] += 1
        postsynaptic['RIGR'][nextState] += 1
        postsynaptic['RIML'][nextState] += 2
        postsynaptic['RIMR'][nextState] += 2
        postsynaptic['RMDR'][nextState] += 1
        postsynaptic['RMFL'][nextState] += 1
        postsynaptic['SAADL'][nextState] += 1
        postsynaptic['SMBDL'][nextState] += 2
        postsynaptic['SMBDR'][nextState] += 2
        postsynaptic['SMBVR'][nextState] += 1
        postsynaptic['SMDDL'][nextState] += 1
        postsynaptic['SMDDR'][nextState] += 2

def AVL():
        postsynaptic['AVEL'][nextState] += 1
        postsynaptic['AVFR'][nextState] += 1
        postsynaptic['DA2'][nextState] += 1
        postsynaptic['DD1'][nextState] += 1
        postsynaptic['DD6'][nextState] += 2
        postsynaptic['DVB'][nextState] += 1
        postsynaptic['DVC'][nextState] += 9
        postsynaptic['HSNR'][nextState] += 1
        postsynaptic['MVL10'][nextState] += -5
        postsynaptic['MVR10'][nextState] += -5
        postsynaptic['PVM'][nextState] += 1
        postsynaptic['PVPR'][nextState] += 1
        postsynaptic['PVWL'][nextState] += 1
        postsynaptic['SABD'][nextState] += 5
        postsynaptic['SABVL'][nextState] += 4
        postsynaptic['SABVR'][nextState] += 3
        postsynaptic['VD12'][nextState] += 4

def AVM():
        postsynaptic['ADER'][nextState] += 1
        postsynaptic['ALML'][nextState] += 1
        postsynaptic['ALMR'][nextState] += 1
        postsynaptic['AVBL'][nextState] += 6
        postsynaptic['AVBR'][nextState] += 6
        postsynaptic['AVDL'][nextState] += 2
        postsynaptic['AVJR'][nextState] += 1
        postsynaptic['BDUL'][nextState] += 3
        postsynaptic['BDUR'][nextState] += 2
        postsynaptic['DA1'][nextState] += 1
        postsynaptic['PVCL'][nextState] += 4
        postsynaptic['PVCR'][nextState] += 5
        postsynaptic['PVNL'][nextState] += 1
        postsynaptic['PVR'][nextState] += 3
        postsynaptic['RID'][nextState] += 1
        postsynaptic['SIBVL'][nextState] += 1
        postsynaptic['VA1'][nextState] += 2

def AWAL():
        postsynaptic['ADAL'][nextState] += 1
        postsynaptic['AFDL'][nextState] += 5
        postsynaptic['AIAL'][nextState] += 1
        postsynaptic['AIYL'][nextState] += 1
        postsynaptic['AIZL'][nextState] += 10
        postsynaptic['ASEL'][nextState] += 4
        postsynaptic['ASGL'][nextState] += 1
        postsynaptic['AWAR'][nextState] += 1
        postsynaptic['AWBL'][nextState] += 1

def AWAR():
        postsynaptic['ADFR'][nextState] += 3
        postsynaptic['AFDR'][nextState] += 7
        postsynaptic['AIAR'][nextState] += 1
        postsynaptic['AIYR'][nextState] += 2
        postsynaptic['AIZR'][nextState] += 7
        postsynaptic['AIZR'][nextState] += 1
        postsynaptic['ASEL'][nextState] += 1
        postsynaptic['ASER'][nextState] += 2
        postsynaptic['AUAR'][nextState] += 1
        postsynaptic['AWAL'][nextState] += 1
        postsynaptic['AWBR'][nextState] += 1
        postsynaptic['RIFR'][nextState] += 2
        postsynaptic['RIGR'][nextState] += 1
        postsynaptic['RIR'][nextState] += 2

def AWBL():
        postsynaptic['ADFL'][nextState] += 9
        postsynaptic['AIBR'][nextState] += 1
        postsynaptic['AIZL'][nextState] += 9
        postsynaptic['AUAL'][nextState] += 1
        postsynaptic['AVBL'][nextState] += 1
        postsynaptic['AWBR'][nextState] += 1
        postsynaptic['RIAL'][nextState] += 3
        postsynaptic['RMGL'][nextState] += 1
        postsynaptic['SMBDL'][nextState] += 1

def AWBR():
        postsynaptic['ADFR'][nextState] += 4
        postsynaptic['AIZR'][nextState] += 4
        postsynaptic['ASGR'][nextState] += 1
        postsynaptic['ASHR'][nextState] += 2
        postsynaptic['AUAR'][nextState] += 1
        postsynaptic['AVBR'][nextState] += 2
        postsynaptic['AWBL'][nextState] += 1
        postsynaptic['RIAR'][nextState] += 1
        postsynaptic['RICL'][nextState] += 1
        postsynaptic['RIR'][nextState] += 2
        postsynaptic['RMGR'][nextState] += 1
        postsynaptic['SMBVR'][nextState] += 1

def AWCL():
        postsynaptic['AIAL'][nextState] += 2
        postsynaptic['AIAR'][nextState] += 4
        postsynaptic['AIBL'][nextState] += 1
        postsynaptic['AIBR'][nextState] += 1
        postsynaptic['AIYL'][nextState] += 10
        postsynaptic['ASEL'][nextState] += 1
        postsynaptic['AVAL'][nextState] += 1
        postsynaptic['AWCR'][nextState] += 1
        postsynaptic['RIAL'][nextState] += 3

def AWCR():
        postsynaptic['AIAR'][nextState] += 1
        postsynaptic['AIBR'][nextState] += 4
        postsynaptic['AIYL'][nextState] += 4
        postsynaptic['AIYR'][nextState] += 9
        postsynaptic['ASEL'][nextState] += 1
        postsynaptic['ASGR'][nextState] += 1
        postsynaptic['AWCL'][nextState] += 5

def BAGL():
        postsynaptic['AIBL'][nextState] += 1
        postsynaptic['AVAR'][nextState] += 1
        postsynaptic['AVEL'][nextState] += 1
        postsynaptic['AVER'][nextState] += 4
        postsynaptic['BAGR'][nextState] += 2
        postsynaptic['RIAR'][nextState] += 5
        postsynaptic['RIBL'][nextState] += 1
        postsynaptic['RIBR'][nextState] += 7
        postsynaptic['RIGL'][nextState] += 1
        postsynaptic['RIGR'][nextState] += 4
        postsynaptic['RIGR'][nextState] += 1
        postsynaptic['RIR'][nextState] += 1

def BAGR():
        postsynaptic['AIYL'][nextState] += 1
        postsynaptic['AVAL'][nextState] += 1
        postsynaptic['AVEL'][nextState] += 2
        postsynaptic['BAGL'][nextState] += 1
        postsynaptic['RIAL'][nextState] += 5
        postsynaptic['RIBL'][nextState] += 4
        postsynaptic['RIGL'][nextState] += 5
        postsynaptic['RIGL'][nextState] += 1
        postsynaptic['RIR'][nextState] += 1

def BDUL():
        postsynaptic['ADEL'][nextState] += 3
        postsynaptic['AVHL'][nextState] += 1
        postsynaptic['AVJR'][nextState] += 1
        postsynaptic['HSNL'][nextState] += 1
        postsynaptic['PVNL'][nextState] += 2
        postsynaptic['PVNR'][nextState] += 2
        postsynaptic['SAADL'][nextState] += 1
        postsynaptic['URADL'][nextState] += 1

def BDUR():
        postsynaptic['ADER'][nextState] += 1
        postsynaptic['ALMR'][nextState] += 1
        postsynaptic['AVAL'][nextState] += 3
        postsynaptic['AVHL'][nextState] += 1
        postsynaptic['AVJL'][nextState] += 2
        postsynaptic['HSNR'][nextState] += 4
        postsynaptic['PVCL'][nextState] += 1
        postsynaptic['PVNL'][nextState] += 2
        postsynaptic['PVNR'][nextState] += 1
        postsynaptic['SDQL'][nextState] += 1
        postsynaptic['URADR'][nextState] += 1

def CEPDL():
        postsynaptic['AVER'][nextState] += 5
        postsynaptic['IL1DL'][nextState] += 4
        postsynaptic['OLLL'][nextState] += 2
        postsynaptic['OLQDL'][nextState] += 6
        postsynaptic['OLQDL'][nextState] += 1
        postsynaptic['RIBL'][nextState] += 2
        postsynaptic['RICL'][nextState] += 1
        postsynaptic['RICR'][nextState] += 2
        postsynaptic['RIH'][nextState] += 1
        postsynaptic['RIPL'][nextState] += 2
        postsynaptic['RIS'][nextState] += 1
        postsynaptic['RMDVL'][nextState] += 3
        postsynaptic['RMGL'][nextState] += 4
        postsynaptic['RMHR'][nextState] += 4
        postsynaptic['SIADR'][nextState] += 1
        postsynaptic['SMBDR'][nextState] += 1
        postsynaptic['URADL'][nextState] += 2
        postsynaptic['URBL'][nextState] += 4
        postsynaptic['URYDL'][nextState] += 2

def CEPDR():
        postsynaptic['AVEL'][nextState] += 6
        postsynaptic['BDUR'][nextState] += 1
        postsynaptic['IL1DR'][nextState] += 5
        postsynaptic['IL1R'][nextState] += 1
        postsynaptic['OLLR'][nextState] += 8
        postsynaptic['OLQDR'][nextState] += 5
        postsynaptic['OLQDR'][nextState] += 2
        postsynaptic['RIBR'][nextState] += 1
        postsynaptic['RICL'][nextState] += 4
        postsynaptic['RICR'][nextState] += 3
        postsynaptic['RIH'][nextState] += 1
        postsynaptic['RIS'][nextState] += 1
        postsynaptic['RMDDL'][nextState] += 1
        postsynaptic['RMDVR'][nextState] += 2
        postsynaptic['RMGR'][nextState] += 1
        postsynaptic['RMHL'][nextState] += 4
        postsynaptic['RMHR'][nextState] += 1
        postsynaptic['SIADL'][nextState] += 1
        postsynaptic['SMBDR'][nextState] += 1
        postsynaptic['URADR'][nextState] += 1
        postsynaptic['URBR'][nextState] += 2
        postsynaptic['URYDR'][nextState] += 1

def CEPVL():
        postsynaptic['ADLL'][nextState] += 1
        postsynaptic['AVER'][nextState] += 3
        postsynaptic['IL1VL'][nextState] += 2
        postsynaptic['MVL03'][nextState] += 1
        postsynaptic['OLLL'][nextState] += 4
        postsynaptic['OLQVL'][nextState] += 6
        postsynaptic['OLQVL'][nextState] += 1
        postsynaptic['RICL'][nextState] += 7
        postsynaptic['RICR'][nextState] += 4
        postsynaptic['RIH'][nextState] += 1
        postsynaptic['RIPL'][nextState] += 1
        postsynaptic['RMDDL'][nextState] += 4
        postsynaptic['RMHL'][nextState] += 1
        postsynaptic['SIAVL'][nextState] += 1
        postsynaptic['URAVL'][nextState] += 2

def CEPVR():
        postsynaptic['ASGR'][nextState] += 1
        postsynaptic['AVEL'][nextState] += 5
        postsynaptic['IL1VR'][nextState] += 1
        postsynaptic['IL2VR'][nextState] += 2
        postsynaptic['MVR04'][nextState] += 1
        postsynaptic['OLLR'][nextState] += 7
        postsynaptic['OLQVR'][nextState] += 3
        postsynaptic['OLQVR'][nextState] += 1
        postsynaptic['RICL'][nextState] += 2
        postsynaptic['RICR'][nextState] += 2
        postsynaptic['RIH'][nextState] += 1
        postsynaptic['RIPR'][nextState] += 1
        postsynaptic['RIVL'][nextState] += 1
        postsynaptic['RMDDR'][nextState] += 2
        postsynaptic['RMHR'][nextState] += 2
        postsynaptic['SIAVR'][nextState] += 2
        postsynaptic['URAVR'][nextState] += 1

def DA1():
        postsynaptic['AVAL'][nextState] += 2
        postsynaptic['AVAR'][nextState] += 6
        postsynaptic['DA4'][nextState] += 1
        postsynaptic['DD1'][nextState] += 4
        postsynaptic['MDL08'][nextState] += 8
        postsynaptic['MDR08'][nextState] += 8
        postsynaptic['SABVL'][nextState] += 2
        postsynaptic['SABVR'][nextState] += 3
        postsynaptic['VD1'][nextState] += 17
        postsynaptic['VD2'][nextState] += 1

def DA2():
        postsynaptic['AS2'][nextState] += 2
        postsynaptic['AS3'][nextState] += 1
        postsynaptic['AVAL'][nextState] += 2
        postsynaptic['AVAR'][nextState] += 2
        postsynaptic['DD1'][nextState] += 1
        postsynaptic['MDL07'][nextState] += 2
        postsynaptic['MDL08'][nextState] += 1
        postsynaptic['MDL09'][nextState] += 2
        postsynaptic['MDL10'][nextState] += 2
        postsynaptic['MDR07'][nextState] += 2
        postsynaptic['MDR08'][nextState] += 2
        postsynaptic['MDR09'][nextState] += 2
        postsynaptic['MDR10'][nextState] += 2
        postsynaptic['SABVL'][nextState] += 1
        postsynaptic['VA1'][nextState] += 2
        postsynaptic['VD1'][nextState] += 2
        postsynaptic['VD2'][nextState] += 11
        postsynaptic['VD3'][nextState] += 5

def DA3():
        postsynaptic['AS4'][nextState] += 2
        postsynaptic['AVAR'][nextState] += 2
        postsynaptic['DA4'][nextState] += 2
        postsynaptic['DB3'][nextState] += 1
        postsynaptic['DD2'][nextState] += 1
        postsynaptic['MDL09'][nextState] += 5
        postsynaptic['MDL10'][nextState] += 5
        postsynaptic['MDL12'][nextState] += 5
        postsynaptic['MDR09'][nextState] += 5
        postsynaptic['MDR10'][nextState] += 5
        postsynaptic['MDR12'][nextState] += 5
        postsynaptic['VD3'][nextState] += 25
        postsynaptic['VD4'][nextState] += 6

def DA4():
        postsynaptic['AVAL'][nextState] += 3
        postsynaptic['AVAR'][nextState] += 2
        postsynaptic['DA1'][nextState] += 1
        postsynaptic['DA3'][nextState] += 1
        postsynaptic['DB3'][nextState] += 2
        postsynaptic['DD2'][nextState] += 1
        postsynaptic['MDL11'][nextState] += 4
        postsynaptic['MDL12'][nextState] += 4
        postsynaptic['MDL14'][nextState] += 5
        postsynaptic['MDR11'][nextState] += 4
        postsynaptic['MDR12'][nextState] += 4
        postsynaptic['MDR14'][nextState] += 5
        postsynaptic['VB6'][nextState] += 1
        postsynaptic['VD4'][nextState] += 12
        postsynaptic['VD5'][nextState] += 15

def DA5():
        postsynaptic['AS6'][nextState] += 2
        postsynaptic['AVAL'][nextState] += 1
        postsynaptic['AVAR'][nextState] += 5
        postsynaptic['DB4'][nextState] += 1
        postsynaptic['MDL13'][nextState] += 5
        postsynaptic['MDL14'][nextState] += 4
        postsynaptic['MDR13'][nextState] += 5
        postsynaptic['MDR14'][nextState] += 4
        postsynaptic['VA4'][nextState] += 1
        postsynaptic['VA5'][nextState] += 2
        postsynaptic['VD5'][nextState] += 1
        postsynaptic['VD6'][nextState] += 16

def DA6():
        postsynaptic['AVAL'][nextState] += 10
        postsynaptic['AVAR'][nextState] += 2
        postsynaptic['MDL11'][nextState] += 6
        postsynaptic['MDL12'][nextState] += 4
        postsynaptic['MDL13'][nextState] += 4
        postsynaptic['MDL14'][nextState] += 4
        postsynaptic['MDL16'][nextState] += 4
        postsynaptic['MDR11'][nextState] += 4
        postsynaptic['MDR12'][nextState] += 4
        postsynaptic['MDR13'][nextState] += 4
        postsynaptic['MDR14'][nextState] += 4
        postsynaptic['MDR16'][nextState] += 4
        postsynaptic['VD4'][nextState] += 4
        postsynaptic['VD5'][nextState] += 3
        postsynaptic['VD6'][nextState] += 3

def DA7():
        postsynaptic['AVAL'][nextState] += 2
        postsynaptic['MDL15'][nextState] += 4
        postsynaptic['MDL17'][nextState] += 4
        postsynaptic['MDL18'][nextState] += 4
        postsynaptic['MDR15'][nextState] += 4
        postsynaptic['MDR17'][nextState] += 4
        postsynaptic['MDR18'][nextState] += 4

def DA8():
        postsynaptic['AVAR'][nextState] += 1
        postsynaptic['DA9'][nextState] += 1
        postsynaptic['MDL17'][nextState] += 4
        postsynaptic['MDL19'][nextState] += 4
        postsynaptic['MDL20'][nextState] += 4
        postsynaptic['MDR17'][nextState] += 4
        postsynaptic['MDR19'][nextState] += 4
        postsynaptic['MDR20'][nextState] += 4

def DA9():
        postsynaptic['DA8'][nextState] += 1
        postsynaptic['DD6'][nextState] += 1
        postsynaptic['MDL19'][nextState] += 4
        postsynaptic['MDL21'][nextState] += 4
        postsynaptic['MDL22'][nextState] += 4
        postsynaptic['MDL23'][nextState] += 4
        postsynaptic['MDL24'][nextState] += 4
        postsynaptic['MDR19'][nextState] += 4
        postsynaptic['MDR21'][nextState] += 4
        postsynaptic['MDR22'][nextState] += 4
        postsynaptic['MDR23'][nextState] += 4
        postsynaptic['MDR24'][nextState] += 4
        postsynaptic['PDA'][nextState] += 1
        postsynaptic['PHCL'][nextState] += 1
        postsynaptic['RID'][nextState] += 1
        postsynaptic['VD13'][nextState] += 1

def DB1():
        postsynaptic['AIBR'][nextState] += 1
        postsynaptic['AS1'][nextState] += 1
        postsynaptic['AS2'][nextState] += 1
        postsynaptic['AS3'][nextState] += 1
        postsynaptic['AVBR'][nextState] += 3
        postsynaptic['DB2'][nextState] += 1
        postsynaptic['DB4'][nextState] += 1
        postsynaptic['DD1'][nextState] += 10
        postsynaptic['DVA'][nextState] += 1
        postsynaptic['MDL07'][nextState] += 1
        postsynaptic['MDL08'][nextState] += 1
        postsynaptic['MDR07'][nextState] += 1
        postsynaptic['MDR08'][nextState] += 1
        postsynaptic['RID'][nextState] += 1
        postsynaptic['RIS'][nextState] += 1
        postsynaptic['VB3'][nextState] += 1
        postsynaptic['VB4'][nextState] += 1
        postsynaptic['VD1'][nextState] += 21
        postsynaptic['VD2'][nextState] += 15
        postsynaptic['VD3'][nextState] += 1

def DB2():
        postsynaptic['AVBR'][nextState] += 1
        postsynaptic['DA3'][nextState] += 5
        postsynaptic['DB1'][nextState] += 1
        postsynaptic['DB3'][nextState] += 6
        postsynaptic['DD2'][nextState] += 3
        postsynaptic['MDL09'][nextState] += 3
        postsynaptic['MDL10'][nextState] += 3
        postsynaptic['MDL11'][nextState] += 3
        postsynaptic['MDL12'][nextState] += 3
        postsynaptic['MDR09'][nextState] += 3
        postsynaptic['MDR10'][nextState] += 3
        postsynaptic['MDR11'][nextState] += 3
        postsynaptic['MDR12'][nextState] += 3
        postsynaptic['VB1'][nextState] += 2
        postsynaptic['VD3'][nextState] += 23
        postsynaptic['VD4'][nextState] += 14
        postsynaptic['VD5'][nextState] += 1

def DB3():
        postsynaptic['AS4'][nextState] += 1
        postsynaptic['AS5'][nextState] += 1
        postsynaptic['AVBL'][nextState] += 1
        postsynaptic['AVBR'][nextState] += 1
        postsynaptic['DA4'][nextState] += 1
        postsynaptic['DB2'][nextState] += 6
        postsynaptic['DB4'][nextState] += 1
        postsynaptic['DD2'][nextState] += 4
        postsynaptic['DD3'][nextState] += 10
        postsynaptic['MDL11'][nextState] += 3
        postsynaptic['MDL12'][nextState] += 3
        postsynaptic['MDL13'][nextState] += 4
        postsynaptic['MDL14'][nextState] += 3
        postsynaptic['MDR11'][nextState] += 3
        postsynaptic['MDR12'][nextState] += 3
        postsynaptic['MDR13'][nextState] += 4
        postsynaptic['MDR14'][nextState] += 3
        postsynaptic['VD4'][nextState] += 9
        postsynaptic['VD5'][nextState] += 26
        postsynaptic['VD6'][nextState] += 7

def DB4():
        postsynaptic['AVBL'][nextState] += 1
        postsynaptic['AVBR'][nextState] += 1
        postsynaptic['DB1'][nextState] += 1
        postsynaptic['DB3'][nextState] += 1
        postsynaptic['DD3'][nextState] += 3
        postsynaptic['MDL13'][nextState] += 2
        postsynaptic['MDL14'][nextState] += 2
        postsynaptic['MDL16'][nextState] += 2
        postsynaptic['MDR13'][nextState] += 2
        postsynaptic['MDR14'][nextState] += 2
        postsynaptic['MDR16'][nextState] += 2
        postsynaptic['VB2'][nextState] += 1
        postsynaptic['VB4'][nextState] += 1
        postsynaptic['VD6'][nextState] += 13

def DB5():
        postsynaptic['AVAR'][nextState] += 2
        postsynaptic['AVBL'][nextState] += 1
        postsynaptic['AVBR'][nextState] += 1
        postsynaptic['MDL15'][nextState] += 2
        postsynaptic['MDL17'][nextState] += 2
        postsynaptic['MDL18'][nextState] += 2
        postsynaptic['MDR15'][nextState] += 2
        postsynaptic['MDR17'][nextState] += 2
        postsynaptic['MDR18'][nextState] += 2

def DB6():
        postsynaptic['AVAL'][nextState] += 3
        postsynaptic['AVBL'][nextState] += 2
        postsynaptic['AVBR'][nextState] += 1
        postsynaptic['MDL17'][nextState] += 2
        postsynaptic['MDL19'][nextState] += 2
        postsynaptic['MDL20'][nextState] += 2
        postsynaptic['MDR17'][nextState] += 2
        postsynaptic['MDR19'][nextState] += 2
        postsynaptic['MDR20'][nextState] += 2

def DB7():
        postsynaptic['AVBL'][nextState] += 2
        postsynaptic['AVBR'][nextState] += 1
        postsynaptic['MDL19'][nextState] += 2
        postsynaptic['MDL21'][nextState] += 2
        postsynaptic['MDL22'][nextState] += 2
        postsynaptic['MDL23'][nextState] += 2
        postsynaptic['MDL24'][nextState] += 2
        postsynaptic['MDR19'][nextState] += 2
        postsynaptic['MDR21'][nextState] += 2
        postsynaptic['MDR22'][nextState] += 2
        postsynaptic['MDR23'][nextState] += 2
        postsynaptic['MDR24'][nextState] += 2
        postsynaptic['VD13'][nextState] += 2

def DD1():
        postsynaptic['AVBR'][nextState] += 1
        postsynaptic['DD2'][nextState] += 3
        postsynaptic['MDL07'][nextState] += -6
        postsynaptic['MDL08'][nextState] += -6
        postsynaptic['MDL09'][nextState] += -7
        postsynaptic['MDL10'][nextState] += -6
        postsynaptic['MDR07'][nextState] += -6
        postsynaptic['MDR08'][nextState] += -6
        postsynaptic['MDR09'][nextState] += -7
        postsynaptic['MDR10'][nextState] += -6
        postsynaptic['VD1'][nextState] += 4
        postsynaptic['VD2'][nextState] += 1
        postsynaptic['VD2'][nextState] += 2

def DD2():
        postsynaptic['DA3'][nextState] += 1
        postsynaptic['DD1'][nextState] += 1
        postsynaptic['DD3'][nextState] += 2
        postsynaptic['MDL09'][nextState] += -6
        postsynaptic['MDL11'][nextState] += -7
        postsynaptic['MDL12'][nextState] += -6
        postsynaptic['MDR09'][nextState] += -6
        postsynaptic['MDR11'][nextState] += -7
        postsynaptic['MDR12'][nextState] += -6
        postsynaptic['VD3'][nextState] += 1
        postsynaptic['VD4'][nextState] += 3

def DD3():
        postsynaptic['DD2'][nextState] += 2
        postsynaptic['DD4'][nextState] += 1
        postsynaptic['MDL11'][nextState] += -7
        postsynaptic['MDL13'][nextState] += -9
        postsynaptic['MDL14'][nextState] += -7
        postsynaptic['MDR11'][nextState] += -7
        postsynaptic['MDR13'][nextState] += -9
        postsynaptic['MDR14'][nextState] += -7

def DD4():
        postsynaptic['DD3'][nextState] += 1
        postsynaptic['MDL13'][nextState] += -7
        postsynaptic['MDL15'][nextState] += -7
        postsynaptic['MDL16'][nextState] += -7
        postsynaptic['MDR13'][nextState] += -7
        postsynaptic['MDR15'][nextState] += -7
        postsynaptic['MDR16'][nextState] += -7
        postsynaptic['VC3'][nextState] += 1
        postsynaptic['VD8'][nextState] += 1

def DD5():
        postsynaptic['MDL17'][nextState] += -7
        postsynaptic['MDL18'][nextState] += -7
        postsynaptic['MDL20'][nextState] += -7
        postsynaptic['MDR17'][nextState] += -7
        postsynaptic['MDR18'][nextState] += -7
        postsynaptic['MDR20'][nextState] += -7
        postsynaptic['VB8'][nextState] += 1
        postsynaptic['VD10'][nextState] += 1
        postsynaptic['VD9'][nextState] += 1

def DD6():
        postsynaptic['MDL19'][nextState] += -7
        postsynaptic['MDL21'][nextState] += -7
        postsynaptic['MDL22'][nextState] += -7
        postsynaptic['MDL23'][nextState] += -7
        postsynaptic['MDL24'][nextState] += -7
        postsynaptic['MDR19'][nextState] += -7
        postsynaptic['MDR21'][nextState] += -7
        postsynaptic['MDR22'][nextState] += -7
        postsynaptic['MDR23'][nextState] += -7
        postsynaptic['MDR24'][nextState] += -7

def DVA():
        postsynaptic['AIZL'][nextState] += 3
        postsynaptic['AQR'][nextState] += 4
        postsynaptic['AUAL'][nextState] += 1
        postsynaptic['AUAR'][nextState] += 1
        postsynaptic['AVAL'][nextState] += 3
        postsynaptic['AVAR'][nextState] += 1
        postsynaptic['AVBL'][nextState] += 2
        postsynaptic['AVBR'][nextState] += 1
        postsynaptic['AVEL'][nextState] += 9
        postsynaptic['AVER'][nextState] += 5
        postsynaptic['DB1'][nextState] += 1
        postsynaptic['DB2'][nextState] += 1
        postsynaptic['DB3'][nextState] += 2
        postsynaptic['DB4'][nextState] += 1
        postsynaptic['DB5'][nextState] += 1
        postsynaptic['DB6'][nextState] += 2
        postsynaptic['DB7'][nextState] += 1
        postsynaptic['PDEL'][nextState] += 3
        postsynaptic['PVCL'][nextState] += 3
        postsynaptic['PVCL'][nextState] += 1
        postsynaptic['PVCR'][nextState] += 1
        postsynaptic['PVR'][nextState] += 3
        postsynaptic['PVR'][nextState] += 2
        postsynaptic['RIAL'][nextState] += 1
        postsynaptic['RIAR'][nextState] += 1
        postsynaptic['RIMR'][nextState] += 1
        postsynaptic['RIR'][nextState] += 3
        postsynaptic['SAADR'][nextState] += 1
        postsynaptic['SAAVL'][nextState] += 1
        postsynaptic['SAAVR'][nextState] += 1
        postsynaptic['SABD'][nextState] += 1
        postsynaptic['SMBDL'][nextState] += 3
        postsynaptic['SMBDR'][nextState] += 2
        postsynaptic['SMBVL'][nextState] += 3
        postsynaptic['SMBVR'][nextState] += 2
        postsynaptic['VA12'][nextState] += 1
        postsynaptic['VA2'][nextState] += 1
        postsynaptic['VB1'][nextState] += 1
        postsynaptic['VB11'][nextState] += 2

def DVB():
        postsynaptic['AS9'][nextState] += 7
        postsynaptic['AVL'][nextState] += 5
        postsynaptic['AVL'][nextState] += 1
        postsynaptic['DA8'][nextState] += 2
        postsynaptic['DD6'][nextState] += 3
        postsynaptic['DVC'][nextState] += 3
        # postsynaptic['MANAL'][nextState] += -5 - just not needed or used
        postsynaptic['PDA'][nextState] += 1
        postsynaptic['PHCL'][nextState] += 1
        postsynaptic['PVPL'][nextState] += 1
        postsynaptic['VA9'][nextState] += 1
        postsynaptic['VB9'][nextState] += 1

def DVC():
        postsynaptic['AIBL'][nextState] += 2
        postsynaptic['AIBR'][nextState] += 5
        postsynaptic['AVAL'][nextState] += 5
        postsynaptic['AVAR'][nextState] += 7
        postsynaptic['AVBL'][nextState] += 1
        postsynaptic['AVKL'][nextState] += 2
        postsynaptic['AVKR'][nextState] += 1
        postsynaptic['AVL'][nextState] += 9
        postsynaptic['PVPL'][nextState] += 2
        postsynaptic['PVPR'][nextState] += 13
        postsynaptic['PVT'][nextState] += 1
        postsynaptic['RIBL'][nextState] += 1
        postsynaptic['RIBR'][nextState] += 1
        postsynaptic['RIGL'][nextState] += 5
        postsynaptic['RIGR'][nextState] += 5
        postsynaptic['RMFL'][nextState] += 2
        postsynaptic['RMFR'][nextState] += 4
        postsynaptic['VA9'][nextState] += 1
        postsynaptic['VD1'][nextState] += 5
        postsynaptic['VD10'][nextState] += 4

def FLPL():
        postsynaptic['ADEL'][nextState] += 2
        postsynaptic['ADER'][nextState] += 2
        postsynaptic['AIBL'][nextState] += 1
        postsynaptic['AIBR'][nextState] += 2
        postsynaptic['AVAL'][nextState] += 15
        postsynaptic['AVAR'][nextState] += 17
        postsynaptic['AVBL'][nextState] += 4
        postsynaptic['AVBR'][nextState] += 5
        postsynaptic['AVDL'][nextState] += 7
        postsynaptic['AVDR'][nextState] += 13
        postsynaptic['DVA'][nextState] += 1
        postsynaptic['FLPR'][nextState] += 3
        postsynaptic['RIH'][nextState] += 1

def FLPR():
        postsynaptic['ADER'][nextState] += 1
        postsynaptic['AIBR'][nextState] += 1
        postsynaptic['AVAL'][nextState] += 12
        postsynaptic['AVAR'][nextState] += 5
        postsynaptic['AVBL'][nextState] += 5
        postsynaptic['AVBR'][nextState] += 1
        postsynaptic['AVDL'][nextState] += 10
        postsynaptic['AVDL'][nextState] += 1
        postsynaptic['AVDR'][nextState] += 2
        postsynaptic['AVEL'][nextState] += 4
        postsynaptic['AVER'][nextState] += 2
        postsynaptic['AVJR'][nextState] += 1
        postsynaptic['DVA'][nextState] += 1
        postsynaptic['FLPL'][nextState] += 4
        postsynaptic['PVCL'][nextState] += 2
        postsynaptic['VB1'][nextState] += 1

def HSNL():
        postsynaptic['AIAL'][nextState] += 1
        postsynaptic['AIZL'][nextState] += 2
        postsynaptic['AIZR'][nextState] += 1
        postsynaptic['ASHL'][nextState] += 1
        postsynaptic['ASHR'][nextState] += 2
        postsynaptic['ASJR'][nextState] += 1
        postsynaptic['ASKL'][nextState] += 1
        postsynaptic['AVDR'][nextState] += 2
        postsynaptic['AVFL'][nextState] += 6
        postsynaptic['AVJL'][nextState] += 1
        postsynaptic['AWBL'][nextState] += 1
        postsynaptic['AWBR'][nextState] += 2
        postsynaptic['HSNR'][nextState] += 3
        postsynaptic['HSNR'][nextState] += 1
        postsynaptic['MVULVA'][nextState] += 7
        postsynaptic['RIFL'][nextState] += 3
        postsynaptic['RIML'][nextState] += 2
        postsynaptic['SABVL'][nextState] += 2
        postsynaptic['VC5'][nextState] += 3

def HSNR():
        postsynaptic['AIBL'][nextState] += 1
        postsynaptic['AIBR'][nextState] += 1
        postsynaptic['AIZL'][nextState] += 1
        postsynaptic['AIZR'][nextState] += 1
        postsynaptic['AS5'][nextState] += 1
        postsynaptic['ASHL'][nextState] += 2
        postsynaptic['AVDR'][nextState] += 1
        postsynaptic['AVFL'][nextState] += 1
        postsynaptic['AVJL'][nextState] += 1
        postsynaptic['AVL'][nextState] += 1
        postsynaptic['AWBL'][nextState] += 1
        postsynaptic['BDUR'][nextState] += 1
        postsynaptic['DA5'][nextState] += 1
        postsynaptic['DA6'][nextState] += 1
        postsynaptic['HSNL'][nextState] += 2
        postsynaptic['MVULVA'][nextState] += 6
        postsynaptic['PVNR'][nextState] += 2
        postsynaptic['PVQR'][nextState] += 1
        postsynaptic['RIFR'][nextState] += 4
        postsynaptic['RMGR'][nextState] += 1
        postsynaptic['SABD'][nextState] += 1
        postsynaptic['SABVR'][nextState] += 1
        postsynaptic['VA6'][nextState] += 1
        postsynaptic['VC2'][nextState] += 3
        postsynaptic['VC3'][nextState] += 1
        postsynaptic['VD4'][nextState] += 2

def I1L():
        postsynaptic['I1R'][nextState] += 1
        postsynaptic['I3'][nextState] += 1
        postsynaptic['I5'][nextState] += 1
        postsynaptic['RIPL'][nextState] += 1
        postsynaptic['RIPR'][nextState] += 1

def I1R():
        postsynaptic['I1L'][nextState] += 1
        postsynaptic['I3'][nextState] += 1
        postsynaptic['I5'][nextState] += 1
        postsynaptic['RIPL'][nextState] += 1
        postsynaptic['RIPR'][nextState] += 1

def I2L():
        postsynaptic['I1L'][nextState] += 1
        postsynaptic['I1R'][nextState] += 1
        postsynaptic['M1'][nextState] += 4

def I2R():
        postsynaptic['I1L'][nextState] += 1
        postsynaptic['I1R'][nextState] += 1
        postsynaptic['M1'][nextState] += 4

def I3():
        postsynaptic['M1'][nextState] += 4
        postsynaptic['M2L'][nextState] += 2
        postsynaptic['M2R'][nextState] += 2

def I4():
        postsynaptic['I2L'][nextState] += 5
        postsynaptic['I2R'][nextState] += 5
        postsynaptic['I5'][nextState] += 2
        postsynaptic['M1'][nextState] += 4

def I5():
        postsynaptic['I1L'][nextState] += 4
        postsynaptic['I1R'][nextState] += 3
        postsynaptic['M1'][nextState] += 2
        postsynaptic['M5'][nextState] += 2
        postsynaptic['MI'][nextState] += 4

def I6():
        postsynaptic['I2L'][nextState] += 2
        postsynaptic['I2R'][nextState] += 2
        postsynaptic['I3'][nextState] += 1
        postsynaptic['M4'][nextState] += 1
        postsynaptic['M5'][nextState] += 2
        postsynaptic['NSML'][nextState] += 2
        postsynaptic['NSMR'][nextState] += 2

def IL1DL():
        postsynaptic['IL1DR'][nextState] += 1
        postsynaptic['IL1L'][nextState] += 1
        postsynaptic['MDL01'][nextState] += 1
        postsynaptic['MDL02'][nextState] += 1
        postsynaptic['MDL04'][nextState] += 2
        postsynaptic['OLLL'][nextState] += 1
        postsynaptic['PVR'][nextState] += 1
        postsynaptic['RIH'][nextState] += 1
        postsynaptic['RIPL'][nextState] += 2
        postsynaptic['RMDDR'][nextState] += 1
        postsynaptic['RMDVL'][nextState] += 4
        postsynaptic['RMEV'][nextState] += 1
        postsynaptic['URYDL'][nextState] += 1

def IL1DR():
        postsynaptic['IL1DL'][nextState] += 1
        postsynaptic['IL1R'][nextState] += 1
        postsynaptic['MDR01'][nextState] += 4
        postsynaptic['MDR02'][nextState] += 3
        postsynaptic['OLLR'][nextState] += 1
        postsynaptic['RIPR'][nextState] += 5
        postsynaptic['RMDVR'][nextState] += 5
        postsynaptic['RMEV'][nextState] += 1

def IL1L():
        postsynaptic['AVER'][nextState] += 2
        postsynaptic['IL1DL'][nextState] += 2
        postsynaptic['IL1VL'][nextState] += 1
        postsynaptic['MDL01'][nextState] += 3
        postsynaptic['MDL03'][nextState] += 3
        postsynaptic['MDL05'][nextState] += 4
        postsynaptic['MVL01'][nextState] += 3
        postsynaptic['MVL03'][nextState] += 3
        postsynaptic['RMDDL'][nextState] += 5
        postsynaptic['RMDL'][nextState] += 1
        postsynaptic['RMDR'][nextState] += 3
        postsynaptic['RMDVL'][nextState] += 4
        postsynaptic['RMDVR'][nextState] += 2
        postsynaptic['RMER'][nextState] += 1

def IL1R():
        postsynaptic['AVEL'][nextState] += 1
        postsynaptic['AVER'][nextState] += 1
        postsynaptic['IL1DR'][nextState] += 2
        postsynaptic['IL1VR'][nextState] += 1
        postsynaptic['MDR01'][nextState] += 3
        postsynaptic['MDR03'][nextState] += 3
        postsynaptic['MVR01'][nextState] += 3
        postsynaptic['MVR03'][nextState] += 3
        postsynaptic['RMDDL'][nextState] += 3
        postsynaptic['RMDDR'][nextState] += 2
        postsynaptic['RMDL'][nextState] += 4
        postsynaptic['RMDR'][nextState] += 2
        postsynaptic['RMDVL'][nextState] += 1
        postsynaptic['RMDVR'][nextState] += 4
        postsynaptic['RMEL'][nextState] += 2
        postsynaptic['RMHL'][nextState] += 1
        postsynaptic['URXR'][nextState] += 2

def IL1VL():
        postsynaptic['IL1L'][nextState] += 2
        postsynaptic['IL1VR'][nextState] += 1
        postsynaptic['MVL01'][nextState] += 5
        postsynaptic['MVL02'][nextState] += 4
        postsynaptic['RIPL'][nextState] += 4
        postsynaptic['RMDDL'][nextState] += 5
        postsynaptic['RMED'][nextState] += 1
        postsynaptic['URYVL'][nextState] += 1

def IL1VR():
        postsynaptic['IL1R'][nextState] += 2
        postsynaptic['IL1VL'][nextState] += 1
        postsynaptic['IL2R'][nextState] += 1
        postsynaptic['IL2VR'][nextState] += 1
        postsynaptic['MVR01'][nextState] += 5
        postsynaptic['MVR02'][nextState] += 5
        postsynaptic['RIPR'][nextState] += 6
        postsynaptic['RMDDR'][nextState] += 10
        postsynaptic['RMER'][nextState] += 1

def IL2DL():
        postsynaptic['AUAL'][nextState] += 1
        postsynaptic['IL1DL'][nextState] += 7
        postsynaptic['OLQDL'][nextState] += 2
        postsynaptic['RIBL'][nextState] += 1
        postsynaptic['RIPL'][nextState] += 10
        postsynaptic['RMEL'][nextState] += 4
        postsynaptic['RMER'][nextState] += 3
        postsynaptic['URADL'][nextState] += 3

def IL2DR():
        postsynaptic['CEPDR'][nextState] += 1
        postsynaptic['IL1DR'][nextState] += 7
        postsynaptic['RICR'][nextState] += 1
        postsynaptic['RIPR'][nextState] += 11
        postsynaptic['RMED'][nextState] += 1
        postsynaptic['RMEL'][nextState] += 2
        postsynaptic['RMER'][nextState] += 2
        postsynaptic['RMEV'][nextState] += 1
        postsynaptic['URADR'][nextState] += 3

def IL2L():
        postsynaptic['ADEL'][nextState] += 2
        postsynaptic['AVEL'][nextState] += 1
        postsynaptic['IL1L'][nextState] += 1
        postsynaptic['OLQDL'][nextState] += 5
        postsynaptic['OLQVL'][nextState] += 8
        postsynaptic['RICL'][nextState] += 1
        postsynaptic['RIH'][nextState] += 7
        postsynaptic['RMDL'][nextState] += 3
        postsynaptic['RMDR'][nextState] += 1
        postsynaptic['RMER'][nextState] += 2
        postsynaptic['RMEV'][nextState] += 2
        postsynaptic['RMGL'][nextState] += 1
        postsynaptic['URXL'][nextState] += 2

def IL2R():
        postsynaptic['ADER'][nextState] += 1
        postsynaptic['IL1R'][nextState] += 1
        postsynaptic['IL1VR'][nextState] += 1
        postsynaptic['OLLR'][nextState] += 1
        postsynaptic['OLQDR'][nextState] += 2
        postsynaptic['OLQVR'][nextState] += 7
        postsynaptic['RIH'][nextState] += 6
        postsynaptic['RMDL'][nextState] += 1
        postsynaptic['RMEL'][nextState] += 2
        postsynaptic['RMEV'][nextState] += 1
        postsynaptic['RMGR'][nextState] += 1
        postsynaptic['URBR'][nextState] += 1
        postsynaptic['URXR'][nextState] += 1

def IL2VL():
        postsynaptic['BAGR'][nextState] += 1
        postsynaptic['IL1VL'][nextState] += 7
        postsynaptic['IL2L'][nextState] += 1
        postsynaptic['OLQVL'][nextState] += 1
        postsynaptic['RIAL'][nextState] += 1
        postsynaptic['RIH'][nextState] += 2
        postsynaptic['RIPL'][nextState] += 1
        postsynaptic['RMEL'][nextState] += 1
        postsynaptic['RMER'][nextState] += 4
        postsynaptic['RMEV'][nextState] += 1
        postsynaptic['URAVL'][nextState] += 3

def IL2VR():
        postsynaptic['IL1VR'][nextState] += 6
        postsynaptic['OLQVR'][nextState] += 1
        postsynaptic['RIAR'][nextState] += 2
        postsynaptic['RIH'][nextState] += 3
        postsynaptic['RIPR'][nextState] += 15
        postsynaptic['RMEL'][nextState] += 3
        postsynaptic['RMER'][nextState] += 2
        postsynaptic['RMEV'][nextState] += 3
        postsynaptic['URAVR'][nextState] += 4
        postsynaptic['URXR'][nextState] += 1

def LUAL():
        postsynaptic['AVAL'][nextState] += 6
        postsynaptic['AVAR'][nextState] += 6
        postsynaptic['AVDL'][nextState] += 4
        postsynaptic['AVDR'][nextState] += 2
        postsynaptic['AVJL'][nextState] += 1
        postsynaptic['PHBL'][nextState] += 1
        postsynaptic['PLML'][nextState] += 1
        postsynaptic['PVNL'][nextState] += 1
        postsynaptic['PVR'][nextState] += 1
        postsynaptic['PVWL'][nextState] += 1

def LUAR():
        postsynaptic['AVAL'][nextState] += 3
        postsynaptic['AVAR'][nextState] += 7
        postsynaptic['AVDL'][nextState] += 1
        postsynaptic['AVDR'][nextState] += 3
        postsynaptic['AVJR'][nextState] += 1
        postsynaptic['PLMR'][nextState] += 1
        postsynaptic['PQR'][nextState] += 1
        postsynaptic['PVCR'][nextState] += 3
        postsynaptic['PVR'][nextState] += 2
        postsynaptic['PVWL'][nextState] += 1

def M1():
        postsynaptic['I2L'][nextState] += 2
        postsynaptic['I2R'][nextState] += 2
        postsynaptic['I3'][nextState] += 1
        postsynaptic['I4'][nextState] += 1

def M2L():
        postsynaptic['I1L'][nextState] += 3
        postsynaptic['I1R'][nextState] += 3
        postsynaptic['I3'][nextState] += 3
        postsynaptic['M2R'][nextState] += 1
        postsynaptic['M5'][nextState] += 1
        postsynaptic['MI'][nextState] += 4

def M2R():
        postsynaptic['I1L'][nextState] += 3
        postsynaptic['I1R'][nextState] += 3
        postsynaptic['I3'][nextState] += 3
        postsynaptic['M3L'][nextState] += 1
        postsynaptic['M3R'][nextState] += 1
        postsynaptic['M5'][nextState] += 1
        postsynaptic['MI'][nextState] += 4

def M3L():
        postsynaptic['I1L'][nextState] += 4
        postsynaptic['I1R'][nextState] += 4
        postsynaptic['I4'][nextState] += 2
        postsynaptic['I5'][nextState] += 3
        postsynaptic['I6'][nextState] += 1
        postsynaptic['M1'][nextState] += 2
        postsynaptic['M3R'][nextState] += 1
        postsynaptic['MCL'][nextState] += 1
        postsynaptic['MCR'][nextState] += 1
        postsynaptic['MI'][nextState] += 2
        postsynaptic['NSML'][nextState] += 2
        postsynaptic['NSMR'][nextState] += 3

def M3R():
        postsynaptic['I1L'][nextState] += 4
        postsynaptic['I1R'][nextState] += 4
        postsynaptic['I3'][nextState] += 2
        postsynaptic['I4'][nextState] += 6
        postsynaptic['I5'][nextState] += 3
        postsynaptic['I6'][nextState] += 1
        postsynaptic['M1'][nextState] += 2
        postsynaptic['M3L'][nextState] += 1
        postsynaptic['MCL'][nextState] += 1
        postsynaptic['MCR'][nextState] += 1
        postsynaptic['MI'][nextState] += 2
        postsynaptic['NSML'][nextState] += 2
        postsynaptic['NSMR'][nextState] += 3

def M4():
        postsynaptic['I3'][nextState] += 1
        postsynaptic['I5'][nextState] += 13
        postsynaptic['I6'][nextState] += 3
        postsynaptic['M2L'][nextState] += 1
        postsynaptic['M2R'][nextState] += 1
        postsynaptic['M4'][nextState] += 6
        postsynaptic['M5'][nextState] += 1
        postsynaptic['NSML'][nextState] += 1
        postsynaptic['NSMR'][nextState] += 1

def M5():
        postsynaptic['I5'][nextState] += 3
        postsynaptic['I5'][nextState] += 1
        postsynaptic['I6'][nextState] += 1
        postsynaptic['M1'][nextState] += 2
        postsynaptic['M2L'][nextState] += 2
        postsynaptic['M2R'][nextState] += 2
        postsynaptic['M5'][nextState] += 4

def MCL():
        postsynaptic['I1L'][nextState] += 3
        postsynaptic['I1R'][nextState] += 3
        postsynaptic['I2L'][nextState] += 1
        postsynaptic['I2R'][nextState] += 1
        postsynaptic['I3'][nextState] += 1
        postsynaptic['M1'][nextState] += 2
        postsynaptic['M2L'][nextState] += 2
        postsynaptic['M2R'][nextState] += 2

def MCR():
        postsynaptic['I1L'][nextState] += 3
        postsynaptic['I1R'][nextState] += 3
        postsynaptic['I3'][nextState] += 1
        postsynaptic['M1'][nextState] += 2
        postsynaptic['M2L'][nextState] += 2
        postsynaptic['M2R'][nextState] += 2

def MI():
        postsynaptic['I1L'][nextState] += 1
        postsynaptic['I1R'][nextState] += 1
        postsynaptic['I3'][nextState] += 1
        postsynaptic['I4'][nextState] += 1
        postsynaptic['I5'][nextState] += 2
        postsynaptic['M1'][nextState] += 1
        postsynaptic['M2L'][nextState] += 2
        postsynaptic['M2R'][nextState] += 2
        postsynaptic['M3L'][nextState] += 1
        postsynaptic['M3R'][nextState] += 1
        postsynaptic['MCL'][nextState] += 2
        postsynaptic['MCR'][nextState] += 2

def NSML():
        postsynaptic['I1L'][nextState] += 1
        postsynaptic['I1R'][nextState] += 2
        postsynaptic['I2L'][nextState] += 6
        postsynaptic['I2R'][nextState] += 6
        postsynaptic['I3'][nextState] += 2
        postsynaptic['I4'][nextState] += 3
        postsynaptic['I5'][nextState] += 2
        postsynaptic['I6'][nextState] += 2
        postsynaptic['M3L'][nextState] += 2
        postsynaptic['M3R'][nextState] += 2

def NSMR():
        postsynaptic['I1L'][nextState] += 2
        postsynaptic['I1R'][nextState] += 2
        postsynaptic['I2L'][nextState] += 6
        postsynaptic['I2R'][nextState] += 6
        postsynaptic['I3'][nextState] += 2
        postsynaptic['I4'][nextState] += 3
        postsynaptic['I5'][nextState] += 2
        postsynaptic['I6'][nextState] += 2
        postsynaptic['M3L'][nextState] += 2
        postsynaptic['M3R'][nextState] += 2

def OLLL():
        postsynaptic['AVER'][nextState] += 21
        postsynaptic['CEPDL'][nextState] += 3
        postsynaptic['CEPVL'][nextState] += 4
        postsynaptic['IL1DL'][nextState] += 1
        postsynaptic['IL1VL'][nextState] += 2
        postsynaptic['OLLR'][nextState] += 2
        postsynaptic['RIBL'][nextState] += 8
        postsynaptic['RIGL'][nextState] += 1
        postsynaptic['RMDDL'][nextState] += 7
        postsynaptic['RMDL'][nextState] += 2
        postsynaptic['RMDVL'][nextState] += 1
        postsynaptic['RMEL'][nextState] += 2
        postsynaptic['SMDDL'][nextState] += 3
        postsynaptic['SMDDR'][nextState] += 4
        postsynaptic['SMDVR'][nextState] += 4
        postsynaptic['URYDL'][nextState] += 1

def OLLR():
        postsynaptic['AVEL'][nextState] += 16
        postsynaptic['CEPDR'][nextState] += 1
        postsynaptic['CEPVR'][nextState] += 6
        postsynaptic['IL1DR'][nextState] += 3
        postsynaptic['IL1VR'][nextState] += 1
        postsynaptic['IL2R'][nextState] += 1
        postsynaptic['OLLL'][nextState] += 2
        postsynaptic['RIBR'][nextState] += 10
        postsynaptic['RIGR'][nextState] += 1
        postsynaptic['RMDDR'][nextState] += 10
        postsynaptic['RMDL'][nextState] += 3
        postsynaptic['RMDVR'][nextState] += 3
        postsynaptic['RMER'][nextState] += 2
        postsynaptic['SMDDR'][nextState] += 1
        postsynaptic['SMDVL'][nextState] += 4
        postsynaptic['SMDVR'][nextState] += 3

def OLQDL():
        postsynaptic['CEPDL'][nextState] += 1
        postsynaptic['RIBL'][nextState] += 2
        postsynaptic['RICR'][nextState] += 1
        postsynaptic['RIGL'][nextState] += 1
        postsynaptic['RMDDR'][nextState] += 4
        postsynaptic['RMDVL'][nextState] += 1
        postsynaptic['SIBVL'][nextState] += 3
        postsynaptic['URBL'][nextState] += 1

def OLQDR():
        postsynaptic['CEPDR'][nextState] += 2
        postsynaptic['RIBR'][nextState] += 2
        postsynaptic['RICL'][nextState] += 1
        postsynaptic['RICR'][nextState] += 1
        postsynaptic['RIGR'][nextState] += 1
        postsynaptic['RIH'][nextState] += 1
        postsynaptic['RMDDL'][nextState] += 3
        postsynaptic['RMDVR'][nextState] += 1
        postsynaptic['RMHR'][nextState] += 1
        postsynaptic['SIBVR'][nextState] += 2
        postsynaptic['URBR'][nextState] += 1

def OLQVL():
        postsynaptic['ADLL'][nextState] += 1
        postsynaptic['CEPVL'][nextState] += 1
        postsynaptic['IL1VL'][nextState] += 1
        postsynaptic['IL2VL'][nextState] += 1
        postsynaptic['RIBL'][nextState] += 1
        postsynaptic['RICL'][nextState] += 1
        postsynaptic['RIGL'][nextState] += 1
        postsynaptic['RIH'][nextState] += 1
        postsynaptic['RIPL'][nextState] += 1
        postsynaptic['RMDDL'][nextState] += 1
        postsynaptic['RMDVR'][nextState] += 4
        postsynaptic['SIBDL'][nextState] += 3
        postsynaptic['URBL'][nextState] += 1

def OLQVR():
        postsynaptic['CEPVR'][nextState] += 1
        postsynaptic['IL1VR'][nextState] += 1
        postsynaptic['RIBR'][nextState] += 1
        postsynaptic['RICR'][nextState] += 1
        postsynaptic['RIGR'][nextState] += 1
        postsynaptic['RIH'][nextState] += 2
        postsynaptic['RIPR'][nextState] += 2
        postsynaptic['RMDDR'][nextState] += 1
        postsynaptic['RMDVL'][nextState] += 4
        postsynaptic['RMER'][nextState] += 1
        postsynaptic['SIBDR'][nextState] += 4
        postsynaptic['URBR'][nextState] += 1

def PDA():
        postsynaptic['AS11'][nextState] += 1
        postsynaptic['DA9'][nextState] += 1
        postsynaptic['DD6'][nextState] += 1
        postsynaptic['MDL21'][nextState] += 2
        postsynaptic['PVNR'][nextState] += 1
        postsynaptic['VD13'][nextState] += 3

def PDB():
        postsynaptic['AS11'][nextState] += 2
        postsynaptic['MVL22'][nextState] += 1
        postsynaptic['MVR21'][nextState] += 1
        postsynaptic['RID'][nextState] += 2
        postsynaptic['VD13'][nextState] += 2

def PDEL():
        postsynaptic['AVKL'][nextState] += 6
        postsynaptic['DVA'][nextState] += 24
        postsynaptic['PDER'][nextState] += 1
        postsynaptic['PDER'][nextState] += 3
        postsynaptic['PVCR'][nextState] += 1
        postsynaptic['PVM'][nextState] += 2
        postsynaptic['PVM'][nextState] += 1
        postsynaptic['PVR'][nextState] += 2
        postsynaptic['VA9'][nextState] += 1
        postsynaptic['VD11'][nextState] += 1

def PDER():
        postsynaptic['AVKL'][nextState] += 16
        postsynaptic['DVA'][nextState] += 35
        postsynaptic['PDEL'][nextState] += 3
        postsynaptic['PVCL'][nextState] += 1
        postsynaptic['PVCR'][nextState] += 1
        postsynaptic['PVM'][nextState] += 1
        postsynaptic['VA8'][nextState] += 1
        postsynaptic['VD9'][nextState] += 1

def PHAL():
        postsynaptic['AVDR'][nextState] += 1
        postsynaptic['AVFL'][nextState] += 3
        postsynaptic['AVG'][nextState] += 5
        postsynaptic['AVHL'][nextState] += 1
        postsynaptic['AVHR'][nextState] += 1
        postsynaptic['DVA'][nextState] += 2
        postsynaptic['PHAR'][nextState] += 5
        postsynaptic['PHAR'][nextState] += 2
        postsynaptic['PHBL'][nextState] += 5
        postsynaptic['PHBR'][nextState] += 5
        postsynaptic['PVQL'][nextState] += 2

def PHAR():
        postsynaptic['AVG'][nextState] += 3
        postsynaptic['AVHR'][nextState] += 1
        postsynaptic['DA8'][nextState] += 1
        postsynaptic['DVA'][nextState] += 1
        postsynaptic['PHAL'][nextState] += 6
        postsynaptic['PHAL'][nextState] += 2
        postsynaptic['PHBL'][nextState] += 1
        postsynaptic['PHBR'][nextState] += 5
        postsynaptic['PVPL'][nextState] += 3
        postsynaptic['PVQL'][nextState] += 2

def PHBL():
        postsynaptic['AVAL'][nextState] += 9
        postsynaptic['AVAR'][nextState] += 6
        postsynaptic['AVDL'][nextState] += 1
        postsynaptic['PHBR'][nextState] += 1
        postsynaptic['PHBR'][nextState] += 3
        postsynaptic['PVCL'][nextState] += 13
        postsynaptic['VA12'][nextState] += 1

def PHBR():
        postsynaptic['AVAL'][nextState] += 7
        postsynaptic['AVAR'][nextState] += 7
        postsynaptic['AVDL'][nextState] += 1
        postsynaptic['AVDR'][nextState] += 1
        postsynaptic['AVFL'][nextState] += 1
        postsynaptic['AVHL'][nextState] += 1
        postsynaptic['DA8'][nextState] += 1
        postsynaptic['PHBL'][nextState] += 1
        postsynaptic['PHBL'][nextState] += 3
        postsynaptic['PVCL'][nextState] += 6
        postsynaptic['PVCR'][nextState] += 3
        postsynaptic['VA12'][nextState] += 2

def PHCL():
        postsynaptic['AVAL'][nextState] += 1
        postsynaptic['DA9'][nextState] += 7
        postsynaptic['DA9'][nextState] += 1
        postsynaptic['DVA'][nextState] += 6
        postsynaptic['LUAL'][nextState] += 1
        postsynaptic['PHCR'][nextState] += 1
        postsynaptic['PLML'][nextState] += 1
        postsynaptic['PVCL'][nextState] += 2
        postsynaptic['VA12'][nextState] += 3

def PHCR():
        postsynaptic['AVHR'][nextState] += 1
        postsynaptic['DA9'][nextState] += 2
        postsynaptic['DVA'][nextState] += 8
        postsynaptic['LUAR'][nextState] += 1
        postsynaptic['PHCL'][nextState] += 2
        postsynaptic['PVCR'][nextState] += 9
        postsynaptic['VA12'][nextState] += 2

def PLML():
        postsynaptic['HSNL'][nextState] += 1
        postsynaptic['LUAL'][nextState] += 1
        postsynaptic['PHCL'][nextState] += 1
        postsynaptic['PVCL'][nextState] += 1

def PLMR():
        postsynaptic['AS6'][nextState] += 1
        postsynaptic['AVAL'][nextState] += 4
        postsynaptic['AVAR'][nextState] += 1
        postsynaptic['AVDL'][nextState] += 1
        postsynaptic['AVDR'][nextState] += 4
        postsynaptic['DVA'][nextState] += 5
        postsynaptic['HSNR'][nextState] += 1
        postsynaptic['LUAR'][nextState] += 1
        postsynaptic['PDEL'][nextState] += 2
        postsynaptic['PDER'][nextState] += 3
        postsynaptic['PVCL'][nextState] += 2
        postsynaptic['PVCR'][nextState] += 1
        postsynaptic['PVR'][nextState] += 2

def PLNL():
        postsynaptic['SAADL'][nextState] += 5
        postsynaptic['SMBVL'][nextState] += 6

def PLNR():
        postsynaptic['SAADR'][nextState] += 4
        postsynaptic['SMBVR'][nextState] += 6

def PQR():
        postsynaptic['AVAL'][nextState] += 8
        postsynaptic['AVAR'][nextState] += 11
        postsynaptic['AVDL'][nextState] += 7
        postsynaptic['AVDR'][nextState] += 6
        postsynaptic['AVG'][nextState] += 1
        postsynaptic['LUAR'][nextState] += 1
        postsynaptic['PVNL'][nextState] += 1
        postsynaptic['PVPL'][nextState] += 4

def PVCL():
        postsynaptic['AS1'][nextState] += 1
        postsynaptic['AVAL'][nextState] += 3
        postsynaptic['AVAR'][nextState] += 4
        postsynaptic['AVBL'][nextState] += 5
        postsynaptic['AVBR'][nextState] += 12
        postsynaptic['AVDL'][nextState] += 5
        postsynaptic['AVDR'][nextState] += 2
        postsynaptic['AVEL'][nextState] += 3
        postsynaptic['AVER'][nextState] += 1
        postsynaptic['AVJL'][nextState] += 4
        postsynaptic['AVJR'][nextState] += 2
        postsynaptic['DA2'][nextState] += 1
        postsynaptic['DA5'][nextState] += 1
        postsynaptic['DA6'][nextState] += 1
        postsynaptic['DB2'][nextState] += 3
        postsynaptic['DB3'][nextState] += 4
        postsynaptic['DB4'][nextState] += 3
        postsynaptic['DB5'][nextState] += 2
        postsynaptic['DB6'][nextState] += 2
        postsynaptic['DB7'][nextState] += 3
        postsynaptic['DVA'][nextState] += 5
        postsynaptic['PLML'][nextState] += 1
        postsynaptic['PVCR'][nextState] += 7
        postsynaptic['RID'][nextState] += 5
        postsynaptic['RIS'][nextState] += 2
        postsynaptic['SIBVL'][nextState] += 2
        postsynaptic['VB10'][nextState] += 3
        postsynaptic['VB11'][nextState] += 1
        postsynaptic['VB3'][nextState] += 1
        postsynaptic['VB4'][nextState] += 1
        postsynaptic['VB5'][nextState] += 1
        postsynaptic['VB6'][nextState] += 2
        postsynaptic['VB8'][nextState] += 1
        postsynaptic['VB9'][nextState] += 2

def PVCR():
        postsynaptic['AQR'][nextState] += 1
        postsynaptic['AS2'][nextState] += 1
        postsynaptic['AVAL'][nextState] += 12
        postsynaptic['AVAR'][nextState] += 10
        postsynaptic['AVBL'][nextState] += 8
        postsynaptic['AVBR'][nextState] += 6
        postsynaptic['AVDL'][nextState] += 5
        postsynaptic['AVDR'][nextState] += 1
        postsynaptic['AVEL'][nextState] += 1
        postsynaptic['AVER'][nextState] += 1
        postsynaptic['AVJL'][nextState] += 3
        postsynaptic['AVL'][nextState] += 1
        postsynaptic['DA9'][nextState] += 1
        postsynaptic['DB2'][nextState] += 1
        postsynaptic['DB3'][nextState] += 3
        postsynaptic['DB4'][nextState] += 4
        postsynaptic['DB5'][nextState] += 1
        postsynaptic['DB6'][nextState] += 2
        postsynaptic['DB7'][nextState] += 1
        postsynaptic['FLPL'][nextState] += 1
        postsynaptic['LUAR'][nextState] += 1
        postsynaptic['PDEL'][nextState] += 2
        postsynaptic['PHCR'][nextState] += 1
        postsynaptic['PLMR'][nextState] += 1
        postsynaptic['PVCL'][nextState] += 8
        postsynaptic['PVDL'][nextState] += 1
        postsynaptic['PVR'][nextState] += 1
        postsynaptic['PVWL'][nextState] += 2
        postsynaptic['PVWR'][nextState] += 2
        postsynaptic['RID'][nextState] += 5
        postsynaptic['SIBVR'][nextState] += 2
        postsynaptic['VA8'][nextState] += 2
        postsynaptic['VA9'][nextState] += 1
        postsynaptic['VB10'][nextState] += 1
        postsynaptic['VB4'][nextState] += 3
        postsynaptic['VB6'][nextState] += 2
        postsynaptic['VB7'][nextState] += 3
        postsynaptic['VB8'][nextState] += 1

def PVDL():
        postsynaptic['AVAL'][nextState] += 6
        postsynaptic['AVAR'][nextState] += 6
        postsynaptic['DD5'][nextState] += 1
        postsynaptic['PVCL'][nextState] += 1
        postsynaptic['PVCR'][nextState] += 6
        postsynaptic['VD10'][nextState] += 6

def PVDR():
        postsynaptic['AVAL'][nextState] += 6
        postsynaptic['AVAR'][nextState] += 9
        postsynaptic['DVA'][nextState] += 3
        postsynaptic['PVCL'][nextState] += 13
        postsynaptic['PVCR'][nextState] += 10
        postsynaptic['PVDL'][nextState] += 1
        postsynaptic['VA9'][nextState] += 1

def PVM():
        postsynaptic['AVKL'][nextState] += 11
        postsynaptic['AVL'][nextState] += 1
        postsynaptic['AVM'][nextState] += 1
        postsynaptic['DVA'][nextState] += 3
        postsynaptic['PDEL'][nextState] += 7
        postsynaptic['PDEL'][nextState] += 1
        postsynaptic['PDER'][nextState] += 8
        postsynaptic['PDER'][nextState] += 1
        postsynaptic['PVCL'][nextState] += 2
        postsynaptic['PVR'][nextState] += 1

def PVNL():
        postsynaptic['AVAL'][nextState] += 2
        postsynaptic['AVBR'][nextState] += 3
        postsynaptic['AVDL'][nextState] += 3
        postsynaptic['AVDR'][nextState] += 3
        postsynaptic['AVEL'][nextState] += 1
        postsynaptic['AVFR'][nextState] += 1
        postsynaptic['AVG'][nextState] += 1
        postsynaptic['AVJL'][nextState] += 5
        postsynaptic['AVJR'][nextState] += 5
        postsynaptic['AVL'][nextState] += 2
        postsynaptic['BDUL'][nextState] += 1
        postsynaptic['BDUR'][nextState] += 2
        postsynaptic['DD1'][nextState] += 2
        postsynaptic['MVL09'][nextState] += 3
        postsynaptic['PQR'][nextState] += 1
        postsynaptic['PVCL'][nextState] += 1
        postsynaptic['PVNR'][nextState] += 5
        postsynaptic['PVQR'][nextState] += 1
        postsynaptic['PVT'][nextState] += 1
        postsynaptic['PVWL'][nextState] += 1
        postsynaptic['RIFL'][nextState] += 1

def PVNR():
        postsynaptic['AVAL'][nextState] += 2
        postsynaptic['AVBL'][nextState] += 1
        postsynaptic['AVBR'][nextState] += 2
        postsynaptic['AVDR'][nextState] += 1
        postsynaptic['AVEL'][nextState] += 3
        postsynaptic['AVJL'][nextState] += 4
        postsynaptic['AVJR'][nextState] += 1
        postsynaptic['AVL'][nextState] += 2
        postsynaptic['BDUL'][nextState] += 1
        postsynaptic['BDUR'][nextState] += 2
        postsynaptic['DD3'][nextState] += 1
        postsynaptic['HSNR'][nextState] += 2
        postsynaptic['MVL12'][nextState] += 1
        postsynaptic['MVL13'][nextState] += 2
        postsynaptic['PQR'][nextState] += 2
        postsynaptic['PVCL'][nextState] += 1
        postsynaptic['PVNL'][nextState] += 1
        postsynaptic['PVT'][nextState] += 2
        postsynaptic['PVWL'][nextState] += 2
        postsynaptic['VC2'][nextState] += 1
        postsynaptic['VC3'][nextState] += 1
        postsynaptic['VD12'][nextState] += 1
        postsynaptic['VD6'][nextState] += 1
        postsynaptic['VD7'][nextState] += 1

def PVPL():
        postsynaptic['ADAL'][nextState] += 1
        postsynaptic['AQR'][nextState] += 8
        postsynaptic['AVAL'][nextState] += 2
        postsynaptic['AVAR'][nextState] += 1
        postsynaptic['AVBL'][nextState] += 5
        postsynaptic['AVBR'][nextState] += 6
        postsynaptic['AVDR'][nextState] += 2
        postsynaptic['AVER'][nextState] += 1
        postsynaptic['AVHR'][nextState] += 1
        postsynaptic['AVKL'][nextState] += 1
        postsynaptic['AVKR'][nextState] += 6
        postsynaptic['DVC'][nextState] += 2
        postsynaptic['PHAR'][nextState] += 3
        postsynaptic['PQR'][nextState] += 4
        postsynaptic['PVCR'][nextState] += 3
        postsynaptic['PVPR'][nextState] += 1
        postsynaptic['PVT'][nextState] += 1
        postsynaptic['RIGL'][nextState] += 2
        postsynaptic['VD13'][nextState] += 2
        postsynaptic['VD3'][nextState] += 1

def PVPR():
        postsynaptic['ADFR'][nextState] += 1
        postsynaptic['AQR'][nextState] += 11
        postsynaptic['ASHR'][nextState] += 1
        postsynaptic['AVAL'][nextState] += 1
        postsynaptic['AVAR'][nextState] += 2
        postsynaptic['AVBL'][nextState] += 4
        postsynaptic['AVBR'][nextState] += 5
        postsynaptic['AVHL'][nextState] += 3
        postsynaptic['AVKL'][nextState] += 1
        postsynaptic['AVL'][nextState] += 4
        postsynaptic['DD2'][nextState] += 1
        postsynaptic['DVC'][nextState] += 14
        postsynaptic['PVCL'][nextState] += 4
        postsynaptic['PVCR'][nextState] += 7
        postsynaptic['PVPL'][nextState] += 1
        postsynaptic['PVQR'][nextState] += 1
        postsynaptic['RIAR'][nextState] += 2
        postsynaptic['RIGR'][nextState] += 1
        postsynaptic['RIMR'][nextState] += 1
        postsynaptic['RMGR'][nextState] += 1
        postsynaptic['VD4'][nextState] += 1
        postsynaptic['VD5'][nextState] += 1

def PVQL():
        postsynaptic['ADAL'][nextState] += 1
        postsynaptic['AIAL'][nextState] += 3
        postsynaptic['ASJL'][nextState] += 1
        postsynaptic['ASKL'][nextState] += 4
        postsynaptic['ASKL'][nextState] += 5
        postsynaptic['HSNL'][nextState] += 2
        postsynaptic['PVQR'][nextState] += 2
        postsynaptic['RMGL'][nextState] += 1

def PVQR():
        postsynaptic['ADAR'][nextState] += 1
        postsynaptic['AIAR'][nextState] += 7
        postsynaptic['ASER'][nextState] += 1
        postsynaptic['ASKR'][nextState] += 8
        postsynaptic['AVBL'][nextState] += 1
        postsynaptic['AVFL'][nextState] += 1
        postsynaptic['AVFR'][nextState] += 1
        postsynaptic['AVL'][nextState] += 1
        postsynaptic['AWAR'][nextState] += 2
        postsynaptic['DD1'][nextState] += 1
        postsynaptic['DVC'][nextState] += 1
        postsynaptic['HSNR'][nextState] += 1
        postsynaptic['PVNL'][nextState] += 1
        postsynaptic['PVQL'][nextState] += 1
        postsynaptic['PVT'][nextState] += 1
        postsynaptic['RIFR'][nextState] += 1
        postsynaptic['VD1'][nextState] += 1

def PVR():
        postsynaptic['ADAL'][nextState] += 1
        postsynaptic['ALML'][nextState] += 1
        postsynaptic['AS6'][nextState] += 1
        postsynaptic['AVBL'][nextState] += 4
        postsynaptic['AVBR'][nextState] += 4
        postsynaptic['AVJL'][nextState] += 3
        postsynaptic['AVJR'][nextState] += 2
        postsynaptic['AVKL'][nextState] += 1
        postsynaptic['DA9'][nextState] += 1
        postsynaptic['DB2'][nextState] += 1
        postsynaptic['DB3'][nextState] += 1
        postsynaptic['DVA'][nextState] += 3
        postsynaptic['IL1DL'][nextState] += 1
        postsynaptic['IL1DR'][nextState] += 1
        postsynaptic['IL1VL'][nextState] += 1
        postsynaptic['IL1VR'][nextState] += 1
        postsynaptic['LUAL'][nextState] += 1
        postsynaptic['LUAR'][nextState] += 1
        postsynaptic['PDEL'][nextState] += 1
        postsynaptic['PDER'][nextState] += 1
        postsynaptic['PLMR'][nextState] += 2
        postsynaptic['PVCR'][nextState] += 1
        postsynaptic['RIPL'][nextState] += 3
        postsynaptic['RIPR'][nextState] += 3
        postsynaptic['SABD'][nextState] += 1
        postsynaptic['URADL'][nextState] += 1

def PVT():
        postsynaptic['AIBL'][nextState] += 3
        postsynaptic['AIBR'][nextState] += 5
        postsynaptic['AVKL'][nextState] += 9
        postsynaptic['AVKR'][nextState] += 7
        postsynaptic['AVL'][nextState] += 2
        postsynaptic['DVC'][nextState] += 2
        postsynaptic['PVPL'][nextState] += 1
        postsynaptic['RIBL'][nextState] += 1
        postsynaptic['RIBR'][nextState] += 1
        postsynaptic['RIGL'][nextState] += 2
        postsynaptic['RIGR'][nextState] += 3
        postsynaptic['RIH'][nextState] += 1
        postsynaptic['RMEV'][nextState] += 1
        postsynaptic['RMFL'][nextState] += 2
        postsynaptic['RMFR'][nextState] += 3
        postsynaptic['SMBDR'][nextState] += 1

def PVWL():
        postsynaptic['AVJL'][nextState] += 1
        postsynaptic['PVCR'][nextState] += 2
        postsynaptic['PVT'][nextState] += 2
        postsynaptic['PVWR'][nextState] += 1
        postsynaptic['VA12'][nextState] += 1


def PVWR():
        postsynaptic['AVAR'][nextState] += 1
        postsynaptic['AVDR'][nextState] += 1
        postsynaptic['PVCR'][nextState] += 2
        postsynaptic['PVT'][nextState] += 1
        postsynaptic['VA12'][nextState] += 1

def RIAL():
        postsynaptic['CEPVL'][nextState] += 1
        postsynaptic['RIAR'][nextState] += 1
        postsynaptic['RIVL'][nextState] += 2
        postsynaptic['RIVR'][nextState] += 4
        postsynaptic['RMDDL'][nextState] += 12
        postsynaptic['RMDDR'][nextState] += 7
        postsynaptic['RMDL'][nextState] += 6
        postsynaptic['RMDR'][nextState] += 6
        postsynaptic['RMDVL'][nextState] += 9
        postsynaptic['RMDVR'][nextState] += 11
        postsynaptic['SIADL'][nextState] += 2
        postsynaptic['SMDDL'][nextState] += 8
        postsynaptic['SMDDR'][nextState] += 10
        postsynaptic['SMDVL'][nextState] += 6
        postsynaptic['SMDVR'][nextState] += 11

def RIAR():
        postsynaptic['CEPVR'][nextState] += 1
        postsynaptic['IL1R'][nextState] += 1
        postsynaptic['RIAL'][nextState] += 4
        postsynaptic['RIVL'][nextState] += 1
        postsynaptic['RMDDL'][nextState] += 10
        postsynaptic['RMDDR'][nextState] += 11
        postsynaptic['RMDL'][nextState] += 3
        postsynaptic['RMDR'][nextState] += 8
        postsynaptic['RMDVL'][nextState] += 12
        postsynaptic['RMDVR'][nextState] += 10
        postsynaptic['SAADR'][nextState] += 1
        postsynaptic['SIADL'][nextState] += 1
        postsynaptic['SIADR'][nextState] += 1
        postsynaptic['SIAVL'][nextState] += 1
        postsynaptic['SMDDL'][nextState] += 7
        postsynaptic['SMDDR'][nextState] += 7
        postsynaptic['SMDVL'][nextState] += 13
        postsynaptic['SMDVR'][nextState] += 7

def RIBL():
        postsynaptic['AIBR'][nextState] += 2
        postsynaptic['AUAL'][nextState] += 1
        postsynaptic['AVAL'][nextState] += 1
        postsynaptic['AVBL'][nextState] += 1
        postsynaptic['AVBR'][nextState] += 2
        postsynaptic['AVDR'][nextState] += 1
        postsynaptic['AVEL'][nextState] += 1
        postsynaptic['AVER'][nextState] += 5
        postsynaptic['BAGR'][nextState] += 1
        postsynaptic['OLQDL'][nextState] += 2
        postsynaptic['OLQVL'][nextState] += 1
        postsynaptic['PVT'][nextState] += 1
        postsynaptic['RIAL'][nextState] += 3
        postsynaptic['RIBL'][nextState] += 1
        postsynaptic['RIBR'][nextState] += 3
        postsynaptic['RIGL'][nextState] += 1
        postsynaptic['SIADL'][nextState] += 1
        postsynaptic['SIAVL'][nextState] += 1
        postsynaptic['SIBDL'][nextState] += 1
        postsynaptic['SIBVL'][nextState] += 1
        postsynaptic['SIBVR'][nextState] += 1
        postsynaptic['SMBDL'][nextState] += 1
        postsynaptic['SMDDL'][nextState] += 1
        postsynaptic['SMDVR'][nextState] += 4

def RIBR():
        postsynaptic['AIBL'][nextState] += 1
        postsynaptic['AIZR'][nextState] += 1
        postsynaptic['AVAR'][nextState] += 2
        postsynaptic['AVBL'][nextState] += 1
        postsynaptic['AVBR'][nextState] += 1
        postsynaptic['AVEL'][nextState] += 3
        postsynaptic['AVER'][nextState] += 1
        postsynaptic['BAGL'][nextState] += 1
        postsynaptic['OLQDR'][nextState] += 2
        postsynaptic['OLQVR'][nextState] += 1
        postsynaptic['PVT'][nextState] += 1
        postsynaptic['RIAR'][nextState] += 2
        postsynaptic['RIBL'][nextState] += 3
        postsynaptic['RIBR'][nextState] += 1
        postsynaptic['RIGR'][nextState] += 2
        postsynaptic['RIH'][nextState] += 1
        postsynaptic['SIADR'][nextState] += 1
        postsynaptic['SIAVR'][nextState] += 1
        postsynaptic['SIBDR'][nextState] += 1
        postsynaptic['SIBVR'][nextState] += 1
        postsynaptic['SMBDR'][nextState] += 1
        postsynaptic['SMDDL'][nextState] += 2
        postsynaptic['SMDDR'][nextState] += 1
        postsynaptic['SMDVL'][nextState] += 2

def RICL():
        postsynaptic['ADAR'][nextState] += 1
        postsynaptic['ASHL'][nextState] += 2
        postsynaptic['AVAL'][nextState] += 5
        postsynaptic['AVAR'][nextState] += 6
        postsynaptic['AVKL'][nextState] += 1
        postsynaptic['AVKR'][nextState] += 2
        postsynaptic['AWBR'][nextState] += 1
        postsynaptic['RIML'][nextState] += 1
        postsynaptic['RIMR'][nextState] += 3
        postsynaptic['RIVR'][nextState] += 1
        postsynaptic['RMFR'][nextState] += 1
        postsynaptic['SMBDL'][nextState] += 2
        postsynaptic['SMDDL'][nextState] += 3
        postsynaptic['SMDDR'][nextState] += 3
        postsynaptic['SMDVR'][nextState] += 1

def RICR():
        postsynaptic['ADAR'][nextState] += 1
        postsynaptic['ASHR'][nextState] += 2
        postsynaptic['AVAL'][nextState] += 5
        postsynaptic['AVAR'][nextState] += 5
        postsynaptic['AVKL'][nextState] += 1
        postsynaptic['SMBDR'][nextState] += 1
        postsynaptic['SMDDL'][nextState] += 4
        postsynaptic['SMDDR'][nextState] += 3
        postsynaptic['SMDVL'][nextState] += 2
        postsynaptic['SMDVR'][nextState] += 1

def RID():
        postsynaptic['ALA'][nextState] += 1
        postsynaptic['AS2'][nextState] += 1
        postsynaptic['AVBL'][nextState] += 1
        postsynaptic['AVBR'][nextState] += 2
        postsynaptic['DA6'][nextState] += 3
        postsynaptic['DA9'][nextState] += 1
        postsynaptic['DB1'][nextState] += 1
        postsynaptic['DD1'][nextState] += 4
        postsynaptic['DD2'][nextState] += 4
        postsynaptic['DD3'][nextState] += 3
        postsynaptic['MDL14'][nextState] += -2
        postsynaptic['MDL21'][nextState] += -3
        postsynaptic['PDB'][nextState] += 2
        postsynaptic['VD13'][nextState] += 1
        postsynaptic['VD5'][nextState] += 1

def RIFL():
        postsynaptic['ALML'][nextState] += 2
        postsynaptic['AVBL'][nextState] += 10
        postsynaptic['AVBR'][nextState] += 1
        postsynaptic['AVG'][nextState] += 1
        postsynaptic['AVHR'][nextState] += 1
        postsynaptic['AVJR'][nextState] += 2
        postsynaptic['PVPL'][nextState] += 3
        postsynaptic['RIML'][nextState] += 4
        postsynaptic['VD1'][nextState] += 1

def RIFR():
        postsynaptic['ASHR'][nextState] += 2
        postsynaptic['AVBL'][nextState] += 1
        postsynaptic['AVBR'][nextState] += 17
        postsynaptic['AVFL'][nextState] += 1
        postsynaptic['AVG'][nextState] += 1
        postsynaptic['AVHL'][nextState] += 1
        postsynaptic['AVJL'][nextState] += 1
        postsynaptic['AVJR'][nextState] += 2
        postsynaptic['HSNR'][nextState] += 1
        postsynaptic['PVCL'][nextState] += 1
        postsynaptic['PVCR'][nextState] += 1
        postsynaptic['PVPR'][nextState] += 4
        postsynaptic['RIMR'][nextState] += 4
        postsynaptic['RIPR'][nextState] += 1

def RIGL():
        postsynaptic['AIBR'][nextState] += 3
        postsynaptic['AIZR'][nextState] += 1
        postsynaptic['ALNL'][nextState] += 1
        postsynaptic['AQR'][nextState] += 2
        postsynaptic['AVEL'][nextState] += 1
        postsynaptic['AVER'][nextState] += 1
        postsynaptic['AVKL'][nextState] += 1
        postsynaptic['AVKR'][nextState] += 2
        postsynaptic['BAGR'][nextState] += 2
        postsynaptic['DVC'][nextState] += 1
        postsynaptic['OLLL'][nextState] += 1
        postsynaptic['OLQDL'][nextState] += 1
        postsynaptic['OLQVL'][nextState] += 1
        postsynaptic['RIBL'][nextState] += 2
        postsynaptic['RIGR'][nextState] += 3
        postsynaptic['RIR'][nextState] += 2
        postsynaptic['RMEL'][nextState] += 2
        postsynaptic['RMHR'][nextState] += 3
        postsynaptic['URYDL'][nextState] += 1
        postsynaptic['URYVL'][nextState] += 1
        postsynaptic['VB2'][nextState] += 1
        postsynaptic['VD1'][nextState] += 2

def RIGR():
        postsynaptic['AIBL'][nextState] += 3
        postsynaptic['ALNR'][nextState] += 1
        postsynaptic['AQR'][nextState] += 1
        postsynaptic['AVER'][nextState] += 2
        postsynaptic['AVKL'][nextState] += 4
        postsynaptic['AVKR'][nextState] += 2
        postsynaptic['BAGL'][nextState] += 1
        postsynaptic['OLLR'][nextState] += 1
        postsynaptic['OLQDR'][nextState] += 1
        postsynaptic['OLQVR'][nextState] += 1
        postsynaptic['RIBR'][nextState] += 2
        postsynaptic['RIGL'][nextState] += 3
        postsynaptic['RIR'][nextState] += 1
        postsynaptic['RMHL'][nextState] += 4
        postsynaptic['URYDR'][nextState] += 1
        postsynaptic['URYVR'][nextState] += 1

def RIH():
        postsynaptic['ADFR'][nextState] += 1
        postsynaptic['AIZL'][nextState] += 4
        postsynaptic['AIZR'][nextState] += 4
        postsynaptic['AUAR'][nextState] += 1
        postsynaptic['BAGR'][nextState] += 1
        postsynaptic['CEPDL'][nextState] += 2
        postsynaptic['CEPDR'][nextState] += 2
        postsynaptic['CEPVL'][nextState] += 2
        postsynaptic['CEPVR'][nextState] += 2
        postsynaptic['FLPL'][nextState] += 1
        postsynaptic['IL2L'][nextState] += 2
        postsynaptic['IL2R'][nextState] += 1
        postsynaptic['OLQDL'][nextState] += 4
        postsynaptic['OLQDR'][nextState] += 2
        postsynaptic['OLQVL'][nextState] += 1
        postsynaptic['OLQVR'][nextState] += 6
        postsynaptic['RIAL'][nextState] += 10
        postsynaptic['RIAR'][nextState] += 8
        postsynaptic['RIBL'][nextState] += 5
        postsynaptic['RIBR'][nextState] += 4
        postsynaptic['RIPL'][nextState] += 4
        postsynaptic['RIPR'][nextState] += 6
        postsynaptic['RMER'][nextState] += 2
        postsynaptic['RMEV'][nextState] += 1
        postsynaptic['URYVR'][nextState] += 1

def RIML():
        postsynaptic['AIBR'][nextState] += 1
        postsynaptic['AIYL'][nextState] += 1
        postsynaptic['AVAL'][nextState] += 1
        postsynaptic['AVAR'][nextState] += 2
        postsynaptic['AVBL'][nextState] += 2
        postsynaptic['AVBR'][nextState] += 3
        postsynaptic['AVEL'][nextState] += 2
        postsynaptic['AVER'][nextState] += 3
        postsynaptic['MDR05'][nextState] += 2
        postsynaptic['MVR05'][nextState] += 2
        postsynaptic['RIBL'][nextState] += 1
        postsynaptic['RIS'][nextState] += 1
        postsynaptic['RMDL'][nextState] += 1
        postsynaptic['RMDR'][nextState] += 1
        postsynaptic['RMFR'][nextState] += 1
        postsynaptic['SAADR'][nextState] += 1
        postsynaptic['SAAVL'][nextState] += 3
        postsynaptic['SAAVR'][nextState] += 2
        postsynaptic['SMDDR'][nextState] += 5
        postsynaptic['SMDVL'][nextState] += 1

def RIMR():
        postsynaptic['ADAR'][nextState] += 1
        postsynaptic['AIBL'][nextState] += 4
        postsynaptic['AIBL'][nextState] += 1
        postsynaptic['AIYR'][nextState] += 1
        postsynaptic['AVAL'][nextState] += 5
        postsynaptic['AVAR'][nextState] += 1
        postsynaptic['AVBL'][nextState] += 2
        postsynaptic['AVBR'][nextState] += 5
        postsynaptic['AVEL'][nextState] += 3
        postsynaptic['AVER'][nextState] += 2
        postsynaptic['AVJL'][nextState] += 1
        postsynaptic['AVKL'][nextState] += 1
        postsynaptic['MDL05'][nextState] += 1
        postsynaptic['MDL07'][nextState] += 1
        postsynaptic['MVL05'][nextState] += 1
        postsynaptic['MVL07'][nextState] += 1
        postsynaptic['RIBR'][nextState] += 1
        postsynaptic['RIS'][nextState] += 2
        postsynaptic['RMDL'][nextState] += 1
        postsynaptic['RMDR'][nextState] += 1
        postsynaptic['RMFL'][nextState] += 1
        postsynaptic['RMFR'][nextState] += 1
        postsynaptic['SAAVL'][nextState] += 3
        postsynaptic['SAAVR'][nextState] += 3
        postsynaptic['SMDDL'][nextState] += 2
        postsynaptic['SMDDR'][nextState] += 4

def RIPL():
        postsynaptic['OLQDL'][nextState] += 1
        postsynaptic['OLQDR'][nextState] += 1
        postsynaptic['RMED'][nextState] += 1

def RIPR():
        postsynaptic['OLQDL'][nextState] += 1
        postsynaptic['OLQDR'][nextState] += 1
        postsynaptic['RMED'][nextState] += 1

def RIR():
        postsynaptic['AFDR'][nextState] += 1
        postsynaptic['AIZL'][nextState] += 3
        postsynaptic['AIZR'][nextState] += 5
        postsynaptic['AUAL'][nextState] += 1
        postsynaptic['AWBR'][nextState] += 1
        postsynaptic['BAGL'][nextState] += 1
        postsynaptic['BAGR'][nextState] += 2
        postsynaptic['DVA'][nextState] += 2
        postsynaptic['HSNL'][nextState] += 1
        postsynaptic['PVPL'][nextState] += 1
        postsynaptic['RIAL'][nextState] += 5
        postsynaptic['RIAR'][nextState] += 1
        postsynaptic['RIGL'][nextState] += 1
        postsynaptic['URXL'][nextState] += 5
        postsynaptic['URXR'][nextState] += 1

def RIS():
        postsynaptic['AIBR'][nextState] += 1
        postsynaptic['AVEL'][nextState] += 7
        postsynaptic['AVER'][nextState] += 7
        postsynaptic['AVJL'][nextState] += 1
        postsynaptic['AVKL'][nextState] += 1
        postsynaptic['AVKR'][nextState] += 4
        postsynaptic['AVL'][nextState] += 2
        postsynaptic['CEPDR'][nextState] += 1
        postsynaptic['CEPVL'][nextState] += 2
        postsynaptic['CEPVR'][nextState] += 1
        postsynaptic['DB1'][nextState] += 1
        postsynaptic['OLLR'][nextState] += 1
        postsynaptic['RIBL'][nextState] += 3
        postsynaptic['RIBR'][nextState] += 5
        postsynaptic['RIML'][nextState] += 2
        postsynaptic['RIMR'][nextState] += 5
        postsynaptic['RMDDL'][nextState] += 1
        postsynaptic['RMDL'][nextState] += 2
        postsynaptic['RMDR'][nextState] += 4
        postsynaptic['SMDDL'][nextState] += 1
        postsynaptic['SMDDR'][nextState] += 3
        postsynaptic['SMDVL'][nextState] += 1
        postsynaptic['SMDVR'][nextState] += 1
        postsynaptic['URYVR'][nextState] += 1

def RIVL():
        postsynaptic['AIBL'][nextState] += 1
        postsynaptic['MVR05'][nextState] += -2
        postsynaptic['MVR06'][nextState] += -2
        postsynaptic['MVR08'][nextState] += -3
        postsynaptic['RIAL'][nextState] += 1
        postsynaptic['RIAR'][nextState] += 1
        postsynaptic['RIVR'][nextState] += 2
        postsynaptic['RMDL'][nextState] += 2
        postsynaptic['SAADR'][nextState] += 3
        postsynaptic['SDQR'][nextState] += 2
        postsynaptic['SIAVR'][nextState] += 2
        postsynaptic['SMDDR'][nextState] += 1
        postsynaptic['SMDVL'][nextState] += 1

def RIVR():
        postsynaptic['AIBR'][nextState] += 1
        postsynaptic['MVL05'][nextState] += -2
        postsynaptic['MVL06'][nextState] += -2
        postsynaptic['MVL08'][nextState] += -2
        postsynaptic['MVR04'][nextState] += -2
        postsynaptic['MVR06'][nextState] += -2
        postsynaptic['RIAL'][nextState] += 2
        postsynaptic['RIAR'][nextState] += 1
        postsynaptic['RIVL'][nextState] += 2
        postsynaptic['RMDDL'][nextState] += 1
        postsynaptic['RMDR'][nextState] += 1
        postsynaptic['RMDVR'][nextState] += 1
        postsynaptic['RMEV'][nextState] += 1
        postsynaptic['SAADL'][nextState] += 2
        postsynaptic['SDQR'][nextState] += 2
        postsynaptic['SIAVL'][nextState] += 2
        postsynaptic['SMDDL'][nextState] += 2
        postsynaptic['SMDVR'][nextState] += 4

def RMDDL():
        postsynaptic['MDR01'][nextState] += 1
        postsynaptic['MDR02'][nextState] += 1
        postsynaptic['MDR03'][nextState] += 1
        postsynaptic['MDR04'][nextState] += 1
        postsynaptic['MDR08'][nextState] += 2
        postsynaptic['MVR01'][nextState] += 1
        postsynaptic['OLQVL'][nextState] += 1
        postsynaptic['RMDL'][nextState] += 1
        postsynaptic['RMDVL'][nextState] += 1
        postsynaptic['RMDVR'][nextState] += 7
        postsynaptic['SMDDL'][nextState] += 1

def RMDDR():
        postsynaptic['MDL01'][nextState] += 1
        postsynaptic['MDL02'][nextState] += 1
        postsynaptic['MDL03'][nextState] += 2
        postsynaptic['MDL04'][nextState] += 1
        postsynaptic['MDR04'][nextState] += 1
        postsynaptic['MVR01'][nextState] += 1
        postsynaptic['MVR02'][nextState] += 1
        postsynaptic['OLQVR'][nextState] += 1
        postsynaptic['RMDVL'][nextState] += 12
        postsynaptic['RMDVR'][nextState] += 1
        postsynaptic['SAADR'][nextState] += 1
        postsynaptic['SMDDR'][nextState] += 1
        postsynaptic['URYDL'][nextState] += 1

def RMDL():
        postsynaptic['MDL03'][nextState] += 1
        postsynaptic['MDL05'][nextState] += 2
        postsynaptic['MDR01'][nextState] += 1
        postsynaptic['MDR03'][nextState] += 1
        postsynaptic['MVL01'][nextState] += 1
        postsynaptic['MVR01'][nextState] += 1
        postsynaptic['MVR03'][nextState] += 1
        postsynaptic['MVR05'][nextState] += 2
        postsynaptic['MVR07'][nextState] += 1
        postsynaptic['OLLR'][nextState] += 2
        postsynaptic['RIAL'][nextState] += 4
        postsynaptic['RIAR'][nextState] += 3
        postsynaptic['RMDDL'][nextState] += 1
        postsynaptic['RMDDR'][nextState] += 1
        postsynaptic['RMDR'][nextState] += 3
        postsynaptic['RMDVL'][nextState] += 1
        postsynaptic['RMER'][nextState] += 1
        postsynaptic['RMFL'][nextState] += 1

def RMDR():
        postsynaptic['AVKL'][nextState] += 1
        postsynaptic['MDL03'][nextState] += 1
        postsynaptic['MDL05'][nextState] += 1
        postsynaptic['MDR05'][nextState] += 1
        postsynaptic['MVL03'][nextState] += 1
        postsynaptic['MVL05'][nextState] += 1
        postsynaptic['RIAL'][nextState] += 3
        postsynaptic['RIAR'][nextState] += 7
        postsynaptic['RIMR'][nextState] += 2
        postsynaptic['RIS'][nextState] += 1
        postsynaptic['RMDDL'][nextState] += 1
        postsynaptic['RMDL'][nextState] += 1
        postsynaptic['RMDVR'][nextState] += 1

def RMDVL():
        postsynaptic['AVER'][nextState] += 1
        postsynaptic['MDR01'][nextState] += 1
        postsynaptic['MVL04'][nextState] += 1
        postsynaptic['MVR01'][nextState] += 1
        postsynaptic['MVR02'][nextState] += 1
        postsynaptic['MVR03'][nextState] += 1
        postsynaptic['MVR04'][nextState] += 1
        postsynaptic['MVR05'][nextState] += 1
        postsynaptic['MVR06'][nextState] += 1
        postsynaptic['MVR08'][nextState] += 1
        postsynaptic['OLQDL'][nextState] += 1
        postsynaptic['RMDDL'][nextState] += 1
        postsynaptic['RMDDR'][nextState] += 6
        postsynaptic['RMDL'][nextState] += 1
        postsynaptic['RMDVR'][nextState] += 1
        postsynaptic['SAAVL'][nextState] += 1
        postsynaptic['SMDVL'][nextState] += 1

def RMDVR():
        postsynaptic['AVEL'][nextState] += 1
        postsynaptic['AVER'][nextState] += 1
        postsynaptic['MDL01'][nextState] += 1
        postsynaptic['MVL01'][nextState] += 1
        postsynaptic['MVL02'][nextState] += 1
        postsynaptic['MVL03'][nextState] += 1
        postsynaptic['MVL04'][nextState] += 1
        postsynaptic['MVL05'][nextState] += 1
        postsynaptic['MVL06'][nextState] += 1
        postsynaptic['MVL08'][nextState] += 1
        postsynaptic['MVR04'][nextState] += 1
        postsynaptic['MVR06'][nextState] += 1
        postsynaptic['MVR08'][nextState] += 1
        postsynaptic['OLQDR'][nextState] += 1
        postsynaptic['RMDDL'][nextState] += 4
        postsynaptic['RMDDR'][nextState] += 1
        postsynaptic['RMDR'][nextState] += 1
        postsynaptic['RMDVL'][nextState] += 1
        postsynaptic['SAAVR'][nextState] += 1
        postsynaptic['SIBDR'][nextState] += 1
        postsynaptic['SIBVR'][nextState] += 1
        postsynaptic['SMDVR'][nextState] += 1

def RMED():
        postsynaptic['IL1VL'][nextState] += 1
        postsynaptic['MVL02'][nextState] += -4
        postsynaptic['MVL04'][nextState] += -4
        postsynaptic['MVL06'][nextState] += -4
        postsynaptic['MVR02'][nextState] += -4
        postsynaptic['MVR04'][nextState] += -4
        postsynaptic['RIBL'][nextState] += 1
        postsynaptic['RIBR'][nextState] += 1
        postsynaptic['RIPL'][nextState] += 1
        postsynaptic['RIPR'][nextState] += 1
        postsynaptic['RMEV'][nextState] += 2

def RMEL():
        postsynaptic['MDR01'][nextState] += -5
        postsynaptic['MDR03'][nextState] += -5
        postsynaptic['MVR01'][nextState] += -5
        postsynaptic['MVR03'][nextState] += -5
        postsynaptic['RIGL'][nextState] += 1
        postsynaptic['RMEV'][nextState] += 1

def RMER():
        postsynaptic['MDL01'][nextState] += -7
        postsynaptic['MDL03'][nextState] += -7
        postsynaptic['MVL01'][nextState] += -7
        postsynaptic['RMEV'][nextState] += 1

def RMEV():
        postsynaptic['AVEL'][nextState] += 1
        postsynaptic['AVER'][nextState] += 1
        postsynaptic['IL1DL'][nextState] += 1
        postsynaptic['IL1DR'][nextState] += 1
        postsynaptic['MDL02'][nextState] += -3
        postsynaptic['MDL04'][nextState] += -3
        postsynaptic['MDL06'][nextState] += -3
        postsynaptic['MDR02'][nextState] += -3
        postsynaptic['MDR04'][nextState] += -3
        postsynaptic['RMED'][nextState] += 2
        postsynaptic['RMEL'][nextState] += 1
        postsynaptic['RMER'][nextState] += 1
        postsynaptic['SMDDR'][nextState] += 1

def RMFL():
        postsynaptic['AVKL'][nextState] += 4
        postsynaptic['AVKR'][nextState] += 4
        postsynaptic['MDR03'][nextState] += 1
        postsynaptic['MVR01'][nextState] += 1
        postsynaptic['MVR03'][nextState] += 1
        postsynaptic['PVT'][nextState] += 1
        postsynaptic['RIGR'][nextState] += 1
        postsynaptic['RMDR'][nextState] += 3
        postsynaptic['RMGR'][nextState] += 1
        postsynaptic['URBR'][nextState] += 1

def RMFR():
        postsynaptic['AVKL'][nextState] += 3
        postsynaptic['AVKR'][nextState] += 3
        postsynaptic['RMDL'][nextState] += 2

def RMGL():
        postsynaptic['ADAL'][nextState] += 1
        postsynaptic['ADLL'][nextState] += 1
        postsynaptic['AIBR'][nextState] += 1
        postsynaptic['ALML'][nextState] += 1
        postsynaptic['ALNL'][nextState] += 1
        postsynaptic['ASHL'][nextState] += 2
        postsynaptic['ASKL'][nextState] += 2
        postsynaptic['AVAL'][nextState] += 1
        postsynaptic['AVBR'][nextState] += 2
        postsynaptic['AVEL'][nextState] += 2
        postsynaptic['AWBL'][nextState] += 1
        postsynaptic['CEPDL'][nextState] += 1
        postsynaptic['IL2L'][nextState] += 1
        postsynaptic['MDL05'][nextState] += 2
        postsynaptic['MVL05'][nextState] += 2
        postsynaptic['RID'][nextState] += 1
        postsynaptic['RMDL'][nextState] += 1
        postsynaptic['RMDR'][nextState] += 3
        postsynaptic['RMDVL'][nextState] += 3
        postsynaptic['RMHL'][nextState] += 3
        postsynaptic['RMHR'][nextState] += 1
        postsynaptic['SIAVL'][nextState] += 1
        postsynaptic['SIBVL'][nextState] += 3
        postsynaptic['SIBVR'][nextState] += 1
        postsynaptic['SMBVL'][nextState] += 1
        postsynaptic['URXL'][nextState] += 2

def RMGR():
        postsynaptic['ADAR'][nextState] += 1
        postsynaptic['AIMR'][nextState] += 1
        postsynaptic['ALNR'][nextState] += 1
        postsynaptic['ASHR'][nextState] += 2
        postsynaptic['ASKR'][nextState] += 1
        postsynaptic['AVAR'][nextState] += 1
        postsynaptic['AVBR'][nextState] += 1
        postsynaptic['AVDL'][nextState] += 1
        postsynaptic['AVER'][nextState] += 3
        postsynaptic['AVJL'][nextState] += 1
        postsynaptic['AWBR'][nextState] += 1
        postsynaptic['IL2R'][nextState] += 1
        postsynaptic['MDR05'][nextState] += 1
        postsynaptic['MVR05'][nextState] += 1
        postsynaptic['MVR07'][nextState] += 1
        postsynaptic['RIR'][nextState] += 1
        postsynaptic['RMDL'][nextState] += 4
        postsynaptic['RMDR'][nextState] += 2
        postsynaptic['RMDVR'][nextState] += 5
        postsynaptic['RMHR'][nextState] += 1
        postsynaptic['URXR'][nextState] += 2

def RMHL():
        postsynaptic['MDR01'][nextState] += 2
        postsynaptic['MDR03'][nextState] += 3
        postsynaptic['MVR01'][nextState] += 2
        postsynaptic['RMDR'][nextState] += 1
        postsynaptic['RMGL'][nextState] += 3
        postsynaptic['SIBVR'][nextState] += 1

def RMHR():
        postsynaptic['MDL01'][nextState] += 2
        postsynaptic['MDL03'][nextState] += 2
        postsynaptic['MDL05'][nextState] += 2
        postsynaptic['MVL01'][nextState] += 2
        postsynaptic['RMER'][nextState] += 1
        postsynaptic['RMGL'][nextState] += 1
        postsynaptic['RMGR'][nextState] += 1

def SAADL():
        postsynaptic['AIBL'][nextState] += 1
        postsynaptic['AVAL'][nextState] += 6
        postsynaptic['RIML'][nextState] += 3
        postsynaptic['RIMR'][nextState] += 6
        postsynaptic['RMGR'][nextState] += 1
        postsynaptic['SMBDL'][nextState] += 1

def SAADR():
        postsynaptic['AIBR'][nextState] += 1
        postsynaptic['AVAR'][nextState] += 3
        postsynaptic['OLLL'][nextState] += 1
        postsynaptic['RIML'][nextState] += 4
        postsynaptic['RIMR'][nextState] += 5
        postsynaptic['RMDDR'][nextState] += 1
        postsynaptic['RMFL'][nextState] += 1
        postsynaptic['RMGL'][nextState] += 1

def SAAVL():
        postsynaptic['AIBL'][nextState] += 1
        postsynaptic['ALNL'][nextState] += 1
        postsynaptic['AVAL'][nextState] += 16
        postsynaptic['OLLR'][nextState] += 1
        postsynaptic['RIML'][nextState] += 2
        postsynaptic['RIMR'][nextState] += 12
        postsynaptic['RMDVL'][nextState] += 2
        postsynaptic['RMFR'][nextState] += 2
        postsynaptic['SMBVR'][nextState] += 3
        postsynaptic['SMDDR'][nextState] += 8

def SAAVR():
        postsynaptic['AVAR'][nextState] += 13
        postsynaptic['RIML'][nextState] += 5
        postsynaptic['RIMR'][nextState] += 2
        postsynaptic['RMDVR'][nextState] += 1
        postsynaptic['SMBVL'][nextState] += 2
        postsynaptic['SMDDL'][nextState] += 6

def SABD():
        postsynaptic['AVAL'][nextState] += 4
        postsynaptic['VA2'][nextState] += 4
        postsynaptic['VA3'][nextState] += 2
        postsynaptic['VA4'][nextState] += 1

def SABVL():
        postsynaptic['AVAR'][nextState] += 3
        postsynaptic['DA1'][nextState] += 2
        postsynaptic['DA2'][nextState] += 1

def SABVR():
        postsynaptic['AVAL'][nextState] += 1
        postsynaptic['AVAR'][nextState] += 1
        postsynaptic['DA1'][nextState] += 3

def SDQL():
        postsynaptic['ALML'][nextState] += 2
        postsynaptic['AVAL'][nextState] += 1
        postsynaptic['AVAR'][nextState] += 3
        postsynaptic['AVEL'][nextState] += 1
        postsynaptic['FLPL'][nextState] += 1
        postsynaptic['RICR'][nextState] += 1
        postsynaptic['RIS'][nextState] += 3
        postsynaptic['RMFL'][nextState] += 1
        postsynaptic['SDQR'][nextState] += 1

def SDQR():
        postsynaptic['ADLL'][nextState] += 1
        postsynaptic['AIBL'][nextState] += 2
        postsynaptic['AVAL'][nextState] += 3
        postsynaptic['AVBL'][nextState] += 7
        postsynaptic['AVBR'][nextState] += 4
        postsynaptic['DVA'][nextState] += 3
        postsynaptic['RICR'][nextState] += 1
        postsynaptic['RIVL'][nextState] += 2
        postsynaptic['RIVR'][nextState] += 2
        postsynaptic['RMHL'][nextState] += 2
        postsynaptic['RMHR'][nextState] += 1
        postsynaptic['SDQL'][nextState] += 1
        postsynaptic['SIBVL'][nextState] += 1

def SIADL():
        postsynaptic['RIBL'][nextState] += 1

def SIADR():
        postsynaptic['RIBR'][nextState] += 1

def SIAVL():
        postsynaptic['RIBL'][nextState] += 1

def SIAVR():
        postsynaptic['RIBR'][nextState] += 1

def SIBDL():
        postsynaptic['RIBL'][nextState] += 1
        postsynaptic['SIBVL'][nextState] += 1

def SIBDR():
        postsynaptic['AIML'][nextState] += 1
        postsynaptic['RIBR'][nextState] += 1
        postsynaptic['SIBVR'][nextState] += 1

def SIBVL():
        postsynaptic['AVBL'][nextState] += 1
        postsynaptic['AVBR'][nextState] += 1
        postsynaptic['RIBL'][nextState] += 1
        postsynaptic['SDQR'][nextState] += 1
        postsynaptic['SIBDL'][nextState] += 1

def SIBVR():
        postsynaptic['RIBL'][nextState] += 1
        postsynaptic['RIBR'][nextState] += 1
        postsynaptic['RMHL'][nextState] += 1
        postsynaptic['SIBDR'][nextState] += 1

def SMBDL():
        postsynaptic['AVAR'][nextState] += 1
        postsynaptic['AVKL'][nextState] += 1
        postsynaptic['AVKR'][nextState] += 1
        postsynaptic['MDR01'][nextState] += 2
        postsynaptic['MDR02'][nextState] += 2
        postsynaptic['MDR03'][nextState] += 2
        postsynaptic['MDR04'][nextState] += 2
        postsynaptic['MDR06'][nextState] += 3
        postsynaptic['RIBL'][nextState] += 1
        postsynaptic['RMED'][nextState] += 3
        postsynaptic['SAADL'][nextState] += 1
        postsynaptic['SAAVR'][nextState] += 1

def SMBDR():
        postsynaptic['ALNL'][nextState] += 1
        postsynaptic['AVAL'][nextState] += 1
        postsynaptic['AVKL'][nextState] += 1
        postsynaptic['AVKR'][nextState] += 2
        postsynaptic['MDL02'][nextState] += 1
        postsynaptic['MDL03'][nextState] += 1
        postsynaptic['MDL04'][nextState] += 1
        postsynaptic['MDL06'][nextState] += 2
        postsynaptic['MDR04'][nextState] += 1
        postsynaptic['MDR08'][nextState] += 1
        postsynaptic['RIBR'][nextState] += 1
        postsynaptic['RMED'][nextState] += 4
        postsynaptic['SAAVL'][nextState] += 3

def SMBVL():
        postsynaptic['MVL01'][nextState] += 1
        postsynaptic['MVL02'][nextState] += 1
        postsynaptic['MVL03'][nextState] += 1
        postsynaptic['MVL04'][nextState] += 1
        postsynaptic['MVL05'][nextState] += 1
        postsynaptic['MVL06'][nextState] += 1
        postsynaptic['MVL08'][nextState] += 1
        postsynaptic['PLNL'][nextState] += 1
        postsynaptic['RMEV'][nextState] += 5
        postsynaptic['SAADL'][nextState] += 3
        postsynaptic['SAAVR'][nextState] += 2

def SMBVR():
        postsynaptic['AVKL'][nextState] += 1
        postsynaptic['AVKR'][nextState] += 1
        postsynaptic['MVR01'][nextState] += 1
        postsynaptic['MVR02'][nextState] += 1
        postsynaptic['MVR03'][nextState] += 1
        postsynaptic['MVR04'][nextState] += 1
        postsynaptic['MVR06'][nextState] += 1
        postsynaptic['MVR07'][nextState] += 1
        postsynaptic['RMEV'][nextState] += 3
        postsynaptic['SAADR'][nextState] += 4
        postsynaptic['SAAVL'][nextState] += 3

def SMDDL():
        postsynaptic['MDL04'][nextState] += 1
        postsynaptic['MDL06'][nextState] += 1
        postsynaptic['MDL08'][nextState] += 1
        postsynaptic['MDR02'][nextState] += 1
        postsynaptic['MDR03'][nextState] += 1
        postsynaptic['MDR04'][nextState] += 1
        postsynaptic['MDR05'][nextState] += 1
        postsynaptic['MDR06'][nextState] += 1
        postsynaptic['MDR07'][nextState] += 1
        postsynaptic['MVL02'][nextState] += 1
        postsynaptic['MVL04'][nextState] += 1
        postsynaptic['RIAL'][nextState] += 1
        postsynaptic['RIAR'][nextState] += 1
        postsynaptic['RIBL'][nextState] += 1
        postsynaptic['RIBR'][nextState] += 1
        postsynaptic['RIS'][nextState] += 1
        postsynaptic['RMDDL'][nextState] += 1
        postsynaptic['SMDVR'][nextState] += 2

def SMDDR():
        postsynaptic['MDL04'][nextState] += 1
        postsynaptic['MDL05'][nextState] += 1
        postsynaptic['MDL06'][nextState] += 1
        postsynaptic['MDL08'][nextState] += 1
        postsynaptic['MDR04'][nextState] += 1
        postsynaptic['MDR06'][nextState] += 1
        postsynaptic['MVR02'][nextState] += 1
        postsynaptic['RIAL'][nextState] += 2
        postsynaptic['RIAR'][nextState] += 1
        postsynaptic['RIBR'][nextState] += 1
        postsynaptic['RIS'][nextState] += 1
        postsynaptic['RMDDR'][nextState] += 1
        postsynaptic['VD1'][nextState] += 1

def SMDVL():
        postsynaptic['MVL03'][nextState] += 1
        postsynaptic['MVL06'][nextState] += 1
        postsynaptic['MVR02'][nextState] += 1
        postsynaptic['MVR03'][nextState] += 1
        postsynaptic['MVR04'][nextState] += 1
        postsynaptic['MVR06'][nextState] += 1
        postsynaptic['PVR'][nextState] += 1
        postsynaptic['RIAL'][nextState] += 3
        postsynaptic['RIAR'][nextState] += 8
        postsynaptic['RIBR'][nextState] += 2
        postsynaptic['RIS'][nextState] += 1
        postsynaptic['RIVL'][nextState] += 2
        postsynaptic['RMDDR'][nextState] += 1
        postsynaptic['RMDVL'][nextState] += 1
        postsynaptic['SMDDR'][nextState] += 4
        postsynaptic['SMDVR'][nextState] += 1

def SMDVR():
        postsynaptic['MVL02'][nextState] += 1
        postsynaptic['MVL03'][nextState] += 1
        postsynaptic['MVL04'][nextState] += 1
        postsynaptic['MVR07'][nextState] += 1
        postsynaptic['RIAL'][nextState] += 7
        postsynaptic['RIAR'][nextState] += 5
        postsynaptic['RIBL'][nextState] += 2
        postsynaptic['RIVR'][nextState] += 1
        postsynaptic['RIVR'][nextState] += 2
        postsynaptic['RMDDL'][nextState] += 1
        postsynaptic['RMDVR'][nextState] += 1
        postsynaptic['SMDDL'][nextState] += 2
        postsynaptic['SMDVL'][nextState] += 1
        postsynaptic['VB1'][nextState] += 1

def URADL():
        postsynaptic['IL1DL'][nextState] += 2
        postsynaptic['MDL02'][nextState] += 2
        postsynaptic['MDL03'][nextState] += 2
        postsynaptic['MDL04'][nextState] += 2
        postsynaptic['RIPL'][nextState] += 3
        postsynaptic['RMEL'][nextState] += 1

def URADR():
        postsynaptic['IL1DR'][nextState] += 1
        postsynaptic['MDR01'][nextState] += 3
        postsynaptic['MDR02'][nextState] += 2
        postsynaptic['MDR03'][nextState] += 3
        postsynaptic['RIPR'][nextState] += 3
        postsynaptic['RMDVR'][nextState] += 1
        postsynaptic['RMED'][nextState] += 1
        postsynaptic['RMER'][nextState] += 1
        postsynaptic['URYDR'][nextState] += 1

def URAVL():
        postsynaptic['MVL01'][nextState] += 2
        postsynaptic['MVL02'][nextState] += 2
        postsynaptic['MVL03'][nextState] += 3
        postsynaptic['MVL04'][nextState] += 2
        postsynaptic['RIPL'][nextState] += 3
        postsynaptic['RMEL'][nextState] += 1
        postsynaptic['RMER'][nextState] += 1
        postsynaptic['RMEV'][nextState] += 2

def URAVR():
        postsynaptic['IL1R'][nextState] += 1
        postsynaptic['MVR01'][nextState] += 2
        postsynaptic['MVR02'][nextState] += 2
        postsynaptic['MVR03'][nextState] += 2
        postsynaptic['MVR04'][nextState] += 2
        postsynaptic['RIPR'][nextState] += 3
        postsynaptic['RMDVL'][nextState] += 1
        postsynaptic['RMER'][nextState] += 2
        postsynaptic['RMEV'][nextState] += 2

def URBL():
        postsynaptic['AVBL'][nextState] += 1
        postsynaptic['CEPDL'][nextState] += 1
        postsynaptic['IL1L'][nextState] += 1
        postsynaptic['OLQDL'][nextState] += 1
        postsynaptic['OLQVL'][nextState] += 1
        postsynaptic['RICR'][nextState] += 1
        postsynaptic['RMDDR'][nextState] += 1
        postsynaptic['SIAVL'][nextState] += 1
        postsynaptic['SMBDR'][nextState] += 1
        postsynaptic['URXL'][nextState] += 2

def URBR():
        postsynaptic['ADAR'][nextState] += 1
        postsynaptic['AVBR'][nextState] += 1
        postsynaptic['CEPDR'][nextState] += 1
        postsynaptic['IL1R'][nextState] += 3
        postsynaptic['IL2R'][nextState] += 1
        postsynaptic['OLQDR'][nextState] += 1
        postsynaptic['OLQVR'][nextState] += 1
        postsynaptic['RICR'][nextState] += 1
        postsynaptic['RMDL'][nextState] += 1
        postsynaptic['RMDR'][nextState] += 1
        postsynaptic['RMFL'][nextState] += 1
        postsynaptic['SIAVR'][nextState] += 2
        postsynaptic['SMBDL'][nextState] += 1
        postsynaptic['URXR'][nextState] += 4

def URXL():
        postsynaptic['ASHL'][nextState] += 1
        postsynaptic['AUAL'][nextState] += 5
        postsynaptic['AVBL'][nextState] += 1
        postsynaptic['AVEL'][nextState] += 4
        postsynaptic['AVJR'][nextState] += 1
        postsynaptic['RIAL'][nextState] += 8
        postsynaptic['RICL'][nextState] += 1
        postsynaptic['RIGL'][nextState] += 3
        postsynaptic['RMGL'][nextState] += 2
        postsynaptic['RMGL'][nextState] += 1

def URXR():
        postsynaptic['AUAR'][nextState] += 4
        postsynaptic['AVBL'][nextState] += 1
        postsynaptic['AVBR'][nextState] += 2
        postsynaptic['AVER'][nextState] += 2
        postsynaptic['IL2R'][nextState] += 1
        postsynaptic['OLQVR'][nextState] += 1
        postsynaptic['RIAR'][nextState] += 3
        postsynaptic['RIGR'][nextState] += 2
        postsynaptic['RIPR'][nextState] += 3
        postsynaptic['RMDR'][nextState] += 1
        postsynaptic['RMGR'][nextState] += 2
        postsynaptic['SIAVR'][nextState] += 1

def URYDL():
        postsynaptic['AVAL'][nextState] += 1
        postsynaptic['AVER'][nextState] += 2
        postsynaptic['RIBL'][nextState] += 1
        postsynaptic['RIGL'][nextState] += 1
        postsynaptic['RMDDR'][nextState] += 4
        postsynaptic['RMDVL'][nextState] += 6
        postsynaptic['SMDDL'][nextState] += 1
        postsynaptic['SMDDR'][nextState] += 1

def URYDR():
        postsynaptic['AVAR'][nextState] += 1
        postsynaptic['AVEL'][nextState] += 2
        postsynaptic['AVER'][nextState] += 2
        postsynaptic['RIBR'][nextState] += 1
        postsynaptic['RIGR'][nextState] += 1
        postsynaptic['RMDDL'][nextState] += 3
        postsynaptic['RMDVR'][nextState] += 5
        postsynaptic['SMDDL'][nextState] += 4

def URYVL():
        postsynaptic['AVAR'][nextState] += 1
        postsynaptic['AVBR'][nextState] += 1
        postsynaptic['AVER'][nextState] += 5
        postsynaptic['IL1VL'][nextState] += 1
        postsynaptic['RIAL'][nextState] += 1
        postsynaptic['RIBL'][nextState] += 2
        postsynaptic['RIGL'][nextState] += 1
        postsynaptic['RIH'][nextState] += 1
        postsynaptic['RIS'][nextState] += 1
        postsynaptic['RMDDL'][nextState] += 4
        postsynaptic['RMDVR'][nextState] += 2
        postsynaptic['SIBVR'][nextState] += 1
        postsynaptic['SMDVR'][nextState] += 4

def URYVR():
        postsynaptic['AVAL'][nextState] += 2
        postsynaptic['AVEL'][nextState] += 6
        postsynaptic['IL1VR'][nextState] += 1
        postsynaptic['RIAR'][nextState] += 1
        postsynaptic['RIBR'][nextState] += 1
        postsynaptic['RIGR'][nextState] += 1
        postsynaptic['RMDDR'][nextState] += 6
        postsynaptic['RMDVL'][nextState] += 4
        postsynaptic['SIBDR'][nextState] += 1
        postsynaptic['SIBVL'][nextState] += 1
        postsynaptic['SMDVL'][nextState] += 3

def VA1():
        postsynaptic['AVAL'][nextState] += 3
        postsynaptic['DA2'][nextState] += 2
        postsynaptic['DD1'][nextState] += 9
        postsynaptic['MVL07'][nextState] += 3
        postsynaptic['MVL08'][nextState] += 3
        postsynaptic['MVR07'][nextState] += 3
        postsynaptic['MVR08'][nextState] += 3
        postsynaptic['VD1'][nextState] += 2

def VA2():
        postsynaptic['AVAL'][nextState] += 5
        postsynaptic['DD1'][nextState] += 13
        postsynaptic['MVL07'][nextState] += 5
        postsynaptic['MVL10'][nextState] += 5
        postsynaptic['MVR07'][nextState] += 5
        postsynaptic['MVR10'][nextState] += 5
        postsynaptic['SABD'][nextState] += 3
        postsynaptic['VA3'][nextState] += 2
        postsynaptic['VB1'][nextState] += 2
        postsynaptic['VD1'][nextState] += 2
        postsynaptic['VD1'][nextState] += 1
        postsynaptic['VD2'][nextState] += 11

def VA3():
        postsynaptic['AS1'][nextState] += 1
        postsynaptic['AVAL'][nextState] += 1
        postsynaptic['AVAR'][nextState] += 2
        postsynaptic['DD1'][nextState] += 18
        postsynaptic['DD2'][nextState] += 11
        postsynaptic['MVL09'][nextState] += 5
        postsynaptic['MVL10'][nextState] += 5
        postsynaptic['MVL12'][nextState] += 5
        postsynaptic['MVR09'][nextState] += 5
        postsynaptic['MVR10'][nextState] += 5
        postsynaptic['MVR12'][nextState] += 5
        postsynaptic['SABD'][nextState] += 2
        postsynaptic['VA4'][nextState] += 1
        postsynaptic['VD2'][nextState] += 3
        postsynaptic['VD3'][nextState] += 3

def VA4():
        postsynaptic['AS2'][nextState] += 2
        postsynaptic['AVAL'][nextState] += 1
        postsynaptic['AVAR'][nextState] += 2
        postsynaptic['AVDL'][nextState] += 1
        postsynaptic['DA5'][nextState] += 1
        postsynaptic['DD2'][nextState] += 21
        postsynaptic['MVL11'][nextState] += 6
        postsynaptic['MVL12'][nextState] += 6
        postsynaptic['MVR11'][nextState] += 6
        postsynaptic['MVR12'][nextState] += 6
        postsynaptic['SABD'][nextState] += 1
        postsynaptic['VB3'][nextState] += 2
        postsynaptic['VD4'][nextState] += 3
        
def VA5():
        postsynaptic['AS3'][nextState] += 2
        postsynaptic['AVAL'][nextState] += 5
        postsynaptic['AVAR'][nextState] += 3
        postsynaptic['DA5'][nextState] += 2
        postsynaptic['DD2'][nextState] += 5
        postsynaptic['DD3'][nextState] += 13
        postsynaptic['MVL11'][nextState] += 5
        postsynaptic['MVL14'][nextState] += 5
        postsynaptic['MVR11'][nextState] += 5
        postsynaptic['MVR14'][nextState] += 5
        postsynaptic['VD5'][nextState] += 2

def VA6():
        postsynaptic['AVAL'][nextState] += 6
        postsynaptic['AVAR'][nextState] += 2
        postsynaptic['DD3'][nextState] += 24
        postsynaptic['MVL13'][nextState] += 5
        postsynaptic['MVL14'][nextState] += 5
        postsynaptic['MVR13'][nextState] += 5
        postsynaptic['MVR14'][nextState] += 5
        postsynaptic['VB5'][nextState] += 2
        postsynaptic['VD5'][nextState] += 1
        postsynaptic['VD6'][nextState] += 2

def VA7():
        postsynaptic['AS5'][nextState] += 1
        postsynaptic['AVAL'][nextState] += 2
        postsynaptic['AVAR'][nextState] += 4
        postsynaptic['DD3'][nextState] += 3
        postsynaptic['DD4'][nextState] += 12
        postsynaptic['MVL13'][nextState] += 4
        postsynaptic['MVL15'][nextState] += 4
        postsynaptic['MVL16'][nextState] += 4
        postsynaptic['MVR13'][nextState] += 4
        postsynaptic['MVR15'][nextState] += 4
        postsynaptic['MVR16'][nextState] += 4
        postsynaptic['MVULVA'][nextState] += 4
        postsynaptic['VB3'][nextState] += 1
        postsynaptic['VD7'][nextState] += 9

def VA8():
        postsynaptic['AS6'][nextState] += 1
        postsynaptic['AVAL'][nextState] += 10
        postsynaptic['AVAR'][nextState] += 4
        postsynaptic['AVBR'][nextState] += 1
        postsynaptic['DD4'][nextState] += 21
        postsynaptic['MVL15'][nextState] += 6
        postsynaptic['MVL16'][nextState] += 6
        postsynaptic['MVR15'][nextState] += 6
        postsynaptic['MVR16'][nextState] += 6
        postsynaptic['PDER'][nextState] += 1
        postsynaptic['PVCR'][nextState] += 2
        postsynaptic['VA8'][nextState] += 1
        postsynaptic['VA9'][nextState] += 1
        postsynaptic['VB6'][nextState] += 1
        postsynaptic['VB8'][nextState] += 1
        postsynaptic['VB8'][nextState] += 3
        postsynaptic['VB9'][nextState] += 3
        postsynaptic['VD7'][nextState] += 5
        postsynaptic['VD8'][nextState] += 5
        postsynaptic['VD8'][nextState] += 1

def VA9():
        postsynaptic['AVAL'][nextState] += 1
        postsynaptic['AVBR'][nextState] += 1
        postsynaptic['DD4'][nextState] += 3
        postsynaptic['DD5'][nextState] += 15
        postsynaptic['DVB'][nextState] += 1
        postsynaptic['DVC'][nextState] += 1
        postsynaptic['MVL15'][nextState] += 5
        postsynaptic['MVL18'][nextState] += 5
        postsynaptic['MVR15'][nextState] += 5
        postsynaptic['MVR18'][nextState] += 5
        postsynaptic['PVCR'][nextState] += 1
        postsynaptic['PVT'][nextState] += 1
        postsynaptic['VB8'][nextState] += 6
        postsynaptic['VB8'][nextState] += 1
        postsynaptic['VB9'][nextState] += 4
        postsynaptic['VD7'][nextState] += 1
        postsynaptic['VD9'][nextState] += 10


def VA10():
        postsynaptic['AVAL'][nextState] += 1
        postsynaptic['AVAR'][nextState] += 1
        postsynaptic['MVL17'][nextState] += 5
        postsynaptic['MVL18'][nextState] += 5
        postsynaptic['MVR17'][nextState] += 5
        postsynaptic['MVR18'][nextState] += 5

def VA11():
        postsynaptic['AVAL'][nextState] += 1
        postsynaptic['AVAR'][nextState] += 7
        postsynaptic['DD6'][nextState] += 10
        postsynaptic['MVL19'][nextState] += 5
        postsynaptic['MVL20'][nextState] += 5
        postsynaptic['MVR19'][nextState] += 5
        postsynaptic['MVR20'][nextState] += 5
        postsynaptic['PVNR'][nextState] += 2
        postsynaptic['VB10'][nextState] += 1
        postsynaptic['VD12'][nextState] += 4

def VA12():
        postsynaptic['AS11'][nextState] += 2
        postsynaptic['AVAR'][nextState] += 1
        postsynaptic['DA8'][nextState] += 3
        postsynaptic['DA9'][nextState] += 5
        postsynaptic['DB7'][nextState] += 4
        postsynaptic['DD6'][nextState] += 2
        postsynaptic['LUAL'][nextState] += 2
        postsynaptic['MVL21'][nextState] += 5
        postsynaptic['MVL22'][nextState] += 5
        postsynaptic['MVL23'][nextState] += 5
        postsynaptic['MVR21'][nextState] += 5
        postsynaptic['MVR22'][nextState] += 5
        postsynaptic['MVR23'][nextState] += 5
        postsynaptic['MVR24'][nextState] += 5
        postsynaptic['PHCL'][nextState] += 1
        postsynaptic['PHCR'][nextState] += 1
        postsynaptic['PVCL'][nextState] += 2
        postsynaptic['PVCR'][nextState] += 3
        postsynaptic['VA11'][nextState] += 1
        postsynaptic['VB11'][nextState] += 1
        postsynaptic['VD12'][nextState] += 3
        postsynaptic['VD13'][nextState] += 11

def VB1():
        postsynaptic['AIBR'][nextState] += 1
        postsynaptic['AVBL'][nextState] += 1
        postsynaptic['AVKL'][nextState] += 4
        postsynaptic['DB2'][nextState] += 2
        postsynaptic['DD1'][nextState] += 1
        postsynaptic['DVA'][nextState] += 1
        postsynaptic['MVL07'][nextState] += 1
        postsynaptic['MVL08'][nextState] += 1
        postsynaptic['MVR07'][nextState] += 1
        postsynaptic['MVR08'][nextState] += 1
        postsynaptic['RIML'][nextState] += 2
        postsynaptic['RMFL'][nextState] += 2
        postsynaptic['SAADL'][nextState] += 9
        postsynaptic['SAADR'][nextState] += 2
        postsynaptic['SABD'][nextState] += 1
        postsynaptic['SMDVR'][nextState] += 1
        postsynaptic['VA1'][nextState] += 3
        postsynaptic['VA3'][nextState] += 1
        postsynaptic['VB2'][nextState] += 4
        postsynaptic['VD1'][nextState] += 3
        postsynaptic['VD2'][nextState] += 1

def VB2():
        postsynaptic['AVBL'][nextState] += 3
        postsynaptic['AVBR'][nextState] += 1
        postsynaptic['DB4'][nextState] += 1
        postsynaptic['DD1'][nextState] += 20
        postsynaptic['DD2'][nextState] += 1
        postsynaptic['MVL07'][nextState] += 4
        postsynaptic['MVL09'][nextState] += 4
        postsynaptic['MVL10'][nextState] += 4
        postsynaptic['MVL12'][nextState] += 4
        postsynaptic['MVR07'][nextState] += 4
        postsynaptic['MVR09'][nextState] += 4
        postsynaptic['MVR10'][nextState] += 4
        postsynaptic['MVR12'][nextState] += 4
        postsynaptic['RIGL'][nextState] += 1
        postsynaptic['VA2'][nextState] += 1
        postsynaptic['VB1'][nextState] += 4
        postsynaptic['VB3'][nextState] += 1
        postsynaptic['VB5'][nextState] += 1
        postsynaptic['VB7'][nextState] += 2
        postsynaptic['VC2'][nextState] += 1
        postsynaptic['VD2'][nextState] += 9
        postsynaptic['VD3'][nextState] += 3

def VB3():
        postsynaptic['AVBR'][nextState] += 1
        postsynaptic['DB1'][nextState] += 1
        postsynaptic['DD2'][nextState] += 37
        postsynaptic['MVL11'][nextState] += 6
        postsynaptic['MVL12'][nextState] += 6
        postsynaptic['MVL14'][nextState] += 6
        postsynaptic['MVR11'][nextState] += 6
        postsynaptic['MVR12'][nextState] += 6
        postsynaptic['MVR14'][nextState] += 6
        postsynaptic['VA4'][nextState] += 1
        postsynaptic['VA7'][nextState] += 1
        postsynaptic['VB2'][nextState] += 1

def VB4():
        postsynaptic['AVBL'][nextState] += 1
        postsynaptic['AVBR'][nextState] += 1
        postsynaptic['DB1'][nextState] += 1
        postsynaptic['DB4'][nextState] += 1
        postsynaptic['DD2'][nextState] += 6
        postsynaptic['DD3'][nextState] += 16
        postsynaptic['MVL11'][nextState] += 5
        postsynaptic['MVL14'][nextState] += 5
        postsynaptic['MVR11'][nextState] += 5
        postsynaptic['MVR14'][nextState] += 5
        postsynaptic['VB5'][nextState] += 1

def VB5():
        postsynaptic['AVBL'][nextState] += 1
        postsynaptic['DD3'][nextState] += 27
        postsynaptic['MVL13'][nextState] += 6
        postsynaptic['MVL14'][nextState] += 6
        postsynaptic['MVR13'][nextState] += 6
        postsynaptic['MVR14'][nextState] += 6
        postsynaptic['VB2'][nextState] += 1
        postsynaptic['VB4'][nextState] += 1
        postsynaptic['VB6'][nextState] += 8

def VB6():
        postsynaptic['AVBL'][nextState] += 1
        postsynaptic['AVBR'][nextState] += 2
        postsynaptic['DA4'][nextState] += 1
        postsynaptic['DD4'][nextState] += 30
        postsynaptic['MVL15'][nextState] += 6
        postsynaptic['MVL16'][nextState] += 6
        postsynaptic['MVR15'][nextState] += 6
        postsynaptic['MVR16'][nextState] += 6
        postsynaptic['MVULVA'][nextState] += 6
        postsynaptic['VA8'][nextState] += 1
        postsynaptic['VB5'][nextState] += 1
        postsynaptic['VB7'][nextState] += 1
        postsynaptic['VD6'][nextState] += 1
        postsynaptic['VD7'][nextState] += 8

def VB7():
        postsynaptic['AVBL'][nextState] += 2
        postsynaptic['AVBR'][nextState] += 2
        postsynaptic['DD4'][nextState] += 2
        postsynaptic['MVL15'][nextState] += 5
        postsynaptic['MVR15'][nextState] += 5
        postsynaptic['VB2'][nextState] += 2

def VB8():
        postsynaptic['AVBL'][nextState] += 7
        postsynaptic['AVBR'][nextState] += 3
        postsynaptic['DD5'][nextState] += 30
        postsynaptic['MVL17'][nextState] += 5
        postsynaptic['MVL18'][nextState] += 5
        postsynaptic['MVL20'][nextState] += 5
        postsynaptic['MVR17'][nextState] += 5
        postsynaptic['MVR18'][nextState] += 5
        postsynaptic['MVR20'][nextState] += 5
        postsynaptic['VA8'][nextState] += 3
        postsynaptic['VA9'][nextState] += 9
        postsynaptic['VA9'][nextState] += 1
        postsynaptic['VB9'][nextState] += 6
        postsynaptic['VD10'][nextState] += 1
        postsynaptic['VD9'][nextState] += 10

def VB9():
        postsynaptic['AVAL'][nextState] += 5
        postsynaptic['AVAR'][nextState] += 4
        postsynaptic['AVBL'][nextState] += 1
        postsynaptic['AVBR'][nextState] += 6
        postsynaptic['DD5'][nextState] += 8
        postsynaptic['DVB'][nextState] += 1
        postsynaptic['MVL17'][nextState] += 6
        postsynaptic['MVL20'][nextState] += 6
        postsynaptic['MVR17'][nextState] += 6
        postsynaptic['MVR20'][nextState] += 6
        postsynaptic['PVCL'][nextState] += 2
        postsynaptic['VA8'][nextState] += 3
        postsynaptic['VA9'][nextState] += 4
        postsynaptic['VB8'][nextState] += 1
        postsynaptic['VB8'][nextState] += 3
        postsynaptic['VD10'][nextState] += 5

def VB10():
        postsynaptic['AVBL'][nextState] += 2
        postsynaptic['AVBR'][nextState] += 1
        postsynaptic['AVKL'][nextState] += 1
        postsynaptic['DD6'][nextState] += 9
        postsynaptic['MVL19'][nextState] += 5
        postsynaptic['MVL20'][nextState] += 5
        postsynaptic['MVR19'][nextState] += 5
        postsynaptic['MVR20'][nextState] += 5
        postsynaptic['PVCL'][nextState] += 1
        postsynaptic['PVT'][nextState] += 1
        postsynaptic['VD11'][nextState] += 1
        postsynaptic['VD12'][nextState] += 2

def VB11():
        postsynaptic['AVBL'][nextState] += 2
        postsynaptic['AVBR'][nextState] += 1
        postsynaptic['DD6'][nextState] += 7
        postsynaptic['MVL21'][nextState] += 5
        postsynaptic['MVL22'][nextState] += 5
        postsynaptic['MVL23'][nextState] += 5
        postsynaptic['MVR21'][nextState] += 5
        postsynaptic['MVR22'][nextState] += 5
        postsynaptic['MVR23'][nextState] += 5
        postsynaptic['MVR24'][nextState] += 5
        postsynaptic['PVCR'][nextState] += 1
        postsynaptic['VA12'][nextState] += 2

def VC1():
        postsynaptic['AVL'][nextState] += 2
        postsynaptic['DD1'][nextState] += 7
        postsynaptic['DD2'][nextState] += 6
        postsynaptic['DD3'][nextState] += 6
        postsynaptic['DVC'][nextState] += 1
        postsynaptic['MVULVA'][nextState] += 6
        postsynaptic['PVT'][nextState] += 2
        postsynaptic['VC2'][nextState] += 9
        postsynaptic['VC3'][nextState] += 3
        postsynaptic['VD1'][nextState] += 5
        postsynaptic['VD2'][nextState] += 1
        postsynaptic['VD3'][nextState] += 1
        postsynaptic['VD4'][nextState] += 2
        postsynaptic['VD5'][nextState] += 5
        postsynaptic['VD6'][nextState] += 1

def VC2():
        postsynaptic['DB4'][nextState] += 1
        postsynaptic['DD1'][nextState] += 6
        postsynaptic['DD2'][nextState] += 4
        postsynaptic['DD3'][nextState] += 9
        postsynaptic['DVC'][nextState] += 1
        postsynaptic['MVULVA'][nextState] += 10
        postsynaptic['PVCR'][nextState] += 1
        postsynaptic['PVQR'][nextState] += 1
        postsynaptic['PVT'][nextState] += 2
        postsynaptic['VC1'][nextState] += 10
        postsynaptic['VC3'][nextState] += 6
        postsynaptic['VD1'][nextState] += 2
        postsynaptic['VD2'][nextState] += 2
        postsynaptic['VD4'][nextState] += 5
        postsynaptic['VD5'][nextState] += 5
        postsynaptic['VD6'][nextState] += 1

def VC3():
        postsynaptic['AVL'][nextState] += 1
        postsynaptic['DD1'][nextState] += 2
        postsynaptic['DD2'][nextState] += 4
        postsynaptic['DD3'][nextState] += 5
        postsynaptic['DD4'][nextState] += 13
        postsynaptic['DVC'][nextState] += 1
        postsynaptic['HSNR'][nextState] += 1
        postsynaptic['MVULVA'][nextState] += 11
        postsynaptic['PVNR'][nextState] += 1
        postsynaptic['PVPR'][nextState] += 1
        postsynaptic['PVQR'][nextState] += 4
        postsynaptic['VC1'][nextState] += 4
        postsynaptic['VC2'][nextState] += 3
        postsynaptic['VC4'][nextState] += 1
        postsynaptic['VC5'][nextState] += 2
        postsynaptic['VD1'][nextState] += 1
        postsynaptic['VD2'][nextState] += 1
        postsynaptic['VD3'][nextState] += 1
        postsynaptic['VD4'][nextState] += 2
        postsynaptic['VD5'][nextState] += 4
        postsynaptic['VD6'][nextState] += 4
        postsynaptic['VD7'][nextState] += 5

def VC4():
        postsynaptic['AVBL'][nextState] += 1
        postsynaptic['AVFR'][nextState] += 1
        postsynaptic['AVHR'][nextState] += 1
        postsynaptic['MVULVA'][nextState] += 7
        postsynaptic['VC1'][nextState] += 1
        postsynaptic['VC3'][nextState] += 5
        postsynaptic['VC5'][nextState] += 2

def VC5():
        postsynaptic['AVFL'][nextState] += 1
        postsynaptic['AVFR'][nextState] += 1
        postsynaptic['DVC'][nextState] += 2
        postsynaptic['HSNL'][nextState] += 1
        postsynaptic['MVULVA'][nextState] += 2
        postsynaptic['OLLR'][nextState] += 1
        postsynaptic['PVT'][nextState] += 1
        postsynaptic['URBL'][nextState] += 3
        postsynaptic['VC3'][nextState] += 3
        postsynaptic['VC4'][nextState] += 2

def VC6():
        postsynaptic['MVULVA'][nextState] += 1
           
def VD1():
        postsynaptic['DD1'][nextState] += 5
        postsynaptic['DVC'][nextState] += 5
        postsynaptic['MVL05'][nextState] += -5
        postsynaptic['MVL08'][nextState] += -5
        postsynaptic['MVR05'][nextState] += -5
        postsynaptic['MVR08'][nextState] += -5
        postsynaptic['RIFL'][nextState] += 1
        postsynaptic['RIGL'][nextState] += 2
        postsynaptic['SMDDR'][nextState] += 1
        postsynaptic['VA1'][nextState] += 2
        postsynaptic['VA2'][nextState] += 1
        postsynaptic['VC1'][nextState] += 1
        postsynaptic['VD2'][nextState] += 7

def VD2():
        postsynaptic['AS1'][nextState] += 1
        postsynaptic['DD1'][nextState] += 3
        postsynaptic['MVL07'][nextState] += -7
        postsynaptic['MVL10'][nextState] += -7
        postsynaptic['MVR07'][nextState] += -7
        postsynaptic['MVR10'][nextState] += -7
        postsynaptic['VA2'][nextState] += 9
        postsynaptic['VB2'][nextState] += 3
        postsynaptic['VD1'][nextState] += 7
        postsynaptic['VD3'][nextState] += 2

def VD3():
        postsynaptic['MVL09'][nextState] += -7
        postsynaptic['MVL12'][nextState] += -9
        postsynaptic['MVR09'][nextState] += -7
        postsynaptic['MVR12'][nextState] += -7
        postsynaptic['PVPL'][nextState] += 1
        postsynaptic['VA3'][nextState] += 2
        postsynaptic['VB2'][nextState] += 2
        postsynaptic['VD2'][nextState] += 2
        postsynaptic['VD4'][nextState] += 1

def VD4():
        postsynaptic['DD2'][nextState] += 2
        postsynaptic['MVL11'][nextState] += -9
        postsynaptic['MVL12'][nextState] += -9
        postsynaptic['MVR11'][nextState] += -9
        postsynaptic['MVR12'][nextState] += -9
        postsynaptic['PVPR'][nextState] += 1
        postsynaptic['VD3'][nextState] += 1
        postsynaptic['VD5'][nextState] += 1

def VD5():
        postsynaptic['AVAR'][nextState] += 1
        postsynaptic['MVL14'][nextState] += -17
        postsynaptic['MVR14'][nextState] += -17
        postsynaptic['PVPR'][nextState] += 1
        postsynaptic['VA5'][nextState] += 2
        postsynaptic['VB4'][nextState] += 2
        postsynaptic['VD4'][nextState] += 1
        postsynaptic['VD6'][nextState] += 2

def VD6():
        postsynaptic['AVAL'][nextState] += 1
        postsynaptic['MVL13'][nextState] += -7
        postsynaptic['MVL14'][nextState] += -7
        postsynaptic['MVL16'][nextState] += -7
        postsynaptic['MVR13'][nextState] += -7
        postsynaptic['MVR14'][nextState] += -7
        postsynaptic['MVR16'][nextState] += -7
        postsynaptic['VA6'][nextState] += 1
        postsynaptic['VB5'][nextState] += 2
        postsynaptic['VD5'][nextState] += 2
        postsynaptic['VD7'][nextState] += 1

def VD7():
        postsynaptic['MVL15'][nextState] += -7
        postsynaptic['MVL16'][nextState] += -7
        postsynaptic['MVR15'][nextState] += -7
        postsynaptic['MVR16'][nextState] += -7
        postsynaptic['MVULVA'][nextState] += -15
        postsynaptic['VA9'][nextState] += 1
        postsynaptic['VD6'][nextState] += 1

def VD8():
        postsynaptic['DD4'][nextState] += 2
        postsynaptic['MVL15'][nextState] += -18
        postsynaptic['MVR15'][nextState] += -18
        postsynaptic['VA8'][nextState] += 5

def VD9():
        postsynaptic['MVL17'][nextState] += -10
        postsynaptic['MVL18'][nextState] += -10
        postsynaptic['MVR17'][nextState] += -10
        postsynaptic['MVR18'][nextState] += -10
        postsynaptic['PDER'][nextState] += 1
        postsynaptic['VD10'][nextState] += 5

def VD10():
        postsynaptic['AVBR'][nextState] += 1
        postsynaptic['DD5'][nextState] += 2
        postsynaptic['DVC'][nextState] += 4
        postsynaptic['MVL17'][nextState] += -9
        postsynaptic['MVL20'][nextState] += -9
        postsynaptic['MVR17'][nextState] += -9
        postsynaptic['MVR20'][nextState] += -9
        postsynaptic['VB9'][nextState] += 2
        postsynaptic['VD9'][nextState] += 5

def VD11():
        postsynaptic['AVAR'][nextState] += 2
        postsynaptic['MVL19'][nextState] += -9
        postsynaptic['MVL20'][nextState] += -9
        postsynaptic['MVR19'][nextState] += -9
        postsynaptic['MVR20'][nextState] += -9
        postsynaptic['VA11'][nextState] += 1
        postsynaptic['VB10'][nextState] += 1

def VD12():
        postsynaptic['MVL19'][nextState] += -5
        postsynaptic['MVL21'][nextState] += -5
        postsynaptic['MVR19'][nextState] += -5
        postsynaptic['MVR22'][nextState] += -5
        postsynaptic['VA11'][nextState] += 3
        postsynaptic['VA12'][nextState] += 2
        postsynaptic['VB10'][nextState] += 1
        postsynaptic['VB11'][nextState] += 1

def VD13():
        postsynaptic['AVAR'][nextState] += 2
        postsynaptic['MVL21'][nextState] += -9
        postsynaptic['MVL22'][nextState] += -9
        postsynaptic['MVL23'][nextState] += -9
        postsynaptic['MVR21'][nextState] += -9
        postsynaptic['MVR22'][nextState] += -9
        postsynaptic['MVR23'][nextState] += -9
        postsynaptic['MVR24'][nextState] += -9
        postsynaptic['PVCL'][nextState] += 1
        postsynaptic['PVCR'][nextState] += 1
        postsynaptic['PVPL'][nextState] += 2
        postsynaptic['VA12'][nextState] += 1
        
        
def createpostsynaptic():
        # The PostSynaptic dictionary maintains the accumulated values for
        # each neuron and muscle. The Accumulated values are initialized to Zero
        postsynaptic['ADAL'] = [0,0]
        postsynaptic['ADAR'] = [0,0]
        postsynaptic['ADEL'] = [0,0]
        postsynaptic['ADER'] = [0,0]
        postsynaptic['ADFL'] = [0,0]
        postsynaptic['ADFR'] = [0,0]
        postsynaptic['ADLL'] = [0,0]
        postsynaptic['ADLR'] = [0,0]
        postsynaptic['AFDL'] = [0,0]
        postsynaptic['AFDR'] = [0,0]
        postsynaptic['AIAL'] = [0,0]
        postsynaptic['AIAR'] = [0,0]
        postsynaptic['AIBL'] = [0,0]
        postsynaptic['AIBR'] = [0,0]
        postsynaptic['AIML'] = [0,0]
        postsynaptic['AIMR'] = [0,0]
        postsynaptic['AINL'] = [0,0]
        postsynaptic['AINR'] = [0,0]
        postsynaptic['AIYL'] = [0,0]
        postsynaptic['AIYR'] = [0,0]
        postsynaptic['AIZL'] = [0,0]
        postsynaptic['AIZR'] = [0,0]
        postsynaptic['ALA'] = [0,0]
        postsynaptic['ALML'] = [0,0]
        postsynaptic['ALMR'] = [0,0]
        postsynaptic['ALNL'] = [0,0]
        postsynaptic['ALNR'] = [0,0]
        postsynaptic['AQR'] = [0,0]
        postsynaptic['AS1'] = [0,0]
        postsynaptic['AS10'] = [0,0]
        postsynaptic['AS11'] = [0,0]
        postsynaptic['AS2'] = [0,0]
        postsynaptic['AS3'] = [0,0]
        postsynaptic['AS4'] = [0,0]
        postsynaptic['AS5'] = [0,0]
        postsynaptic['AS6'] = [0,0]
        postsynaptic['AS7'] = [0,0]
        postsynaptic['AS8'] = [0,0]
        postsynaptic['AS9'] = [0,0]
        postsynaptic['ASEL'] = [0,0]
        postsynaptic['ASER'] = [0,0]
        postsynaptic['ASGL'] = [0,0]
        postsynaptic['ASGR'] = [0,0]
        postsynaptic['ASHL'] = [0,0]
        postsynaptic['ASHR'] = [0,0]
        postsynaptic['ASIL'] = [0,0]
        postsynaptic['ASIR'] = [0,0]
        postsynaptic['ASJL'] = [0,0]
        postsynaptic['ASJR'] = [0,0]
        postsynaptic['ASKL'] = [0,0]
        postsynaptic['ASKR'] = [0,0]
        postsynaptic['AUAL'] = [0,0]
        postsynaptic['AUAR'] = [0,0]
        postsynaptic['AVAL'] = [0,0]
        postsynaptic['AVAR'] = [0,0]
        postsynaptic['AVBL'] = [0,0]
        postsynaptic['AVBR'] = [0,0]
        postsynaptic['AVDL'] = [0,0]
        postsynaptic['AVDR'] = [0,0]
        postsynaptic['AVEL'] = [0,0]
        postsynaptic['AVER'] = [0,0]
        postsynaptic['AVFL'] = [0,0]
        postsynaptic['AVFR'] = [0,0]
        postsynaptic['AVG'] = [0,0]
        postsynaptic['AVHL'] = [0,0]
        postsynaptic['AVHR'] = [0,0]
        postsynaptic['AVJL'] = [0,0]
        postsynaptic['AVJR'] = [0,0]
        postsynaptic['AVKL'] = [0,0]
        postsynaptic['AVKR'] = [0,0]
        postsynaptic['AVL'] = [0,0]
        postsynaptic['AVM'] = [0,0]
        postsynaptic['AWAL'] = [0,0]
        postsynaptic['AWAR'] = [0,0]
        postsynaptic['AWBL'] = [0,0]
        postsynaptic['AWBR'] = [0,0]
        postsynaptic['AWCL'] = [0,0]
        postsynaptic['AWCR'] = [0,0]
        postsynaptic['BAGL'] = [0,0]
        postsynaptic['BAGR'] = [0,0]
        postsynaptic['BDUL'] = [0,0]
        postsynaptic['BDUR'] = [0,0]
        postsynaptic['CEPDL'] = [0,0]
        postsynaptic['CEPDR'] = [0,0]
        postsynaptic['CEPVL'] = [0,0]
        postsynaptic['CEPVR'] = [0,0]
        postsynaptic['DA1'] = [0,0]
        postsynaptic['DA2'] = [0,0]
        postsynaptic['DA3'] = [0,0]
        postsynaptic['DA4'] = [0,0]
        postsynaptic['DA5'] = [0,0]
        postsynaptic['DA6'] = [0,0]
        postsynaptic['DA7'] = [0,0]
        postsynaptic['DA8'] = [0,0]
        postsynaptic['DA9'] = [0,0]
        postsynaptic['DB1'] = [0,0]
        postsynaptic['DB2'] = [0,0]
        postsynaptic['DB3'] = [0,0]
        postsynaptic['DB4'] = [0,0]
        postsynaptic['DB5'] = [0,0]
        postsynaptic['DB6'] = [0,0]
        postsynaptic['DB7'] = [0,0]
        postsynaptic['DD1'] = [0,0]
        postsynaptic['DD2'] = [0,0]
        postsynaptic['DD3'] = [0,0]
        postsynaptic['DD4'] = [0,0]
        postsynaptic['DD5'] = [0,0]
        postsynaptic['DD6'] = [0,0]
        postsynaptic['DVA'] = [0,0]
        postsynaptic['DVB'] = [0,0]
        postsynaptic['DVC'] = [0,0]
        postsynaptic['FLPL'] = [0,0]
        postsynaptic['FLPR'] = [0,0]
        postsynaptic['HSNL'] = [0,0]
        postsynaptic['HSNR'] = [0,0]
        postsynaptic['I1L'] = [0,0]
        postsynaptic['I1R'] = [0,0]
        postsynaptic['I2L'] = [0,0]
        postsynaptic['I2R'] = [0,0]
        postsynaptic['I3'] = [0,0]
        postsynaptic['I4'] = [0,0]
        postsynaptic['I5'] = [0,0]
        postsynaptic['I6'] = [0,0]
        postsynaptic['IL1DL'] = [0,0]
        postsynaptic['IL1DR'] = [0,0]
        postsynaptic['IL1L'] = [0,0]
        postsynaptic['IL1R'] = [0,0]
        postsynaptic['IL1VL'] = [0,0]
        postsynaptic['IL1VR'] = [0,0]
        postsynaptic['IL2L'] = [0,0]
        postsynaptic['IL2R'] = [0,0]
        postsynaptic['IL2DL'] = [0,0]
        postsynaptic['IL2DR'] = [0,0]
        postsynaptic['IL2VL'] = [0,0]
        postsynaptic['IL2VR'] = [0,0]
        postsynaptic['LUAL'] = [0,0]
        postsynaptic['LUAR'] = [0,0]
        postsynaptic['M1'] = [0,0]
        postsynaptic['M2L'] = [0,0]
        postsynaptic['M2R'] = [0,0]
        postsynaptic['M3L'] = [0,0]
        postsynaptic['M3R'] = [0,0]
        postsynaptic['M4'] = [0,0]
        postsynaptic['M5'] = [0,0]
        postsynaptic['MANAL'] = [0,0]
        postsynaptic['MCL'] = [0,0]
        postsynaptic['MCR'] = [0,0]
        postsynaptic['MDL01'] = [0,0]
        postsynaptic['MDL02'] = [0,0]
        postsynaptic['MDL03'] = [0,0]
        postsynaptic['MDL04'] = [0,0]
        postsynaptic['MDL05'] = [0,0]
        postsynaptic['MDL06'] = [0,0]
        postsynaptic['MDL07'] = [0,0]
        postsynaptic['MDL08'] = [0,0]
        postsynaptic['MDL09'] = [0,0]
        postsynaptic['MDL10'] = [0,0]
        postsynaptic['MDL11'] = [0,0]
        postsynaptic['MDL12'] = [0,0]
        postsynaptic['MDL13'] = [0,0]
        postsynaptic['MDL14'] = [0,0]
        postsynaptic['MDL15'] = [0,0]
        postsynaptic['MDL16'] = [0,0]
        postsynaptic['MDL17'] = [0,0]
        postsynaptic['MDL18'] = [0,0]
        postsynaptic['MDL19'] = [0,0]
        postsynaptic['MDL20'] = [0,0]
        postsynaptic['MDL21'] = [0,0]
        postsynaptic['MDL22'] = [0,0]
        postsynaptic['MDL23'] = [0,0]
        postsynaptic['MDL24'] = [0,0]
        postsynaptic['MDR01'] = [0,0]
        postsynaptic['MDR02'] = [0,0]
        postsynaptic['MDR03'] = [0,0]
        postsynaptic['MDR04'] = [0,0]
        postsynaptic['MDR05'] = [0,0]
        postsynaptic['MDR06'] = [0,0]
        postsynaptic['MDR07'] = [0,0]
        postsynaptic['MDR08'] = [0,0]
        postsynaptic['MDR09'] = [0,0]
        postsynaptic['MDR10'] = [0,0]
        postsynaptic['MDR11'] = [0,0]
        postsynaptic['MDR12'] = [0,0]
        postsynaptic['MDR13'] = [0,0]
        postsynaptic['MDR14'] = [0,0]
        postsynaptic['MDR15'] = [0,0]
        postsynaptic['MDR16'] = [0,0]
        postsynaptic['MDR17'] = [0,0]
        postsynaptic['MDR18'] = [0,0]
        postsynaptic['MDR19'] = [0,0]
        postsynaptic['MDR20'] = [0,0]
        postsynaptic['MDR21'] = [0,0]
        postsynaptic['MDR22'] = [0,0]
        postsynaptic['MDR23'] = [0,0]
        postsynaptic['MDR24'] = [0,0]
        postsynaptic['MI'] = [0,0]
        postsynaptic['MVL01'] = [0,0]
        postsynaptic['MVL02'] = [0,0]
        postsynaptic['MVL03'] = [0,0]
        postsynaptic['MVL04'] = [0,0]
        postsynaptic['MVL05'] = [0,0]
        postsynaptic['MVL06'] = [0,0]
        postsynaptic['MVL07'] = [0,0]
        postsynaptic['MVL08'] = [0,0]
        postsynaptic['MVL09'] = [0,0]
        postsynaptic['MVL10'] = [0,0]
        postsynaptic['MVL11'] = [0,0]
        postsynaptic['MVL12'] = [0,0]
        postsynaptic['MVL13'] = [0,0]
        postsynaptic['MVL14'] = [0,0]
        postsynaptic['MVL15'] = [0,0]
        postsynaptic['MVL16'] = [0,0]
        postsynaptic['MVL17'] = [0,0]
        postsynaptic['MVL18'] = [0,0]
        postsynaptic['MVL19'] = [0,0]
        postsynaptic['MVL20'] = [0,0]
        postsynaptic['MVL21'] = [0,0]
        postsynaptic['MVL22'] = [0,0]
        postsynaptic['MVL23'] = [0,0]
        postsynaptic['MVR01'] = [0,0]
        postsynaptic['MVR02'] = [0,0]
        postsynaptic['MVR03'] = [0,0]
        postsynaptic['MVR04'] = [0,0]
        postsynaptic['MVR05'] = [0,0]
        postsynaptic['MVR06'] = [0,0]
        postsynaptic['MVR07'] = [0,0]
        postsynaptic['MVR08'] = [0,0]
        postsynaptic['MVR09'] = [0,0]
        postsynaptic['MVR10'] = [0,0]
        postsynaptic['MVR11'] = [0,0]
        postsynaptic['MVR12'] = [0,0]
        postsynaptic['MVR13'] = [0,0]
        postsynaptic['MVR14'] = [0,0]
        postsynaptic['MVR15'] = [0,0]
        postsynaptic['MVR16'] = [0,0]
        postsynaptic['MVR17'] = [0,0]
        postsynaptic['MVR18'] = [0,0]
        postsynaptic['MVR19'] = [0,0]
        postsynaptic['MVR20'] = [0,0]
        postsynaptic['MVR21'] = [0,0]
        postsynaptic['MVR22'] = [0,0]
        postsynaptic['MVR23'] = [0,0]
        postsynaptic['MVR24'] = [0,0]
        postsynaptic['MVULVA'] = [0,0]
        postsynaptic['NSML'] = [0,0]
        postsynaptic['NSMR'] = [0,0]
        postsynaptic['OLLL'] = [0,0]
        postsynaptic['OLLR'] = [0,0]
        postsynaptic['OLQDL'] = [0,0]
        postsynaptic['OLQDR'] = [0,0]
        postsynaptic['OLQVL'] = [0,0]
        postsynaptic['OLQVR'] = [0,0]
        postsynaptic['PDA'] = [0,0]
        postsynaptic['PDB'] = [0,0]
        postsynaptic['PDEL'] = [0,0]
        postsynaptic['PDER'] = [0,0]
        postsynaptic['PHAL'] = [0,0]
        postsynaptic['PHAR'] = [0,0]
        postsynaptic['PHBL'] = [0,0]
        postsynaptic['PHBR'] = [0,0]
        postsynaptic['PHCL'] = [0,0]
        postsynaptic['PHCR'] = [0,0]
        postsynaptic['PLML'] = [0,0]
        postsynaptic['PLMR'] = [0,0]
        postsynaptic['PLNL'] = [0,0]
        postsynaptic['PLNR'] = [0,0]
        postsynaptic['PQR'] = [0,0]
        postsynaptic['PVCL'] = [0,0]
        postsynaptic['PVCR'] = [0,0]
        postsynaptic['PVDL'] = [0,0]
        postsynaptic['PVDR'] = [0,0]
        postsynaptic['PVM'] = [0,0]
        postsynaptic['PVNL'] = [0,0]
        postsynaptic['PVNR'] = [0,0]
        postsynaptic['PVPL'] = [0,0]
        postsynaptic['PVPR'] = [0,0]
        postsynaptic['PVQL'] = [0,0]
        postsynaptic['PVQR'] = [0,0]
        postsynaptic['PVR'] = [0,0]
        postsynaptic['PVT'] = [0,0]
        postsynaptic['PVWL'] = [0,0]
        postsynaptic['PVWR'] = [0,0]
        postsynaptic['RIAL'] = [0,0]
        postsynaptic['RIAR'] = [0,0]
        postsynaptic['RIBL'] = [0,0]
        postsynaptic['RIBR'] = [0,0]
        postsynaptic['RICL'] = [0,0]
        postsynaptic['RICR'] = [0,0]
        postsynaptic['RID'] = [0,0]
        postsynaptic['RIFL'] = [0,0]
        postsynaptic['RIFR'] = [0,0]
        postsynaptic['RIGL'] = [0,0]
        postsynaptic['RIGR'] = [0,0]
        postsynaptic['RIH'] = [0,0]
        postsynaptic['RIML'] = [0,0]
        postsynaptic['RIMR'] = [0,0]
        postsynaptic['RIPL'] = [0,0]
        postsynaptic['RIPR'] = [0,0]
        postsynaptic['RIR'] = [0,0]
        postsynaptic['RIS'] = [0,0]
        postsynaptic['RIVL'] = [0,0]
        postsynaptic['RIVR'] = [0,0]
        postsynaptic['RMDDL'] = [0,0]
        postsynaptic['RMDDR'] = [0,0]
        postsynaptic['RMDL'] = [0,0]
        postsynaptic['RMDR'] = [0,0]
        postsynaptic['RMDVL'] = [0,0]
        postsynaptic['RMDVR'] = [0,0]
        postsynaptic['RMED'] = [0,0]
        postsynaptic['RMEL'] = [0,0]
        postsynaptic['RMER'] = [0,0]
        postsynaptic['RMEV'] = [0,0]
        postsynaptic['RMFL'] = [0,0]
        postsynaptic['RMFR'] = [0,0]
        postsynaptic['RMGL'] = [0,0]
        postsynaptic['RMGR'] = [0,0]
        postsynaptic['RMHL'] = [0,0]
        postsynaptic['RMHR'] = [0,0]
        postsynaptic['SAADL'] = [0,0]
        postsynaptic['SAADR'] = [0,0]
        postsynaptic['SAAVL'] = [0,0]
        postsynaptic['SAAVR'] = [0,0]
        postsynaptic['SABD'] = [0,0]
        postsynaptic['SABVL'] = [0,0]
        postsynaptic['SABVR'] = [0,0]
        postsynaptic['SDQL'] = [0,0]
        postsynaptic['SDQR'] = [0,0]
        postsynaptic['SIADL'] = [0,0]
        postsynaptic['SIADR'] = [0,0]
        postsynaptic['SIAVL'] = [0,0]
        postsynaptic['SIAVR'] = [0,0]
        postsynaptic['SIBDL'] = [0,0]
        postsynaptic['SIBDR'] = [0,0]
        postsynaptic['SIBVL'] = [0,0]
        postsynaptic['SIBVR'] = [0,0]
        postsynaptic['SMBDL'] = [0,0]
        postsynaptic['SMBDR'] = [0,0]
        postsynaptic['SMBVL'] = [0,0]
        postsynaptic['SMBVR'] = [0,0]
        postsynaptic['SMDDL'] = [0,0]
        postsynaptic['SMDDR'] = [0,0]
        postsynaptic['SMDVL'] = [0,0]
        postsynaptic['SMDVR'] = [0,0]
        postsynaptic['URADL'] = [0,0]
        postsynaptic['URADR'] = [0,0]
        postsynaptic['URAVL'] = [0,0]
        postsynaptic['URAVR'] = [0,0]
        postsynaptic['URBL'] = [0,0]
        postsynaptic['URBR'] = [0,0]
        postsynaptic['URXL'] = [0,0]
        postsynaptic['URXR'] = [0,0]
        postsynaptic['URYDL'] = [0,0]
        postsynaptic['URYDR'] = [0,0]
        postsynaptic['URYVL'] = [0,0]
        postsynaptic['URYVR'] = [0,0]
        postsynaptic['VA1'] = [0,0]
        postsynaptic['VA10'] = [0,0]
        postsynaptic['VA11'] = [0,0]
        postsynaptic['VA12'] = [0,0]
        postsynaptic['VA2'] = [0,0]
        postsynaptic['VA3'] = [0,0]
        postsynaptic['VA4'] = [0,0]
        postsynaptic['VA5'] = [0,0]
        postsynaptic['VA6'] = [0,0]
        postsynaptic['VA7'] = [0,0]
        postsynaptic['VA8'] = [0,0]
        postsynaptic['VA9'] = [0,0]
        postsynaptic['VB1'] = [0,0]
        postsynaptic['VB10'] = [0,0]
        postsynaptic['VB11'] = [0,0]
        postsynaptic['VB2'] = [0,0]
        postsynaptic['VB3'] = [0,0]
        postsynaptic['VB4'] = [0,0]
        postsynaptic['VB5'] = [0,0]
        postsynaptic['VB6'] = [0,0]
        postsynaptic['VB7'] = [0,0]
        postsynaptic['VB8'] = [0,0]
        postsynaptic['VB9'] = [0,0]
        postsynaptic['VC1'] = [0,0]
        postsynaptic['VC2'] = [0,0]
        postsynaptic['VC3'] = [0,0]
        postsynaptic['VC4'] = [0,0]
        postsynaptic['VC5'] = [0,0]
        postsynaptic['VC6'] = [0,0]
        postsynaptic['VD1'] = [0,0]
        postsynaptic['VD10'] = [0,0]
        postsynaptic['VD11'] = [0,0]
        postsynaptic['VD12'] = [0,0]
        postsynaptic['VD13'] = [0,0]
        postsynaptic['VD2'] = [0,0]
        postsynaptic['VD3'] = [0,0]
        postsynaptic['VD4'] = [0,0]
        postsynaptic['VD5'] = [0,0]
        postsynaptic['VD6'] = [0,0]
        postsynaptic['VD7'] = [0,0]
        postsynaptic['VD8'] = [0,0]
        postsynaptic['VD9'] = [0,0]

#global postsynapticNext = copy.deepcopy(postsynaptic)

def motorcontrol():
        global accumright
        global accumleft

        # accumulate left and right muscles and the accumulated values are
        # used to move the left and right motors of the robot
        for pscheck in postsynaptic:
                if pscheck in musDleft or pscheck in musVleft:
                   accumleft += postsynaptic[pscheck][thisState]
                   postsynaptic[pscheck][thisState] = 0                 #Both states have to be set to 0 once the muscle is fired, or
                   #postsynaptic[pscheck][nextState] = 0                 # it will keep returning beyond the threshold within one iteration.
                elif pscheck in musDright or pscheck in musVright:
                   accumright += postsynaptic[pscheck][thisState]
                   postsynaptic[pscheck][thisState] = 0
                   #postsynaptic[pscheck][nextState] = 0

        # We turn the wheels according to the motor weight accumulation
        new_speed = abs(accumleft) + abs(accumright)
        if new_speed > 150:
                new_speed = 150
        elif new_speed < 75:
                new_speed = 75
        print "Left: ", accumleft, "Right:", accumright, "Speed: ", new_speed
        ## Start Commented section
        # set_speed(new_speed)
        # if accumleft == 0 and accumright == 0:
        #         stop()
        # elif accumright <= 0 and accumleft < 0:
        #         set_speed(150)
        #         turnratio = float(accumright) / float(accumleft)
        #         # print "Turn Ratio: ", turnratio
        #         if turnratio <= 0.6:
        #                  left_rot()
        #                  time.sleep(0.8)
        #         elif turnratio >= 2:
        #                  right_rot()
        #                  time.sleep(0.8)
        #         bwd()
        #         time.sleep(0.5)
        # elif accumright <= 0 and accumleft >= 0:
        #         right_rot()
        #         time.sleep(.8)
        # elif accumright >= 0 and accumleft <= 0:
        #         left_rot()
        #         time.sleep(.8)
        # elif accumright >= 0 and accumleft > 0:
        #         turnratio = float(accumright) / float(accumleft)
        #         # print "Turn Ratio: ", turnratio
        #         if turnratio <= 0.6:
        #                  left_rot()
        #                  time.sleep(0.8)
        #         elif turnratio >= 2:
        #                  right_rot()
        #                  time.sleep(0.8)
        #         fwd()
        #         time.sleep(0.5)
        # else:
        #         stop()
         ## End Commented section
        accumleft = 0
        accumright = 0
        time.sleep(0.2)


def dendriteAccumulate(dneuron):
        f = eval(dneuron)
        f()

def fireNeuron(fneuron):
        # The threshold has been exceeded and we fire the neurite
        if fneuron != "MVULVA":
                f = eval(fneuron)
                f()
                #postsynaptic[fneuron][nextState] = 0
                #postsynaptic[fneuron] = [0,0]

def runconnectome():
        # Each time a set of neuron is stimulated, this method will execute
        # The weigted values are accumulated in the PostSynaptic array
        # Once the accumulation is read, we see what neurons are greater
        # then the threshold and fire the neuron or muscle that has exceeded
        # the threshold 
        global thisState
        global nextState
        for ps in postsynaptic:
                postsynaptic[ps][thisState] = postsynaptic[ps][nextState]
        for ps in postsynaptic:
                if ps[:3] not in muscles and abs(postsynaptic[ps][thisState]) > threshold:
                        fireNeuron(ps)
                        print ps
                        #print (ps)
                        postsynaptic[ps] = [0,0]
        motorcontrol()

        thisState,nextState=nextState,thisState               


# Create the dictionary      
createpostsynaptic()
dist=0
#set_speed(120)
print "Voltage: "#, volt()
tfood = 0
try:
### Here is where you would put in a method to stimulate the neurons ###
### We stimulate chemosensory neurons constantly unless nose touch   ###
### (sonar) is stimulated and then we fire nose touch neurites       ###
### Use CNTRL-C to stop the program
    while True:
        ## Start comment - use a fixed value if you want to stimulte nose touch
        ## use something like "dist = 27" if you want to stop nose stimulation
        #dist = us_dist(15)
        ## End Comment

        #Do we need to switch states at the end of each loop? No, this is done inside the runconnectome()
        #function, called inside each loop.
        if dist>0 and dist<30:
            print "OBSTACLE (Nose Touch)", dist 
            dendriteAccumulate("FLPR")
            dendriteAccumulate("FLPL")
            dendriteAccumulate("ASHL")
            dendriteAccumulate("ASHR")
            dendriteAccumulate("IL1VL")
            dendriteAccumulate("IL1VR")
            dendriteAccumulate("OLQDL")
            dendriteAccumulate("OLQDR")
            dendriteAccumulate("OLQVR")
            dendriteAccumulate("OLQVL")
            runconnectome()
        else:
            if tfood < 2:
                    print "FOOD"
                    print (thisState)
                    dendriteAccumulate("ADFL")
                    dendriteAccumulate("ADFR")
                    dendriteAccumulate("ASGR")
                    dendriteAccumulate("ASGL")
                    dendriteAccumulate("ASIL")
                    dendriteAccumulate("ASIR")
                    dendriteAccumulate("ASJR")
                    dendriteAccumulate("ASJL")
                    runconnectome()
                    time.sleep(0.2)
            tfood += 0.5
            if (tfood > 20):
                    tfood = 0
        

       
except KeyboardInterrupt:
    ## Start Comment
    #stop()
    ## End Comment
    print "Ctrl+C detected. Program Stopped!"
    for pscheck in postsynaptic:
        print (pscheck,' ',postsynaptic[pscheck][0],' ',postsynaptic[pscheck][1])

    