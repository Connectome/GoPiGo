# GoPiGo Connectome
# Written by Timothy Busbice, (c) 2014, in Python 2.7
# The GoPiGo Connectome uses a Postsynaptic dictionary based on the C Elegans Connectome Model
# This application can be ran on the Raspberry Pi GoPiGo robot with a Sonar that represents Nose Touch when activated
# To run standalone without a GoPiGo robot, simply comment out the sections with Start and End comments 
## Start Comment
from gopigo import *
## End Comment
import time

# The postsynatpic dictionary contains the accumulated weighted values as the
# connectome is executed
postsynaptic = {}

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
def ADAL():
        postsynaptic['ADAR'] += 1
        postsynaptic['ADFL'] += 1
        postsynaptic['AIBL'] += 1
        postsynaptic['AIBR'] += 2
        postsynaptic['ASHL'] += 1
        postsynaptic['AVAR'] += 2
        postsynaptic['AVBL'] += 4
        postsynaptic['AVBR'] += 7
        postsynaptic['AVDL'] += 1
        postsynaptic['AVDR'] += 2
        postsynaptic['AVEL'] += 1
        postsynaptic['AVJR'] += 5
        postsynaptic['FLPR'] += 1
        postsynaptic['PVQL'] += 1
        postsynaptic['RICL'] += 1
        postsynaptic['RICR'] += 1
        postsynaptic['RIML'] += 3
        postsynaptic['RIPL'] += 1
        postsynaptic['SMDVR'] += 2

def ADAR():
        postsynaptic['ADAL'] += 1
        postsynaptic['ADFR'] += 1
        postsynaptic['AIBL'] += 1
        postsynaptic['AIBR'] += 1
        postsynaptic['ASHR'] += 1
        postsynaptic['AVAL'] += 1
        postsynaptic['AVBL'] += 1
        postsynaptic['AVBR'] += 5
        postsynaptic['AVDL'] += 2
        postsynaptic['AVEL'] += 1
        postsynaptic['AVJL'] += 3
        postsynaptic['PVQR'] += 1
        postsynaptic['RICL'] += 1
        postsynaptic['RIMR'] += 5
        postsynaptic['RIPR'] += 1
        postsynaptic['RIVR'] += 1
        postsynaptic['SMDVL'] += 2

def ADEL():
        postsynaptic['ADAL'] += 1
        postsynaptic['ADER'] += 1
        postsynaptic['AINL'] += 1
        postsynaptic['AVAL'] += 2
        postsynaptic['AVAR'] += 3
        postsynaptic['AVEL'] += 1
        postsynaptic['AVKR'] += 1
        postsynaptic['AVL'] += 1
        postsynaptic['BDUL'] += 1
        postsynaptic['CEPDL'] += 1
        postsynaptic['FLPL'] += 1
        postsynaptic['IL1L'] += 1
        postsynaptic['IL2L'] += 1
        postsynaptic['MDL05'] += 1
        postsynaptic['OLLL'] += 1
        postsynaptic['RIAL'] += 1
        postsynaptic['RIFL'] += 1
        postsynaptic['RIGL'] += 5
        postsynaptic['RIGR'] += 3
        postsynaptic['RIH'] += 2
        postsynaptic['RIVL'] += 1
        postsynaptic['RIVR'] += 1
        postsynaptic['RMDL'] += 2
        postsynaptic['RMGL'] += 1
        postsynaptic['RMHL'] += 1
        postsynaptic['SIADR'] += 1
        postsynaptic['SIBDR'] += 1
        postsynaptic['SMBDR'] += 1
        postsynaptic['URBL'] += 1

def ADER():
        postsynaptic['ADAR'] += 1
        postsynaptic['ADEL'] += 2
        postsynaptic['ALA'] += 1
        postsynaptic['AVAL'] += 5
        postsynaptic['AVAR'] += 1
        postsynaptic['AVDR'] += 2
        postsynaptic['AVER'] += 1
        postsynaptic['AVJR'] += 1
        postsynaptic['AVKL'] += 1
        postsynaptic['AVKR'] += 1
        postsynaptic['CEPDR'] += 1
        postsynaptic['FLPL'] += 1
        postsynaptic['FLPR'] += 1
        postsynaptic['OLLR'] += 2
        postsynaptic['PVR'] += 1
        postsynaptic['RIGL'] += 7
        postsynaptic['RIGR'] += 4
        postsynaptic['RIH'] += 1
        postsynaptic['RMDR'] += 2
        postsynaptic['SAAVR'] += 1

def ADFL():
        postsynaptic['ADAL'] += 2
        postsynaptic['AIZL'] += 12
        postsynaptic['AUAL'] += 5
        postsynaptic['OLQVL'] += 1
        postsynaptic['RIAL'] += 15
        postsynaptic['RIGL'] += 1
        postsynaptic['RIR'] += 2
        postsynaptic['SMBVL'] += 2

def ADFR():
        postsynaptic['ADAR'] += 2
        postsynaptic['AIAR'] += 1
        postsynaptic['AIYR'] += 1
        postsynaptic['AIZR'] += 8
        postsynaptic['ASHR'] += 1
        postsynaptic['AUAR'] += 4
        postsynaptic['AWBR'] += 1
        postsynaptic['PVPR'] += 1
        postsynaptic['RIAR'] += 16
        postsynaptic['RIGR'] += 3
        postsynaptic['RIR'] += 3
        postsynaptic['SMBDR'] += 1
        postsynaptic['SMBVR'] += 2
        postsynaptic['URXR'] += 1

def ADLL():
        postsynaptic['ADLR'] += 1
        postsynaptic['AIAL'] += 6
        postsynaptic['AIBL'] += 7
        postsynaptic['AIBR'] += 1
        postsynaptic['ALA'] += 2
        postsynaptic['ASER'] += 3
        postsynaptic['ASHL'] += 2
        postsynaptic['AVAL'] += 2
        postsynaptic['AVAR'] += 3
        postsynaptic['AVBL'] += 2
        postsynaptic['AVDL'] += 1
        postsynaptic['AVDR'] += 4
        postsynaptic['AVDR'] += 1
        postsynaptic['AVJL'] += 1
        postsynaptic['AVJR'] += 3
        postsynaptic['AWBL'] += 2
        postsynaptic['OLQVL'] += 1
        postsynaptic['RIPL'] += 1
        postsynaptic['RMGL'] += 1

def ADLR():
        postsynaptic['ADLL'] += 1
        postsynaptic['AIAR'] += 10
        postsynaptic['AIBR'] += 10
        postsynaptic['ASER'] += 1
        postsynaptic['ASHR'] += 3
        postsynaptic['AVAR'] += 2
        postsynaptic['AVBL'] += 1
        postsynaptic['AVBR'] += 2
        postsynaptic['AVDL'] += 5
        postsynaptic['AVDR'] += 2
        postsynaptic['AVJR'] += 1
        postsynaptic['AWCR'] += 3
        postsynaptic['OLLR'] += 1
        postsynaptic['PVCL'] += 1
        postsynaptic['RICL'] += 1
        postsynaptic['RICR'] += 1

def AFDL():
        postsynaptic['AFDR'] += 1
        postsynaptic['AIBL'] += 1
        postsynaptic['AINR'] += 1
        postsynaptic['AIYL'] += 7

def AFDR():
        postsynaptic['AFDL'] += 1
        postsynaptic['AIBR'] += 1
        postsynaptic['AIYR'] += 13
        postsynaptic['ASER'] += 1
                   
def AIAL():
        postsynaptic['ADAL'] += 1
        postsynaptic['AIAR'] += 1
        postsynaptic['AIBL'] += 10
        postsynaptic['AIML'] += 2
        postsynaptic['AIZL'] += 1
        postsynaptic['ASER'] += 3
        postsynaptic['ASGL'] += 1
        postsynaptic['ASHL'] += 1
        postsynaptic['ASIL'] += 2
        postsynaptic['ASKL'] += 3
        postsynaptic['AWAL'] += 1
        postsynaptic['AWCR'] += 1
        postsynaptic['HSNL'] += 1
        postsynaptic['RIFL'] += 1
        postsynaptic['RMGL'] += 1

def AIAR():
        postsynaptic['ADAR'] += 1
        postsynaptic['ADFR'] += 1
        postsynaptic['ADLR'] += 2
        postsynaptic['AIAL'] += 1
        postsynaptic['AIBR'] += 14
        postsynaptic['AIZR'] += 1
        postsynaptic['ASER'] += 1
        postsynaptic['ASGR'] += 1
        postsynaptic['ASIR'] += 2
        postsynaptic['AWAR'] += 1
        postsynaptic['AWCL'] += 1
        postsynaptic['AWCR'] += 3
        postsynaptic['RIFR'] += 2

def AIBL():
        postsynaptic['AFDL'] += 1
        postsynaptic['AIYL'] += 1
        postsynaptic['ASER'] += 1
        postsynaptic['AVAL'] += 2
        postsynaptic['AVBL'] += 5
        postsynaptic['DVC'] += 1
        postsynaptic['FLPL'] += 1
        postsynaptic['PVT'] += 1
        postsynaptic['RIBR'] += 4
        postsynaptic['RIFL'] += 1
        postsynaptic['RIGR'] += 1
        postsynaptic['RIGR'] += 3
        postsynaptic['RIML'] += 2
        postsynaptic['RIMR'] += 13
        postsynaptic['RIMR'] += 1
        postsynaptic['RIVL'] += 1
        postsynaptic['SAADL'] += 2
        postsynaptic['SAADR'] += 2
        postsynaptic['SMDDR'] += 4

def AIBR():
        postsynaptic['AFDR'] += 1
        postsynaptic['AVAR'] += 1
        postsynaptic['AVBR'] += 3
        postsynaptic['AVEL'] += 1
        postsynaptic['DB1'] += 1
        postsynaptic['DVC'] += 2
        postsynaptic['PVT'] += 1
        postsynaptic['RIAL'] += 1
        postsynaptic['RIBL'] += 4
        postsynaptic['RIGL'] += 3
        postsynaptic['RIML'] += 16
        postsynaptic['RIML'] += 1
        postsynaptic['RIMR'] += 1
        postsynaptic['RIS'] += 1
        postsynaptic['RIVR'] += 1
        postsynaptic['SAADL'] += 1
        postsynaptic['SMDDL'] += 3
        postsynaptic['SMDVL'] += 1
        postsynaptic['VB1'] += 3

def AIML():
        postsynaptic['AIAL'] += 5
        postsynaptic['ALML'] += 1
        postsynaptic['ASGL'] += 2
        postsynaptic['ASKL'] += 2
        postsynaptic['AVBR'] += 2
        postsynaptic['AVDL'] += 1
        postsynaptic['AVDR'] += 1
        postsynaptic['AVER'] += 1
        postsynaptic['AVFL'] += 4
        postsynaptic['AVFR'] += 1
        postsynaptic['AVHL'] += 2
        postsynaptic['AVHR'] += 1
        postsynaptic['AVJL'] += 1
        postsynaptic['PVQL'] += 1
        postsynaptic['RIFL'] += 1
        postsynaptic['SIBDR'] += 1
        postsynaptic['SMBVL'] += 1

def AIMR():
        postsynaptic['AIAR'] += 5
        postsynaptic['ASGR'] += 2
        postsynaptic['ASJR'] += 2
        postsynaptic['ASKR'] += 3
        postsynaptic['AVDR'] += 1
        postsynaptic['AVFL'] += 1
        postsynaptic['AVFR'] += 1
        postsynaptic['HSNL'] += 1
        postsynaptic['HSNR'] += 2
        postsynaptic['OLQDR'] += 1
        postsynaptic['PVNR'] += 1
        postsynaptic['RIFR'] += 1
        postsynaptic['RMGR'] += 1

def AINL():
        postsynaptic['ADEL'] += 1
        postsynaptic['AFDR'] += 5
        postsynaptic['AINR'] += 2
        postsynaptic['ASEL'] += 3
        postsynaptic['ASGR'] += 1
        postsynaptic['AUAR'] += 1
        postsynaptic['BAGL'] += 3
        postsynaptic['RIBL'] += 1
        postsynaptic['RIBR'] += 2

def AINR():
        postsynaptic['AFDL'] += 4
        postsynaptic['AFDR'] += 1
        postsynaptic['AIAL'] += 2
        postsynaptic['AIBL'] += 2
        postsynaptic['AINL'] += 2
        postsynaptic['ASEL'] += 1
        postsynaptic['ASER'] += 1
        postsynaptic['ASGL'] += 1
        postsynaptic['AUAL'] += 1
        postsynaptic['AUAR'] += 1
        postsynaptic['BAGR'] += 3
        postsynaptic['RIBL'] += 2
        postsynaptic['RID'] += 1

def AIYL():
        postsynaptic['AIYR'] += 1
        postsynaptic['AIZL'] += 13
        postsynaptic['AWAL'] += 3
        postsynaptic['AWCL'] += 1
        postsynaptic['AWCR'] += 1
        postsynaptic['HSNR'] += 1
        postsynaptic['RIAL'] += 7
        postsynaptic['RIBL'] += 4
        postsynaptic['RIML'] += 1

def AIYR():
        postsynaptic['ADFR'] += 1
        postsynaptic['AIYL'] += 1
        postsynaptic['AIZR'] += 8
        postsynaptic['AWAR'] += 1
        postsynaptic['HSNL'] += 1
        postsynaptic['RIAR'] += 6
        postsynaptic['RIBR'] += 2
        postsynaptic['RIMR'] += 1

def AIZL():
        postsynaptic['AIAL'] += 3
        postsynaptic['AIBL'] += 2
        postsynaptic['AIBR'] += 8
        postsynaptic['AIZR'] += 2
        postsynaptic['ASEL'] += 1
        postsynaptic['ASGL'] += 1
        postsynaptic['ASHL'] += 1
        postsynaptic['AVER'] += 5
        postsynaptic['DVA'] += 1
        postsynaptic['RIAL'] += 8
        postsynaptic['RIGL'] += 1
        postsynaptic['RIML'] += 4
        postsynaptic['SMBDL'] += 9
        postsynaptic['SMBVL'] += 7
        postsynaptic['VB2'] += 1

def AIZR():
        postsynaptic['AIAR'] += 1
        postsynaptic['AIBL'] += 8
        postsynaptic['AIBR'] += 1
        postsynaptic['AIZL'] += 2
        postsynaptic['ASGR'] += 1
        postsynaptic['ASHR'] += 1
        postsynaptic['AVEL'] += 4
        postsynaptic['AVER'] += 1
        postsynaptic['AWAR'] += 1
        postsynaptic['DVA'] += 1
        postsynaptic['RIAR'] += 7
        postsynaptic['RIMR'] += 4
        postsynaptic['SMBDR'] += 5
        postsynaptic['SMBVR'] += 3
        postsynaptic['SMDDR'] += 1

def ALA():
        postsynaptic['ADEL'] += 1
        postsynaptic['AVAL'] += 1
        postsynaptic['AVEL'] += 2
        postsynaptic['AVER'] += 1
        postsynaptic['RID'] += 1
        postsynaptic['RMDR'] += 1

def ALML():
        postsynaptic['AVDR'] += 1
        postsynaptic['AVEL'] += 1
        postsynaptic['AVM'] += 1
        postsynaptic['BDUL'] += 6
        postsynaptic['CEPDL'] += 3
        postsynaptic['CEPVL'] += 2
        postsynaptic['PVCL'] += 2
        postsynaptic['PVCR'] += 1
        postsynaptic['PVR'] += 1
        postsynaptic['RMDDR'] += 1
        postsynaptic['RMGL'] += 1
        postsynaptic['SDQL'] += 1

def ALMR():
        postsynaptic['AVM'] += 1
        postsynaptic['BDUR'] += 5
        postsynaptic['CEPDR'] += 1
        postsynaptic['CEPVR'] += 1
        postsynaptic['PVCR'] += 3
        postsynaptic['RMDDL'] += 1
        postsynaptic['SIADL'] += 1

def ALNL():
        postsynaptic['SAAVL'] += 3
        postsynaptic['SMBDR'] += 2
        postsynaptic['SMBDR'] += 1
        postsynaptic['SMDVL'] += 1

def ALNR():
        postsynaptic['ADER'] += 1
        postsynaptic['RMHR'] += 1
        postsynaptic['SAAVR'] += 2
        postsynaptic['SMBDL'] += 2
        postsynaptic['SMDDR'] += 1
        postsynaptic['SMDVL'] += 1

def AQR():
        postsynaptic['AVAL'] += 1
        postsynaptic['AVAR'] += 3
        postsynaptic['AVBL'] += 3
        postsynaptic['AVBL'] += 1
        postsynaptic['AVBR'] += 4
        postsynaptic['AVDL'] += 1
        postsynaptic['AVDR'] += 1
        postsynaptic['AVJL'] += 1
        postsynaptic['AVKL'] += 2
        postsynaptic['AVKR'] += 1
        postsynaptic['BAGL'] += 2
        postsynaptic['BAGR'] += 2
        postsynaptic['PVCR'] += 2
        postsynaptic['PVPL'] += 1
        postsynaptic['PVPL'] += 7
        postsynaptic['PVPR'] += 9
        postsynaptic['RIAL'] += 3
        postsynaptic['RIAR'] += 1
        postsynaptic['RIGL'] += 2
        postsynaptic['RIGR'] += 1
        postsynaptic['URXL'] += 1

def AS1():
        postsynaptic['AVAL'] += 3
        postsynaptic['AVAR'] += 2
        postsynaptic['DA1'] += 2
        postsynaptic['MDL05'] += 3
        postsynaptic['MDL08'] += 3
        postsynaptic['MDR05'] += 3
        postsynaptic['MDR08'] += 4
        postsynaptic['VA3'] += 1
        postsynaptic['VD1'] += 5
        postsynaptic['VD2'] += 1

def AS2():
        postsynaptic['DA2'] += 1
        postsynaptic['DB1'] += 1
        postsynaptic['DD1'] += 1
        postsynaptic['MDL07'] += 3
        postsynaptic['MDL08'] += 2
        postsynaptic['MDR07'] += 3
        postsynaptic['MDR08'] += 3
        postsynaptic['VA4'] += 2
        postsynaptic['VD2'] += 10

def AS3():
        postsynaptic['AVAL'] += 2
        postsynaptic['AVAR'] += 1
        postsynaptic['DA2'] += 1
        postsynaptic['DA3'] += 1
        postsynaptic['DD1'] += 1
        postsynaptic['MDL09'] += 3
        postsynaptic['MDL10'] += 3
        postsynaptic['MDR09'] += 3
        postsynaptic['MDR10'] += 3
        postsynaptic['VA5'] += 2
        postsynaptic['VD2'] += 1
        postsynaptic['VD3'] += 15

def AS4():
        postsynaptic['AS5'] += 1
        postsynaptic['DA3'] += 1
        postsynaptic['MDL11'] += 2
        postsynaptic['MDL12'] += 2
        postsynaptic['MDR11'] += 3
        postsynaptic['MDR12'] += 2
        postsynaptic['VD4'] += 11

def AS5():
        postsynaptic['AVAL'] += 1
        postsynaptic['AVAR'] += 1
        postsynaptic['DD2'] += 1
        postsynaptic['MDL11'] += 2
        postsynaptic['MDL14'] += 3
        postsynaptic['MDR11'] += 2
        postsynaptic['MDR14'] += 3
        postsynaptic['VA7'] += 1
        postsynaptic['VD5'] += 9

def AS6():
        postsynaptic['AVAL'] += 1
        postsynaptic['AVAR'] += 1
        postsynaptic['AVBR'] += 1
        postsynaptic['DA5'] += 2
        postsynaptic['MDL13'] += 3
        postsynaptic['MDL14'] += 2
        postsynaptic['MDR13'] += 3
        postsynaptic['MDR14'] += 2
        postsynaptic['VA8'] += 1
        postsynaptic['VD6'] += 13

def AS7():
        postsynaptic['AVAL'] += 6
        postsynaptic['AVAR'] += 5
        postsynaptic['AVBL'] += 2
        postsynaptic['AVBR'] += 2
        postsynaptic['MDL13'] += 2
        postsynaptic['MDL16'] += 3
        postsynaptic['MDR13'] += 2
        postsynaptic['MDR16'] += 3

def AS8():
        postsynaptic['AVAL'] += 4
        postsynaptic['AVAR'] += 3
        postsynaptic['MDL15'] += 2
        postsynaptic['MDL18'] += 3
        postsynaptic['MDR15'] += 2
        postsynaptic['MDR18'] += 3

def AS9():
        postsynaptic['AVAL'] += 4
        postsynaptic['AVAR'] += 1
        postsynaptic['DVB'] += 7
        postsynaptic['MDL17'] += 2
        postsynaptic['MDL20'] += 3
        postsynaptic['MDR17'] += 2
        postsynaptic['MDR20'] += 3

def AS10():
        postsynaptic['AVAL'] += 1
        postsynaptic['AVAR'] += 1
        postsynaptic['MDL19'] += 3
        postsynaptic['MDL20'] += 2
        postsynaptic['MDR19'] += 3
        postsynaptic['MDR20'] += 2

def AS11():
        postsynaptic['MDL21'] += 1
        postsynaptic['MDL22'] += 1
        postsynaptic['MDL23'] += 1
        postsynaptic['MDL24'] += 1
        postsynaptic['MDR21'] += 1
        postsynaptic['MDR22'] += 1
        postsynaptic['MDR23'] += 1
        postsynaptic['MDR24'] += 1
        postsynaptic['PDA'] += 1
        postsynaptic['PDB'] += 1
        postsynaptic['PDB'] += 2
        postsynaptic['VD13'] += 2

def ASEL():
        postsynaptic['ADFR'] += 1
        postsynaptic['AIAL'] += 3
        postsynaptic['AIBL'] += 7
        postsynaptic['AIBR'] += 2
        postsynaptic['AIYL'] += 13
        postsynaptic['AIYR'] += 6
        postsynaptic['AWCL'] += 4
        postsynaptic['AWCR'] += 1
        postsynaptic['RIAR'] += 1

def ASER():
        postsynaptic['AFDL'] += 1
        postsynaptic['AFDR'] += 2
        postsynaptic['AIAL'] += 1
        postsynaptic['AIAR'] += 3
        postsynaptic['AIBL'] += 2
        postsynaptic['AIBR'] += 10
        postsynaptic['AIYL'] += 2
        postsynaptic['AIYR'] += 14
        postsynaptic['AWAR'] += 1
        postsynaptic['AWCL'] += 1
        postsynaptic['AWCR'] += 1

def ASGL():
        postsynaptic['AIAL'] += 9
        postsynaptic['AIBL'] += 3
        postsynaptic['AINR'] += 1
        postsynaptic['AIZL'] += 1
        postsynaptic['ASKL'] += 1

def ASGR():
        postsynaptic['AIAR'] += 10
        postsynaptic['AIBR'] += 2
        postsynaptic['AINL'] += 1
        postsynaptic['AIYR'] += 1
        postsynaptic['AIZR'] += 1

def ASHL():
        postsynaptic['ADAL'] += 1
        postsynaptic['ADFL'] += 3
        postsynaptic['AIAL'] += 7
        postsynaptic['AIBL'] += 5
        postsynaptic['AIZL'] += 1
        postsynaptic['ASHR'] += 1
        postsynaptic['ASKL'] += 1
        postsynaptic['AVAL'] += 2
        postsynaptic['AVBL'] += 6
        postsynaptic['AVDL'] += 2
        postsynaptic['AVDR'] += 2
        postsynaptic['RIAL'] += 4
        postsynaptic['RICL'] += 2
        postsynaptic['RIML'] += 1
        postsynaptic['RIPL'] += 1
        postsynaptic['RMGL'] += 1

def ASHR():
        postsynaptic['ADAR'] += 3
        postsynaptic['ADFR'] += 2
        postsynaptic['AIAR'] += 10
        postsynaptic['AIBR'] += 3
        postsynaptic['AIZR'] += 1
        postsynaptic['ASHL'] += 1
        postsynaptic['ASKR'] += 1
        postsynaptic['AVAR'] += 5
        postsynaptic['AVBR'] += 3
        postsynaptic['AVDL'] += 5
        postsynaptic['AVDR'] += 1
        postsynaptic['AVER'] += 3
        postsynaptic['HSNR'] += 1
        postsynaptic['PVPR'] += 1
        postsynaptic['RIAR'] += 2
        postsynaptic['RICR'] += 2
        postsynaptic['RMGR'] += 2
        postsynaptic['RMGR'] += 1

def ASIL():
        postsynaptic['AIAL'] += 2
        postsynaptic['AIBL'] += 1
        postsynaptic['AIYL'] += 2
        postsynaptic['AIZL'] += 1
        postsynaptic['ASER'] += 1
        postsynaptic['ASIR'] += 1
        postsynaptic['ASKL'] += 2
        postsynaptic['AWCL'] += 1
        postsynaptic['AWCR'] += 1
        postsynaptic['RIBL'] += 1

def ASIR():
        postsynaptic['AIAL'] += 1
        postsynaptic['AIAR'] += 3
        postsynaptic['AIAR'] += 2
        postsynaptic['AIBR'] += 1
        postsynaptic['ASEL'] += 2
        postsynaptic['ASHR'] += 1
        postsynaptic['ASIL'] += 1
        postsynaptic['AWCL'] += 1
        postsynaptic['AWCR'] += 1

def ASJL():
        postsynaptic['ASJR'] += 1
        postsynaptic['ASKL'] += 4
        postsynaptic['HSNL'] += 1
        postsynaptic['HSNR'] += 1
        postsynaptic['PVQL'] += 14

def ASJR():
        postsynaptic['ASJL'] += 1
        postsynaptic['ASKR'] += 4
        postsynaptic['HSNR'] += 1
        postsynaptic['PVQR'] += 13

def ASKL():
        postsynaptic['AIAL'] += 11
        postsynaptic['AIBL'] += 2
        postsynaptic['AIML'] += 2
        postsynaptic['ASKR'] += 1
        postsynaptic['PVQL'] += 5
        postsynaptic['RMGL'] += 1

def ASKR():
        postsynaptic['AIAR'] += 11
        postsynaptic['AIMR'] += 1
        postsynaptic['ASHR'] += 1
        postsynaptic['ASKL'] += 1
        postsynaptic['AWAR'] += 1
        postsynaptic['CEPVR'] += 1
        postsynaptic['PVQR'] += 4
        postsynaptic['RIFR'] += 1
        postsynaptic['RMGR'] += 1

def AUAL():
        postsynaptic['AINR'] += 1
        postsynaptic['AUAR'] += 1
        postsynaptic['AVAL'] += 3
        postsynaptic['AVDR'] += 1
        postsynaptic['AVEL'] += 3
        postsynaptic['AWBL'] += 1
        postsynaptic['RIAL'] += 5
        postsynaptic['RIBL'] += 9

def AUAR():
        postsynaptic['AINL'] += 1
        postsynaptic['AIYR'] += 1
        postsynaptic['AUAL'] += 1
        postsynaptic['AVAR'] += 1
        postsynaptic['AVER'] += 4
        postsynaptic['AWBR'] += 1
        postsynaptic['RIAR'] += 6
        postsynaptic['RIBR'] += 13
        postsynaptic['URXR'] += 1

def AVAL():
        postsynaptic['AS1'] += 3
        postsynaptic['AS10'] += 3
        postsynaptic['AS11'] += 4
        postsynaptic['AS2'] += 1
        postsynaptic['AS3'] += 3
        postsynaptic['AS4'] += 1
        postsynaptic['AS5'] += 4
        postsynaptic['AS6'] += 1
        postsynaptic['AS7'] += 14
        postsynaptic['AS8'] += 9
        postsynaptic['AS9'] += 12
        postsynaptic['AVAR'] += 7
        postsynaptic['AVBR'] += 1
        postsynaptic['AVDL'] += 1
        postsynaptic['AVHL'] += 1
        postsynaptic['AVJL'] += 2
        postsynaptic['DA1'] += 4
        postsynaptic['DA2'] += 4
        postsynaptic['DA3'] += 6
        postsynaptic['DA4'] += 10
        postsynaptic['DA5'] += 8
        postsynaptic['DA6'] += 21
        postsynaptic['DA7'] += 4
        postsynaptic['DA8'] += 4
        postsynaptic['DA9'] += 3
        postsynaptic['DB5'] += 2
        postsynaptic['DB6'] += 4
        postsynaptic['FLPL'] += 1
        postsynaptic['LUAL'] += 2
        postsynaptic['PVCL'] += 12
        postsynaptic['PVCR'] += 11
        postsynaptic['PVPL'] += 1
        postsynaptic['RIMR'] += 3
        postsynaptic['SABD'] += 4
        postsynaptic['SABVR'] += 1
        postsynaptic['SDQR'] += 1
        postsynaptic['URYDL'] += 1
        postsynaptic['URYVR'] += 1
        postsynaptic['VA1'] += 3
        postsynaptic['VA10'] += 6
        postsynaptic['VA11'] += 7
        postsynaptic['VA12'] += 2
        postsynaptic['VA2'] += 5
        postsynaptic['VA3'] += 3
        postsynaptic['VA4'] += 3
        postsynaptic['VA5'] += 8
        postsynaptic['VA6'] += 10
        postsynaptic['VA7'] += 2
        postsynaptic['VA8'] += 19
        postsynaptic['VA9'] += 8
        postsynaptic['VB9'] += 5

def AVAR():
        postsynaptic['ADER'] += 1
        postsynaptic['AS1'] += 3
        postsynaptic['AS10'] += 2
        postsynaptic['AS11'] += 6
        postsynaptic['AS2'] += 2
        postsynaptic['AS3'] += 2
        postsynaptic['AS4'] += 1
        postsynaptic['AS5'] += 2
        postsynaptic['AS6'] += 3
        postsynaptic['AS7'] += 8
        postsynaptic['AS8'] += 9
        postsynaptic['AS9'] += 6
        postsynaptic['AVAL'] += 6
        postsynaptic['AVBL'] += 1
        postsynaptic['AVDL'] += 1
        postsynaptic['AVDR'] += 2
        postsynaptic['AVEL'] += 2
        postsynaptic['AVER'] += 2
        postsynaptic['DA1'] += 8
        postsynaptic['DA2'] += 4
        postsynaptic['DA3'] += 5
        postsynaptic['DA4'] += 8
        postsynaptic['DA5'] += 7
        postsynaptic['DA6'] += 13
        postsynaptic['DA7'] += 3
        postsynaptic['DA8'] += 9
        postsynaptic['DA9'] += 2
        postsynaptic['DB3'] += 1
        postsynaptic['DB5'] += 3
        postsynaptic['DB6'] += 5
        postsynaptic['LUAL'] += 1
        postsynaptic['LUAR'] += 3
        postsynaptic['PDEL'] += 1
        postsynaptic['PDER'] += 1
        postsynaptic['PVCL'] += 7
        postsynaptic['PVCR'] += 8
        postsynaptic['RIGL'] += 1
        postsynaptic['RIML'] += 2
        postsynaptic['RIMR'] += 1
        postsynaptic['SABD'] += 1
        postsynaptic['SABVL'] += 6
        postsynaptic['SABVR'] += 1
        postsynaptic['URYDR'] += 1
        postsynaptic['URYVL'] += 1
        postsynaptic['VA10'] += 5
        postsynaptic['VA11'] += 15
        postsynaptic['VA12'] += 1
        postsynaptic['VA2'] += 2
        postsynaptic['VA3'] += 7
        postsynaptic['VA4'] += 5
        postsynaptic['VA5'] += 4
        postsynaptic['VA6'] += 5
        postsynaptic['VA7'] += 4
        postsynaptic['VA8'] += 16
        postsynaptic['VB9'] += 10
        postsynaptic['VD13'] += 2

def AVBL():
        postsynaptic['AQR'] += 1
        postsynaptic['AS10'] += 1
        postsynaptic['AS3'] += 1
        postsynaptic['AS4'] += 1
        postsynaptic['AS5'] += 1
        postsynaptic['AS6'] += 1
        postsynaptic['AS7'] += 2
        postsynaptic['AS9'] += 1
        postsynaptic['AVAL'] += 7
        postsynaptic['AVAR'] += 7
        postsynaptic['AVBR'] += 4
        postsynaptic['AVDL'] += 1
        postsynaptic['AVDR'] += 2
        postsynaptic['AVEL'] += 1
        postsynaptic['AVER'] += 2
        postsynaptic['AVL'] += 1
        postsynaptic['DB3'] += 1
        postsynaptic['DB4'] += 1
        postsynaptic['DB5'] += 1
        postsynaptic['DB6'] += 2
        postsynaptic['DB7'] += 2
        postsynaptic['DVA'] += 1
        postsynaptic['PVNR'] += 1
        postsynaptic['RIBL'] += 1
        postsynaptic['RIBR'] += 1
        postsynaptic['RID'] += 1
        postsynaptic['SDQR'] += 1
        postsynaptic['SIBVL'] += 1
        postsynaptic['VA10'] += 1
        postsynaptic['VA2'] += 1
        postsynaptic['VA7'] += 1
        postsynaptic['VB1'] += 1
        postsynaptic['VB10'] += 2
        postsynaptic['VB11'] += 2
        postsynaptic['VB2'] += 4
        postsynaptic['VB4'] += 1
        postsynaptic['VB5'] += 1
        postsynaptic['VB6'] += 1
        postsynaptic['VB7'] += 2
        postsynaptic['VB8'] += 7
        postsynaptic['VB9'] += 1
        postsynaptic['VC3'] += 1

def AVBR():
        postsynaptic['AS1'] += 1
        postsynaptic['AS10'] += 1
        postsynaptic['AS3'] += 1
        postsynaptic['AS4'] += 1
        postsynaptic['AS5'] += 1
        postsynaptic['AS6'] += 2
        postsynaptic['AS7'] += 3
        postsynaptic['AVAL'] += 6
        postsynaptic['AVAR'] += 7
        postsynaptic['AVBL'] += 4
        postsynaptic['DA5'] += 1
        postsynaptic['DB1'] += 3
        postsynaptic['DB2'] += 1
        postsynaptic['DB3'] += 1
        postsynaptic['DB4'] += 1
        postsynaptic['DB5'] += 1
        postsynaptic['DB6'] += 1
        postsynaptic['DB7'] += 1
        postsynaptic['DD1'] += 1
        postsynaptic['DVA'] += 1
        postsynaptic['HSNR'] += 1
        postsynaptic['PVNL'] += 2
        postsynaptic['RIBL'] += 1
        postsynaptic['RIBR'] += 1
        postsynaptic['RID'] += 2
        postsynaptic['SIBVL'] += 1
        postsynaptic['VA4'] += 1
        postsynaptic['VA8'] += 1
        postsynaptic['VA9'] += 2
        postsynaptic['VB10'] += 1
        postsynaptic['VB11'] += 1
        postsynaptic['VB2'] += 1
        postsynaptic['VB3'] += 1
        postsynaptic['VB4'] += 1
        postsynaptic['VB6'] += 2
        postsynaptic['VB7'] += 2
        postsynaptic['VB8'] += 3
        postsynaptic['VB9'] += 6
        postsynaptic['VD10'] += 1
        postsynaptic['VD3'] += 1

def AVDL():
        postsynaptic['ADAR'] += 2
        postsynaptic['AS1'] += 1
        postsynaptic['AS10'] += 1
        postsynaptic['AS11'] += 2
        postsynaptic['AS4'] += 1
        postsynaptic['AS5'] += 1
        postsynaptic['AVAL'] += 13
        postsynaptic['AVAR'] += 19
        postsynaptic['AVM'] += 2
        postsynaptic['DA1'] += 1
        postsynaptic['DA2'] += 1
        postsynaptic['DA3'] += 4
        postsynaptic['DA4'] += 1
        postsynaptic['DA5'] += 1
        postsynaptic['DA8'] += 1
        postsynaptic['FLPL'] += 1
        postsynaptic['FLPR'] += 1
        postsynaptic['LUAL'] += 1
        postsynaptic['PVCL'] += 1
        postsynaptic['SABD'] += 1
        postsynaptic['SABVL'] += 1
        postsynaptic['SABVR'] += 1
        postsynaptic['VA5'] += 1

def AVDR():
        postsynaptic['ADAL'] += 2
        postsynaptic['ADLL'] += 1
        postsynaptic['AS10'] += 1
        postsynaptic['AS5'] += 1
        postsynaptic['AVAL'] += 16
        postsynaptic['AVAR'] += 15
        postsynaptic['AVBL'] += 1
        postsynaptic['AVDL'] += 2
        postsynaptic['AVJL'] += 2
        postsynaptic['DA1'] += 2
        postsynaptic['DA2'] += 1
        postsynaptic['DA3'] += 1
        postsynaptic['DA4'] += 1
        postsynaptic['DA5'] += 2
        postsynaptic['DA8'] += 1
        postsynaptic['DA9'] += 1
        postsynaptic['DB4'] += 1
        postsynaptic['DVC'] += 1
        postsynaptic['FLPR'] += 1
        postsynaptic['LUAL'] += 2
        postsynaptic['PQR'] += 1
        postsynaptic['SABD'] += 1
        postsynaptic['SABVL'] += 3
        postsynaptic['SABVR'] += 1
        postsynaptic['VA11'] += 1
        postsynaptic['VA2'] += 1
        postsynaptic['VA3'] += 2
        postsynaptic['VA6'] += 1

def AVEL():
        postsynaptic['AS1'] += 1
        postsynaptic['AVAL'] += 12
        postsynaptic['AVAR'] += 7
        postsynaptic['AVER'] += 1
        postsynaptic['DA1'] += 5
        postsynaptic['DA2'] += 1
        postsynaptic['DA3'] += 3
        postsynaptic['DA4'] += 1
        postsynaptic['PVCR'] += 1
        postsynaptic['PVT'] += 1
        postsynaptic['RIML'] += 2
        postsynaptic['RIMR'] += 3
        postsynaptic['RMDVR'] += 1
        postsynaptic['RMEV'] += 1
        postsynaptic['SABD'] += 6
        postsynaptic['SABVL'] += 7
        postsynaptic['SABVR'] += 3
        postsynaptic['VA1'] += 5
        postsynaptic['VA3'] += 3
        postsynaptic['VD2'] += 1
        postsynaptic['VD3'] += 1

def AVER():
        postsynaptic['AS1'] += 3
        postsynaptic['AS2'] += 2
        postsynaptic['AS3'] += 1
        postsynaptic['AVAL'] += 7
        postsynaptic['AVAR'] += 16
        postsynaptic['AVDR'] += 1
        postsynaptic['AVEL'] += 1
        postsynaptic['DA1'] += 5
        postsynaptic['DA2'] += 3
        postsynaptic['DA3'] += 1
        postsynaptic['DB3'] += 1
        postsynaptic['RIML'] += 3
        postsynaptic['RIMR'] += 2
        postsynaptic['RMDVL'] += 1
        postsynaptic['RMDVR'] += 1
        postsynaptic['RMEV'] += 1
        postsynaptic['SABD'] += 2
        postsynaptic['SABVL'] += 3
        postsynaptic['SABVR'] += 3
        postsynaptic['VA1'] += 1
        postsynaptic['VA2'] += 1
        postsynaptic['VA3'] += 2
        postsynaptic['VA4'] += 1
        postsynaptic['VA5'] += 1

def AVFL():
        postsynaptic['AVBL'] += 1
        postsynaptic['AVBR'] += 2
        postsynaptic['AVFR'] += 30
        postsynaptic['AVG'] += 1
        postsynaptic['AVHL'] += 4
        postsynaptic['AVHR'] += 7
        postsynaptic['AVJL'] += 1
        postsynaptic['AVJR'] += 1
        postsynaptic['AVL'] += 1
        postsynaptic['HSNL'] += 1
        postsynaptic['MVL11'] += 1
        postsynaptic['MVL12'] += 1
        postsynaptic['PDER'] += 1
        postsynaptic['PVNL'] += 2
        postsynaptic['PVQL'] += 1
        postsynaptic['PVQR'] += 2
        postsynaptic['VB1'] += 1

def AVFR():
        postsynaptic['ASJL'] += 1
        postsynaptic['ASKL'] += 1
        postsynaptic['AVBL'] += 1
        postsynaptic['AVBR'] += 5
        postsynaptic['AVFL'] += 24
        postsynaptic['AVHL'] += 4
        postsynaptic['AVHR'] += 2
        postsynaptic['AVJL'] += 1
        postsynaptic['AVJR'] += 1
        postsynaptic['HSNR'] += 1
        postsynaptic['MVL14'] += 2
        postsynaptic['MVR14'] += 2
        postsynaptic['PVQL'] += 1
        postsynaptic['VC4'] += 1
        postsynaptic['VD11'] += 1

def AVG():
        postsynaptic['AVAR'] += 3
        postsynaptic['AVBL'] += 1
        postsynaptic['AVBR'] += 2
        postsynaptic['AVDR'] += 1
        postsynaptic['AVEL'] += 1
        postsynaptic['AVER'] += 1
        postsynaptic['AVFL'] += 1
        postsynaptic['AVJL'] += 1
        postsynaptic['AVL'] += 1
        postsynaptic['DA8'] += 1
        postsynaptic['PHAL'] += 2
        postsynaptic['PVCL'] += 1
        postsynaptic['PVNR'] += 1
        postsynaptic['PVPR'] += 1
        postsynaptic['PVQR'] += 1
        postsynaptic['PVT'] += 1
        postsynaptic['RIFL'] += 1
        postsynaptic['RIFR'] += 1
        postsynaptic['VA11'] += 1

def AVHL():
        postsynaptic['ADFR'] += 3
        postsynaptic['AVBL'] += 1
        postsynaptic['AVBR'] += 1
        postsynaptic['AVDL'] += 1
        postsynaptic['AVFL'] += 1
        postsynaptic['AVFL'] += 2
        postsynaptic['AVFR'] += 5
        postsynaptic['AVHR'] += 2
        postsynaptic['AVJL'] += 1
        postsynaptic['AWBR'] += 1
        postsynaptic['PHBR'] += 1
        postsynaptic['PVPR'] += 2
        postsynaptic['PVQL'] += 1
        postsynaptic['PVQR'] += 2
        postsynaptic['RIMR'] += 1
        postsynaptic['RIR'] += 3
        postsynaptic['SMBDR'] += 1
        postsynaptic['SMBVR'] += 1
        postsynaptic['VD1'] += 1

def AVHR():
        postsynaptic['ADLL'] += 1
        postsynaptic['ADLR'] += 2
        postsynaptic['AQR'] += 2
        postsynaptic['AVBL'] += 2
        postsynaptic['AVBR'] += 1
        postsynaptic['AVDR'] += 1
        postsynaptic['AVFL'] += 1
        postsynaptic['AVFR'] += 2
        postsynaptic['AVHL'] += 2
        postsynaptic['AVJR'] += 4
        postsynaptic['PVNL'] += 1
        postsynaptic['PVPL'] += 3
        postsynaptic['RIGL'] += 1
        postsynaptic['RIR'] += 4
        postsynaptic['SMBDL'] += 1
        postsynaptic['SMBVL'] += 1

def AVJL():
        postsynaptic['AVAL'] += 2
        postsynaptic['AVAR'] += 1
        postsynaptic['AVBL'] += 1
        postsynaptic['AVBR'] += 4
        postsynaptic['AVDL'] += 1
        postsynaptic['AVDR'] += 2
        postsynaptic['AVEL'] += 1
        postsynaptic['AVFR'] += 1
        postsynaptic['AVHL'] += 2
        postsynaptic['AVJR'] += 4
        postsynaptic['HSNR'] += 1
        postsynaptic['PLMR'] += 2
        postsynaptic['PVCL'] += 2
        postsynaptic['PVCR'] += 5
        postsynaptic['PVNR'] += 1
        postsynaptic['RIFR'] += 1
        postsynaptic['RIS'] += 2

def AVJR():
        postsynaptic['AVAL'] += 1
        postsynaptic['AVAR'] += 1
        postsynaptic['AVBL'] += 3
        postsynaptic['AVBR'] += 1
        postsynaptic['AVDL'] += 1
        postsynaptic['AVDR'] += 3
        postsynaptic['AVER'] += 3
        postsynaptic['AVJL'] += 5
        postsynaptic['PVCL'] += 3
        postsynaptic['PVCR'] += 4
        postsynaptic['PVQR'] += 1
        postsynaptic['SABVL'] += 1

def AVKL():
        postsynaptic['ADER'] += 1
        postsynaptic['AQR'] += 2
        postsynaptic['AVBL'] += 1
        postsynaptic['AVEL'] += 2
        postsynaptic['AVER'] += 1
        postsynaptic['AVKR'] += 2
        postsynaptic['AVM'] += 1
        postsynaptic['DVA'] += 1
        postsynaptic['PDEL'] += 3
        postsynaptic['PDER'] += 1
        postsynaptic['PVM'] += 1
        postsynaptic['PVPL'] += 1
        postsynaptic['PVPR'] += 1
        postsynaptic['PVT'] += 2
        postsynaptic['RICL'] += 1
        postsynaptic['RICR'] += 1
        postsynaptic['RIGL'] += 1
        postsynaptic['RIML'] += 2
        postsynaptic['RIMR'] += 1
        postsynaptic['RMFR'] += 1
        postsynaptic['SAADR'] += 1
        postsynaptic['SIAVR'] += 1
        postsynaptic['SMBDL'] += 1
        postsynaptic['SMBDR'] += 1
        postsynaptic['SMBVR'] += 1
        postsynaptic['SMDDR'] += 1
        postsynaptic['VB1'] += 4
        postsynaptic['VB10'] += 1

def AVKR():
        postsynaptic['ADEL'] += 1
        postsynaptic['AQR'] += 1
        postsynaptic['AVKL'] += 2
        postsynaptic['BDUL'] += 1
        postsynaptic['MVL10'] += 1
        postsynaptic['PVPL'] += 6
        postsynaptic['PVQL'] += 1
        postsynaptic['RICL'] += 1
        postsynaptic['RIGR'] += 1
        postsynaptic['RIML'] += 2
        postsynaptic['RIMR'] += 2
        postsynaptic['RMDR'] += 1
        postsynaptic['RMFL'] += 1
        postsynaptic['SAADL'] += 1
        postsynaptic['SMBDL'] += 1
        postsynaptic['SMBDR'] += 2
        postsynaptic['SMBVR'] += 1
        postsynaptic['SMDDL'] += 1
        postsynaptic['SMDDR'] += 2

def AVL():
        postsynaptic['AVEL'] += 1
        postsynaptic['AVFR'] += 1
        postsynaptic['DA2'] += 1
        postsynaptic['DD1'] += 1
        postsynaptic['DD6'] += 2
        postsynaptic['DVB'] += 1
        postsynaptic['DVC'] += 9
        postsynaptic['HSNR'] += 1
        postsynaptic['MVL10'] += -5
        postsynaptic['MVR10'] += -5
        postsynaptic['PVM'] += 1
        postsynaptic['PVPR'] += 1
        postsynaptic['PVWL'] += 1
        postsynaptic['SABD'] += 5
        postsynaptic['SABVL'] += 4
        postsynaptic['SABVR'] += 3
        postsynaptic['VD12'] += 4

def AVM():
        postsynaptic['ADER'] += 1
        postsynaptic['ALML'] += 1
        postsynaptic['ALMR'] += 1
        postsynaptic['AVBL'] += 6
        postsynaptic['AVBR'] += 6
        postsynaptic['AVDL'] += 2
        postsynaptic['AVJR'] += 1
        postsynaptic['BDUL'] += 3
        postsynaptic['BDUR'] += 2
        postsynaptic['DA1'] += 1
        postsynaptic['PVCL'] += 4
        postsynaptic['PVCR'] += 5
        postsynaptic['PVNL'] += 1
        postsynaptic['PVR'] += 3
        postsynaptic['RID'] += 1
        postsynaptic['SIBVL'] += 1
        postsynaptic['VA1'] += 2

def AWAL():
        postsynaptic['ADAL'] += 1
        postsynaptic['AFDL'] += 5
        postsynaptic['AIAL'] += 1
        postsynaptic['AIYL'] += 1
        postsynaptic['AIZL'] += 10
        postsynaptic['ASEL'] += 4
        postsynaptic['ASGL'] += 1
        postsynaptic['AWAR'] += 1
        postsynaptic['AWBL'] += 1

def AWAR():
        postsynaptic['ADFR'] += 3
        postsynaptic['AFDR'] += 7
        postsynaptic['AIAR'] += 1
        postsynaptic['AIYR'] += 2
        postsynaptic['AIZR'] += 7
        postsynaptic['AIZR'] += 1
        postsynaptic['ASEL'] += 1
        postsynaptic['ASER'] += 2
        postsynaptic['AUAR'] += 1
        postsynaptic['AWAL'] += 1
        postsynaptic['AWBR'] += 1
        postsynaptic['RIFR'] += 2
        postsynaptic['RIGR'] += 1
        postsynaptic['RIR'] += 2

def AWBL():
        postsynaptic['ADFL'] += 9
        postsynaptic['AIBR'] += 1
        postsynaptic['AIZL'] += 9
        postsynaptic['AUAL'] += 1
        postsynaptic['AVBL'] += 1
        postsynaptic['AWBR'] += 1
        postsynaptic['RIAL'] += 3
        postsynaptic['RMGL'] += 1
        postsynaptic['SMBDL'] += 1

def AWBR():
        postsynaptic['ADFR'] += 4
        postsynaptic['AIZR'] += 4
        postsynaptic['ASGR'] += 1
        postsynaptic['ASHR'] += 2
        postsynaptic['AUAR'] += 1
        postsynaptic['AVBR'] += 2
        postsynaptic['AWBL'] += 1
        postsynaptic['RIAR'] += 1
        postsynaptic['RICL'] += 1
        postsynaptic['RIR'] += 2
        postsynaptic['RMGR'] += 1
        postsynaptic['SMBVR'] += 1

def AWCL():
        postsynaptic['AIAL'] += 2
        postsynaptic['AIAR'] += 4
        postsynaptic['AIBL'] += 1
        postsynaptic['AIBR'] += 1
        postsynaptic['AIYL'] += 10
        postsynaptic['ASEL'] += 1
        postsynaptic['AVAL'] += 1
        postsynaptic['AWCR'] += 1
        postsynaptic['RIAL'] += 3

def AWCR():
        postsynaptic['AIAR'] += 1
        postsynaptic['AIBR'] += 4
        postsynaptic['AIYL'] += 4
        postsynaptic['AIYR'] += 9
        postsynaptic['ASEL'] += 1
        postsynaptic['ASGR'] += 1
        postsynaptic['AWCL'] += 5

def BAGL():
        postsynaptic['AIBL'] += 1
        postsynaptic['AVAR'] += 1
        postsynaptic['AVEL'] += 1
        postsynaptic['AVER'] += 4
        postsynaptic['BAGR'] += 1
        postsynaptic['RIAR'] += 5
        postsynaptic['RIBL'] += 1
        postsynaptic['RIBR'] += 7
        postsynaptic['RIGL'] += 1
        postsynaptic['RIGR'] += 4
        postsynaptic['RIGR'] += 1
        postsynaptic['RIR'] += 1

def BAGR():
        postsynaptic['AIYL'] += 1
        postsynaptic['AVAL'] += 1
        postsynaptic['AVEL'] += 2
        postsynaptic['BAGL'] += 1
        postsynaptic['RIAL'] += 5
        postsynaptic['RIBL'] += 4
        postsynaptic['RIGL'] += 5
        postsynaptic['RIGL'] += 1
        postsynaptic['RIR'] += 1

def BDUL():
        postsynaptic['ADEL'] += 3
        postsynaptic['AVHL'] += 1
        postsynaptic['AVJR'] += 1
        postsynaptic['HSNL'] += 1
        postsynaptic['PVNL'] += 2
        postsynaptic['PVNR'] += 2
        postsynaptic['SAADL'] += 1
        postsynaptic['URADL'] += 1

def BDUR():
        postsynaptic['ADER'] += 1
        postsynaptic['ALMR'] += 1
        postsynaptic['AVAL'] += 3
        postsynaptic['AVHL'] += 1
        postsynaptic['AVJL'] += 2
        postsynaptic['HSNR'] += 4
        postsynaptic['PVCL'] += 1
        postsynaptic['PVNL'] += 2
        postsynaptic['PVNR'] += 1
        postsynaptic['SDQL'] += 1
        postsynaptic['URADR'] += 1

def CEPDL():
        postsynaptic['AVER'] += 5
        postsynaptic['IL1DL'] += 4
        postsynaptic['OLLL'] += 2
        postsynaptic['OLQDL'] += 6
        postsynaptic['OLQDL'] += 1
        postsynaptic['RIBL'] += 2
        postsynaptic['RICL'] += 1
        postsynaptic['RICR'] += 2
        postsynaptic['RIH'] += 1
        postsynaptic['RIPL'] += 2
        postsynaptic['RIS'] += 1
        postsynaptic['RMDVL'] += 3
        postsynaptic['RMGL'] += 4
        postsynaptic['RMHR'] += 4
        postsynaptic['SIADR'] += 1
        postsynaptic['SMBDR'] += 1
        postsynaptic['URADL'] += 2
        postsynaptic['URBL'] += 4
        postsynaptic['URYDL'] += 2

def CEPDR():
        postsynaptic['AVEL'] += 6
        postsynaptic['BDUR'] += 1
        postsynaptic['IL1DR'] += 5
        postsynaptic['IL1R'] += 1
        postsynaptic['OLLR'] += 8
        postsynaptic['OLQDR'] += 5
        postsynaptic['OLQDR'] += 2
        postsynaptic['RIBR'] += 1
        postsynaptic['RICL'] += 4
        postsynaptic['RICR'] += 3
        postsynaptic['RIH'] += 1
        postsynaptic['RIS'] += 1
        postsynaptic['RMDDL'] += 1
        postsynaptic['RMDVR'] += 2
        postsynaptic['RMGR'] += 1
        postsynaptic['RMHL'] += 4
        postsynaptic['RMHR'] += 1
        postsynaptic['SIADL'] += 1
        postsynaptic['SMBDR'] += 1
        postsynaptic['URADR'] += 1
        postsynaptic['URBR'] += 2
        postsynaptic['URYDR'] += 1

def CEPVL():
        postsynaptic['ADLL'] += 1
        postsynaptic['AVER'] += 3
        postsynaptic['IL1VL'] += 2
        postsynaptic['MVL03'] += 1
        postsynaptic['OLLL'] += 4
        postsynaptic['OLQVL'] += 6
        postsynaptic['OLQVL'] += 1
        postsynaptic['RICL'] += 7
        postsynaptic['RICR'] += 4
        postsynaptic['RIH'] += 1
        postsynaptic['RIPL'] += 1
        postsynaptic['RMDDL'] += 4
        postsynaptic['RMHL'] += 1
        postsynaptic['SIAVL'] += 1
        postsynaptic['URAVL'] += 2

def CEPVR():
        postsynaptic['ASGR'] += 1
        postsynaptic['AVEL'] += 5
        postsynaptic['IL1VR'] += 1
        postsynaptic['IL2VR'] += 2
        postsynaptic['MVR04'] += 1
        postsynaptic['OLLR'] += 7
        postsynaptic['OLQVR'] += 3
        postsynaptic['OLQVR'] += 1
        postsynaptic['RICL'] += 2
        postsynaptic['RICR'] += 2
        postsynaptic['RIH'] += 1
        postsynaptic['RIPR'] += 1
        postsynaptic['RIVL'] += 1
        postsynaptic['RMDDR'] += 2
        postsynaptic['RMHR'] += 2
        postsynaptic['SIAVR'] += 2
        postsynaptic['URAVR'] += 1

def DA1():
        postsynaptic['AVAL'] += 2
        postsynaptic['AVAR'] += 6
        postsynaptic['DA4'] += 1
        postsynaptic['DD1'] += 4
        postsynaptic['MDL08'] += 8
        postsynaptic['MDR08'] += 8
        postsynaptic['SABVL'] += 2
        postsynaptic['SABVR'] += 3
        postsynaptic['VD1'] += 17
        postsynaptic['VD2'] += 1

def DA2():
        postsynaptic['AS2'] += 1
        postsynaptic['AS3'] += 1
        postsynaptic['AVAL'] += 2
        postsynaptic['AVAR'] += 2
        postsynaptic['DD1'] += 1
        postsynaptic['MDL07'] += 2
        postsynaptic['MDL08'] += 1
        postsynaptic['MDL09'] += 2
        postsynaptic['MDL10'] += 2
        postsynaptic['MDR07'] += 2
        postsynaptic['MDR08'] += 2
        postsynaptic['MDR09'] += 2
        postsynaptic['MDR10'] += 2
        postsynaptic['SABVL'] += 1
        postsynaptic['VA1'] += 2
        postsynaptic['VD1'] += 2
        postsynaptic['VD2'] += 11
        postsynaptic['VD3'] += 5

def DA3():
        postsynaptic['AS4'] += 2
        postsynaptic['AVAR'] += 2
        postsynaptic['DA4'] += 2
        postsynaptic['DB3'] += 1
        postsynaptic['DD2'] += 1
        postsynaptic['MDL09'] += 5
        postsynaptic['MDL10'] += 5
        postsynaptic['MDL12'] += 5
        postsynaptic['MDR09'] += 5
        postsynaptic['MDR10'] += 5
        postsynaptic['MDR12'] += 5
        postsynaptic['VD3'] += 25
        postsynaptic['VD4'] += 6

def DA4():
        postsynaptic['AVAL'] += 3
        postsynaptic['AVAR'] += 2
        postsynaptic['DA1'] += 1
        postsynaptic['DA3'] += 1
        postsynaptic['DB3'] += 1
        postsynaptic['DD2'] += 1
        postsynaptic['MDL11'] += 4
        postsynaptic['MDL12'] += 4
        postsynaptic['MDL14'] += 5
        postsynaptic['MDR11'] += 4
        postsynaptic['MDR12'] += 4
        postsynaptic['MDR14'] += 5
        postsynaptic['VB6'] += 1
        postsynaptic['VD4'] += 12
        postsynaptic['VD5'] += 15

def DA5():
        postsynaptic['AS6'] += 2
        postsynaptic['AVAL'] += 1
        postsynaptic['AVAR'] += 5
        postsynaptic['DB4'] += 1
        postsynaptic['MDL13'] += 5
        postsynaptic['MDL14'] += 4
        postsynaptic['MDR13'] += 5
        postsynaptic['MDR14'] += 4
        postsynaptic['VA4'] += 1
        postsynaptic['VA5'] += 2
        postsynaptic['VD5'] += 1
        postsynaptic['VD6'] += 16

def DA6():
        postsynaptic['AVAL'] += 10
        postsynaptic['AVAR'] += 2
        postsynaptic['MDL11'] += 6
        postsynaptic['MDL12'] += 4
        postsynaptic['MDL13'] += 4
        postsynaptic['MDL14'] += 4
        postsynaptic['MDL16'] += 4
        postsynaptic['MDR11'] += 4
        postsynaptic['MDR12'] += 4
        postsynaptic['MDR13'] += 4
        postsynaptic['MDR14'] += 4
        postsynaptic['MDR16'] += 4
        postsynaptic['VD4'] += 4
        postsynaptic['VD5'] += 3
        postsynaptic['VD6'] += 3

def DA7():
        postsynaptic['AVAL'] += 2
        postsynaptic['MDL15'] += 4
        postsynaptic['MDL17'] += 4
        postsynaptic['MDL18'] += 4
        postsynaptic['MDR15'] += 4
        postsynaptic['MDR17'] += 4
        postsynaptic['MDR18'] += 4

def DA8():
        postsynaptic['AVAR'] += 1
        postsynaptic['DA9'] += 1
        postsynaptic['MDL17'] += 4
        postsynaptic['MDL19'] += 4
        postsynaptic['MDL20'] += 4
        postsynaptic['MDR17'] += 4
        postsynaptic['MDR19'] += 4
        postsynaptic['MDR20'] += 4

def DA9():
        postsynaptic['DA8'] += 1
        postsynaptic['DD6'] += 1
        postsynaptic['MDL19'] += 4
        postsynaptic['MDL21'] += 4
        postsynaptic['MDL22'] += 4
        postsynaptic['MDL23'] += 4
        postsynaptic['MDL24'] += 4
        postsynaptic['MDR19'] += 4
        postsynaptic['MDR21'] += 4
        postsynaptic['MDR22'] += 4
        postsynaptic['MDR23'] += 4
        postsynaptic['MDR24'] += 4
        postsynaptic['PDA'] += 1
        postsynaptic['PHCL'] += 1
        postsynaptic['RID'] += 1
        postsynaptic['VD13'] += 1

def DB1():
        postsynaptic['AIBR'] += 1
        postsynaptic['AS1'] += 1
        postsynaptic['AS2'] += 1
        postsynaptic['AS3'] += 1
        postsynaptic['AVBR'] += 3
        postsynaptic['DB2'] += 1
        postsynaptic['DB4'] += 1
        postsynaptic['DD1'] += 10
        postsynaptic['DVA'] += 1
        postsynaptic['MDL07'] += 1
        postsynaptic['MDL08'] += 1
        postsynaptic['MDR07'] += 1
        postsynaptic['MDR08'] += 1
        postsynaptic['RID'] += 1
        postsynaptic['RIS'] += 1
        postsynaptic['VB3'] += 1
        postsynaptic['VB4'] += 1
        postsynaptic['VD1'] += 21
        postsynaptic['VD2'] += 15
        postsynaptic['VD3'] += 1

def DB2():
        postsynaptic['AVBR'] += 1
        postsynaptic['DA3'] += 5
        postsynaptic['DB1'] += 1
        postsynaptic['DB3'] += 6
        postsynaptic['DD2'] += 3
        postsynaptic['MDL09'] += 3
        postsynaptic['MDL10'] += 3
        postsynaptic['MDL11'] += 3
        postsynaptic['MDL12'] += 3
        postsynaptic['MDR09'] += 3
        postsynaptic['MDR10'] += 3
        postsynaptic['MDR11'] += 3
        postsynaptic['MDR12'] += 3
        postsynaptic['VB1'] += 2
        postsynaptic['VD3'] += 23
        postsynaptic['VD4'] += 14
        postsynaptic['VD5'] += 1

def DB3():
        postsynaptic['AS4'] += 1
        postsynaptic['AS5'] += 1
        postsynaptic['AVBL'] += 1
        postsynaptic['AVBR'] += 1
        postsynaptic['DA4'] += 1
        postsynaptic['DB2'] += 6
        postsynaptic['DB4'] += 1
        postsynaptic['DD2'] += 4
        postsynaptic['DD3'] += 10
        postsynaptic['MDL11'] += 3
        postsynaptic['MDL12'] += 3
        postsynaptic['MDL13'] += 4
        postsynaptic['MDL14'] += 3
        postsynaptic['MDR11'] += 3
        postsynaptic['MDR12'] += 3
        postsynaptic['MDR13'] += 4
        postsynaptic['MDR14'] += 3
        postsynaptic['VD4'] += 9
        postsynaptic['VD5'] += 26
        postsynaptic['VD6'] += 7

def DB4():
        postsynaptic['AVBL'] += 1
        postsynaptic['AVBR'] += 1
        postsynaptic['DB1'] += 1
        postsynaptic['DB3'] += 1
        postsynaptic['DD3'] += 3
        postsynaptic['MDL13'] += 2
        postsynaptic['MDL14'] += 2
        postsynaptic['MDL16'] += 2
        postsynaptic['MDR13'] += 2
        postsynaptic['MDR14'] += 2
        postsynaptic['MDR16'] += 2
        postsynaptic['VB2'] += 1
        postsynaptic['VB4'] += 1
        postsynaptic['VD6'] += 13

def DB5():
        postsynaptic['AVAR'] += 2
        postsynaptic['AVBL'] += 1
        postsynaptic['AVBR'] += 1
        postsynaptic['MDL15'] += 2
        postsynaptic['MDL17'] += 2
        postsynaptic['MDL18'] += 2
        postsynaptic['MDR15'] += 2
        postsynaptic['MDR17'] += 2
        postsynaptic['MDR18'] += 2

def DB6():
        postsynaptic['AVAL'] += 3
        postsynaptic['AVBL'] += 2
        postsynaptic['AVBR'] += 1
        postsynaptic['MDL17'] += 2
        postsynaptic['MDL19'] += 2
        postsynaptic['MDL20'] += 2
        postsynaptic['MDR17'] += 2
        postsynaptic['MDR19'] += 2
        postsynaptic['MDR20'] += 2

def DB7():
        postsynaptic['AVBL'] += 2
        postsynaptic['AVBR'] += 1
        postsynaptic['MDL19'] += 2
        postsynaptic['MDL21'] += 2
        postsynaptic['MDL22'] += 2
        postsynaptic['MDL23'] += 2
        postsynaptic['MDL24'] += 2
        postsynaptic['MDR19'] += 2
        postsynaptic['MDR21'] += 2
        postsynaptic['MDR22'] += 2
        postsynaptic['MDR23'] += 2
        postsynaptic['MDR24'] += 2
        postsynaptic['VD13'] += 2

def DD1():
        postsynaptic['AVBR'] += 1
        postsynaptic['DD2'] += 3
        postsynaptic['MDL07'] += -6
        postsynaptic['MDL08'] += -6
        postsynaptic['MDL09'] += -7
        postsynaptic['MDL10'] += -6
        postsynaptic['MDR07'] += -6
        postsynaptic['MDR08'] += -6
        postsynaptic['MDR09'] += -7
        postsynaptic['MDR10'] += -6
        postsynaptic['VD1'] += 4
        postsynaptic['VD2'] += 1
        postsynaptic['VD2'] += 2

def DD2():
        postsynaptic['DA3'] += 1
        postsynaptic['DD1'] += 1
        postsynaptic['DD3'] += 2
        postsynaptic['MDL09'] += -6
        postsynaptic['MDL11'] += -7
        postsynaptic['MDL12'] += -6
        postsynaptic['MDR09'] += -6
        postsynaptic['MDR11'] += -7
        postsynaptic['MDR12'] += -6
        postsynaptic['VD3'] += 1
        postsynaptic['VD4'] += 3

def DD3():
        postsynaptic['DD2'] += 2
        postsynaptic['DD4'] += 1
        postsynaptic['MDL11'] += -7
        postsynaptic['MDL13'] += -9
        postsynaptic['MDL14'] += -7
        postsynaptic['MDR11'] += -7
        postsynaptic['MDR13'] += -9
        postsynaptic['MDR14'] += -7

def DD4():
        postsynaptic['DD3'] += 1
        postsynaptic['MDL13'] += -7
        postsynaptic['MDL15'] += -7
        postsynaptic['MDL16'] += -7
        postsynaptic['MDR13'] += -7
        postsynaptic['MDR15'] += -7
        postsynaptic['MDR16'] += -7
        postsynaptic['VC3'] += 1
        postsynaptic['VD8'] += 1

def DD5():
        postsynaptic['MDL17'] += -7
        postsynaptic['MDL18'] += -7
        postsynaptic['MDL20'] += -7
        postsynaptic['MDR17'] += -7
        postsynaptic['MDR18'] += -7
        postsynaptic['MDR20'] += -7
        postsynaptic['VB8'] += 1
        postsynaptic['VD10'] += 1
        postsynaptic['VD9'] += 1

def DD6():
        postsynaptic['MDL19'] += -7
        postsynaptic['MDL21'] += -7
        postsynaptic['MDL22'] += -7
        postsynaptic['MDL23'] += -7
        postsynaptic['MDL24'] += -7
        postsynaptic['MDR19'] += -7
        postsynaptic['MDR21'] += -7
        postsynaptic['MDR22'] += -7
        postsynaptic['MDR23'] += -7
        postsynaptic['MDR24'] += -7

def DVA():
        postsynaptic['AIZL'] += 3
        postsynaptic['AQR'] += 4
        postsynaptic['AUAL'] += 1
        postsynaptic['AUAR'] += 1
        postsynaptic['AVAL'] += 3
        postsynaptic['AVAR'] += 1
        postsynaptic['AVBL'] += 1
        postsynaptic['AVBR'] += 1
        postsynaptic['AVEL'] += 9
        postsynaptic['AVER'] += 5
        postsynaptic['DB1'] += 1
        postsynaptic['DB2'] += 1
        postsynaptic['DB3'] += 2
        postsynaptic['DB4'] += 1
        postsynaptic['DB5'] += 1
        postsynaptic['DB6'] += 2
        postsynaptic['DB7'] += 1
        postsynaptic['PDEL'] += 3
        postsynaptic['PVCL'] += 3
        postsynaptic['PVCL'] += 1
        postsynaptic['PVCR'] += 1
        postsynaptic['PVR'] += 3
        postsynaptic['PVR'] += 2
        postsynaptic['RIAL'] += 1
        postsynaptic['RIAR'] += 1
        postsynaptic['RIMR'] += 1
        postsynaptic['RIR'] += 3
        postsynaptic['SAADR'] += 1
        postsynaptic['SAAVL'] += 1
        postsynaptic['SAAVR'] += 1
        postsynaptic['SABD'] += 1
        postsynaptic['SMBDL'] += 3
        postsynaptic['SMBDR'] += 2
        postsynaptic['SMBVL'] += 3
        postsynaptic['SMBVR'] += 2
        postsynaptic['VA12'] += 1
        postsynaptic['VA2'] += 1
        postsynaptic['VB1'] += 1
        postsynaptic['VB11'] += 2

def DVB():
        postsynaptic['AS9'] += 7
        postsynaptic['AVL'] += 5
        postsynaptic['AVL'] += 1
        postsynaptic['DA8'] += 2
        postsynaptic['DD6'] += 3
        postsynaptic['DVC'] += 3
        # postsynaptic['MANAL'] += -5 - just not needed or used
        postsynaptic['PDA'] += 1
        postsynaptic['PHCL'] += 1
        postsynaptic['PVPL'] += 1
        postsynaptic['VA9'] += 1
        postsynaptic['VB9'] += 1

def DVC():
        postsynaptic['AIBL'] += 2
        postsynaptic['AIBR'] += 5
        postsynaptic['AVAL'] += 5
        postsynaptic['AVAR'] += 7
        postsynaptic['AVBL'] += 1
        postsynaptic['AVKL'] += 2
        postsynaptic['AVKR'] += 1
        postsynaptic['AVL'] += 9
        postsynaptic['PVPL'] += 2
        postsynaptic['PVPR'] += 13
        postsynaptic['PVT'] += 1
        postsynaptic['RIBL'] += 1
        postsynaptic['RIBR'] += 1
        postsynaptic['RIGL'] += 5
        postsynaptic['RIGR'] += 5
        postsynaptic['RMFL'] += 2
        postsynaptic['RMFR'] += 4
        postsynaptic['VA9'] += 1
        postsynaptic['VD1'] += 5
        postsynaptic['VD10'] += 4

def FLPL():
        postsynaptic['ADEL'] += 2
        postsynaptic['ADER'] += 2
        postsynaptic['AIBL'] += 1
        postsynaptic['AIBR'] += 2
        postsynaptic['AVAL'] += 15
        postsynaptic['AVAR'] += 17
        postsynaptic['AVBL'] += 4
        postsynaptic['AVBR'] += 5
        postsynaptic['AVDL'] += 7
        postsynaptic['AVDR'] += 13
        postsynaptic['DVA'] += 1
        postsynaptic['FLPR'] += 3
        postsynaptic['RIH'] += 1

def FLPR():
        postsynaptic['ADER'] += 1
        postsynaptic['AIBR'] += 1
        postsynaptic['AVAL'] += 12
        postsynaptic['AVAR'] += 5
        postsynaptic['AVBL'] += 5
        postsynaptic['AVBR'] += 1
        postsynaptic['AVDL'] += 10
        postsynaptic['AVDL'] += 1
        postsynaptic['AVDR'] += 2
        postsynaptic['AVEL'] += 4
        postsynaptic['AVER'] += 2
        postsynaptic['AVJR'] += 1
        postsynaptic['DVA'] += 1
        postsynaptic['FLPL'] += 4
        postsynaptic['PVCL'] += 2
        postsynaptic['VB1'] += 1

def HSNL():
        postsynaptic['AIAL'] += 1
        postsynaptic['AIZL'] += 2
        postsynaptic['AIZR'] += 1
        postsynaptic['ASHL'] += 1
        postsynaptic['ASHR'] += 2
        postsynaptic['ASJR'] += 1
        postsynaptic['ASKL'] += 1
        postsynaptic['AVDR'] += 2
        postsynaptic['AVFL'] += 6
        postsynaptic['AVJL'] += 1
        postsynaptic['AWBL'] += 1
        postsynaptic['AWBR'] += 2
        postsynaptic['HSNR'] += 3
        postsynaptic['HSNR'] += 1
        postsynaptic['MVULVA'] += 7
        postsynaptic['RIFL'] += 3
        postsynaptic['RIML'] += 2
        postsynaptic['SABVL'] += 2
        postsynaptic['VC5'] += 3

def HSNR():
        postsynaptic['AIBL'] += 1
        postsynaptic['AIBR'] += 1
        postsynaptic['AIZL'] += 1
        postsynaptic['AIZR'] += 1
        postsynaptic['AS5'] += 1
        postsynaptic['ASHL'] += 2
        postsynaptic['AVDR'] += 1
        postsynaptic['AVFL'] += 1
        postsynaptic['AVJL'] += 1
        postsynaptic['AVL'] += 1
        postsynaptic['AWBL'] += 1
        postsynaptic['BDUR'] += 1
        postsynaptic['DA5'] += 1
        postsynaptic['DA6'] += 1
        postsynaptic['HSNL'] += 1
        postsynaptic['MVULVA'] += 6
        postsynaptic['PVNR'] += 1
        postsynaptic['PVQR'] += 1
        postsynaptic['RIFR'] += 4
        postsynaptic['RMGR'] += 1
        postsynaptic['SABD'] += 1
        postsynaptic['SABVR'] += 1
        postsynaptic['VA6'] += 1
        postsynaptic['VC2'] += 3
        postsynaptic['VC3'] += 1
        postsynaptic['VD4'] += 2

def I1L():
        postsynaptic['I1R'] += 1
        postsynaptic['I3'] += 1
        postsynaptic['I5'] += 1
        postsynaptic['RIPL'] += 1
        postsynaptic['RIPR'] += 1

def I1R():
        postsynaptic['I1L'] += 1
        postsynaptic['I3'] += 1
        postsynaptic['I5'] += 1
        postsynaptic['RIPL'] += 1
        postsynaptic['RIPR'] += 1

def I2L():
        postsynaptic['I1L'] += 1
        postsynaptic['I1R'] += 1
        postsynaptic['M1'] += 4

def I2R():
        postsynaptic['I1L'] += 1
        postsynaptic['I1R'] += 1
        postsynaptic['M1'] += 4

def I3():
        postsynaptic['M1'] += 4
        postsynaptic['M2L'] += 2
        postsynaptic['M2R'] += 2

def I4():
        postsynaptic['I2L'] += 5
        postsynaptic['I2R'] += 5
        postsynaptic['I5'] += 2
        postsynaptic['M1'] += 4

def I5():
        postsynaptic['I1L'] += 4
        postsynaptic['I1R'] += 3
        postsynaptic['M1'] += 2
        postsynaptic['M5'] += 2
        postsynaptic['MI'] += 4

def I6():
        postsynaptic['I2L'] += 2
        postsynaptic['I2R'] += 2
        postsynaptic['I3'] += 1
        postsynaptic['M4'] += 1
        postsynaptic['M5'] += 2
        postsynaptic['NSML'] += 2
        postsynaptic['NSMR'] += 2

def IL1DL():
        postsynaptic['IL1DR'] += 1
        postsynaptic['IL1L'] += 1
        postsynaptic['MDL01'] += 1
        postsynaptic['MDL02'] += 1
        postsynaptic['MDL04'] += 2
        postsynaptic['OLLL'] += 1
        postsynaptic['PVR'] += 1
        postsynaptic['RIH'] += 1
        postsynaptic['RIPL'] += 2
        postsynaptic['RMDDR'] += 1
        postsynaptic['RMDVL'] += 4
        postsynaptic['RMEV'] += 1
        postsynaptic['URYDL'] += 1

def IL1DR():
        postsynaptic['IL1DL'] += 1
        postsynaptic['IL1R'] += 1
        postsynaptic['MDR01'] += 4
        postsynaptic['MDR02'] += 3
        postsynaptic['OLLR'] += 1
        postsynaptic['RIPR'] += 5
        postsynaptic['RMDVR'] += 5
        postsynaptic['RMEV'] += 1

def IL1L():
        postsynaptic['AVER'] += 2
        postsynaptic['IL1DL'] += 2
        postsynaptic['IL1VL'] += 1
        postsynaptic['MDL01'] += 3
        postsynaptic['MDL03'] += 3
        postsynaptic['MDL05'] += 4
        postsynaptic['MVL01'] += 3
        postsynaptic['MVL03'] += 3
        postsynaptic['RMDDL'] += 5
        postsynaptic['RMDL'] += 1
        postsynaptic['RMDR'] += 3
        postsynaptic['RMDVL'] += 4
        postsynaptic['RMDVR'] += 2
        postsynaptic['RMER'] += 1

def IL1R():
        postsynaptic['AVEL'] += 1
        postsynaptic['AVER'] += 1
        postsynaptic['IL1DR'] += 2
        postsynaptic['IL1VR'] += 1
        postsynaptic['MDR01'] += 3
        postsynaptic['MDR03'] += 3
        postsynaptic['MVR01'] += 3
        postsynaptic['MVR03'] += 3
        postsynaptic['RMDDL'] += 3
        postsynaptic['RMDDR'] += 2
        postsynaptic['RMDL'] += 4
        postsynaptic['RMDR'] += 2
        postsynaptic['RMDVL'] += 1
        postsynaptic['RMDVR'] += 4
        postsynaptic['RMEL'] += 2
        postsynaptic['RMHL'] += 1
        postsynaptic['URXR'] += 2

def IL1VL():
        postsynaptic['IL1L'] += 2
        postsynaptic['IL1VR'] += 1
        postsynaptic['MVL01'] += 5
        postsynaptic['MVL02'] += 4
        postsynaptic['RIPL'] += 4
        postsynaptic['RMDDL'] += 5
        postsynaptic['RMED'] += 1
        postsynaptic['URYVL'] += 1

def IL1VR():
        postsynaptic['IL1R'] += 2
        postsynaptic['IL1VL'] += 1
        postsynaptic['IL2R'] += 1
        postsynaptic['IL2VR'] += 1
        postsynaptic['MVR01'] += 5
        postsynaptic['MVR02'] += 5
        postsynaptic['RIPR'] += 6
        postsynaptic['RMDDR'] += 10
        postsynaptic['RMER'] += 1

def IL2DL():
        postsynaptic['AUAL'] += 1
        postsynaptic['IL1DL'] += 7
        postsynaptic['OLQDL'] += 2
        postsynaptic['RIBL'] += 1
        postsynaptic['RIPL'] += 10
        postsynaptic['RMEL'] += 4
        postsynaptic['RMER'] += 3
        postsynaptic['URADL'] += 3

def IL2DR():
        postsynaptic['CEPDR'] += 1
        postsynaptic['IL1DR'] += 7
        postsynaptic['RICR'] += 1
        postsynaptic['RIPR'] += 11
        postsynaptic['RMED'] += 1
        postsynaptic['RMEL'] += 2
        postsynaptic['RMER'] += 2
        postsynaptic['RMEV'] += 1
        postsynaptic['URADR'] += 3

def IL2L():
        postsynaptic['ADEL'] += 2
        postsynaptic['AVEL'] += 1
        postsynaptic['IL1L'] += 1
        postsynaptic['OLQDL'] += 5
        postsynaptic['OLQVL'] += 8
        postsynaptic['RICL'] += 1
        postsynaptic['RIH'] += 7
        postsynaptic['RMDL'] += 3
        postsynaptic['RMDR'] += 1
        postsynaptic['RMER'] += 2
        postsynaptic['RMEV'] += 2
        postsynaptic['RMGL'] += 1
        postsynaptic['URXL'] += 2

def IL2R():
        postsynaptic['ADER'] += 1
        postsynaptic['IL1R'] += 1
        postsynaptic['IL1VR'] += 1
        postsynaptic['OLLR'] += 1
        postsynaptic['OLQDR'] += 2
        postsynaptic['OLQVR'] += 7
        postsynaptic['RIH'] += 6
        postsynaptic['RMDL'] += 1
        postsynaptic['RMEL'] += 2
        postsynaptic['RMEV'] += 1
        postsynaptic['RMGR'] += 1
        postsynaptic['URBR'] += 1
        postsynaptic['URXR'] += 1

def IL2VL():
        postsynaptic['BAGR'] += 1
        postsynaptic['IL1VL'] += 7
        postsynaptic['IL2L'] += 1
        postsynaptic['OLQVL'] += 1
        postsynaptic['RIAL'] += 1
        postsynaptic['RIH'] += 2
        postsynaptic['RIPL'] += 1
        postsynaptic['RMEL'] += 1
        postsynaptic['RMER'] += 4
        postsynaptic['RMEV'] += 1
        postsynaptic['URAVL'] += 3

def IL2VR():
        postsynaptic['IL1VR'] += 6
        postsynaptic['OLQVR'] += 1
        postsynaptic['RIAR'] += 2
        postsynaptic['RIH'] += 3
        postsynaptic['RIPR'] += 15
        postsynaptic['RMEL'] += 3
        postsynaptic['RMER'] += 2
        postsynaptic['RMEV'] += 3
        postsynaptic['URAVR'] += 4
        postsynaptic['URXR'] += 1

def LUAL():
        postsynaptic['AVAL'] += 6
        postsynaptic['AVAR'] += 6
        postsynaptic['AVDL'] += 4
        postsynaptic['AVDR'] += 2
        postsynaptic['AVJL'] += 1
        postsynaptic['PHBL'] += 1
        postsynaptic['PLML'] += 1
        postsynaptic['PVNL'] += 1
        postsynaptic['PVR'] += 1
        postsynaptic['PVWL'] += 1

def LUAR():
        postsynaptic['AVAL'] += 3
        postsynaptic['AVAR'] += 7
        postsynaptic['AVDL'] += 1
        postsynaptic['AVDR'] += 3
        postsynaptic['AVJR'] += 1
        postsynaptic['PLMR'] += 1
        postsynaptic['PQR'] += 1
        postsynaptic['PVCR'] += 3
        postsynaptic['PVR'] += 1
        postsynaptic['PVWL'] += 1

def M1():
        postsynaptic['I2L'] += 2
        postsynaptic['I2R'] += 2
        postsynaptic['I3'] += 1
        postsynaptic['I4'] += 1

def M2L():
        postsynaptic['I1L'] += 3
        postsynaptic['I1R'] += 3
        postsynaptic['I3'] += 3
        postsynaptic['M2R'] += 1
        postsynaptic['M5'] += 1
        postsynaptic['MI'] += 4

def M2R():
        postsynaptic['I1L'] += 3
        postsynaptic['I1R'] += 3
        postsynaptic['I3'] += 3
        postsynaptic['M3L'] += 1
        postsynaptic['M3R'] += 1
        postsynaptic['M5'] += 1
        postsynaptic['MI'] += 4

def M3L():
        postsynaptic['I1L'] += 4
        postsynaptic['I1R'] += 4
        postsynaptic['I4'] += 2
        postsynaptic['I5'] += 3
        postsynaptic['I6'] += 1
        postsynaptic['M1'] += 2
        postsynaptic['M3R'] += 1
        postsynaptic['MCL'] += 1
        postsynaptic['MCR'] += 1
        postsynaptic['MI'] += 2
        postsynaptic['NSML'] += 2
        postsynaptic['NSMR'] += 3

def M3R():
        postsynaptic['I1L'] += 4
        postsynaptic['I1R'] += 4
        postsynaptic['I3'] += 2
        postsynaptic['I4'] += 6
        postsynaptic['I5'] += 3
        postsynaptic['I6'] += 1
        postsynaptic['M1'] += 2
        postsynaptic['M3L'] += 1
        postsynaptic['MCL'] += 1
        postsynaptic['MCR'] += 1
        postsynaptic['MI'] += 2
        postsynaptic['NSML'] += 2
        postsynaptic['NSMR'] += 3

def M4():
        postsynaptic['I3'] += 1
        postsynaptic['I5'] += 13
        postsynaptic['I6'] += 3
        postsynaptic['M2L'] += 1
        postsynaptic['M2R'] += 1
        postsynaptic['M4'] += 6
        postsynaptic['M5'] += 1
        postsynaptic['NSML'] += 1
        postsynaptic['NSMR'] += 1

def M5():
        postsynaptic['I5'] += 3
        postsynaptic['I5'] += 1
        postsynaptic['I6'] += 1
        postsynaptic['M1'] += 2
        postsynaptic['M2L'] += 2
        postsynaptic['M2R'] += 2
        postsynaptic['M5'] += 4

def MCL():
        postsynaptic['I1L'] += 3
        postsynaptic['I1R'] += 3
        postsynaptic['I2L'] += 1
        postsynaptic['I2R'] += 1
        postsynaptic['I3'] += 1
        postsynaptic['M1'] += 2
        postsynaptic['M2L'] += 2
        postsynaptic['M2R'] += 2

def MCR():
        postsynaptic['I1L'] += 3
        postsynaptic['I1R'] += 3
        postsynaptic['I3'] += 1
        postsynaptic['M1'] += 2
        postsynaptic['M2L'] += 2
        postsynaptic['M2R'] += 2

def MI():
        postsynaptic['I1L'] += 1
        postsynaptic['I1R'] += 1
        postsynaptic['I3'] += 1
        postsynaptic['I4'] += 1
        postsynaptic['I5'] += 2
        postsynaptic['M1'] += 1
        postsynaptic['M2L'] += 2
        postsynaptic['M2R'] += 2
        postsynaptic['M3L'] += 1
        postsynaptic['M3R'] += 1
        postsynaptic['MCL'] += 2
        postsynaptic['MCR'] += 2

def NSML():
        postsynaptic['I1L'] += 1
        postsynaptic['I1R'] += 2
        postsynaptic['I2L'] += 6
        postsynaptic['I2R'] += 6
        postsynaptic['I3'] += 2
        postsynaptic['I4'] += 3
        postsynaptic['I5'] += 2
        postsynaptic['I6'] += 2
        postsynaptic['M3L'] += 2
        postsynaptic['M3R'] += 2

def NSMR():
        postsynaptic['I1L'] += 2
        postsynaptic['I1R'] += 2
        postsynaptic['I2L'] += 6
        postsynaptic['I2R'] += 6
        postsynaptic['I3'] += 2
        postsynaptic['I4'] += 3
        postsynaptic['I5'] += 2
        postsynaptic['I6'] += 2
        postsynaptic['M3L'] += 2
        postsynaptic['M3R'] += 2

def OLLL():
        postsynaptic['AVER'] += 21
        postsynaptic['CEPDL'] += 3
        postsynaptic['CEPVL'] += 4
        postsynaptic['IL1DL'] += 1
        postsynaptic['IL1VL'] += 2
        postsynaptic['OLLR'] += 2
        postsynaptic['RIBL'] += 8
        postsynaptic['RIGL'] += 1
        postsynaptic['RMDDL'] += 7
        postsynaptic['RMDL'] += 2
        postsynaptic['RMDVL'] += 1
        postsynaptic['RMEL'] += 2
        postsynaptic['SMDDL'] += 3
        postsynaptic['SMDDR'] += 4
        postsynaptic['SMDVR'] += 4
        postsynaptic['URYDL'] += 1

def OLLR():
        postsynaptic['AVEL'] += 16
        postsynaptic['CEPDR'] += 1
        postsynaptic['CEPVR'] += 6
        postsynaptic['IL1DR'] += 3
        postsynaptic['IL1VR'] += 1
        postsynaptic['IL2R'] += 1
        postsynaptic['OLLL'] += 2
        postsynaptic['RIBR'] += 10
        postsynaptic['RIGR'] += 1
        postsynaptic['RMDDR'] += 10
        postsynaptic['RMDL'] += 3
        postsynaptic['RMDVR'] += 3
        postsynaptic['RMER'] += 2
        postsynaptic['SMDDR'] += 1
        postsynaptic['SMDVL'] += 4
        postsynaptic['SMDVR'] += 3

def OLQDL():
        postsynaptic['CEPDL'] += 1
        postsynaptic['RIBL'] += 2
        postsynaptic['RICR'] += 1
        postsynaptic['RIGL'] += 1
        postsynaptic['RMDDR'] += 4
        postsynaptic['RMDVL'] += 1
        postsynaptic['SIBVL'] += 3
        postsynaptic['URBL'] += 1

def OLQDR():
        postsynaptic['CEPDR'] += 2
        postsynaptic['RIBR'] += 2
        postsynaptic['RICL'] += 1
        postsynaptic['RICR'] += 1
        postsynaptic['RIGR'] += 1
        postsynaptic['RIH'] += 1
        postsynaptic['RMDDL'] += 3
        postsynaptic['RMDVR'] += 1
        postsynaptic['RMHR'] += 1
        postsynaptic['SIBVR'] += 2
        postsynaptic['URBR'] += 1

def OLQVL():
        postsynaptic['ADLL'] += 1
        postsynaptic['CEPVL'] += 1
        postsynaptic['IL1VL'] += 1
        postsynaptic['IL2VL'] += 1
        postsynaptic['RIBL'] += 1
        postsynaptic['RICL'] += 1
        postsynaptic['RIGL'] += 1
        postsynaptic['RIH'] += 1
        postsynaptic['RIPL'] += 1
        postsynaptic['RMDDL'] += 1
        postsynaptic['RMDVR'] += 4
        postsynaptic['SIBDL'] += 3
        postsynaptic['URBL'] += 1

def OLQVR():
        postsynaptic['CEPVR'] += 1
        postsynaptic['IL1VR'] += 1
        postsynaptic['RIBR'] += 1
        postsynaptic['RICR'] += 1
        postsynaptic['RIGR'] += 1
        postsynaptic['RIH'] += 2
        postsynaptic['RIPR'] += 2
        postsynaptic['RMDDR'] += 1
        postsynaptic['RMDVL'] += 4
        postsynaptic['RMER'] += 1
        postsynaptic['SIBDR'] += 4
        postsynaptic['URBR'] += 1

def PDA():
        postsynaptic['AS11'] += 1
        postsynaptic['DA9'] += 1
        postsynaptic['DD6'] += 1
        postsynaptic['MDL21'] += 2
        postsynaptic['PVNR'] += 1
        postsynaptic['VD13'] += 3

def PDB():
        postsynaptic['AS11'] += 2
        postsynaptic['MVL22'] += 1
        postsynaptic['MVR21'] += 1
        postsynaptic['RID'] += 2
        postsynaptic['VD13'] += 2

def PDEL():
        postsynaptic['AVKL'] += 6
        postsynaptic['DVA'] += 24
        postsynaptic['PDER'] += 1
        postsynaptic['PDER'] += 3
        postsynaptic['PVCR'] += 1
        postsynaptic['PVM'] += 2
        postsynaptic['PVM'] += 1
        postsynaptic['PVR'] += 2
        postsynaptic['VA9'] += 1
        postsynaptic['VD11'] += 1

def PDER():
        postsynaptic['AVKL'] += 16
        postsynaptic['DVA'] += 35
        postsynaptic['PDEL'] += 3
        postsynaptic['PVCL'] += 1
        postsynaptic['PVCR'] += 1
        postsynaptic['PVM'] += 1
        postsynaptic['VA8'] += 1
        postsynaptic['VD9'] += 1

def PHAL():
        postsynaptic['AVDR'] += 1
        postsynaptic['AVFL'] += 3
        postsynaptic['AVG'] += 5
        postsynaptic['AVHL'] += 1
        postsynaptic['AVHR'] += 1
        postsynaptic['DVA'] += 2
        postsynaptic['PHAR'] += 5
        postsynaptic['PHAR'] += 2
        postsynaptic['PHBL'] += 5
        postsynaptic['PHBR'] += 5
        postsynaptic['PVQL'] += 2

def PHAR():
        postsynaptic['AVG'] += 3
        postsynaptic['AVHR'] += 1
        postsynaptic['DA8'] += 1
        postsynaptic['DVA'] += 1
        postsynaptic['PHAL'] += 6
        postsynaptic['PHAL'] += 2
        postsynaptic['PHBL'] += 1
        postsynaptic['PHBR'] += 5
        postsynaptic['PVPL'] += 3
        postsynaptic['PVQL'] += 2

def PHBL():
        postsynaptic['AVAL'] += 9
        postsynaptic['AVAR'] += 6
        postsynaptic['AVDL'] += 1
        postsynaptic['PHBR'] += 1
        postsynaptic['PHBR'] += 3
        postsynaptic['PVCL'] += 13
        postsynaptic['VA12'] += 1

def PHBR():
        postsynaptic['AVAL'] += 7
        postsynaptic['AVAR'] += 7
        postsynaptic['AVDL'] += 1
        postsynaptic['AVDR'] += 1
        postsynaptic['AVFL'] += 1
        postsynaptic['AVHL'] += 1
        postsynaptic['DA8'] += 1
        postsynaptic['PHBL'] += 1
        postsynaptic['PHBL'] += 3
        postsynaptic['PVCL'] += 6
        postsynaptic['PVCR'] += 3
        postsynaptic['VA12'] += 2

def PHCL():
        postsynaptic['AVAL'] += 1
        postsynaptic['DA9'] += 7
        postsynaptic['DA9'] += 1
        postsynaptic['DVA'] += 6
        postsynaptic['LUAL'] += 1
        postsynaptic['PHCR'] += 1
        postsynaptic['PLML'] += 1
        postsynaptic['PVCL'] += 2
        postsynaptic['VA12'] += 3

def PHCR():
        postsynaptic['AVHR'] += 1
        postsynaptic['DA9'] += 2
        postsynaptic['DVA'] += 8
        postsynaptic['LUAR'] += 1
        postsynaptic['PHCL'] += 2
        postsynaptic['PVCR'] += 9
        postsynaptic['VA12'] += 2

def PLML():
        postsynaptic['HSNL'] += 1
        postsynaptic['LUAL'] += 1
        postsynaptic['PHCL'] += 1
        postsynaptic['PVCL'] += 1

def PLMR():
        postsynaptic['AS6'] += 1
        postsynaptic['AVAL'] += 4
        postsynaptic['AVAR'] += 1
        postsynaptic['AVDL'] += 1
        postsynaptic['AVDR'] += 4
        postsynaptic['DVA'] += 5
        postsynaptic['HSNR'] += 1
        postsynaptic['LUAR'] += 1
        postsynaptic['PDEL'] += 2
        postsynaptic['PDER'] += 3
        postsynaptic['PVCL'] += 2
        postsynaptic['PVCR'] += 1
        postsynaptic['PVR'] += 2

def PLNL():
        postsynaptic['SAADL'] += 5
        postsynaptic['SMBVL'] += 6

def PLNR():
        postsynaptic['SAADR'] += 4
        postsynaptic['SMBVR'] += 6

def PQR():
        postsynaptic['AVAL'] += 8
        postsynaptic['AVAR'] += 11
        postsynaptic['AVDL'] += 7
        postsynaptic['AVDR'] += 6
        postsynaptic['AVG'] += 1
        postsynaptic['LUAR'] += 1
        postsynaptic['PVNL'] += 1
        postsynaptic['PVPL'] += 4

def PVCL():
        postsynaptic['AS1'] += 1
        postsynaptic['AVAL'] += 3
        postsynaptic['AVAR'] += 4
        postsynaptic['AVBL'] += 5
        postsynaptic['AVBR'] += 12
        postsynaptic['AVDL'] += 5
        postsynaptic['AVDR'] += 2
        postsynaptic['AVEL'] += 3
        postsynaptic['AVER'] += 1
        postsynaptic['AVJL'] += 4
        postsynaptic['AVJR'] += 2
        postsynaptic['DA2'] += 1
        postsynaptic['DA5'] += 1
        postsynaptic['DA6'] += 1
        postsynaptic['DB2'] += 3
        postsynaptic['DB3'] += 4
        postsynaptic['DB4'] += 3
        postsynaptic['DB5'] += 2
        postsynaptic['DB6'] += 2
        postsynaptic['DB7'] += 3
        postsynaptic['DVA'] += 5
        postsynaptic['PLML'] += 1
        postsynaptic['PVCR'] += 7
        postsynaptic['RID'] += 5
        postsynaptic['RIS'] += 2
        postsynaptic['SIBVL'] += 2
        postsynaptic['VB10'] += 3
        postsynaptic['VB11'] += 1
        postsynaptic['VB3'] += 1
        postsynaptic['VB4'] += 1
        postsynaptic['VB5'] += 1
        postsynaptic['VB6'] += 2
        postsynaptic['VB8'] += 1
        postsynaptic['VB9'] += 2

def PVCR():
        postsynaptic['AQR'] += 1
        postsynaptic['AS2'] += 1
        postsynaptic['AVAL'] += 12
        postsynaptic['AVAR'] += 10
        postsynaptic['AVBL'] += 8
        postsynaptic['AVBR'] += 6
        postsynaptic['AVDL'] += 5
        postsynaptic['AVDR'] += 1
        postsynaptic['AVEL'] += 1
        postsynaptic['AVER'] += 1
        postsynaptic['AVJL'] += 3
        postsynaptic['AVL'] += 1
        postsynaptic['DA9'] += 1
        postsynaptic['DB2'] += 1
        postsynaptic['DB3'] += 3
        postsynaptic['DB4'] += 4
        postsynaptic['DB5'] += 1
        postsynaptic['DB6'] += 2
        postsynaptic['DB7'] += 1
        postsynaptic['FLPL'] += 1
        postsynaptic['LUAR'] += 1
        postsynaptic['PDEL'] += 2
        postsynaptic['PHCR'] += 1
        postsynaptic['PLMR'] += 1
        postsynaptic['PVCL'] += 8
        postsynaptic['PVDL'] += 1
        postsynaptic['PVR'] += 1
        postsynaptic['PVWL'] += 2
        postsynaptic['PVWR'] += 2
        postsynaptic['RID'] += 5
        postsynaptic['SIBVR'] += 2
        postsynaptic['VA8'] += 2
        postsynaptic['VA9'] += 1
        postsynaptic['VB10'] += 1
        postsynaptic['VB4'] += 3
        postsynaptic['VB6'] += 2
        postsynaptic['VB7'] += 3
        postsynaptic['VB8'] += 1

def PVDL():
        postsynaptic['AVAL'] += 6
        postsynaptic['AVAR'] += 6
        postsynaptic['DD5'] += 1
        postsynaptic['PVCL'] += 1
        postsynaptic['PVCR'] += 6
        postsynaptic['VD10'] += 6

def PVDR():
        postsynaptic['AVAL'] += 6
        postsynaptic['AVAR'] += 9
        postsynaptic['DVA'] += 3
        postsynaptic['PVCL'] += 13
        postsynaptic['PVCR'] += 10
        postsynaptic['PVDL'] += 1
        postsynaptic['VA9'] += 1

def PVM():
        postsynaptic['AVKL'] += 11
        postsynaptic['AVL'] += 1
        postsynaptic['AVM'] += 1
        postsynaptic['DVA'] += 3
        postsynaptic['PDEL'] += 7
        postsynaptic['PDEL'] += 1
        postsynaptic['PDER'] += 8
        postsynaptic['PDER'] += 1
        postsynaptic['PVCL'] += 2
        postsynaptic['PVR'] += 1

def PVNL():
        postsynaptic['AVAL'] += 2
        postsynaptic['AVBR'] += 3
        postsynaptic['AVDL'] += 3
        postsynaptic['AVDR'] += 3
        postsynaptic['AVEL'] += 1
        postsynaptic['AVFR'] += 1
        postsynaptic['AVG'] += 1
        postsynaptic['AVJL'] += 5
        postsynaptic['AVJR'] += 5
        postsynaptic['AVL'] += 2
        postsynaptic['BDUL'] += 1
        postsynaptic['BDUR'] += 2
        postsynaptic['DD1'] += 2
        postsynaptic['MVL09'] += 3
        postsynaptic['PQR'] += 1
        postsynaptic['PVCL'] += 1
        postsynaptic['PVNR'] += 5
        postsynaptic['PVQR'] += 1
        postsynaptic['PVT'] += 1
        postsynaptic['PVWL'] += 1
        postsynaptic['RIFL'] += 1

def PVNR():
        postsynaptic['AVAL'] += 2
        postsynaptic['AVBL'] += 1
        postsynaptic['AVBR'] += 2
        postsynaptic['AVDR'] += 1
        postsynaptic['AVEL'] += 3
        postsynaptic['AVJL'] += 4
        postsynaptic['AVJR'] += 1
        postsynaptic['AVL'] += 2
        postsynaptic['BDUL'] += 1
        postsynaptic['BDUR'] += 2
        postsynaptic['DD3'] += 1
        postsynaptic['HSNR'] += 2
        postsynaptic['MVL12'] += 1
        postsynaptic['MVL13'] += 2
        postsynaptic['PQR'] += 2
        postsynaptic['PVCL'] += 1
        postsynaptic['PVNL'] += 1
        postsynaptic['PVT'] += 2
        postsynaptic['PVWL'] += 2
        postsynaptic['VC2'] += 1
        postsynaptic['VC3'] += 1
        postsynaptic['VD12'] += 1
        postsynaptic['VD6'] += 1
        postsynaptic['VD7'] += 1

def PVPL():
        postsynaptic['ADAL'] += 1
        postsynaptic['AQR'] += 8
        postsynaptic['AVAL'] += 2
        postsynaptic['AVAR'] += 1
        postsynaptic['AVBL'] += 5
        postsynaptic['AVBR'] += 6
        postsynaptic['AVDR'] += 2
        postsynaptic['AVER'] += 1
        postsynaptic['AVHR'] += 1
        postsynaptic['AVKL'] += 1
        postsynaptic['AVKR'] += 6
        postsynaptic['DVC'] += 2
        postsynaptic['PHAR'] += 3
        postsynaptic['PQR'] += 4
        postsynaptic['PVCR'] += 3
        postsynaptic['PVPR'] += 1
        postsynaptic['PVT'] += 1
        postsynaptic['RIGL'] += 2
        postsynaptic['VD13'] += 2
        postsynaptic['VD3'] += 1

def PVPR():
        postsynaptic['ADFR'] += 1
        postsynaptic['AQR'] += 11
        postsynaptic['ASHR'] += 1
        postsynaptic['AVAL'] += 1
        postsynaptic['AVAR'] += 2
        postsynaptic['AVBL'] += 4
        postsynaptic['AVBR'] += 5
        postsynaptic['AVHL'] += 3
        postsynaptic['AVKL'] += 1
        postsynaptic['AVL'] += 4
        postsynaptic['DD2'] += 1
        postsynaptic['DVC'] += 14
        postsynaptic['PVCL'] += 4
        postsynaptic['PVCR'] += 7
        postsynaptic['PVPL'] += 1
        postsynaptic['PVQR'] += 1
        postsynaptic['RIAR'] += 2
        postsynaptic['RIGR'] += 1
        postsynaptic['RIMR'] += 1
        postsynaptic['RMGR'] += 1
        postsynaptic['VD4'] += 1
        postsynaptic['VD5'] += 1

def PVQL():
        postsynaptic['ADAL'] += 1
        postsynaptic['AIAL'] += 3
        postsynaptic['ASJL'] += 1
        postsynaptic['ASKL'] += 4
        postsynaptic['ASKL'] += 5
        postsynaptic['HSNL'] += 2
        postsynaptic['PVQR'] += 2
        postsynaptic['RMGL'] += 1

def PVQR():
        postsynaptic['ADAR'] += 1
        postsynaptic['AIAR'] += 7
        postsynaptic['ASER'] += 1
        postsynaptic['ASKR'] += 8
        postsynaptic['AVBL'] += 1
        postsynaptic['AVFL'] += 1
        postsynaptic['AVFR'] += 1
        postsynaptic['AVL'] += 1
        postsynaptic['AWAR'] += 2
        postsynaptic['DD1'] += 1
        postsynaptic['DVC'] += 1
        postsynaptic['HSNR'] += 1
        postsynaptic['PVNL'] += 1
        postsynaptic['PVQL'] += 1
        postsynaptic['PVT'] += 1
        postsynaptic['RIFR'] += 1
        postsynaptic['VD1'] += 1

def PVR():
        postsynaptic['ADAL'] += 1
        postsynaptic['ALML'] += 1
        postsynaptic['AS6'] += 1
        postsynaptic['AVBL'] += 4
        postsynaptic['AVBR'] += 4
        postsynaptic['AVJL'] += 3
        postsynaptic['AVJR'] += 2
        postsynaptic['AVKL'] += 1
        postsynaptic['DA9'] += 1
        postsynaptic['DB2'] += 1
        postsynaptic['DB3'] += 1
        postsynaptic['DVA'] += 3
        postsynaptic['IL1DL'] += 1
        postsynaptic['IL1DR'] += 1
        postsynaptic['IL1VL'] += 1
        postsynaptic['IL1VR'] += 1
        postsynaptic['LUAL'] += 1
        postsynaptic['LUAR'] += 1
        postsynaptic['PDEL'] += 1
        postsynaptic['PDER'] += 1
        postsynaptic['PLMR'] += 2
        postsynaptic['PVCR'] += 1
        postsynaptic['RIPL'] += 3
        postsynaptic['RIPR'] += 3
        postsynaptic['SABD'] += 1
        postsynaptic['URADL'] += 1

def PVT():
        postsynaptic['AIBL'] += 3
        postsynaptic['AIBR'] += 5
        postsynaptic['AVKL'] += 9
        postsynaptic['AVKR'] += 7
        postsynaptic['AVL'] += 2
        postsynaptic['DVC'] += 2
        postsynaptic['PVPL'] += 1
        postsynaptic['RIBL'] += 1
        postsynaptic['RIBR'] += 1
        postsynaptic['RIGL'] += 2
        postsynaptic['RIGR'] += 3
        postsynaptic['RIH'] += 1
        postsynaptic['RMEV'] += 1
        postsynaptic['RMFL'] += 2
        postsynaptic['RMFR'] += 3
        postsynaptic['SMBDR'] += 1

def PVWL():
        postsynaptic['AVJL'] += 1
        postsynaptic['PVCR'] += 2
        postsynaptic['PVT'] += 2
        postsynaptic['PVWR'] += 1
        postsynaptic['VA12'] += 1

def PVWR():
        postsynaptic['AVAR'] += 1
        postsynaptic['AVDR'] += 1
        postsynaptic['PVCR'] += 2
        postsynaptic['PVT'] += 1
        postsynaptic['VA12'] += 1

def RIAL():
        postsynaptic['CEPVL'] += 1
        postsynaptic['RIAR'] += 1
        postsynaptic['RIVL'] += 2
        postsynaptic['RIVR'] += 4
        postsynaptic['RMDDL'] += 12
        postsynaptic['RMDDR'] += 7
        postsynaptic['RMDL'] += 6
        postsynaptic['RMDR'] += 6
        postsynaptic['RMDVL'] += 9
        postsynaptic['RMDVR'] += 11
        postsynaptic['SIADL'] += 2
        postsynaptic['SMDDL'] += 8
        postsynaptic['SMDDR'] += 10
        postsynaptic['SMDVL'] += 6
        postsynaptic['SMDVR'] += 11

def RIAR():
        postsynaptic['CEPVR'] += 1
        postsynaptic['IL1R'] += 1
        postsynaptic['RIAL'] += 4
        postsynaptic['RIVL'] += 1
        postsynaptic['RMDDL'] += 10
        postsynaptic['RMDDR'] += 11
        postsynaptic['RMDL'] += 3
        postsynaptic['RMDR'] += 8
        postsynaptic['RMDVL'] += 12
        postsynaptic['RMDVR'] += 10
        postsynaptic['SAADR'] += 1
        postsynaptic['SIADL'] += 1
        postsynaptic['SIADR'] += 1
        postsynaptic['SIAVL'] += 1
        postsynaptic['SMDDL'] += 7
        postsynaptic['SMDDR'] += 7
        postsynaptic['SMDVL'] += 13
        postsynaptic['SMDVR'] += 7

def RIBL():
        postsynaptic['AIBR'] += 2
        postsynaptic['AUAL'] += 1
        postsynaptic['AVAL'] += 1
        postsynaptic['AVBL'] += 1
        postsynaptic['AVBR'] += 2
        postsynaptic['AVDR'] += 1
        postsynaptic['AVEL'] += 1
        postsynaptic['AVER'] += 5
        postsynaptic['BAGR'] += 1
        postsynaptic['OLQDL'] += 2
        postsynaptic['OLQVL'] += 1
        postsynaptic['PVT'] += 1
        postsynaptic['RIAL'] += 3
        postsynaptic['RIBL'] += 1
        postsynaptic['RIBR'] += 3
        postsynaptic['RIGL'] += 1
        postsynaptic['SIADL'] += 1
        postsynaptic['SIAVL'] += 1
        postsynaptic['SIBDL'] += 1
        postsynaptic['SIBVL'] += 1
        postsynaptic['SIBVR'] += 1
        postsynaptic['SMBDL'] += 1
        postsynaptic['SMDDL'] += 1
        postsynaptic['SMDVR'] += 4

def RIBR():
        postsynaptic['AIBL'] += 1
        postsynaptic['AIZR'] += 1
        postsynaptic['AVAR'] += 2
        postsynaptic['AVBL'] += 1
        postsynaptic['AVBR'] += 1
        postsynaptic['AVEL'] += 3
        postsynaptic['AVER'] += 1
        postsynaptic['BAGL'] += 1
        postsynaptic['OLQDR'] += 2
        postsynaptic['OLQVR'] += 1
        postsynaptic['PVT'] += 1
        postsynaptic['RIAR'] += 2
        postsynaptic['RIBL'] += 3
        postsynaptic['RIBR'] += 1
        postsynaptic['RIGR'] += 2
        postsynaptic['RIH'] += 1
        postsynaptic['SIADR'] += 1
        postsynaptic['SIAVR'] += 1
        postsynaptic['SIBDR'] += 1
        postsynaptic['SIBVR'] += 1
        postsynaptic['SMBDR'] += 1
        postsynaptic['SMDDL'] += 2
        postsynaptic['SMDDR'] += 1
        postsynaptic['SMDVL'] += 2

def RICL():
        postsynaptic['ADAR'] += 1
        postsynaptic['ASHL'] += 2
        postsynaptic['AVAL'] += 5
        postsynaptic['AVAR'] += 6
        postsynaptic['AVKL'] += 1
        postsynaptic['AVKR'] += 2
        postsynaptic['AWBR'] += 1
        postsynaptic['RIML'] += 1
        postsynaptic['RIMR'] += 3
        postsynaptic['RIVR'] += 1
        postsynaptic['RMFR'] += 1
        postsynaptic['SMBDL'] += 2
        postsynaptic['SMDDL'] += 3
        postsynaptic['SMDDR'] += 3
        postsynaptic['SMDVR'] += 1

def RICR():
        postsynaptic['ADAR'] += 1
        postsynaptic['ASHR'] += 2
        postsynaptic['AVAL'] += 5
        postsynaptic['AVAR'] += 5
        postsynaptic['AVKL'] += 1
        postsynaptic['SMBDR'] += 1
        postsynaptic['SMDDL'] += 4
        postsynaptic['SMDDR'] += 3
        postsynaptic['SMDVL'] += 2
        postsynaptic['SMDVR'] += 1

def RID():
        postsynaptic['ALA'] += 1
        postsynaptic['AS2'] += 1
        postsynaptic['AVBL'] += 1
        postsynaptic['AVBR'] += 2
        postsynaptic['DA6'] += 3
        postsynaptic['DA9'] += 1
        postsynaptic['DB1'] += 1
        postsynaptic['DD1'] += 4
        postsynaptic['DD2'] += 4
        postsynaptic['DD3'] += 3
        postsynaptic['MDL14'] += -2
        postsynaptic['MDL21'] += -3
        postsynaptic['PDB'] += 2
        postsynaptic['VD13'] += 1
        postsynaptic['VD5'] += 1

def RIFL():
        postsynaptic['ALML'] += 2
        postsynaptic['AVBL'] += 10
        postsynaptic['AVBR'] += 1
        postsynaptic['AVG'] += 1
        postsynaptic['AVHR'] += 1
        postsynaptic['AVJR'] += 2
        postsynaptic['PVPL'] += 3
        postsynaptic['RIML'] += 4
        postsynaptic['VD1'] += 1

def RIFR():
        postsynaptic['ASHR'] += 2
        postsynaptic['AVBL'] += 1
        postsynaptic['AVBR'] += 17
        postsynaptic['AVFL'] += 1
        postsynaptic['AVG'] += 1
        postsynaptic['AVHL'] += 1
        postsynaptic['AVJL'] += 1
        postsynaptic['AVJR'] += 2
        postsynaptic['HSNR'] += 1
        postsynaptic['PVCL'] += 1
        postsynaptic['PVCR'] += 1
        postsynaptic['PVPR'] += 4
        postsynaptic['RIMR'] += 4
        postsynaptic['RIPR'] += 1

def RIGL():
        postsynaptic['AIBR'] += 3
        postsynaptic['AIZR'] += 1
        postsynaptic['ALNL'] += 1
        postsynaptic['AQR'] += 2
        postsynaptic['AVEL'] += 1
        postsynaptic['AVER'] += 1
        postsynaptic['AVKL'] += 1
        postsynaptic['AVKR'] += 2
        postsynaptic['BAGR'] += 1
        postsynaptic['DVC'] += 1
        postsynaptic['OLLL'] += 1
        postsynaptic['OLQDL'] += 1
        postsynaptic['OLQVL'] += 1
        postsynaptic['RIBL'] += 2
        postsynaptic['RIGR'] += 3
        postsynaptic['RIR'] += 2
        postsynaptic['RMEL'] += 2
        postsynaptic['RMHR'] += 3
        postsynaptic['URYDL'] += 1
        postsynaptic['URYVL'] += 1
        postsynaptic['VB2'] += 1
        postsynaptic['VD1'] += 2

def RIGR():
        postsynaptic['AIBL'] += 3
        postsynaptic['ALNR'] += 1
        postsynaptic['AQR'] += 1
        postsynaptic['AVER'] += 2
        postsynaptic['AVKL'] += 4
        postsynaptic['AVKR'] += 2
        postsynaptic['BAGL'] += 1
        postsynaptic['OLLR'] += 1
        postsynaptic['OLQDR'] += 1
        postsynaptic['OLQVR'] += 1
        postsynaptic['RIBR'] += 2
        postsynaptic['RIGL'] += 3
        postsynaptic['RIR'] += 1
        postsynaptic['RMHL'] += 4
        postsynaptic['URYDR'] += 1
        postsynaptic['URYVR'] += 1

def RIH():
        postsynaptic['ADFR'] += 1
        postsynaptic['AIZL'] += 4
        postsynaptic['AIZR'] += 4
        postsynaptic['AUAR'] += 1
        postsynaptic['BAGR'] += 1
        postsynaptic['CEPDL'] += 2
        postsynaptic['CEPDR'] += 2
        postsynaptic['CEPVL'] += 2
        postsynaptic['CEPVR'] += 2
        postsynaptic['FLPL'] += 1
        postsynaptic['IL2L'] += 2
        postsynaptic['IL2R'] += 1
        postsynaptic['OLQDL'] += 4
        postsynaptic['OLQDR'] += 2
        postsynaptic['OLQVL'] += 1
        postsynaptic['OLQVR'] += 6
        postsynaptic['RIAL'] += 10
        postsynaptic['RIAR'] += 8
        postsynaptic['RIBL'] += 5
        postsynaptic['RIBR'] += 4
        postsynaptic['RIPL'] += 4
        postsynaptic['RIPR'] += 6
        postsynaptic['RMER'] += 2
        postsynaptic['RMEV'] += 1
        postsynaptic['URYVR'] += 1

def RIML():
        postsynaptic['AIBR'] += 1
        postsynaptic['AIYL'] += 1
        postsynaptic['AVAL'] += 1
        postsynaptic['AVAR'] += 2
        postsynaptic['AVBL'] += 2
        postsynaptic['AVBR'] += 3
        postsynaptic['AVEL'] += 2
        postsynaptic['AVER'] += 3
        postsynaptic['MDR05'] += 2
        postsynaptic['MVR05'] += 2
        postsynaptic['RIBL'] += 1
        postsynaptic['RIS'] += 1
        postsynaptic['RMDL'] += 1
        postsynaptic['RMDR'] += 1
        postsynaptic['RMFR'] += 1
        postsynaptic['SAADR'] += 1
        postsynaptic['SAAVL'] += 3
        postsynaptic['SAAVR'] += 2
        postsynaptic['SMDDR'] += 5
        postsynaptic['SMDVL'] += 1

def RIMR():
        postsynaptic['ADAR'] += 1
        postsynaptic['AIBL'] += 4
        postsynaptic['AIBL'] += 1
        postsynaptic['AIYR'] += 1
        postsynaptic['AVAL'] += 5
        postsynaptic['AVAR'] += 1
        postsynaptic['AVBL'] += 2
        postsynaptic['AVBR'] += 5
        postsynaptic['AVEL'] += 3
        postsynaptic['AVER'] += 2
        postsynaptic['AVJL'] += 1
        postsynaptic['AVKL'] += 1
        postsynaptic['MDL05'] += 1
        postsynaptic['MDL07'] += 1
        postsynaptic['MVL05'] += 1
        postsynaptic['MVL07'] += 1
        postsynaptic['RIBR'] += 1
        postsynaptic['RIS'] += 2
        postsynaptic['RMDL'] += 1
        postsynaptic['RMDR'] += 1
        postsynaptic['RMFL'] += 1
        postsynaptic['RMFR'] += 1
        postsynaptic['SAAVL'] += 3
        postsynaptic['SAAVR'] += 3
        postsynaptic['SMDDL'] += 2
        postsynaptic['SMDDR'] += 4

def RIPL():
        postsynaptic['OLQDL'] += 1
        postsynaptic['OLQDR'] += 1
        postsynaptic['RMED'] += 1

def RIPR():
        postsynaptic['OLQDL'] += 1
        postsynaptic['OLQDR'] += 1
        postsynaptic['RMED'] += 1

def RIR():
        postsynaptic['AFDR'] += 1
        postsynaptic['AIZL'] += 3
        postsynaptic['AIZR'] += 5
        postsynaptic['AUAL'] += 1
        postsynaptic['AWBR'] += 1
        postsynaptic['BAGL'] += 1
        postsynaptic['BAGR'] += 2
        postsynaptic['DVA'] += 2
        postsynaptic['HSNL'] += 1
        postsynaptic['PVPL'] += 1
        postsynaptic['RIAL'] += 5
        postsynaptic['RIAR'] += 1
        postsynaptic['RIGL'] += 1
        postsynaptic['URXL'] += 5
        postsynaptic['URXR'] += 1

def RIS():
        postsynaptic['AIBR'] += 1
        postsynaptic['AVEL'] += 7
        postsynaptic['AVER'] += 7
        postsynaptic['AVJL'] += 1
        postsynaptic['AVKL'] += 1
        postsynaptic['AVKR'] += 4
        postsynaptic['AVL'] += 2
        postsynaptic['CEPDR'] += 1
        postsynaptic['CEPVL'] += 2
        postsynaptic['CEPVR'] += 1
        postsynaptic['DB1'] += 1
        postsynaptic['OLLR'] += 1
        postsynaptic['RIBL'] += 3
        postsynaptic['RIBR'] += 5
        postsynaptic['RIML'] += 2
        postsynaptic['RIMR'] += 5
        postsynaptic['RMDDL'] += 1
        postsynaptic['RMDL'] += 2
        postsynaptic['RMDR'] += 4
        postsynaptic['SMDDL'] += 1
        postsynaptic['SMDDR'] += 3
        postsynaptic['SMDVL'] += 1
        postsynaptic['SMDVR'] += 1
        postsynaptic['URYVR'] += 1

def RIVL():
        postsynaptic['AIBL'] += 1
        postsynaptic['MVR05'] += -2
        postsynaptic['MVR06'] += -2
        postsynaptic['MVR08'] += -3
        postsynaptic['RIAL'] += 1
        postsynaptic['RIAR'] += 1
        postsynaptic['RIVR'] += 2
        postsynaptic['RMDL'] += 2
        postsynaptic['SAADR'] += 3
        postsynaptic['SDQR'] += 2
        postsynaptic['SIAVR'] += 2
        postsynaptic['SMDDR'] += 1
        postsynaptic['SMDVL'] += 1

def RIVR():
        postsynaptic['AIBR'] += 1
        postsynaptic['MVL05'] += -2
        postsynaptic['MVL06'] += -2
        postsynaptic['MVL08'] += -2
        postsynaptic['MVR04'] += -2
        postsynaptic['MVR06'] += -2
        postsynaptic['RIAL'] += 2
        postsynaptic['RIAR'] += 1
        postsynaptic['RIVL'] += 2
        postsynaptic['RMDDL'] += 1
        postsynaptic['RMDR'] += 1
        postsynaptic['RMDVR'] += 1
        postsynaptic['RMEV'] += 1
        postsynaptic['SAADL'] += 2
        postsynaptic['SDQR'] += 2
        postsynaptic['SIAVL'] += 2
        postsynaptic['SMDDL'] += 2
        postsynaptic['SMDVR'] += 4

def RMDDL():
        postsynaptic['MDR01'] += 1
        postsynaptic['MDR02'] += 1
        postsynaptic['MDR03'] += 1
        postsynaptic['MDR04'] += 1
        postsynaptic['MDR08'] += 2
        postsynaptic['MVR01'] += 1
        postsynaptic['OLQVL'] += 1
        postsynaptic['RMDL'] += 1
        postsynaptic['RMDVL'] += 1
        postsynaptic['RMDVR'] += 7
        postsynaptic['SMDDL'] += 1

def RMDDR():
        postsynaptic['MDL01'] += 1
        postsynaptic['MDL02'] += 1
        postsynaptic['MDL03'] += 2
        postsynaptic['MDL04'] += 1
        postsynaptic['MDR04'] += 1
        postsynaptic['MVR01'] += 1
        postsynaptic['MVR02'] += 1
        postsynaptic['OLQVR'] += 1
        postsynaptic['RMDVL'] += 12
        postsynaptic['RMDVR'] += 1
        postsynaptic['SAADR'] += 1
        postsynaptic['SMDDR'] += 1
        postsynaptic['URYDL'] += 1

def RMDL():
        postsynaptic['MDL03'] += 1
        postsynaptic['MDL05'] += 2
        postsynaptic['MDR01'] += 1
        postsynaptic['MDR03'] += 1
        postsynaptic['MVL01'] += 1
        postsynaptic['MVR01'] += 1
        postsynaptic['MVR03'] += 1
        postsynaptic['MVR05'] += 2
        postsynaptic['MVR07'] += 1
        postsynaptic['OLLR'] += 2
        postsynaptic['RIAL'] += 4
        postsynaptic['RIAR'] += 3
        postsynaptic['RMDDL'] += 1
        postsynaptic['RMDDR'] += 1
        postsynaptic['RMDR'] += 3
        postsynaptic['RMDVL'] += 1
        postsynaptic['RMER'] += 1
        postsynaptic['RMFL'] += 1

def RMDR():
        postsynaptic['AVKL'] += 1
        postsynaptic['MDL03'] += 1
        postsynaptic['MDL05'] += 1
        postsynaptic['MDR05'] += 1
        postsynaptic['MVL03'] += 1
        postsynaptic['MVL05'] += 1
        postsynaptic['RIAL'] += 3
        postsynaptic['RIAR'] += 7
        postsynaptic['RIMR'] += 2
        postsynaptic['RIS'] += 1
        postsynaptic['RMDDL'] += 1
        postsynaptic['RMDL'] += 1
        postsynaptic['RMDVR'] += 1

def RMDVL():
        postsynaptic['AVER'] += 1
        postsynaptic['MDR01'] += 1
        postsynaptic['MVL04'] += 1
        postsynaptic['MVR01'] += 1
        postsynaptic['MVR02'] += 1
        postsynaptic['MVR03'] += 1
        postsynaptic['MVR04'] += 1
        postsynaptic['MVR05'] += 1
        postsynaptic['MVR06'] += 1
        postsynaptic['MVR08'] += 1
        postsynaptic['OLQDL'] += 1
        postsynaptic['RMDDL'] += 1
        postsynaptic['RMDDR'] += 6
        postsynaptic['RMDL'] += 1
        postsynaptic['RMDVR'] += 1
        postsynaptic['SAAVL'] += 1
        postsynaptic['SMDVL'] += 1

def RMDVR():
        postsynaptic['AVEL'] += 1
        postsynaptic['AVER'] += 1
        postsynaptic['MDL01'] += 1
        postsynaptic['MVL01'] += 1
        postsynaptic['MVL02'] += 1
        postsynaptic['MVL03'] += 1
        postsynaptic['MVL04'] += 1
        postsynaptic['MVL05'] += 1
        postsynaptic['MVL06'] += 1
        postsynaptic['MVL08'] += 1
        postsynaptic['MVR04'] += 1
        postsynaptic['MVR06'] += 1
        postsynaptic['MVR08'] += 1
        postsynaptic['OLQDR'] += 1
        postsynaptic['RMDDL'] += 4
        postsynaptic['RMDDR'] += 1
        postsynaptic['RMDR'] += 1
        postsynaptic['RMDVL'] += 1
        postsynaptic['SAAVR'] += 1
        postsynaptic['SIBDR'] += 1
        postsynaptic['SIBVR'] += 1
        postsynaptic['SMDVR'] += 1

def RMED():
        postsynaptic['IL1VL'] += 1
        postsynaptic['MVL02'] += -4
        postsynaptic['MVL04'] += -4
        postsynaptic['MVL06'] += -4
        postsynaptic['MVR02'] += -4
        postsynaptic['MVR04'] += -4
        postsynaptic['RIBL'] += 1
        postsynaptic['RIBR'] += 1
        postsynaptic['RIPL'] += 1
        postsynaptic['RIPR'] += 1
        postsynaptic['RMEV'] += 2

def RMEL():
        postsynaptic['MDR01'] += -5
        postsynaptic['MDR03'] += -5
        postsynaptic['MVR01'] += -5
        postsynaptic['MVR03'] += -5
        postsynaptic['RIGL'] += 1
        postsynaptic['RMEV'] += 1

def RMER():
        postsynaptic['MDL01'] += -7
        postsynaptic['MDL03'] += -7
        postsynaptic['MVL01'] += -7
        postsynaptic['RMEV'] += 1

def RMEV():
        postsynaptic['AVEL'] += 1
        postsynaptic['AVER'] += 1
        postsynaptic['IL1DL'] += 1
        postsynaptic['IL1DR'] += 1
        postsynaptic['MDL02'] += -3
        postsynaptic['MDL04'] += -3
        postsynaptic['MDL06'] += -3
        postsynaptic['MDR02'] += -3
        postsynaptic['MDR04'] += -3
        postsynaptic['RMED'] += 2
        postsynaptic['RMEL'] += 1
        postsynaptic['RMER'] += 1
        postsynaptic['SMDDR'] += 1

def RMFL():
        postsynaptic['AVKL'] += 4
        postsynaptic['AVKR'] += 4
        postsynaptic['MDR03'] += 1
        postsynaptic['MVR01'] += 1
        postsynaptic['MVR03'] += 1
        postsynaptic['PVT'] += 1
        postsynaptic['RIGR'] += 1
        postsynaptic['RMDR'] += 3
        postsynaptic['RMGR'] += 1
        postsynaptic['URBR'] += 1

def RMFR():
        postsynaptic['AVKL'] += 3
        postsynaptic['AVKR'] += 3
        postsynaptic['RMDL'] += 2

def RMGL():
        postsynaptic['ADAL'] += 1
        postsynaptic['ADLL'] += 1
        postsynaptic['AIBR'] += 1
        postsynaptic['ALML'] += 1
        postsynaptic['ALNL'] += 1
        postsynaptic['ASHL'] += 2
        postsynaptic['ASKL'] += 2
        postsynaptic['AVAL'] += 1
        postsynaptic['AVBR'] += 2
        postsynaptic['AVEL'] += 2
        postsynaptic['AWBL'] += 1
        postsynaptic['CEPDL'] += 1
        postsynaptic['IL2L'] += 1
        postsynaptic['MDL05'] += 2
        postsynaptic['MVL05'] += 2
        postsynaptic['RID'] += 1
        postsynaptic['RMDL'] += 1
        postsynaptic['RMDR'] += 3
        postsynaptic['RMDVL'] += 3
        postsynaptic['RMHL'] += 3
        postsynaptic['RMHR'] += 1
        postsynaptic['SIAVL'] += 1
        postsynaptic['SIBVL'] += 3
        postsynaptic['SIBVR'] += 1
        postsynaptic['SMBVL'] += 1
        postsynaptic['URXL'] += 2

def RMGR():
        postsynaptic['ADAR'] += 1
        postsynaptic['AIMR'] += 1
        postsynaptic['ALNR'] += 1
        postsynaptic['ASHR'] += 2
        postsynaptic['ASKR'] += 1
        postsynaptic['AVAR'] += 1
        postsynaptic['AVBR'] += 1
        postsynaptic['AVDL'] += 1
        postsynaptic['AVER'] += 3
        postsynaptic['AVJL'] += 1
        postsynaptic['AWBR'] += 1
        postsynaptic['IL2R'] += 1
        postsynaptic['MDR05'] += 1
        postsynaptic['MVR05'] += 1
        postsynaptic['MVR07'] += 1
        postsynaptic['RIR'] += 1
        postsynaptic['RMDL'] += 4
        postsynaptic['RMDR'] += 2
        postsynaptic['RMDVR'] += 5
        postsynaptic['RMHR'] += 1
        postsynaptic['URXR'] += 2

def RMHL():
        postsynaptic['MDR01'] += 2
        postsynaptic['MDR03'] += 3
        postsynaptic['MVR01'] += 2
        postsynaptic['RMDR'] += 1
        postsynaptic['RMGL'] += 3
        postsynaptic['SIBVR'] += 1

def RMHR():
        postsynaptic['MDL01'] += 2
        postsynaptic['MDL03'] += 2
        postsynaptic['MDL05'] += 2
        postsynaptic['MVL01'] += 2
        postsynaptic['RMER'] += 1
        postsynaptic['RMGL'] += 1
        postsynaptic['RMGR'] += 1

def SAADL():
        postsynaptic['AIBL'] += 1
        postsynaptic['AVAL'] += 6
        postsynaptic['RIML'] += 3
        postsynaptic['RIMR'] += 6
        postsynaptic['RMGR'] += 1
        postsynaptic['SMBDL'] += 1

def SAADR():
        postsynaptic['AIBR'] += 1
        postsynaptic['AVAR'] += 3
        postsynaptic['OLLL'] += 1
        postsynaptic['RIML'] += 4
        postsynaptic['RIMR'] += 5
        postsynaptic['RMDDR'] += 1
        postsynaptic['RMFL'] += 1
        postsynaptic['RMGL'] += 1

def SAAVL():
        postsynaptic['AIBL'] += 1
        postsynaptic['ALNL'] += 1
        postsynaptic['AVAL'] += 16
        postsynaptic['OLLR'] += 1
        postsynaptic['RIML'] += 2
        postsynaptic['RIMR'] += 12
        postsynaptic['RMDVL'] += 2
        postsynaptic['RMFR'] += 2
        postsynaptic['SMBVR'] += 3
        postsynaptic['SMDDR'] += 8

def SAAVR():
        postsynaptic['AVAR'] += 13
        postsynaptic['RIML'] += 5
        postsynaptic['RIMR'] += 2
        postsynaptic['RMDVR'] += 1
        postsynaptic['SMBVL'] += 2
        postsynaptic['SMDDL'] += 6

def SABD():
        postsynaptic['AVAL'] += 4
        postsynaptic['VA2'] += 4
        postsynaptic['VA3'] += 2
        postsynaptic['VA4'] += 1

def SABVL():
        postsynaptic['AVAR'] += 3
        postsynaptic['DA1'] += 2
        postsynaptic['DA2'] += 1

def SABVR():
        postsynaptic['AVAL'] += 1
        postsynaptic['AVAR'] += 1
        postsynaptic['DA1'] += 3

def SDQL():
        postsynaptic['ALML'] += 2
        postsynaptic['AVAL'] += 1
        postsynaptic['AVAR'] += 3
        postsynaptic['AVEL'] += 1
        postsynaptic['FLPL'] += 1
        postsynaptic['RICR'] += 1
        postsynaptic['RIS'] += 3
        postsynaptic['RMFL'] += 1
        postsynaptic['SDQR'] += 1

def SDQR():
        postsynaptic['ADLL'] += 1
        postsynaptic['AIBL'] += 2
        postsynaptic['AVAL'] += 3
        postsynaptic['AVBL'] += 7
        postsynaptic['AVBR'] += 4
        postsynaptic['DVA'] += 3
        postsynaptic['RICR'] += 1
        postsynaptic['RIVL'] += 2
        postsynaptic['RIVR'] += 2
        postsynaptic['RMHL'] += 2
        postsynaptic['RMHR'] += 1
        postsynaptic['SDQL'] += 1
        postsynaptic['SIBVL'] += 1

def SIADL():
        postsynaptic['RIBL'] += 1

def SIADR():
        postsynaptic['RIBR'] += 1

def SIAVL():
        postsynaptic['RIBL'] += 1

def SIAVR():
        postsynaptic['RIBR'] += 1

def SIBDL():
        postsynaptic['RIBL'] += 1
        postsynaptic['SIBVL'] += 1

def SIBDR():
        postsynaptic['AIML'] += 1
        postsynaptic['RIBR'] += 1
        postsynaptic['SIBVR'] += 1

def SIBVL():
        postsynaptic['AVBL'] += 1
        postsynaptic['AVBR'] += 1
        postsynaptic['RIBL'] += 1
        postsynaptic['SDQR'] += 1
        postsynaptic['SIBDL'] += 1

def SIBVR():
        postsynaptic['RIBL'] += 1
        postsynaptic['RIBR'] += 1
        postsynaptic['RMHL'] += 1
        postsynaptic['SIBDR'] += 1

def SMBDL():
        postsynaptic['AVAR'] += 1
        postsynaptic['AVKL'] += 1
        postsynaptic['AVKR'] += 1
        postsynaptic['MDR01'] += 2
        postsynaptic['MDR02'] += 2
        postsynaptic['MDR03'] += 2
        postsynaptic['MDR04'] += 2
        postsynaptic['MDR06'] += 3
        postsynaptic['RIBL'] += 1
        postsynaptic['RMED'] += 3
        postsynaptic['SAADL'] += 1
        postsynaptic['SAAVR'] += 1

def SMBDR():
        postsynaptic['ALNL'] += 1
        postsynaptic['AVAL'] += 1
        postsynaptic['AVKL'] += 1
        postsynaptic['AVKR'] += 2
        postsynaptic['MDL02'] += 1
        postsynaptic['MDL03'] += 1
        postsynaptic['MDL04'] += 1
        postsynaptic['MDL06'] += 2
        postsynaptic['MDR04'] += 1
        postsynaptic['MDR08'] += 1
        postsynaptic['RIBR'] += 1
        postsynaptic['RMED'] += 4
        postsynaptic['SAAVL'] += 3

def SMBVL():
        postsynaptic['MVL01'] += 1
        postsynaptic['MVL02'] += 1
        postsynaptic['MVL03'] += 1
        postsynaptic['MVL04'] += 1
        postsynaptic['MVL05'] += 1
        postsynaptic['MVL06'] += 1
        postsynaptic['MVL08'] += 1
        postsynaptic['PLNL'] += 1
        postsynaptic['RMEV'] += 5
        postsynaptic['SAADL'] += 3
        postsynaptic['SAAVR'] += 2

def SMBVR():
        postsynaptic['AVKL'] += 1
        postsynaptic['AVKR'] += 1
        postsynaptic['MVR01'] += 1
        postsynaptic['MVR02'] += 1
        postsynaptic['MVR03'] += 1
        postsynaptic['MVR04'] += 1
        postsynaptic['MVR06'] += 1
        postsynaptic['MVR07'] += 1
        postsynaptic['RMEV'] += 3
        postsynaptic['SAADR'] += 4
        postsynaptic['SAAVL'] += 3

def SMDDL():
        postsynaptic['MDL04'] += 1
        postsynaptic['MDL06'] += 1
        postsynaptic['MDL08'] += 1
        postsynaptic['MDR02'] += 1
        postsynaptic['MDR03'] += 1
        postsynaptic['MDR04'] += 1
        postsynaptic['MDR05'] += 1
        postsynaptic['MDR06'] += 1
        postsynaptic['MDR07'] += 1
        postsynaptic['MVL02'] += 1
        postsynaptic['MVL04'] += 1
        postsynaptic['RIAL'] += 1
        postsynaptic['RIAR'] += 1
        postsynaptic['RIBL'] += 1
        postsynaptic['RIBR'] += 1
        postsynaptic['RIS'] += 1
        postsynaptic['RMDDL'] += 1
        postsynaptic['SMDVR'] += 2

def SMDDR():
        postsynaptic['MDL04'] += 1
        postsynaptic['MDL05'] += 1
        postsynaptic['MDL06'] += 1
        postsynaptic['MDL08'] += 1
        postsynaptic['MDR04'] += 1
        postsynaptic['MDR06'] += 1
        postsynaptic['MVR02'] += 1
        postsynaptic['RIAL'] += 2
        postsynaptic['RIAR'] += 1
        postsynaptic['RIBR'] += 1
        postsynaptic['RIS'] += 1
        postsynaptic['RMDDR'] += 1
        postsynaptic['VD1'] += 1

def SMDVL():
        postsynaptic['MVL03'] += 1
        postsynaptic['MVL06'] += 1
        postsynaptic['MVR02'] += 1
        postsynaptic['MVR03'] += 1
        postsynaptic['MVR04'] += 1
        postsynaptic['MVR06'] += 1
        postsynaptic['PVR'] += 1
        postsynaptic['RIAL'] += 3
        postsynaptic['RIAR'] += 8
        postsynaptic['RIBR'] += 2
        postsynaptic['RIS'] += 1
        postsynaptic['RIVL'] += 1
        postsynaptic['RMDDR'] += 1
        postsynaptic['RMDVL'] += 1
        postsynaptic['SMDDR'] += 4
        postsynaptic['SMDVR'] += 1

def SMDVR():
        postsynaptic['MVL02'] += 1
        postsynaptic['MVL03'] += 1
        postsynaptic['MVL04'] += 1
        postsynaptic['MVR07'] += 1
        postsynaptic['RIAL'] += 7
        postsynaptic['RIAR'] += 5
        postsynaptic['RIBL'] += 2
        postsynaptic['RIVR'] += 1
        postsynaptic['RIVR'] += 2
        postsynaptic['RMDDL'] += 1
        postsynaptic['RMDVR'] += 1
        postsynaptic['SMDDL'] += 2
        postsynaptic['SMDVL'] += 1
        postsynaptic['VB1'] += 1

def URADL():
        postsynaptic['IL1DL'] += 2
        postsynaptic['MDL02'] += 2
        postsynaptic['MDL03'] += 2
        postsynaptic['MDL04'] += 2
        postsynaptic['RIPL'] += 3
        postsynaptic['RMEL'] += 1

def URADR():
        postsynaptic['IL1DR'] += 1
        postsynaptic['MDR01'] += 3
        postsynaptic['MDR02'] += 2
        postsynaptic['MDR03'] += 3
        postsynaptic['RIPR'] += 3
        postsynaptic['RMDVR'] += 1
        postsynaptic['RMED'] += 1
        postsynaptic['RMER'] += 1
        postsynaptic['URYDR'] += 1

def URAVL():
        postsynaptic['MVL01'] += 2
        postsynaptic['MVL02'] += 2
        postsynaptic['MVL03'] += 3
        postsynaptic['MVL04'] += 2
        postsynaptic['RIPL'] += 3
        postsynaptic['RMEL'] += 1
        postsynaptic['RMER'] += 1
        postsynaptic['RMEV'] += 2

def URAVR():
        postsynaptic['IL1R'] += 1
        postsynaptic['MVR01'] += 2
        postsynaptic['MVR02'] += 2
        postsynaptic['MVR03'] += 2
        postsynaptic['MVR04'] += 2
        postsynaptic['RIPR'] += 3
        postsynaptic['RMDVL'] += 1
        postsynaptic['RMER'] += 2
        postsynaptic['RMEV'] += 2

def URBL():
        postsynaptic['AVBL'] += 1
        postsynaptic['CEPDL'] += 1
        postsynaptic['IL1L'] += 1
        postsynaptic['OLQDL'] += 1
        postsynaptic['OLQVL'] += 1
        postsynaptic['RICR'] += 1
        postsynaptic['RMDDR'] += 1
        postsynaptic['SIAVL'] += 1
        postsynaptic['SMBDR'] += 1
        postsynaptic['URXL'] += 2

def URBR():
        postsynaptic['ADAR'] += 1
        postsynaptic['AVBR'] += 1
        postsynaptic['CEPDR'] += 1
        postsynaptic['IL1R'] += 3
        postsynaptic['IL2R'] += 1
        postsynaptic['OLQDR'] += 1
        postsynaptic['OLQVR'] += 1
        postsynaptic['RICR'] += 1
        postsynaptic['RMDL'] += 1
        postsynaptic['RMDR'] += 1
        postsynaptic['RMFL'] += 1
        postsynaptic['SIAVR'] += 2
        postsynaptic['SMBDL'] += 1
        postsynaptic['URXR'] += 4

def URXL():
        postsynaptic['ASHL'] += 1
        postsynaptic['AUAL'] += 5
        postsynaptic['AVBL'] += 1
        postsynaptic['AVEL'] += 4
        postsynaptic['AVJR'] += 1
        postsynaptic['RIAL'] += 8
        postsynaptic['RICL'] += 1
        postsynaptic['RIGL'] += 3
        postsynaptic['RMGL'] += 2
        postsynaptic['RMGL'] += 1

def URXR():
        postsynaptic['AUAR'] += 4
        postsynaptic['AVBL'] += 1
        postsynaptic['AVBR'] += 2
        postsynaptic['AVER'] += 2
        postsynaptic['IL2R'] += 1
        postsynaptic['OLQVR'] += 1
        postsynaptic['RIAR'] += 3
        postsynaptic['RIGR'] += 2
        postsynaptic['RIPR'] += 3
        postsynaptic['RMDR'] += 1
        postsynaptic['RMGR'] += 2
        postsynaptic['SIAVR'] += 1

def URYDL():
        postsynaptic['AVAL'] += 1
        postsynaptic['AVER'] += 2
        postsynaptic['RIBL'] += 1
        postsynaptic['RIGL'] += 1
        postsynaptic['RMDDR'] += 4
        postsynaptic['RMDVL'] += 6
        postsynaptic['SMDDL'] += 1
        postsynaptic['SMDDR'] += 1

def URYDR():
        postsynaptic['AVAR'] += 1
        postsynaptic['AVEL'] += 2
        postsynaptic['AVER'] += 2
        postsynaptic['RIBR'] += 1
        postsynaptic['RIGR'] += 1
        postsynaptic['RMDDL'] += 3
        postsynaptic['RMDVR'] += 5
        postsynaptic['SMDDL'] += 4

def URYVL():
        postsynaptic['AVAR'] += 1
        postsynaptic['AVBR'] += 1
        postsynaptic['AVER'] += 5
        postsynaptic['IL1VL'] += 1
        postsynaptic['RIAL'] += 1
        postsynaptic['RIBL'] += 2
        postsynaptic['RIGL'] += 1
        postsynaptic['RIH'] += 1
        postsynaptic['RIS'] += 1
        postsynaptic['RMDDL'] += 4
        postsynaptic['RMDVR'] += 2
        postsynaptic['SIBVR'] += 1
        postsynaptic['SMDVR'] += 4

def URYVR():
        postsynaptic['AVAL'] += 2
        postsynaptic['AVEL'] += 6
        postsynaptic['IL1VR'] += 1
        postsynaptic['RIAR'] += 1
        postsynaptic['RIBR'] += 1
        postsynaptic['RIGR'] += 1
        postsynaptic['RMDDR'] += 6
        postsynaptic['RMDVL'] += 4
        postsynaptic['SIBDR'] += 1
        postsynaptic['SIBVL'] += 1
        postsynaptic['SMDVL'] += 3

def VA1():
        postsynaptic['AVAL'] += 3
        postsynaptic['DA2'] += 2
        postsynaptic['DD1'] += 9
        postsynaptic['MVL07'] += 3
        postsynaptic['MVL08'] += 3
        postsynaptic['MVR07'] += 3
        postsynaptic['MVR08'] += 3
        postsynaptic['VD1'] += 2

def VA2():
        postsynaptic['AVAL'] += 5
        postsynaptic['DD1'] += 13
        postsynaptic['MVL07'] += 5
        postsynaptic['MVL10'] += 5
        postsynaptic['MVR07'] += 5
        postsynaptic['MVR10'] += 5
        postsynaptic['SABD'] += 3
        postsynaptic['VA3'] += 2
        postsynaptic['VB1'] += 2
        postsynaptic['VD1'] += 2
        postsynaptic['VD1'] += 1
        postsynaptic['VD2'] += 11

def VA3():
        postsynaptic['AS1'] += 1
        postsynaptic['AVAL'] += 1
        postsynaptic['AVAR'] += 2
        postsynaptic['DD1'] += 18
        postsynaptic['DD2'] += 11
        postsynaptic['MVL09'] += 5
        postsynaptic['MVL10'] += 5
        postsynaptic['MVL12'] += 5
        postsynaptic['MVR09'] += 5
        postsynaptic['MVR10'] += 5
        postsynaptic['MVR12'] += 5
        postsynaptic['SABD'] += 2
        postsynaptic['VA4'] += 1
        postsynaptic['VD2'] += 3
        postsynaptic['VD3'] += 3

def VA4():
        postsynaptic['AS2'] += 2
        postsynaptic['AVAL'] += 1
        postsynaptic['AVAR'] += 2
        postsynaptic['AVDL'] += 1
        postsynaptic['DA5'] += 1
        postsynaptic['DD2'] += 21
        postsynaptic['MVL11'] += 6
        postsynaptic['MVL12'] += 6
        postsynaptic['MVR11'] += 6
        postsynaptic['MVR12'] += 6
        postsynaptic['SABD'] += 1
        postsynaptic['VB3'] += 2
        postsynaptic['VD4'] += 3
        
def VA5():
        postsynaptic['AS3'] += 2
        postsynaptic['AVAL'] += 5
        postsynaptic['AVAR'] += 3
        postsynaptic['DA5'] += 2
        postsynaptic['DD2'] += 5
        postsynaptic['DD3'] += 13
        postsynaptic['MVL11'] += 5
        postsynaptic['MVL14'] += 5
        postsynaptic['MVR11'] += 5
        postsynaptic['MVR14'] += 5
        postsynaptic['VD5'] += 2

def VA6():
        postsynaptic['AVAL'] += 6
        postsynaptic['AVAR'] += 2
        postsynaptic['DD3'] += 24
        postsynaptic['MVL13'] += 5
        postsynaptic['MVL14'] += 5
        postsynaptic['MVR13'] += 5
        postsynaptic['MVR14'] += 5
        postsynaptic['VB5'] += 2
        postsynaptic['VD5'] += 1
        postsynaptic['VD6'] += 2

def VA7():
        postsynaptic['AS5'] += 1
        postsynaptic['AVAL'] += 2
        postsynaptic['AVAR'] += 4
        postsynaptic['DD3'] += 3
        postsynaptic['DD4'] += 12
        postsynaptic['MVL13'] += 4
        postsynaptic['MVL15'] += 4
        postsynaptic['MVL16'] += 4
        postsynaptic['MVR13'] += 4
        postsynaptic['MVR15'] += 4
        postsynaptic['MVR16'] += 4
        postsynaptic['MVULVA'] += 4
        postsynaptic['VB3'] += 1
        postsynaptic['VD7'] += 9

def VA8():
        postsynaptic['AS6'] += 1
        postsynaptic['AVAL'] += 10
        postsynaptic['AVAR'] += 4
        postsynaptic['AVBR'] += 1
        postsynaptic['DD4'] += 21
        postsynaptic['MVL15'] += 6
        postsynaptic['MVL16'] += 6
        postsynaptic['MVR15'] += 6
        postsynaptic['MVR16'] += 6
        postsynaptic['PDER'] += 1
        postsynaptic['PVCR'] += 2
        postsynaptic['VA8'] += 1
        postsynaptic['VA9'] += 1
        postsynaptic['VB6'] += 1
        postsynaptic['VB8'] += 1
        postsynaptic['VB8'] += 3
        postsynaptic['VB9'] += 3
        postsynaptic['VD7'] += 5
        postsynaptic['VD8'] += 5
        postsynaptic['VD8'] += 1

def VA9():
        postsynaptic['AVAL'] += 1
        postsynaptic['AVBR'] += 1
        postsynaptic['DD4'] += 3
        postsynaptic['DD5'] += 15
        postsynaptic['DVB'] += 1
        postsynaptic['DVC'] += 1
        postsynaptic['MVL15'] += 5
        postsynaptic['MVL18'] += 5
        postsynaptic['MVR15'] += 5
        postsynaptic['MVR18'] += 5
        postsynaptic['PVCR'] += 1
        postsynaptic['PVT'] += 1
        postsynaptic['VB8'] += 6
        postsynaptic['VB8'] += 1
        postsynaptic['VB9'] += 4
        postsynaptic['VD7'] += 1
        postsynaptic['VD9'] += 10

def VA10():
        postsynaptic['AVAL'] += 1
        postsynaptic['AVAR'] += 1
        postsynaptic['MVL17'] += 5
        postsynaptic['MVL18'] += 5
        postsynaptic['MVR17'] += 5
        postsynaptic['MVR18'] += 5

def VA11():
        postsynaptic['AVAL'] += 1
        postsynaptic['AVAR'] += 7
        postsynaptic['DD6'] += 10
        postsynaptic['MVL19'] += 5
        postsynaptic['MVL20'] += 5
        postsynaptic['MVR19'] += 5
        postsynaptic['MVR20'] += 5
        postsynaptic['PVNR'] += 2
        postsynaptic['VB10'] += 1
        postsynaptic['VD12'] += 4

def VA12():
        postsynaptic['AS11'] += 2
        postsynaptic['AVAR'] += 1
        postsynaptic['DA8'] += 3
        postsynaptic['DA9'] += 5
        postsynaptic['DB7'] += 4
        postsynaptic['DD6'] += 2
        postsynaptic['LUAL'] += 2
        postsynaptic['MVL21'] += 5
        postsynaptic['MVL22'] += 5
        postsynaptic['MVL23'] += 5
        postsynaptic['MVR21'] += 5
        postsynaptic['MVR22'] += 5
        postsynaptic['MVR23'] += 5
        postsynaptic['MVR24'] += 5
        postsynaptic['PHCL'] += 1
        postsynaptic['PHCR'] += 1
        postsynaptic['PVCL'] += 2
        postsynaptic['PVCR'] += 3
        postsynaptic['VA11'] += 1
        postsynaptic['VB11'] += 1
        postsynaptic['VD12'] += 3
        postsynaptic['VD13'] += 11

def VB1():
        postsynaptic['AIBR'] += 1
        postsynaptic['AVBL'] += 1
        postsynaptic['AVKL'] += 4
        postsynaptic['DB2'] += 2
        postsynaptic['DD1'] += 1
        postsynaptic['DVA'] += 1
        postsynaptic['MVL07'] += 1
        postsynaptic['MVL08'] += 1
        postsynaptic['MVR07'] += 1
        postsynaptic['MVR08'] += 1
        postsynaptic['RIML'] += 2
        postsynaptic['RMFL'] += 2
        postsynaptic['SAADL'] += 9
        postsynaptic['SAADR'] += 2
        postsynaptic['SABD'] += 1
        postsynaptic['SMDVR'] += 1
        postsynaptic['VA1'] += 3
        postsynaptic['VA3'] += 1
        postsynaptic['VB2'] += 4
        postsynaptic['VD1'] += 3
        postsynaptic['VD2'] += 1

def VB2():
        postsynaptic['AVBL'] += 3
        postsynaptic['AVBR'] += 1
        postsynaptic['DB4'] += 1
        postsynaptic['DD1'] += 20
        postsynaptic['DD2'] += 1
        postsynaptic['MVL07'] += 4
        postsynaptic['MVL09'] += 4
        postsynaptic['MVL10'] += 4
        postsynaptic['MVL12'] += 4
        postsynaptic['MVR07'] += 4
        postsynaptic['MVR09'] += 4
        postsynaptic['MVR10'] += 4
        postsynaptic['MVR12'] += 4
        postsynaptic['RIGL'] += 1
        postsynaptic['VA2'] += 1
        postsynaptic['VB1'] += 4
        postsynaptic['VB3'] += 1
        postsynaptic['VB5'] += 1
        postsynaptic['VB7'] += 2
        postsynaptic['VC2'] += 1
        postsynaptic['VD2'] += 9
        postsynaptic['VD3'] += 3

def VB3():
        postsynaptic['AVBR'] += 1
        postsynaptic['DB1'] += 1
        postsynaptic['DD2'] += 37
        postsynaptic['MVL11'] += 6
        postsynaptic['MVL12'] += 6
        postsynaptic['MVL14'] += 6
        postsynaptic['MVR11'] += 6
        postsynaptic['MVR12'] += 6
        postsynaptic['MVR14'] += 6
        postsynaptic['VA4'] += 1
        postsynaptic['VA7'] += 1
        postsynaptic['VB2'] += 1

def VB4():
        postsynaptic['AVBL'] += 1
        postsynaptic['AVBR'] += 1
        postsynaptic['DB1'] += 1
        postsynaptic['DB4'] += 1
        postsynaptic['DD2'] += 6
        postsynaptic['DD3'] += 16
        postsynaptic['MVL11'] += 5
        postsynaptic['MVL14'] += 5
        postsynaptic['MVR11'] += 5
        postsynaptic['MVR14'] += 5
        postsynaptic['VB5'] += 1

def VB5():
        postsynaptic['AVBL'] += 1
        postsynaptic['DD3'] += 27
        postsynaptic['MVL13'] += 6
        postsynaptic['MVL14'] += 6
        postsynaptic['MVR13'] += 6
        postsynaptic['MVR14'] += 6
        postsynaptic['VB2'] += 1
        postsynaptic['VB4'] += 1
        postsynaptic['VB6'] += 8

def VB6():
        postsynaptic['AVBL'] += 1
        postsynaptic['AVBR'] += 2
        postsynaptic['DA4'] += 1
        postsynaptic['DD4'] += 30
        postsynaptic['MVL15'] += 6
        postsynaptic['MVL16'] += 6
        postsynaptic['MVR15'] += 6
        postsynaptic['MVR16'] += 6
        postsynaptic['MVULVA'] += 6
        postsynaptic['VA8'] += 1
        postsynaptic['VB5'] += 1
        postsynaptic['VB7'] += 1
        postsynaptic['VD6'] += 1
        postsynaptic['VD7'] += 8

def VB7():
        postsynaptic['AVBL'] += 2
        postsynaptic['AVBR'] += 2
        postsynaptic['DD4'] += 2
        postsynaptic['MVL15'] += 5
        postsynaptic['MVR15'] += 5
        postsynaptic['VB2'] += 2

def VB8():
        postsynaptic['AVBL'] += 7
        postsynaptic['AVBR'] += 3
        postsynaptic['DD5'] += 30
        postsynaptic['MVL17'] += 5
        postsynaptic['MVL18'] += 5
        postsynaptic['MVL20'] += 5
        postsynaptic['MVR17'] += 5
        postsynaptic['MVR18'] += 5
        postsynaptic['MVR20'] += 5
        postsynaptic['VA8'] += 3
        postsynaptic['VA9'] += 9
        postsynaptic['VA9'] += 1
        postsynaptic['VB9'] += 3  
        postsynaptic['VB9'] += 3
        postsynaptic['VD10'] += 1
        postsynaptic['VD9'] += 10

def VB9():
        postsynaptic['AVAL'] += 5
        postsynaptic['AVAR'] += 4
        postsynaptic['AVBL'] += 1
        postsynaptic['AVBR'] += 6
        postsynaptic['DD5'] += 8
        postsynaptic['DVB'] += 1
        postsynaptic['MVL17'] += 6
        postsynaptic['MVL20'] += 6
        postsynaptic['MVR17'] += 6
        postsynaptic['MVR20'] += 6
        postsynaptic['PVCL'] += 2
        postsynaptic['VA8'] += 3
        postsynaptic['VA9'] += 4
        postsynaptic['VB8'] += 1
        postsynaptic['VB8'] += 3
        postsynaptic['VD10'] += 5

def VB10():
        postsynaptic['AVBL'] += 2
        postsynaptic['AVBR'] += 1
        postsynaptic['AVKL'] += 1
        postsynaptic['DD6'] += 9
        postsynaptic['MVL19'] += 5
        postsynaptic['MVL20'] += 5
        postsynaptic['MVR19'] += 5
        postsynaptic['MVR20'] += 5
        postsynaptic['PVCL'] += 1
        postsynaptic['PVT'] += 1
        postsynaptic['VD11'] += 1
        postsynaptic['VD12'] += 2

def VB11():
        postsynaptic['AVBL'] += 2
        postsynaptic['AVBR'] += 1
        postsynaptic['DD6'] += 7
        postsynaptic['MVL21'] += 5
        postsynaptic['MVL22'] += 5
        postsynaptic['MVL23'] += 5
        postsynaptic['MVR21'] += 5
        postsynaptic['MVR22'] += 5
        postsynaptic['MVR23'] += 5
        postsynaptic['MVR24'] += 5
        postsynaptic['PVCR'] += 1
        postsynaptic['VA12'] += 2

def VC1():
        postsynaptic['AVL'] += 2
        postsynaptic['DD1'] += 7
        postsynaptic['DD2'] += 6
        postsynaptic['DD3'] += 6
        postsynaptic['DVC'] += 1
        postsynaptic['MVULVA'] += 6
        postsynaptic['PVT'] += 2
        postsynaptic['VC2'] += 9
        postsynaptic['VC3'] += 3
        postsynaptic['VD1'] += 5
        postsynaptic['VD2'] += 1
        postsynaptic['VD3'] += 1
        postsynaptic['VD4'] += 2
        postsynaptic['VD5'] += 5
        postsynaptic['VD6'] += 1

def VC2():
        postsynaptic['DB4'] += 1
        postsynaptic['DD1'] += 6
        postsynaptic['DD2'] += 4
        postsynaptic['DD3'] += 9
        postsynaptic['DVC'] += 1
        postsynaptic['MVULVA'] += 10
        postsynaptic['PVCR'] += 1
        postsynaptic['PVQR'] += 1
        postsynaptic['PVT'] += 2
        postsynaptic['VC1'] += 10
        postsynaptic['VC3'] += 6
        postsynaptic['VD1'] += 2
        postsynaptic['VD2'] += 2
        postsynaptic['VD4'] += 5
        postsynaptic['VD5'] += 5
        postsynaptic['VD6'] += 1

def VC3():
        postsynaptic['AVL'] += 1
        postsynaptic['DD1'] += 2
        postsynaptic['DD2'] += 4
        postsynaptic['DD3'] += 5
        postsynaptic['DD4'] += 13
        postsynaptic['DVC'] += 1
        postsynaptic['HSNR'] += 1
        postsynaptic['MVULVA'] += 11
        postsynaptic['PVNR'] += 1
        postsynaptic['PVPR'] += 1
        postsynaptic['PVQR'] += 4
        postsynaptic['VC1'] += 4
        postsynaptic['VC2'] += 3
        postsynaptic['VC4'] += 1
        postsynaptic['VC5'] += 2
        postsynaptic['VD1'] += 1
        postsynaptic['VD2'] += 1
        postsynaptic['VD3'] += 1
        postsynaptic['VD4'] += 2
        postsynaptic['VD5'] += 4
        postsynaptic['VD6'] += 4
        postsynaptic['VD7'] += 5

def VC4():
        postsynaptic['AVBL'] += 1
        postsynaptic['AVFR'] += 1
        postsynaptic['AVHR'] += 1
        postsynaptic['MVULVA'] += 7
        postsynaptic['VC1'] += 1
        postsynaptic['VC3'] += 5
        postsynaptic['VC5'] += 2

def VC5():
        postsynaptic['AVFL'] += 1
        postsynaptic['AVFR'] += 1
        postsynaptic['DVC'] += 2
        postsynaptic['HSNL'] += 1
        postsynaptic['MVULVA'] += 2
        postsynaptic['OLLR'] += 1
        postsynaptic['PVT'] += 1
        postsynaptic['URBL'] += 3
        postsynaptic['VC3'] += 3
        postsynaptic['VC4'] += 2

def VC6():
        postsynaptic['MVULVA'] += 1
           
def VD1():
        postsynaptic['DD1'] += 5
        postsynaptic['DVC'] += 5
        postsynaptic['MVL05'] += -5
        postsynaptic['MVL08'] += -5
        postsynaptic['MVR05'] += -5
        postsynaptic['MVR08'] += -5
        postsynaptic['RIFL'] += 1
        postsynaptic['RIGL'] += 2
        postsynaptic['SMDDR'] += 1
        postsynaptic['VA1'] += 2
        postsynaptic['VA2'] += 1
        postsynaptic['VC1'] += 1
        postsynaptic['VD2'] += 7

def VD2():
        postsynaptic['AS1'] += 1
        postsynaptic['DD1'] += 3
        postsynaptic['MVL07'] += -7
        postsynaptic['MVL10'] += -7
        postsynaptic['MVR07'] += -7
        postsynaptic['MVR10'] += -7
        postsynaptic['VA2'] += 9
        postsynaptic['VB2'] += 3
        postsynaptic['VD1'] += 7
        postsynaptic['VD3'] += 2

def VD3():
        postsynaptic['MVL09'] += -7
        postsynaptic['MVL12'] += -9
        postsynaptic['MVR09'] += -7
        postsynaptic['MVR12'] += -7
        postsynaptic['PVPL'] += 1
        postsynaptic['VA3'] += 2
        postsynaptic['VB2'] += 2
        postsynaptic['VD2'] += 2
        postsynaptic['VD4'] += 1

def VD4():
        postsynaptic['DD2'] += 2
        postsynaptic['MVL11'] += -9
        postsynaptic['MVL12'] += -9
        postsynaptic['MVR11'] += -9
        postsynaptic['MVR12'] += -9
        postsynaptic['PVPR'] += 1
        postsynaptic['VD3'] += 1
        postsynaptic['VD5'] += 1

def VD5():
        postsynaptic['AVAR'] += 1
        postsynaptic['MVL14'] += -17
        postsynaptic['MVR14'] += -17
        postsynaptic['PVPR'] += 1
        postsynaptic['VA5'] += 2
        postsynaptic['VB4'] += 2
        postsynaptic['VD4'] += 1
        postsynaptic['VD6'] += 2

def VD6():
        postsynaptic['AVAL'] += 1
        postsynaptic['MVL13'] += -7
        postsynaptic['MVL14'] += -7
        postsynaptic['MVL16'] += -7
        postsynaptic['MVR13'] += -7
        postsynaptic['MVR14'] += -7
        postsynaptic['MVR16'] += -7
        postsynaptic['VA6'] += 1
        postsynaptic['VB5'] += 2
        postsynaptic['VD5'] += 2
        postsynaptic['VD7'] += 1

def VD7():
        postsynaptic['MVL15'] += -7
        postsynaptic['MVL16'] += -7
        postsynaptic['MVR15'] += -7
        postsynaptic['MVR16'] += -7
        postsynaptic['MVULVA'] += -15
        postsynaptic['VA9'] += 1
        postsynaptic['VD6'] += 1

def VD8():
        postsynaptic['DD4'] += 2
        postsynaptic['MVL15'] += -18
        postsynaptic['MVR15'] += -18
        postsynaptic['VA8'] += 5

def VD9():
        postsynaptic['MVL17'] += -10
        postsynaptic['MVL18'] += -10
        postsynaptic['MVR17'] += -10
        postsynaptic['MVR18'] += -10
        postsynaptic['PDER'] += 1
        postsynaptic['VD10'] += 5

def VD10():
        postsynaptic['AVBR'] += 1
        postsynaptic['DD5'] += 2
        postsynaptic['DVC'] += 4
        postsynaptic['MVL17'] += -9
        postsynaptic['MVL20'] += -9
        postsynaptic['MVR17'] += -9
        postsynaptic['MVR20'] += -9
        postsynaptic['VB9'] += 2
        postsynaptic['VD9'] += 5

def VD11():
        postsynaptic['AVAR'] += 2
        postsynaptic['MVL19'] += -9
        postsynaptic['MVL20'] += -9
        postsynaptic['MVR19'] += -9
        postsynaptic['MVR20'] += -9
        postsynaptic['VA11'] += 1
        postsynaptic['VB10'] += 1

def VD12():
        postsynaptic['MVL19'] += -5
        postsynaptic['MVL21'] += -5
        postsynaptic['MVR19'] += -5
        postsynaptic['MVR22'] += -5
        postsynaptic['VA11'] += 3
        postsynaptic['VA12'] += 2
        postsynaptic['VB10'] += 1
        postsynaptic['VB11'] += 1

def VD13():
        postsynaptic['AVAR'] += 2
        postsynaptic['MVL21'] += -9
        postsynaptic['MVL22'] += -9
        postsynaptic['MVL23'] += -9
        postsynaptic['MVR21'] += -9
        postsynaptic['MVR22'] += -9
        postsynaptic['MVR23'] += -9
        postsynaptic['MVR24'] += -9
        postsynaptic['PVCL'] += 1
        postsynaptic['PVCR'] += 1
        postsynaptic['PVPL'] += 2
        postsynaptic['VA12'] += 1
        
        
def createpostsynaptic():
        # The PostSynaptic dictionary maintains the accumulated values for
        # each neuron and muscle. The Accumulated values are initialized to Zero
        postsynaptic['ADAL'] = 0
        postsynaptic['ADAR'] = 0
        postsynaptic['ADEL'] = 0
        postsynaptic['ADER'] = 0
        postsynaptic['ADFL'] = 0
        postsynaptic['ADFR'] = 0
        postsynaptic['ADLL'] = 0
        postsynaptic['ADLR'] = 0
        postsynaptic['AFDL'] = 0
        postsynaptic['AFDR'] = 0
        postsynaptic['AIAL'] = 0
        postsynaptic['AIAR'] = 0
        postsynaptic['AIBL'] = 0
        postsynaptic['AIBR'] = 0
        postsynaptic['AIML'] = 0
        postsynaptic['AIMR'] = 0
        postsynaptic['AINL'] = 0
        postsynaptic['AINR'] = 0
        postsynaptic['AIYL'] = 0
        postsynaptic['AIYR'] = 0
        postsynaptic['AIZL'] = 0
        postsynaptic['AIZR'] = 0
        postsynaptic['ALA'] = 0
        postsynaptic['ALML'] = 0
        postsynaptic['ALMR'] = 0
        postsynaptic['ALNL'] = 0
        postsynaptic['ALNR'] = 0
        postsynaptic['AQR'] = 0
        postsynaptic['AS1'] = 0
        postsynaptic['AS10'] = 0
        postsynaptic['AS11'] = 0
        postsynaptic['AS2'] = 0
        postsynaptic['AS3'] = 0
        postsynaptic['AS4'] = 0
        postsynaptic['AS5'] = 0
        postsynaptic['AS6'] = 0
        postsynaptic['AS7'] = 0
        postsynaptic['AS8'] = 0
        postsynaptic['AS9'] = 0
        postsynaptic['ASEL'] = 0
        postsynaptic['ASER'] = 0
        postsynaptic['ASGL'] = 0
        postsynaptic['ASGR'] = 0
        postsynaptic['ASHL'] = 0
        postsynaptic['ASHR'] = 0
        postsynaptic['ASIL'] = 0
        postsynaptic['ASIR'] = 0
        postsynaptic['ASJL'] = 0
        postsynaptic['ASJR'] = 0
        postsynaptic['ASKL'] = 0
        postsynaptic['ASKR'] = 0
        postsynaptic['AUAL'] = 0
        postsynaptic['AUAR'] = 0
        postsynaptic['AVAL'] = 0
        postsynaptic['AVAR'] = 0
        postsynaptic['AVBL'] = 0
        postsynaptic['AVBR'] = 0
        postsynaptic['AVDL'] = 0
        postsynaptic['AVDR'] = 0
        postsynaptic['AVEL'] = 0
        postsynaptic['AVER'] = 0
        postsynaptic['AVFL'] = 0
        postsynaptic['AVFR'] = 0
        postsynaptic['AVG'] = 0
        postsynaptic['AVHL'] = 0
        postsynaptic['AVHR'] = 0
        postsynaptic['AVJL'] = 0
        postsynaptic['AVJR'] = 0
        postsynaptic['AVKL'] = 0
        postsynaptic['AVKR'] = 0
        postsynaptic['AVL'] = 0
        postsynaptic['AVM'] = 0
        postsynaptic['AWAL'] = 0
        postsynaptic['AWAR'] = 0
        postsynaptic['AWBL'] = 0
        postsynaptic['AWBR'] = 0
        postsynaptic['AWCL'] = 0
        postsynaptic['AWCR'] = 0
        postsynaptic['BAGL'] = 0
        postsynaptic['BAGR'] = 0
        postsynaptic['BDUL'] = 0
        postsynaptic['BDUR'] = 0
        postsynaptic['CEPDL'] = 0
        postsynaptic['CEPDR'] = 0
        postsynaptic['CEPVL'] = 0
        postsynaptic['CEPVR'] = 0
        postsynaptic['DA1'] = 0
        postsynaptic['DA2'] = 0
        postsynaptic['DA3'] = 0
        postsynaptic['DA4'] = 0
        postsynaptic['DA5'] = 0
        postsynaptic['DA6'] = 0
        postsynaptic['DA7'] = 0
        postsynaptic['DA8'] = 0
        postsynaptic['DA9'] = 0
        postsynaptic['DB1'] = 0
        postsynaptic['DB2'] = 0
        postsynaptic['DB3'] = 0
        postsynaptic['DB4'] = 0
        postsynaptic['DB5'] = 0
        postsynaptic['DB6'] = 0
        postsynaptic['DB7'] = 0
        postsynaptic['DD1'] = 0
        postsynaptic['DD2'] = 0
        postsynaptic['DD3'] = 0
        postsynaptic['DD4'] = 0
        postsynaptic['DD5'] = 0
        postsynaptic['DD6'] = 0
        postsynaptic['DVA'] = 0
        postsynaptic['DVB'] = 0
        postsynaptic['DVC'] = 0
        postsynaptic['FLPL'] = 0
        postsynaptic['FLPR'] = 0
        postsynaptic['HSNL'] = 0
        postsynaptic['HSNR'] = 0
        postsynaptic['I1L'] = 0
        postsynaptic['I1R'] = 0
        postsynaptic['I2L'] = 0
        postsynaptic['I2R'] = 0
        postsynaptic['I3'] = 0
        postsynaptic['I4'] = 0
        postsynaptic['I5'] = 0
        postsynaptic['I6'] = 0
        postsynaptic['IL1DL'] = 0
        postsynaptic['IL1DR'] = 0
        postsynaptic['IL1L'] = 0
        postsynaptic['IL1R'] = 0
        postsynaptic['IL1VL'] = 0
        postsynaptic['IL1VR'] = 0
        postsynaptic['IL2L'] = 0
        postsynaptic['IL2R'] = 0
        postsynaptic['IL2DL'] = 0
        postsynaptic['IL2DR'] = 0
        postsynaptic['IL2VL'] = 0
        postsynaptic['IL2VR'] = 0
        postsynaptic['LUAL'] = 0
        postsynaptic['LUAR'] = 0
        postsynaptic['M1'] = 0
        postsynaptic['M2L'] = 0
        postsynaptic['M2R'] = 0
        postsynaptic['M3L'] = 0
        postsynaptic['M3R'] = 0
        postsynaptic['M4'] = 0
        postsynaptic['M5'] = 0
        postsynaptic['MANAL'] = 0
        postsynaptic['MCL'] = 0
        postsynaptic['MCR'] = 0
        postsynaptic['MDL01'] = 0
        postsynaptic['MDL02'] = 0
        postsynaptic['MDL03'] = 0
        postsynaptic['MDL04'] = 0
        postsynaptic['MDL05'] = 0
        postsynaptic['MDL06'] = 0
        postsynaptic['MDL07'] = 0
        postsynaptic['MDL08'] = 0
        postsynaptic['MDL09'] = 0
        postsynaptic['MDL10'] = 0
        postsynaptic['MDL11'] = 0
        postsynaptic['MDL12'] = 0
        postsynaptic['MDL13'] = 0
        postsynaptic['MDL14'] = 0
        postsynaptic['MDL15'] = 0
        postsynaptic['MDL16'] = 0
        postsynaptic['MDL17'] = 0
        postsynaptic['MDL18'] = 0
        postsynaptic['MDL19'] = 0
        postsynaptic['MDL20'] = 0
        postsynaptic['MDL21'] = 0
        postsynaptic['MDL22'] = 0
        postsynaptic['MDL23'] = 0
        postsynaptic['MDL24'] = 0
        postsynaptic['MDR01'] = 0
        postsynaptic['MDR02'] = 0
        postsynaptic['MDR03'] = 0
        postsynaptic['MDR04'] = 0
        postsynaptic['MDR05'] = 0
        postsynaptic['MDR06'] = 0
        postsynaptic['MDR07'] = 0
        postsynaptic['MDR08'] = 0
        postsynaptic['MDR09'] = 0
        postsynaptic['MDR10'] = 0
        postsynaptic['MDR11'] = 0
        postsynaptic['MDR12'] = 0
        postsynaptic['MDR13'] = 0
        postsynaptic['MDR14'] = 0
        postsynaptic['MDR15'] = 0
        postsynaptic['MDR16'] = 0
        postsynaptic['MDR17'] = 0
        postsynaptic['MDR18'] = 0
        postsynaptic['MDR19'] = 0
        postsynaptic['MDR20'] = 0
        postsynaptic['MDR21'] = 0
        postsynaptic['MDR22'] = 0
        postsynaptic['MDR23'] = 0
        postsynaptic['MDR24'] = 0
        postsynaptic['MI'] = 0
        postsynaptic['MVL01'] = 0
        postsynaptic['MVL02'] = 0
        postsynaptic['MVL03'] = 0
        postsynaptic['MVL04'] = 0
        postsynaptic['MVL05'] = 0
        postsynaptic['MVL06'] = 0
        postsynaptic['MVL07'] = 0
        postsynaptic['MVL08'] = 0
        postsynaptic['MVL09'] = 0
        postsynaptic['MVL10'] = 0
        postsynaptic['MVL11'] = 0
        postsynaptic['MVL12'] = 0
        postsynaptic['MVL13'] = 0
        postsynaptic['MVL14'] = 0
        postsynaptic['MVL15'] = 0
        postsynaptic['MVL16'] = 0
        postsynaptic['MVL17'] = 0
        postsynaptic['MVL18'] = 0
        postsynaptic['MVL19'] = 0
        postsynaptic['MVL20'] = 0
        postsynaptic['MVL21'] = 0
        postsynaptic['MVL22'] = 0
        postsynaptic['MVL23'] = 0
        postsynaptic['MVR01'] = 0
        postsynaptic['MVR02'] = 0
        postsynaptic['MVR03'] = 0
        postsynaptic['MVR04'] = 0
        postsynaptic['MVR05'] = 0
        postsynaptic['MVR06'] = 0
        postsynaptic['MVR07'] = 0
        postsynaptic['MVR08'] = 0
        postsynaptic['MVR09'] = 0
        postsynaptic['MVR10'] = 0
        postsynaptic['MVR11'] = 0
        postsynaptic['MVR12'] = 0
        postsynaptic['MVR13'] = 0
        postsynaptic['MVR14'] = 0
        postsynaptic['MVR15'] = 0
        postsynaptic['MVR16'] = 0
        postsynaptic['MVR17'] = 0
        postsynaptic['MVR18'] = 0
        postsynaptic['MVR19'] = 0
        postsynaptic['MVR20'] = 0
        postsynaptic['MVR21'] = 0
        postsynaptic['MVR22'] = 0
        postsynaptic['MVR23'] = 0
        postsynaptic['MVR24'] = 0
        postsynaptic['MVULVA'] = 0
        postsynaptic['NSML'] = 0
        postsynaptic['NSMR'] = 0
        postsynaptic['OLLL'] = 0
        postsynaptic['OLLR'] = 0
        postsynaptic['OLQDL'] = 0
        postsynaptic['OLQDR'] = 0
        postsynaptic['OLQVL'] = 0
        postsynaptic['OLQVR'] = 0
        postsynaptic['PDA'] = 0
        postsynaptic['PDB'] = 0
        postsynaptic['PDEL'] = 0
        postsynaptic['PDER'] = 0
        postsynaptic['PHAL'] = 0
        postsynaptic['PHAR'] = 0
        postsynaptic['PHBL'] = 0
        postsynaptic['PHBR'] = 0
        postsynaptic['PHCL'] = 0
        postsynaptic['PHCR'] = 0
        postsynaptic['PLML'] = 0
        postsynaptic['PLMR'] = 0
        postsynaptic['PLNL'] = 0
        postsynaptic['PLNR'] = 0
        postsynaptic['PQR'] = 0
        postsynaptic['PVCL'] = 0
        postsynaptic['PVCR'] = 0
        postsynaptic['PVDL'] = 0
        postsynaptic['PVDR'] = 0
        postsynaptic['PVM'] = 0
        postsynaptic['PVNL'] = 0
        postsynaptic['PVNR'] = 0
        postsynaptic['PVPL'] = 0
        postsynaptic['PVPR'] = 0
        postsynaptic['PVQL'] = 0
        postsynaptic['PVQR'] = 0
        postsynaptic['PVR'] = 0
        postsynaptic['PVT'] = 0
        postsynaptic['PVWL'] = 0
        postsynaptic['PVWR'] = 0
        postsynaptic['RIAL'] = 0
        postsynaptic['RIAR'] = 0
        postsynaptic['RIBL'] = 0
        postsynaptic['RIBR'] = 0
        postsynaptic['RICL'] = 0
        postsynaptic['RICR'] = 0
        postsynaptic['RID'] = 0
        postsynaptic['RIFL'] = 0
        postsynaptic['RIFR'] = 0
        postsynaptic['RIGL'] = 0
        postsynaptic['RIGR'] = 0
        postsynaptic['RIH'] = 0
        postsynaptic['RIML'] = 0
        postsynaptic['RIMR'] = 0
        postsynaptic['RIPL'] = 0
        postsynaptic['RIPR'] = 0
        postsynaptic['RIR'] = 0
        postsynaptic['RIS'] = 0
        postsynaptic['RIVL'] = 0
        postsynaptic['RIVR'] = 0
        postsynaptic['RMDDL'] = 0
        postsynaptic['RMDDR'] = 0
        postsynaptic['RMDL'] = 0
        postsynaptic['RMDR'] = 0
        postsynaptic['RMDVL'] = 0
        postsynaptic['RMDVR'] = 0
        postsynaptic['RMED'] = 0
        postsynaptic['RMEL'] = 0
        postsynaptic['RMER'] = 0
        postsynaptic['RMEV'] = 0
        postsynaptic['RMFL'] = 0
        postsynaptic['RMFR'] = 0
        postsynaptic['RMGL'] = 0
        postsynaptic['RMGR'] = 0
        postsynaptic['RMHL'] = 0
        postsynaptic['RMHR'] = 0
        postsynaptic['SAADL'] = 0
        postsynaptic['SAADR'] = 0
        postsynaptic['SAAVL'] = 0
        postsynaptic['SAAVR'] = 0
        postsynaptic['SABD'] = 0
        postsynaptic['SABVL'] = 0
        postsynaptic['SABVR'] = 0
        postsynaptic['SDQL'] = 0
        postsynaptic['SDQR'] = 0
        postsynaptic['SIADL'] = 0
        postsynaptic['SIADR'] = 0
        postsynaptic['SIAVL'] = 0
        postsynaptic['SIAVR'] = 0
        postsynaptic['SIBDL'] = 0
        postsynaptic['SIBDR'] = 0
        postsynaptic['SIBVL'] = 0
        postsynaptic['SIBVR'] = 0
        postsynaptic['SMBDL'] = 0
        postsynaptic['SMBDR'] = 0
        postsynaptic['SMBVL'] = 0
        postsynaptic['SMBVR'] = 0
        postsynaptic['SMDDL'] = 0
        postsynaptic['SMDDR'] = 0
        postsynaptic['SMDVL'] = 0
        postsynaptic['SMDVR'] = 0
        postsynaptic['URADL'] = 0
        postsynaptic['URADR'] = 0
        postsynaptic['URAVL'] = 0
        postsynaptic['URAVR'] = 0
        postsynaptic['URBL'] = 0
        postsynaptic['URBR'] = 0
        postsynaptic['URXL'] = 0
        postsynaptic['URXR'] = 0
        postsynaptic['URYDL'] = 0
        postsynaptic['URYDR'] = 0
        postsynaptic['URYVL'] = 0
        postsynaptic['URYVR'] = 0
        postsynaptic['VA1'] = 0
        postsynaptic['VA10'] = 0
        postsynaptic['VA11'] = 0
        postsynaptic['VA12'] = 0
        postsynaptic['VA2'] = 0
        postsynaptic['VA3'] = 0
        postsynaptic['VA4'] = 0
        postsynaptic['VA5'] = 0
        postsynaptic['VA6'] = 0
        postsynaptic['VA7'] = 0
        postsynaptic['VA8'] = 0
        postsynaptic['VA9'] = 0
        postsynaptic['VB1'] = 0
        postsynaptic['VB10'] = 0
        postsynaptic['VB11'] = 0
        postsynaptic['VB2'] = 0
        postsynaptic['VB3'] = 0
        postsynaptic['VB4'] = 0
        postsynaptic['VB5'] = 0
        postsynaptic['VB6'] = 0
        postsynaptic['VB7'] = 0
        postsynaptic['VB8'] = 0
        postsynaptic['VB9'] = 0
        postsynaptic['VC1'] = 0
        postsynaptic['VC2'] = 0
        postsynaptic['VC3'] = 0
        postsynaptic['VC4'] = 0
        postsynaptic['VC5'] = 0
        postsynaptic['VC6'] = 0
        postsynaptic['VD1'] = 0
        postsynaptic['VD10'] = 0
        postsynaptic['VD11'] = 0
        postsynaptic['VD12'] = 0
        postsynaptic['VD13'] = 0
        postsynaptic['VD2'] = 0
        postsynaptic['VD3'] = 0
        postsynaptic['VD4'] = 0
        postsynaptic['VD5'] = 0
        postsynaptic['VD6'] = 0
        postsynaptic['VD7'] = 0
        postsynaptic['VD8'] = 0
        postsynaptic['VD9'] = 0


def motorcontrol():
        global accumright
        global accumleft
        # accumulate left and right muscles and the accumulated values are
        # used to move the left and right motors of the robot
        for pscheck in postsynaptic:
                if pscheck in musDleft or pscheck in musVleft:
                   accumleft += postsynaptic[pscheck]
                   postsynaptic[pscheck] = 0
                elif pscheck in musDright or pscheck in musVright:
                   accumright += postsynaptic[pscheck]
                   postsynaptic[pscheck] = 0
        # We turn the wheels according to the motor weight accumulation
        new_speed = abs(accumleft) + abs(accumright)
        if new_speed > 150:
                new_speed = 150
        elif new_speed < 75:
                new_speed = 75
        print "Left: ", accumleft, "Right:", accumright, "Speed: ", new_speed
        ## Start Commented section
        set_speed(new_speed)
        if accumleft == 0 and accumright == 0:
                stop()
        elif accumright <= 0 and accumleft < 0:
                set_speed(150)
                turnratio = float(accumright) / float(accumleft)
                # print "Turn Ratio: ", turnratio
                if turnratio <= 0.6:
                         left_rot()
                         time.sleep(0.8)
                elif turnratio >= 2:
                         right_rot()
                         time.sleep(0.8)
                bwd()
                time.sleep(0.5)
        elif accumright <= 0 and accumleft >= 0:
                right_rot()
                time.sleep(.8)
        elif accumright >= 0 and accumleft <= 0:
                left_rot()
                time.sleep(.8)
        elif accumright >= 0 and accumleft > 0:
                turnratio = float(accumright) / float(accumleft)
                # print "Turn Ratio: ", turnratio
                if turnratio <= 0.6:
                         left_rot()
                         time.sleep(0.8)
                elif turnratio >= 2:
                         right_rot()
                         time.sleep(0.8)
                fwd()
                time.sleep(0.5)
        else:
                stop()
         ## End Commented section
        accumleft = 0
        accumright = 0
        time.sleep(0.5)


def dendriteAccumulate(dneuron):
        f = eval(dneuron)
        f()

def fireNeuron(fneuron):
        # The threshold has been exceeded and we fire the neurite
        if fneuron != "MVULVA":
                f = eval(fneuron)
                f()

def runconnectome():
        # Each time a set of neuron is stimulated, this method will execute
        # The weigted values are accumulated in the PostSynaptic array
        # Once the accumulation is read, we see what neurons are greater
        # then the threshold and fire the neuron or muscle that has exceeded
        # the threshold 
        for ps in postsynaptic:
                if ps[:3] not in muscles and abs(postsynaptic[ps]) > threshold:
                        fireNeuron(ps)
                        postsynaptic[ps] = 0
        motorcontrol()    
                         

# Create the dictionary      
createpostsynaptic()
dist=0
set_speed(120)
print "Voltage: ", volt()
tfood = 0
try:
### Here is where you would put in a method to stimulate the neurons ###
### We stimulate chemosensory neurons constantly unless nose touch   ###
### (sonar) is stimulated and then we fire nose touch neurites       ###
### Use CNTRL-C to stop the program
    while True:
        ## Start comment - use a fixed value if you want to stimulte nose touch
        ## use something like "dist = 27" if you want to stop nose stimulation
        dist = us_dist(15)
        ## End Comment
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
                    dendriteAccumulate("ADFL")
                    dendriteAccumulate("ADFR")
                    dendriteAccumulate("ASGR")
                    dendriteAccumulate("ASGL")
                    dendriteAccumulate("ASIL")
                    dendriteAccumulate("ASIR")
                    dendriteAccumulate("ASJR")
                    dendriteAccumulate("ASJL")
                    runconnectome()
                    time.sleep(0.5)
            tfood += 0.5
            if (tfood > 20):
                    tfood = 0
        

       
except KeyboardInterrupt:
    ## Start Comment
    stop()
    ## End Comment
    print "Ctrl+C detected. Program Stopped!"
    

