# GoPiGo Connectome
# Originally Written by Timothy Busbice, Gabriel Garrett, Geoffrey Churchill (c) 2015 in Python 2.7
# Modified by John Cole in 2019 to work with Python 3.x and the GoPiGo3
# The GoPiGo Connectome uses a Postsynaptic dictionary based on the C Elegans Connectome Model
# This application can be ran on the Raspberry Pi GoPiGo robot with a Sonar that represents Nose Touch when activated
# To run standalone without a GoPiGo robot, simply comment out the sections with Start and End comments 

###Experimental Optimization. Each accumulation is run inside of a function. If the function detects that the neuron
### exceeds the threshold for the next time state, that neuron is added to a list and used in the next loop of the program.
### Only the neurons in the list are read from the dictionary/fired, whereas before the whole dictionary was read in each iteration
### in order to find and fire the neurons exceeding the threshold.

## Start Comment
from easygopigo3 import EasyGoPiGo3 # importing the EasyGoPiGo3 class
gpg = EasyGoPiGo3() # instantiating a EasyGoPiGo3 object
my_distance_sensor = gpg.init_distance_sensor()
## End Comment
import time

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
nextNeurons = []

#incrementNeuron increments the next state of the neuron by this state's weight plus the weight increment.
# It then determines if the neuron exceeds the threshold in the next state. If it does, it is appended to a nextNeurons list,
# and the nextNeurons list is used to iterate through the dictionary to only read and fire the neurons that are supposed to fire.
def incrementNeuron(neuronName, weight):
        psn = postsynaptic[neuronName]
        global nextNeurons
        psn[nextState] = weight + psn[thisState]
        if psn[nextState] > threshold and not(psn[2]):   #2 represents the boolean column for if neuron already appended
                #print (postsynaptic[neuronName][2])
                #print neuronName
                nextNeurons.append(neuronName) #return neuronName #append to list here instead?
                psn[2] = True
        

def ADAL():
        incrementNeuron('ADAR',2)
        incrementNeuron('ADFL',1)
        incrementNeuron('AIBL',1)
        incrementNeuron('AIBR',2)
        incrementNeuron('ASHL',1)
        incrementNeuron('AVAR',2)
        incrementNeuron('AVBL',4)
        incrementNeuron('AVBR',7)
        incrementNeuron('AVDL',1)
        incrementNeuron('AVDR',2)
        incrementNeuron('AVEL',1)
        incrementNeuron('AVJR',5)
        incrementNeuron('FLPR',1)
        incrementNeuron('PVQL',1)
        incrementNeuron('RICL',1)
        incrementNeuron('RICR',1)
        incrementNeuron('RIML',3)
        incrementNeuron('RIPL',1)
        incrementNeuron('SMDVR',2)

def ADAR():
        incrementNeuron('ADAL',1)
        incrementNeuron('ADFR',1)
        incrementNeuron('AIBL',1)
        incrementNeuron('AIBR',1)
        incrementNeuron('ASHR',1)
        incrementNeuron('AVAL',1)
        incrementNeuron('AVBL',1)
        incrementNeuron('AVBR',5)
        incrementNeuron('AVDL',2)
        incrementNeuron('AVEL',1)
        incrementNeuron('AVJL',3)
        incrementNeuron('PVQR',1)
        incrementNeuron('RICL',1)
        incrementNeuron('RIMR',5)
        incrementNeuron('RIPR',1)
        incrementNeuron('RIVR',1)
        incrementNeuron('SMDVL',2)

def ADEL():
        incrementNeuron('ADAL',1)
        incrementNeuron('ADER',1)
        incrementNeuron('AINL',1)
        incrementNeuron('AVAL',2)
        incrementNeuron('AVAR',3)
        incrementNeuron('AVEL',1)
        incrementNeuron('AVKR',1)
        incrementNeuron('AVL',1)
        incrementNeuron('BDUL',1)
        incrementNeuron('CEPDL',1)
        incrementNeuron('FLPL',1)
        incrementNeuron('IL1L',1)
        incrementNeuron('IL2L',1)
        incrementNeuron('MDL05',1)
        incrementNeuron('OLLL',1)
        incrementNeuron('RIAL',1)
        incrementNeuron('RIFL',1)
        incrementNeuron('RIGL',5)
        incrementNeuron('RIGR',3)
        incrementNeuron('RIH',2)
        incrementNeuron('RIVL',1)
        incrementNeuron('RIVR',1)
        incrementNeuron('RMDL',2)
        incrementNeuron('RMGL',1)
        incrementNeuron('RMHL',1)
        incrementNeuron('SIADR',1)
        incrementNeuron('SIBDR',1)
        incrementNeuron('SMBDR',1)
        incrementNeuron('URBL',1)

def ADER():
        incrementNeuron('ADAR',1)
        incrementNeuron('ADEL',2)
        incrementNeuron('ALA',1)
        incrementNeuron('AVAL',5)
        incrementNeuron('AVAR',1)
        incrementNeuron('AVDR',2)
        incrementNeuron('AVER',1)
        incrementNeuron('AVJR',1)
        incrementNeuron('AVKL',2)
        incrementNeuron('AVKR',1)
        incrementNeuron('CEPDR',1)
        incrementNeuron('FLPL',1)
        incrementNeuron('FLPR',1)
        incrementNeuron('OLLR',2)
        incrementNeuron('PVR',1)
        incrementNeuron('RIGL',7)
        incrementNeuron('RIGR',4)
        incrementNeuron('RIH',1)
        incrementNeuron('RMDR',2)
        incrementNeuron('SAAVR',1)

def ADFL():
        incrementNeuron('ADAL',2)
        incrementNeuron('AIZL',12)
        incrementNeuron('AUAL',5)
        incrementNeuron('OLQVL',1)
        incrementNeuron('RIAL',15)
        incrementNeuron('RIGL',1)
        incrementNeuron('RIR',2)
        incrementNeuron('SMBVL',2)

def ADFR():
        incrementNeuron('ADAR',2)
        incrementNeuron('AIAR',1)
        incrementNeuron('AIYR',1)
        incrementNeuron('AIZR',8)
        incrementNeuron('ASHR',1)
        incrementNeuron('AUAR',4)
        incrementNeuron('AWBR',1)
        incrementNeuron('PVPR',1)
        incrementNeuron('RIAR',16)
        incrementNeuron('RIGR',3)
        incrementNeuron('RIR',3)
        incrementNeuron('SMBDR',1)
        incrementNeuron('SMBVR',2)
        incrementNeuron('URXR',1)

def ADLL():
        incrementNeuron('ADLR',1)
        incrementNeuron('AIAL',6)
        incrementNeuron('AIBL',7)
        incrementNeuron('AIBR',1)
        incrementNeuron('ALA',2)
        incrementNeuron('ASER',3)
        incrementNeuron('ASHL',2)
        incrementNeuron('AVAL',2)
        incrementNeuron('AVAR',3)
        incrementNeuron('AVBL',2)
        incrementNeuron('AVDL',1)
        incrementNeuron('AVDR',4)
        incrementNeuron('AVDR',1)
        incrementNeuron('AVJL',1)
        incrementNeuron('AVJR',3)
        incrementNeuron('AWBL',2)
        incrementNeuron('OLQVL',2)
        incrementNeuron('RIPL',1)
        incrementNeuron('RMGL',1)

def ADLR():
        incrementNeuron('ADLL',1)
        incrementNeuron('AIAR',10)
        incrementNeuron('AIBR',10)
        incrementNeuron('ASER',1)
        incrementNeuron('ASHR',3)
        incrementNeuron('AVAR',2)
        incrementNeuron('AVBL',1)
        incrementNeuron('AVBR',2)
        incrementNeuron('AVDL',5)
        incrementNeuron('AVDR',2)
        incrementNeuron('AVJR',1)
        incrementNeuron('AWCR',3)
        incrementNeuron('OLLR',1)
        incrementNeuron('PVCL',1)
        incrementNeuron('RICL',1)
        incrementNeuron('RICR',1)

def AFDL():
        incrementNeuron('AFDR',1)
        incrementNeuron('AIBL',1)
        incrementNeuron('AINR',1)
        incrementNeuron('AIYL',7)

def AFDR():
        incrementNeuron('AFDL',1)
        incrementNeuron('AIBR',1)
        incrementNeuron('AIYR',13)
        incrementNeuron('ASER',1)
                   
def AIAL():
        incrementNeuron('ADAL',1)
        incrementNeuron('AIAR',1)
        incrementNeuron('AIBL',10)
        incrementNeuron('AIML',2)
        incrementNeuron('AIZL',1)
        incrementNeuron('ASER',3)
        incrementNeuron('ASGL',1)
        incrementNeuron('ASHL',1)
        incrementNeuron('ASIL',2)
        incrementNeuron('ASKL',3)
        incrementNeuron('AWAL',1)
        incrementNeuron('AWCR',1)
        incrementNeuron('HSNL',1)
        incrementNeuron('RIFL',1)
        incrementNeuron('RMGL',1)

def AIAR():
        incrementNeuron('ADAR',1)
        incrementNeuron('ADFR',1)
        incrementNeuron('ADLR',2)
        incrementNeuron('AIAL',1)
        incrementNeuron('AIBR',14)
        incrementNeuron('AIZR',1)
        incrementNeuron('ASER',1)
        incrementNeuron('ASGR',1)
        incrementNeuron('ASIR',2)
        incrementNeuron('AWAR',2)
        incrementNeuron('AWCL',1)
        incrementNeuron('AWCR',3)
        incrementNeuron('RIFR',2)

def AIBL():
        incrementNeuron('AFDL',1)
        incrementNeuron('AIYL',1)
        incrementNeuron('ASER',1)
        incrementNeuron('AVAL',2)
        incrementNeuron('AVBL',5)
        incrementNeuron('DVC',1)
        incrementNeuron('FLPL',1)
        incrementNeuron('PVT',1)
        incrementNeuron('RIBR',4)
        incrementNeuron('RIFL',1)
        incrementNeuron('RIGR',1)
        incrementNeuron('RIGR',3)
        incrementNeuron('RIML',2)
        incrementNeuron('RIMR',13)
        incrementNeuron('RIMR',1)
        incrementNeuron('RIVL',1)
        incrementNeuron('SAADL',2)
        incrementNeuron('SAADR',2)
        incrementNeuron('SMDDR',4)

def AIBR():
        incrementNeuron('AFDR',1)
        incrementNeuron('AVAR',1)
        incrementNeuron('AVBR',3)
        incrementNeuron('AVEL',1)
        incrementNeuron('DB1',1)
        incrementNeuron('DVC',2)
        incrementNeuron('PVT',1)
        incrementNeuron('RIAL',1)
        incrementNeuron('RIBL',4)
        incrementNeuron('RIGL',3)
        incrementNeuron('RIML',16)
        incrementNeuron('RIML',1)
        incrementNeuron('RIMR',1)
        incrementNeuron('RIS',1)
        incrementNeuron('RIVR',1)
        incrementNeuron('SAADL',1)
        incrementNeuron('SMDDL',3)
        incrementNeuron('SMDVL',1)
        incrementNeuron('VB1',3)

def AIML():
        incrementNeuron('AIAL',5)
        incrementNeuron('ALML',1)
        incrementNeuron('ASGL',2)
        incrementNeuron('ASKL',2)
        incrementNeuron('AVBR',2)
        incrementNeuron('AVDL',1)
        incrementNeuron('AVDR',1)
        incrementNeuron('AVER',1)
        incrementNeuron('AVFL',4)
        incrementNeuron('AVFR',1)
        incrementNeuron('AVHL',2)
        incrementNeuron('AVHR',1)
        incrementNeuron('AVJL',1)
        incrementNeuron('PVQL',1)
        incrementNeuron('RIFL',1)
        incrementNeuron('SIBDR',1)
        incrementNeuron('SMBVL',1)

def AIMR():
        incrementNeuron('AIAR',5)
        incrementNeuron('ASGR',2)
        incrementNeuron('ASJR',2)
        incrementNeuron('ASKR',3)
        incrementNeuron('AVDR',1)
        incrementNeuron('AVFL',1)
        incrementNeuron('AVFR',1)
        incrementNeuron('HSNL',1)
        incrementNeuron('HSNR',2)
        incrementNeuron('OLQDR',1)
        incrementNeuron('PVNR',1)
        incrementNeuron('RIFR',1)
        incrementNeuron('RMGR',1)

def AINL():
        incrementNeuron('ADEL',1)
        incrementNeuron('AFDR',5)
        incrementNeuron('AINR',2)
        incrementNeuron('ASEL',3)
        incrementNeuron('ASGR',2)
        incrementNeuron('AUAR',2)
        incrementNeuron('BAGL',3)
        incrementNeuron('RIBL',1)
        incrementNeuron('RIBR',2)

def AINR():
        incrementNeuron('AFDL',4)
        incrementNeuron('AFDR',1)
        incrementNeuron('AIAL',2)
        incrementNeuron('AIBL',2)
        incrementNeuron('AINL',2)
        incrementNeuron('ASEL',1)
        incrementNeuron('ASER',1)
        incrementNeuron('ASGL',1)
        incrementNeuron('AUAL',1)
        incrementNeuron('AUAR',1)
        incrementNeuron('BAGR',3)
        incrementNeuron('RIBL',2)
        incrementNeuron('RID',1)

def AIYL():
        incrementNeuron('AIYR',1)
        incrementNeuron('AIZL',13)
        incrementNeuron('AWAL',3)
        incrementNeuron('AWCL',1)
        incrementNeuron('AWCR',1)
        incrementNeuron('HSNR',1)
        incrementNeuron('RIAL',7)
        incrementNeuron('RIBL',4)
        incrementNeuron('RIML',1)

def AIYR():
        incrementNeuron('ADFR',1)
        incrementNeuron('AIYL',1)
        incrementNeuron('AIZR',8)
        incrementNeuron('AWAR',1)
        incrementNeuron('HSNL',1)
        incrementNeuron('RIAR',6)
        incrementNeuron('RIBR',2)
        incrementNeuron('RIMR',1)

def AIZL():
        incrementNeuron('AIAL',3)
        incrementNeuron('AIBL',2)
        incrementNeuron('AIBR',8)
        incrementNeuron('AIZR',2)
        incrementNeuron('ASEL',1)
        incrementNeuron('ASGL',1)
        incrementNeuron('ASHL',1)
        incrementNeuron('AVER',5)
        incrementNeuron('DVA',1)
        incrementNeuron('RIAL',8)
        incrementNeuron('RIGL',1)
        incrementNeuron('RIML',4)
        incrementNeuron('SMBDL',9)
        incrementNeuron('SMBVL',7)
        incrementNeuron('VB2',1)

def AIZR():
        incrementNeuron('AIAR',1)
        incrementNeuron('AIBL',8)
        incrementNeuron('AIBR',1)
        incrementNeuron('AIZL',2)
        incrementNeuron('ASGR',1)
        incrementNeuron('ASHR',1)
        incrementNeuron('AVEL',4)
        incrementNeuron('AVER',1)
        incrementNeuron('AWAR',1)
        incrementNeuron('DVA',1)
        incrementNeuron('RIAR',7)
        incrementNeuron('RIMR',4)
        incrementNeuron('SMBDR',5)
        incrementNeuron('SMBVR',3)
        incrementNeuron('SMDDR',1)

def ALA():
        incrementNeuron('ADEL',1)
        incrementNeuron('AVAL',1)
        incrementNeuron('AVEL',2)
        incrementNeuron('AVER',1)
        incrementNeuron('RID',1)
        incrementNeuron('RMDR',1)

def ALML():
        incrementNeuron('AVDR',1)
        incrementNeuron('AVEL',1)
        incrementNeuron('AVM',1)
        incrementNeuron('BDUL',6)
        incrementNeuron('CEPDL',3)
        incrementNeuron('CEPVL',2)
        incrementNeuron('PVCL',2)
        incrementNeuron('PVCR',1)
        incrementNeuron('PVR',1)
        incrementNeuron('RMDDR',1)
        incrementNeuron('RMGL',1)
        incrementNeuron('SDQL',1)

def ALMR():
        incrementNeuron('AVM',1)
        incrementNeuron('BDUR',5)
        incrementNeuron('CEPDR',1)
        incrementNeuron('CEPVR',1)
        incrementNeuron('PVCR',3)
        incrementNeuron('RMDDL',1)
        incrementNeuron('SIADL',1)

def ALNL():
        incrementNeuron('SAAVL',3)
        incrementNeuron('SMBDR',2)
        incrementNeuron('SMBDR',1)
        incrementNeuron('SMDVL',1)

def ALNR():
        incrementNeuron('ADER',1)
        incrementNeuron('RMHR',1)
        incrementNeuron('SAAVR',2)
        incrementNeuron('SMBDL',2)
        incrementNeuron('SMDDR',1)
        incrementNeuron('SMDVL',1)

def AQR():
        incrementNeuron('AVAL',1)
        incrementNeuron('AVAR',3)
        incrementNeuron('AVBL',3)
        incrementNeuron('AVBL',1)
        incrementNeuron('AVBR',4)
        incrementNeuron('AVDL',1)
        incrementNeuron('AVDR',1)
        incrementNeuron('AVJL',1)
        incrementNeuron('AVKL',2)
        incrementNeuron('AVKR',1)
        incrementNeuron('BAGL',2)
        incrementNeuron('BAGR',2)
        incrementNeuron('PVCR',2)
        incrementNeuron('PVPL',1)
        incrementNeuron('PVPL',7)
        incrementNeuron('PVPR',9)
        incrementNeuron('RIAL',3)
        incrementNeuron('RIAR',1)
        incrementNeuron('RIGL',2)
        incrementNeuron('RIGR',1)
        incrementNeuron('URXL',1)

def AS1():
        incrementNeuron('AVAL',3)
        incrementNeuron('AVAR',2)
        incrementNeuron('DA1',2)
        incrementNeuron('MDL05',3)
        incrementNeuron('MDL08',3)
        incrementNeuron('MDR05',3)
        incrementNeuron('MDR08',4)
        incrementNeuron('VA3',1)
        incrementNeuron('VD1',5)
        incrementNeuron('VD2',1)

def AS2():
        incrementNeuron('DA2',1)
        incrementNeuron('DB1',1)
        incrementNeuron('DD1',1)
        incrementNeuron('MDL07',3)
        incrementNeuron('MDL08',2)
        incrementNeuron('MDR07',3)
        incrementNeuron('MDR08',3)
        incrementNeuron('VA4',2)
        incrementNeuron('VD2',10)

def AS3():
        incrementNeuron('AVAL',2)
        incrementNeuron('AVAR',1)
        incrementNeuron('DA2',1)
        incrementNeuron('DA3',1)
        incrementNeuron('DD1',1)
        incrementNeuron('MDL09',3)
        incrementNeuron('MDL10',3)
        incrementNeuron('MDR09',3)
        incrementNeuron('MDR10',3)
        incrementNeuron('VA5',2)
        incrementNeuron('VD2',1)
        incrementNeuron('VD3',15)

def AS4():
        incrementNeuron('AS5',1)
        incrementNeuron('DA3',1)
        incrementNeuron('MDL11',2)
        incrementNeuron('MDL12',2)
        incrementNeuron('MDR11',3)
        incrementNeuron('MDR12',2)
        incrementNeuron('VD4',11)

def AS5():
        incrementNeuron('AVAL',1)
        incrementNeuron('AVAR',1)
        incrementNeuron('DD2',1)
        incrementNeuron('MDL11',2)
        incrementNeuron('MDL14',3)
        incrementNeuron('MDR11',2)
        incrementNeuron('MDR14',3)
        incrementNeuron('VA7',1)
        incrementNeuron('VD5',9)

def AS6():
        incrementNeuron('AVAL',1)
        incrementNeuron('AVAR',1)
        incrementNeuron('AVBR',1)
        incrementNeuron('DA5',2)
        incrementNeuron('MDL13',3)
        incrementNeuron('MDL14',2)
        incrementNeuron('MDR13',3)
        incrementNeuron('MDR14',2)
        incrementNeuron('VA8',1)
        incrementNeuron('VD6',13)

def AS7():
        incrementNeuron('AVAL',6)
        incrementNeuron('AVAR',5)
        incrementNeuron('AVBL',2)
        incrementNeuron('AVBR',2)
        incrementNeuron('MDL13',2)
        incrementNeuron('MDL16',3)
        incrementNeuron('MDR13',2)
        incrementNeuron('MDR16',3)

def AS8():
        incrementNeuron('AVAL',4)
        incrementNeuron('AVAR',3)
        incrementNeuron('MDL15',2)
        incrementNeuron('MDL18',3)
        incrementNeuron('MDR15',2)
        incrementNeuron('MDR18',3)

def AS9():
        incrementNeuron('AVAL',4)
        incrementNeuron('AVAR',2)
        incrementNeuron('DVB',7)
        incrementNeuron('MDL17',2)
        incrementNeuron('MDL20',3)
        incrementNeuron('MDR17',2)
        incrementNeuron('MDR20',3)

def AS10():
        incrementNeuron('AVAL',1)
        incrementNeuron('AVAR',1)
        incrementNeuron('MDL19',3)
        incrementNeuron('MDL20',2)
        incrementNeuron('MDR19',3)
        incrementNeuron('MDR20',2)

def AS11():
        incrementNeuron('MDL21',1)
        incrementNeuron('MDL22',1)
        incrementNeuron('MDL23',1)
        incrementNeuron('MDL24',1)
        incrementNeuron('MDR21',1)
        incrementNeuron('MDR22',1)
        incrementNeuron('MDR23',1)
        incrementNeuron('MDR24',1)
        incrementNeuron('PDA',1)
        incrementNeuron('PDB',1)
        incrementNeuron('PDB',2)
        incrementNeuron('VD13',2)

def ASEL():
        incrementNeuron('ADFR',1)
        incrementNeuron('AIAL',3)
        incrementNeuron('AIBL',7)
        incrementNeuron('AIBR',2)
        incrementNeuron('AIYL',13)
        incrementNeuron('AIYR',6)
        incrementNeuron('AWCL',4)
        incrementNeuron('AWCR',1)
        incrementNeuron('RIAR',1)

def ASER():
        incrementNeuron('AFDL',1)
        incrementNeuron('AFDR',2)
        incrementNeuron('AIAL',1)
        incrementNeuron('AIAR',3)
        incrementNeuron('AIBL',2)
        incrementNeuron('AIBR',10)
        incrementNeuron('AIYL',2)
        incrementNeuron('AIYR',14)
        incrementNeuron('AWAR',1)
        incrementNeuron('AWCL',1)
        incrementNeuron('AWCR',1)

def ASGL():
        incrementNeuron('AIAL',9)
        incrementNeuron('AIBL',3)
        incrementNeuron('AINR',2)
        incrementNeuron('AIZL',1)
        incrementNeuron('ASKL',1)

def ASGR():
        incrementNeuron('AIAR',10)
        incrementNeuron('AIBR',2)
        incrementNeuron('AINL',1)
        incrementNeuron('AIYR',1)
        incrementNeuron('AIZR',1)

def ASHL():
        incrementNeuron('ADAL',2)
        incrementNeuron('ADFL',3)
        incrementNeuron('AIAL',7)
        incrementNeuron('AIBL',5)
        incrementNeuron('AIZL',1)
        incrementNeuron('ASHR',1)
        incrementNeuron('ASKL',1)
        incrementNeuron('AVAL',2)
        incrementNeuron('AVBL',6)
        incrementNeuron('AVDL',2)
        incrementNeuron('AVDR',2)
        incrementNeuron('RIAL',4)
        incrementNeuron('RICL',2)
        incrementNeuron('RIML',1)
        incrementNeuron('RIPL',1)
        incrementNeuron('RMGL',1)

def ASHR():
        incrementNeuron('ADAR',3)
        incrementNeuron('ADFR',2)
        incrementNeuron('AIAR',10)
        incrementNeuron('AIBR',3)
        incrementNeuron('AIZR',1)
        incrementNeuron('ASHL',1)
        incrementNeuron('ASKR',1)
        incrementNeuron('AVAR',5)
        incrementNeuron('AVBR',3)
        incrementNeuron('AVDL',5)
        incrementNeuron('AVDR',1)
        incrementNeuron('AVER',3)
        incrementNeuron('HSNR',1)
        incrementNeuron('PVPR',1)
        incrementNeuron('RIAR',2)
        incrementNeuron('RICR',2)
        incrementNeuron('RMGR',2)
        incrementNeuron('RMGR',1)

def ASIL():
        incrementNeuron('AIAL',2)
        incrementNeuron('AIBL',1)
        incrementNeuron('AIYL',2)
        incrementNeuron('AIZL',1)
        incrementNeuron('ASER',1)
        incrementNeuron('ASIR',1)
        incrementNeuron('ASKL',2)
        incrementNeuron('AWCL',1)
        incrementNeuron('AWCR',1)
        incrementNeuron('RIBL',1)

def ASIR():
        incrementNeuron('AIAL',1)
        incrementNeuron('AIAR',3)
        incrementNeuron('AIAR',2)
        incrementNeuron('AIBR',1)
        incrementNeuron('ASEL',2)
        incrementNeuron('ASHR',1)
        incrementNeuron('ASIL',1)
        incrementNeuron('AWCL',1)
        incrementNeuron('AWCR',1)

def ASJL():
        incrementNeuron('ASJR',1)
        incrementNeuron('ASKL',4)
        incrementNeuron('HSNL',1)
        incrementNeuron('HSNR',1)
        incrementNeuron('PVQL',14)

def ASJR():
        incrementNeuron('ASJL',1)
        incrementNeuron('ASKR',4)
        incrementNeuron('HSNR',1)
        incrementNeuron('PVQR',13)

def ASKL():
        incrementNeuron('AIAL',11)
        incrementNeuron('AIBL',2)
        incrementNeuron('AIML',2)
        incrementNeuron('ASKR',1)
        incrementNeuron('PVQL',5)
        incrementNeuron('RMGL',1)

def ASKR():
        incrementNeuron('AIAR',11)
        incrementNeuron('AIMR',1)
        incrementNeuron('ASHR',1)
        incrementNeuron('ASKL',1)
        incrementNeuron('AWAR',1)
        incrementNeuron('CEPVR',1)
        incrementNeuron('PVQR',4)
        incrementNeuron('RIFR',1)
        incrementNeuron('RMGR',1)

def AUAL():
        incrementNeuron('AINR',1)
        incrementNeuron('AUAR',1)
        incrementNeuron('AVAL',3)
        incrementNeuron('AVDR',1)
        incrementNeuron('AVEL',3)
        incrementNeuron('AWBL',1)
        incrementNeuron('RIAL',5)
        incrementNeuron('RIBL',9)

def AUAR():
        incrementNeuron('AINL',1)
        incrementNeuron('AIYR',1)
        incrementNeuron('AUAL',1)
        incrementNeuron('AVAR',1)
        incrementNeuron('AVER',4)
        incrementNeuron('AWBR',1)
        incrementNeuron('RIAR',6)
        incrementNeuron('RIBR',13)
        incrementNeuron('URXR',1)

def AVAL():
        incrementNeuron('AS1',3)
        incrementNeuron('AS10',3)
        incrementNeuron('AS11',4)
        incrementNeuron('AS2',1)
        incrementNeuron('AS3',3)
        incrementNeuron('AS4',1)
        incrementNeuron('AS5',4)
        incrementNeuron('AS6',1)
        incrementNeuron('AS7',14)
        incrementNeuron('AS8',9)
        incrementNeuron('AS9',12)
        incrementNeuron('AVAR',7)
        incrementNeuron('AVBR',1)
        incrementNeuron('AVDL',1)
        incrementNeuron('AVHL',1)
        incrementNeuron('AVJL',2)
        incrementNeuron('DA1',4)
        incrementNeuron('DA2',4)
        incrementNeuron('DA3',6)
        incrementNeuron('DA4',10)
        incrementNeuron('DA5',8)
        incrementNeuron('DA6',21)
        incrementNeuron('DA7',4)
        incrementNeuron('DA8',4)
        incrementNeuron('DA9',3)
        incrementNeuron('DB5',2)
        incrementNeuron('DB6',4)
        incrementNeuron('FLPL',1)
        incrementNeuron('LUAL',2)
        incrementNeuron('PVCL',12)
        incrementNeuron('PVCR',11)
        incrementNeuron('PVPL',1)
        incrementNeuron('RIMR',3)
        incrementNeuron('SABD',4)
        incrementNeuron('SABVR',1)
        incrementNeuron('SDQR',1)
        incrementNeuron('URYDL',1)
        incrementNeuron('URYVR',1)
        incrementNeuron('VA1',3)
        incrementNeuron('VA10',6)
        incrementNeuron('VA11',7)
        incrementNeuron('VA12',2)
        incrementNeuron('VA2',5)
        incrementNeuron('VA3',3)
        incrementNeuron('VA4',3)
        incrementNeuron('VA5',8)
        incrementNeuron('VA6',10)
        incrementNeuron('VA7',2)
        incrementNeuron('VA8',19)
        incrementNeuron('VA9',8)
        incrementNeuron('VB9',5)

def AVAR():
        incrementNeuron('ADER',1)
        incrementNeuron('AS1',3)
        incrementNeuron('AS10',2)
        incrementNeuron('AS11',6)
        incrementNeuron('AS2',2)
        incrementNeuron('AS3',2)
        incrementNeuron('AS4',1)
        incrementNeuron('AS5',2)
        incrementNeuron('AS6',3)
        incrementNeuron('AS7',8)
        incrementNeuron('AS8',9)
        incrementNeuron('AS9',6)
        incrementNeuron('AVAL',6)
        incrementNeuron('AVBL',1)
        incrementNeuron('AVDL',1)
        incrementNeuron('AVDR',2)
        incrementNeuron('AVEL',2)
        incrementNeuron('AVER',2)
        incrementNeuron('DA1',8)
        incrementNeuron('DA2',4)
        incrementNeuron('DA3',5)
        incrementNeuron('DA4',8)
        incrementNeuron('DA5',7)
        incrementNeuron('DA6',13)
        incrementNeuron('DA7',3)
        incrementNeuron('DA8',9)
        incrementNeuron('DA9',2)
        incrementNeuron('DB3',1)
        incrementNeuron('DB5',3)
        incrementNeuron('DB6',5)
        incrementNeuron('LUAL',1)
        incrementNeuron('LUAR',3)
        incrementNeuron('PDEL',1)
        incrementNeuron('PDER',1)
        incrementNeuron('PVCL',7)
        incrementNeuron('PVCR',8)
        incrementNeuron('RIGL',1)
        incrementNeuron('RIML',2)
        incrementNeuron('RIMR',1)
        incrementNeuron('SABD',1)
        incrementNeuron('SABVL',6)
        incrementNeuron('SABVR',1)
        incrementNeuron('URYDR',1)
        incrementNeuron('URYVL',1)
        incrementNeuron('VA10',5)
        incrementNeuron('VA11',15)
        incrementNeuron('VA12',1)
        incrementNeuron('VA2',2)
        incrementNeuron('VA3',7)
        incrementNeuron('VA4',5)
        incrementNeuron('VA5',4)
        incrementNeuron('VA6',5)
        incrementNeuron('VA7',4)
        incrementNeuron('VA8',16)
        incrementNeuron('VB9',10)
        incrementNeuron('VD13',2)

def AVBL():
        incrementNeuron('AQR',1)
        incrementNeuron('AS10',1)
        incrementNeuron('AS3',1)
        incrementNeuron('AS4',1)
        incrementNeuron('AS5',1)
        incrementNeuron('AS6',1)
        incrementNeuron('AS7',2)
        incrementNeuron('AS9',1)
        incrementNeuron('AVAL',7)
        incrementNeuron('AVAR',7)
        incrementNeuron('AVBR',4)
        incrementNeuron('AVDL',1)
        incrementNeuron('AVDR',2)
        incrementNeuron('AVEL',1)
        incrementNeuron('AVER',2)
        incrementNeuron('AVL',1)
        incrementNeuron('DB3',1)
        incrementNeuron('DB4',1)
        incrementNeuron('DB5',1)
        incrementNeuron('DB6',2)
        incrementNeuron('DB7',2)
        incrementNeuron('DVA',1)
        incrementNeuron('PVNR',1)
        incrementNeuron('RIBL',1)
        incrementNeuron('RIBR',1)
        incrementNeuron('RID',1)
        incrementNeuron('SDQR',1)
        incrementNeuron('SIBVL',1)
        incrementNeuron('VA10',1)
        incrementNeuron('VA2',1)
        incrementNeuron('VA7',1)
        incrementNeuron('VB1',1)
        incrementNeuron('VB10',2)
        incrementNeuron('VB11',2)
        incrementNeuron('VB2',4)
        incrementNeuron('VB4',1)
        incrementNeuron('VB5',1)
        incrementNeuron('VB6',1)
        incrementNeuron('VB7',2)
        incrementNeuron('VB8',7)
        incrementNeuron('VB9',1)
        incrementNeuron('VC3',1)

def AVBR():
        incrementNeuron('AS1',1)
        incrementNeuron('AS10',1)
        incrementNeuron('AS3',1)
        incrementNeuron('AS4',1)
        incrementNeuron('AS5',1)
        incrementNeuron('AS6',2)
        incrementNeuron('AS7',3)
        incrementNeuron('AVAL',6)
        incrementNeuron('AVAR',7)
        incrementNeuron('AVBL',4)
        incrementNeuron('DA5',1)
        incrementNeuron('DB1',3)
        incrementNeuron('DB2',1)
        incrementNeuron('DB3',1)
        incrementNeuron('DB4',1)
        incrementNeuron('DB5',1)
        incrementNeuron('DB6',1)
        incrementNeuron('DB7',1)
        incrementNeuron('DD1',1)
        incrementNeuron('DVA',1)
        incrementNeuron('HSNR',1)
        incrementNeuron('PVNL',2)
        incrementNeuron('RIBL',1)
        incrementNeuron('RIBR',1)
        incrementNeuron('RID',2)
        incrementNeuron('SIBVL',1)
        incrementNeuron('VA4',1)
        incrementNeuron('VA8',1)
        incrementNeuron('VA9',2)
        incrementNeuron('VB10',1)
        incrementNeuron('VB11',1)
        incrementNeuron('VB2',1)
        incrementNeuron('VB3',1)
        incrementNeuron('VB4',1)
        incrementNeuron('VB6',2)
        incrementNeuron('VB7',2)
        incrementNeuron('VB8',3)
        incrementNeuron('VB9',6)
        incrementNeuron('VD10',1)
        incrementNeuron('VD3',1)

def AVDL():
        incrementNeuron('ADAR',2)
        incrementNeuron('AS1',1)
        incrementNeuron('AS10',1)
        incrementNeuron('AS11',2)
        incrementNeuron('AS4',1)
        incrementNeuron('AS5',1)
        incrementNeuron('AVAL',13)
        incrementNeuron('AVAR',19)
        incrementNeuron('AVM',2)
        incrementNeuron('DA1',1)
        incrementNeuron('DA2',1)
        incrementNeuron('DA3',4)
        incrementNeuron('DA4',1)
        incrementNeuron('DA5',1)
        incrementNeuron('DA8',1)
        incrementNeuron('FLPL',1)
        incrementNeuron('FLPR',1)
        incrementNeuron('LUAL',1)
        incrementNeuron('PVCL',1)
        incrementNeuron('SABD',1)
        incrementNeuron('SABVL',1)
        incrementNeuron('SABVR',1)
        incrementNeuron('VA5',1)

def AVDR():
        incrementNeuron('ADAL',2)
        incrementNeuron('ADLL',1)
        incrementNeuron('AS10',1)
        incrementNeuron('AS5',1)
        incrementNeuron('AVAL',16)
        incrementNeuron('AVAR',15)
        incrementNeuron('AVBL',1)
        incrementNeuron('AVDL',2)
        incrementNeuron('AVJL',2)
        incrementNeuron('DA1',2)
        incrementNeuron('DA2',1)
        incrementNeuron('DA3',1)
        incrementNeuron('DA4',1)
        incrementNeuron('DA5',2)
        incrementNeuron('DA8',1)
        incrementNeuron('DA9',1)
        incrementNeuron('DB4',1)
        incrementNeuron('DVC',1)
        incrementNeuron('FLPR',1)
        incrementNeuron('LUAL',2)
        incrementNeuron('PQR',1)
        incrementNeuron('SABD',1)
        incrementNeuron('SABVL',3)
        incrementNeuron('SABVR',1)
        incrementNeuron('VA11',1)
        incrementNeuron('VA2',1)
        incrementNeuron('VA3',2)
        incrementNeuron('VA6',1)

def AVEL():
        incrementNeuron('AS1',1)
        incrementNeuron('AVAL',12)
        incrementNeuron('AVAR',7)
        incrementNeuron('AVER',1)
        incrementNeuron('DA1',5)
        incrementNeuron('DA2',1)
        incrementNeuron('DA3',3)
        incrementNeuron('DA4',1)
        incrementNeuron('PVCR',1)
        incrementNeuron('PVT',1)
        incrementNeuron('RIML',2)
        incrementNeuron('RIMR',3)
        incrementNeuron('RMDVR',1)
        incrementNeuron('RMEV',1)
        incrementNeuron('SABD',6)
        incrementNeuron('SABVL',7)
        incrementNeuron('SABVR',3)
        incrementNeuron('VA1',5)
        incrementNeuron('VA3',3)
        incrementNeuron('VD2',1)
        incrementNeuron('VD3',1)

def AVER():
        incrementNeuron('AS1',3)
        incrementNeuron('AS2',2)
        incrementNeuron('AS3',1)
        incrementNeuron('AVAL',7)
        incrementNeuron('AVAR',16)
        incrementNeuron('AVDR',1)
        incrementNeuron('AVEL',1)
        incrementNeuron('DA1',5)
        incrementNeuron('DA2',3)
        incrementNeuron('DA3',1)
        incrementNeuron('DB3',1)
        incrementNeuron('RIML',3)
        incrementNeuron('RIMR',2)
        incrementNeuron('RMDVL',1)
        incrementNeuron('RMDVR',1)
        incrementNeuron('RMEV',1)
        incrementNeuron('SABD',2)
        incrementNeuron('SABVL',3)
        incrementNeuron('SABVR',3)
        incrementNeuron('VA1',1)
        incrementNeuron('VA2',1)
        incrementNeuron('VA3',2)
        incrementNeuron('VA4',1)
        incrementNeuron('VA5',1)

def AVFL():
        incrementNeuron('AVBL',1)
        incrementNeuron('AVBR',2)
        incrementNeuron('AVFR',30)
        incrementNeuron('AVG',1)
        incrementNeuron('AVHL',4)
        incrementNeuron('AVHR',7)
        incrementNeuron('AVJL',1)
        incrementNeuron('AVJR',1)
        incrementNeuron('AVL',1)
        incrementNeuron('HSNL',1)
        incrementNeuron('MVL11',1)
        incrementNeuron('MVL12',1)
        incrementNeuron('PDER',1)
        incrementNeuron('PVNL',2)
        incrementNeuron('PVQL',1)
        incrementNeuron('PVQR',2)
        incrementNeuron('VB1',1)

def AVFR():
        incrementNeuron('ASJL',1)
        incrementNeuron('ASKL',1)
        incrementNeuron('AVBL',1)
        incrementNeuron('AVBR',5)
        incrementNeuron('AVFL',24)
        incrementNeuron('AVHL',4)
        incrementNeuron('AVHR',2)
        incrementNeuron('AVJL',1)
        incrementNeuron('AVJR',1)
        incrementNeuron('HSNR',1)
        incrementNeuron('MVL14',2)
        incrementNeuron('MVR14',2)
        incrementNeuron('PVQL',1)
        incrementNeuron('VC4',1)
        incrementNeuron('VD11',1)

def AVG():
        incrementNeuron('AVAR',3)
        incrementNeuron('AVBL',1)
        incrementNeuron('AVBR',2)
        incrementNeuron('AVDR',1)
        incrementNeuron('AVEL',1)
        incrementNeuron('AVER',1)
        incrementNeuron('AVFL',1)
        incrementNeuron('AVJL',1)
        incrementNeuron('AVL',1)
        incrementNeuron('DA8',1)
        incrementNeuron('PHAL',2)
        incrementNeuron('PVCL',1)
        incrementNeuron('PVNR',1)
        incrementNeuron('PVPR',1)
        incrementNeuron('PVQR',1)
        incrementNeuron('PVT',1)
        incrementNeuron('RIFL',1)
        incrementNeuron('RIFR',1)
        incrementNeuron('VA11',1)

def AVHL():
        incrementNeuron('ADFR',3)
        incrementNeuron('AVBL',1)
        incrementNeuron('AVBR',1)
        incrementNeuron('AVDL',1)
        incrementNeuron('AVFL',1)
        incrementNeuron('AVFL',2)
        incrementNeuron('AVFR',5)
        incrementNeuron('AVHR',2)
        incrementNeuron('AVJL',1)
        incrementNeuron('AWBR',1)
        incrementNeuron('PHBR',1)
        incrementNeuron('PVPR',2)
        incrementNeuron('PVQL',1)
        incrementNeuron('PVQR',2)
        incrementNeuron('RIMR',1)
        incrementNeuron('RIR',3)
        incrementNeuron('SMBDR',1)
        incrementNeuron('SMBVR',1)
        incrementNeuron('VD1',1)

def AVHR():
        incrementNeuron('ADLL',1)
        incrementNeuron('ADLR',2)
        incrementNeuron('AQR',2)
        incrementNeuron('AVBL',2)
        incrementNeuron('AVBR',1)
        incrementNeuron('AVDR',1)
        incrementNeuron('AVFL',1)
        incrementNeuron('AVFR',2)
        incrementNeuron('AVHL',2)
        incrementNeuron('AVJR',4)
        incrementNeuron('PVNL',1)
        incrementNeuron('PVPL',3)
        incrementNeuron('RIGL',1)
        incrementNeuron('RIR',4)
        incrementNeuron('SMBDL',1)
        incrementNeuron('SMBVL',1)

def AVJL():
        incrementNeuron('AVAL',2)
        incrementNeuron('AVAR',1)
        incrementNeuron('AVBL',1)
        incrementNeuron('AVBR',4)
        incrementNeuron('AVDL',1)
        incrementNeuron('AVDR',2)
        incrementNeuron('AVEL',1)
        incrementNeuron('AVFR',1)
        incrementNeuron('AVHL',2)
        incrementNeuron('AVJR',4)
        incrementNeuron('HSNR',1)
        incrementNeuron('PLMR',2)
        incrementNeuron('PVCL',2)
        incrementNeuron('PVCR',5)
        incrementNeuron('PVNR',1)
        incrementNeuron('RIFR',1)
        incrementNeuron('RIS',2)

def AVJR():
        incrementNeuron('AVAL',1)
        incrementNeuron('AVAR',1)
        incrementNeuron('AVBL',3)
        incrementNeuron('AVBR',1)
        incrementNeuron('AVDL',1)
        incrementNeuron('AVDR',3)
        incrementNeuron('AVER',3)
        incrementNeuron('AVJL',5)
        incrementNeuron('PVCL',3)
        incrementNeuron('PVCR',4)
        incrementNeuron('PVQR',1)
        incrementNeuron('SABVL',1)

def AVKL():
        incrementNeuron('ADER',1)
        incrementNeuron('AQR',2)
        incrementNeuron('AVBL',1)
        incrementNeuron('AVEL',2)
        incrementNeuron('AVER',1)
        incrementNeuron('AVKR',2)
        incrementNeuron('AVM',1)
        incrementNeuron('DVA',1)
        incrementNeuron('PDEL',3)
        incrementNeuron('PDER',1)
        incrementNeuron('PVM',1)
        incrementNeuron('PVPL',1)
        incrementNeuron('PVPR',1)
        incrementNeuron('PVT',2)
        incrementNeuron('RICL',1)
        incrementNeuron('RICR',1)
        incrementNeuron('RIGL',1)
        incrementNeuron('RIML',2)
        incrementNeuron('RIMR',1)
        incrementNeuron('RMFR',1)
        incrementNeuron('SAADR',1)
        incrementNeuron('SIAVR',1)
        incrementNeuron('SMBDL',1)
        incrementNeuron('SMBDR',1)
        incrementNeuron('SMBVR',1)
        incrementNeuron('SMDDR',1)
        incrementNeuron('VB1',4)
        incrementNeuron('VB10',1)

def AVKR():
        incrementNeuron('ADEL',1)
        incrementNeuron('AQR',1)
        incrementNeuron('AVKL',2)
        incrementNeuron('BDUL',1)
        incrementNeuron('MVL10',1)
        incrementNeuron('PVPL',6)
        incrementNeuron('PVQL',1)
        incrementNeuron('RICL',1)
        incrementNeuron('RIGR',1)
        incrementNeuron('RIML',2)
        incrementNeuron('RIMR',2)
        incrementNeuron('RMDR',1)
        incrementNeuron('RMFL',1)
        incrementNeuron('SAADL',1)
        incrementNeuron('SMBDL',2)
        incrementNeuron('SMBDR',2)
        incrementNeuron('SMBVR',1)
        incrementNeuron('SMDDL',1)
        incrementNeuron('SMDDR',2)

def AVL():
        incrementNeuron('AVEL',1)
        incrementNeuron('AVFR',1)
        incrementNeuron('DA2',1)
        incrementNeuron('DD1',1)
        incrementNeuron('DD6',2)
        incrementNeuron('DVB',1)
        incrementNeuron('DVC',9)
        incrementNeuron('HSNR',1)
        incrementNeuron('MVL10',-5)
        incrementNeuron('MVR10',-5)
        incrementNeuron('PVM',1)
        incrementNeuron('PVPR',1)
        incrementNeuron('PVWL',1)
        incrementNeuron('SABD',5)
        incrementNeuron('SABVL',4)
        incrementNeuron('SABVR',3)
        incrementNeuron('VD12',4)

def AVM():
        incrementNeuron('ADER',1)
        incrementNeuron('ALML',1)
        incrementNeuron('ALMR',1)
        incrementNeuron('AVBL',6)
        incrementNeuron('AVBR',6)
        incrementNeuron('AVDL',2)
        incrementNeuron('AVJR',1)
        incrementNeuron('BDUL',3)
        incrementNeuron('BDUR',2)
        incrementNeuron('DA1',1)
        incrementNeuron('PVCL',4)
        incrementNeuron('PVCR',5)
        incrementNeuron('PVNL',1)
        incrementNeuron('PVR',3)
        incrementNeuron('RID',1)
        incrementNeuron('SIBVL',1)
        incrementNeuron('VA1',2)

def AWAL():
        incrementNeuron('ADAL',1)
        incrementNeuron('AFDL',5)
        incrementNeuron('AIAL',1)
        incrementNeuron('AIYL',1)
        incrementNeuron('AIZL',10)
        incrementNeuron('ASEL',4)
        incrementNeuron('ASGL',1)
        incrementNeuron('AWAR',1)
        incrementNeuron('AWBL',1)

def AWAR():
        incrementNeuron('ADFR',3)
        incrementNeuron('AFDR',7)
        incrementNeuron('AIAR',1)
        incrementNeuron('AIYR',2)
        incrementNeuron('AIZR',7)
        incrementNeuron('AIZR',1)
        incrementNeuron('ASEL',1)
        incrementNeuron('ASER',2)
        incrementNeuron('AUAR',1)
        incrementNeuron('AWAL',1)
        incrementNeuron('AWBR',1)
        incrementNeuron('RIFR',2)
        incrementNeuron('RIGR',1)
        incrementNeuron('RIR',2)

def AWBL():
        incrementNeuron('ADFL',9)
        incrementNeuron('AIBR',1)
        incrementNeuron('AIZL',9)
        incrementNeuron('AUAL',1)
        incrementNeuron('AVBL',1)
        incrementNeuron('AWBR',1)
        incrementNeuron('RIAL',3)
        incrementNeuron('RMGL',1)
        incrementNeuron('SMBDL',1)

def AWBR():
        incrementNeuron('ADFR',4)
        incrementNeuron('AIZR',4)
        incrementNeuron('ASGR',1)
        incrementNeuron('ASHR',2)
        incrementNeuron('AUAR',1)
        incrementNeuron('AVBR',2)
        incrementNeuron('AWBL',1)
        incrementNeuron('RIAR',1)
        incrementNeuron('RICL',1)
        incrementNeuron('RIR',2)
        incrementNeuron('RMGR',1)
        incrementNeuron('SMBVR',1)

def AWCL():
        incrementNeuron('AIAL',2)
        incrementNeuron('AIAR',4)
        incrementNeuron('AIBL',1)
        incrementNeuron('AIBR',1)
        incrementNeuron('AIYL',10)
        incrementNeuron('ASEL',1)
        incrementNeuron('AVAL',1)
        incrementNeuron('AWCR',1)
        incrementNeuron('RIAL',3)

def AWCR():
        incrementNeuron('AIAR',1)
        incrementNeuron('AIBR',4)
        incrementNeuron('AIYL',4)
        incrementNeuron('AIYR',9)
        incrementNeuron('ASEL',1)
        incrementNeuron('ASGR',1)
        incrementNeuron('AWCL',5)

def BAGL():
        incrementNeuron('AIBL',1)
        incrementNeuron('AVAR',1)
        incrementNeuron('AVEL',1)
        incrementNeuron('AVER',4)
        incrementNeuron('BAGR',2)
        incrementNeuron('RIAR',5)
        incrementNeuron('RIBL',1)
        incrementNeuron('RIBR',7)
        incrementNeuron('RIGL',1)
        incrementNeuron('RIGR',4)
        incrementNeuron('RIGR',1)
        incrementNeuron('RIR',1)

def BAGR():
        incrementNeuron('AIYL',1)
        incrementNeuron('AVAL',1)
        incrementNeuron('AVEL',2)
        incrementNeuron('BAGL',1)
        incrementNeuron('RIAL',5)
        incrementNeuron('RIBL',4)
        incrementNeuron('RIGL',5)
        incrementNeuron('RIGL',1)
        incrementNeuron('RIR',1)

def BDUL():
        incrementNeuron('ADEL',3)
        incrementNeuron('AVHL',1)
        incrementNeuron('AVJR',1)
        incrementNeuron('HSNL',1)
        incrementNeuron('PVNL',2)
        incrementNeuron('PVNR',2)
        incrementNeuron('SAADL',1)
        incrementNeuron('URADL',1)

def BDUR():
        incrementNeuron('ADER',1)
        incrementNeuron('ALMR',1)
        incrementNeuron('AVAL',3)
        incrementNeuron('AVHL',1)
        incrementNeuron('AVJL',2)
        incrementNeuron('HSNR',4)
        incrementNeuron('PVCL',1)
        incrementNeuron('PVNL',2)
        incrementNeuron('PVNR',1)
        incrementNeuron('SDQL',1)
        incrementNeuron('URADR',1)

def CEPDL():
        incrementNeuron('AVER',5)
        incrementNeuron('IL1DL',4)
        incrementNeuron('OLLL',2)
        incrementNeuron('OLQDL',6)
        incrementNeuron('OLQDL',1)
        incrementNeuron('RIBL',2)
        incrementNeuron('RICL',1)
        incrementNeuron('RICR',2)
        incrementNeuron('RIH',1)
        incrementNeuron('RIPL',2)
        incrementNeuron('RIS',1)
        incrementNeuron('RMDVL',3)
        incrementNeuron('RMGL',4)
        incrementNeuron('RMHR',4)
        incrementNeuron('SIADR',1)
        incrementNeuron('SMBDR',1)
        incrementNeuron('URADL',2)
        incrementNeuron('URBL',4)
        incrementNeuron('URYDL',2)

def CEPDR():
        incrementNeuron('AVEL',6)
        incrementNeuron('BDUR',1)
        incrementNeuron('IL1DR',5)
        incrementNeuron('IL1R',1)
        incrementNeuron('OLLR',8)
        incrementNeuron('OLQDR',5)
        incrementNeuron('OLQDR',2)
        incrementNeuron('RIBR',1)
        incrementNeuron('RICL',4)
        incrementNeuron('RICR',3)
        incrementNeuron('RIH',1)
        incrementNeuron('RIS',1)
        incrementNeuron('RMDDL',1)
        incrementNeuron('RMDVR',2)
        incrementNeuron('RMGR',1)
        incrementNeuron('RMHL',4)
        incrementNeuron('RMHR',1)
        incrementNeuron('SIADL',1)
        incrementNeuron('SMBDR',1)
        incrementNeuron('URADR',1)
        incrementNeuron('URBR',2)
        incrementNeuron('URYDR',1)

def CEPVL():
        incrementNeuron('ADLL',1)
        incrementNeuron('AVER',3)
        incrementNeuron('IL1VL',2)
        incrementNeuron('MVL03',1)
        incrementNeuron('OLLL',4)
        incrementNeuron('OLQVL',6)
        incrementNeuron('OLQVL',1)
        incrementNeuron('RICL',7)
        incrementNeuron('RICR',4)
        incrementNeuron('RIH',1)
        incrementNeuron('RIPL',1)
        incrementNeuron('RMDDL',4)
        incrementNeuron('RMHL',1)
        incrementNeuron('SIAVL',1)
        incrementNeuron('URAVL',2)

def CEPVR():
        incrementNeuron('ASGR',1)
        incrementNeuron('AVEL',5)
        incrementNeuron('IL1VR',1)
        incrementNeuron('IL2VR',2)
        incrementNeuron('MVR04',1)
        incrementNeuron('OLLR',7)
        incrementNeuron('OLQVR',3)
        incrementNeuron('OLQVR',1)
        incrementNeuron('RICL',2)
        incrementNeuron('RICR',2)
        incrementNeuron('RIH',1)
        incrementNeuron('RIPR',1)
        incrementNeuron('RIVL',1)
        incrementNeuron('RMDDR',2)
        incrementNeuron('RMHR',2)
        incrementNeuron('SIAVR',2)
        incrementNeuron('URAVR',1)

def DA1():
        incrementNeuron('AVAL',2)
        incrementNeuron('AVAR',6)
        incrementNeuron('DA4',1)
        incrementNeuron('DD1',4)
        incrementNeuron('MDL08',8)
        incrementNeuron('MDR08',8)
        incrementNeuron('SABVL',2)
        incrementNeuron('SABVR',3)
        incrementNeuron('VD1',17)
        incrementNeuron('VD2',1)

def DA2():
        incrementNeuron('AS2',2)
        incrementNeuron('AS3',1)
        incrementNeuron('AVAL',2)
        incrementNeuron('AVAR',2)
        incrementNeuron('DD1',1)
        incrementNeuron('MDL07',2)
        incrementNeuron('MDL08',1)
        incrementNeuron('MDL09',2)
        incrementNeuron('MDL10',2)
        incrementNeuron('MDR07',2)
        incrementNeuron('MDR08',2)
        incrementNeuron('MDR09',2)
        incrementNeuron('MDR10',2)
        incrementNeuron('SABVL',1)
        incrementNeuron('VA1',2)
        incrementNeuron('VD1',2)
        incrementNeuron('VD2',11)
        incrementNeuron('VD3',5)

def DA3():
        incrementNeuron('AS4',2)
        incrementNeuron('AVAR',2)
        incrementNeuron('DA4',2)
        incrementNeuron('DB3',1)
        incrementNeuron('DD2',1)
        incrementNeuron('MDL09',5)
        incrementNeuron('MDL10',5)
        incrementNeuron('MDL12',5)
        incrementNeuron('MDR09',5)
        incrementNeuron('MDR10',5)
        incrementNeuron('MDR12',5)
        incrementNeuron('VD3',25)
        incrementNeuron('VD4',6)

def DA4():
        incrementNeuron('AVAL',3)
        incrementNeuron('AVAR',2)
        incrementNeuron('DA1',1)
        incrementNeuron('DA3',1)
        incrementNeuron('DB3',2)
        incrementNeuron('DD2',1)
        incrementNeuron('MDL11',4)
        incrementNeuron('MDL12',4)
        incrementNeuron('MDL14',5)
        incrementNeuron('MDR11',4)
        incrementNeuron('MDR12',4)
        incrementNeuron('MDR14',5)
        incrementNeuron('VB6',1)
        incrementNeuron('VD4',12)
        incrementNeuron('VD5',15)

def DA5():
        incrementNeuron('AS6',2)
        incrementNeuron('AVAL',1)
        incrementNeuron('AVAR',5)
        incrementNeuron('DB4',1)
        incrementNeuron('MDL13',5)
        incrementNeuron('MDL14',4)
        incrementNeuron('MDR13',5)
        incrementNeuron('MDR14',4)
        incrementNeuron('VA4',1)
        incrementNeuron('VA5',2)
        incrementNeuron('VD5',1)
        incrementNeuron('VD6',16)

def DA6():
        incrementNeuron('AVAL',10)
        incrementNeuron('AVAR',2)
        incrementNeuron('MDL11',6)
        incrementNeuron('MDL12',4)
        incrementNeuron('MDL13',4)
        incrementNeuron('MDL14',4)
        incrementNeuron('MDL16',4)
        incrementNeuron('MDR11',4)
        incrementNeuron('MDR12',4)
        incrementNeuron('MDR13',4)
        incrementNeuron('MDR14',4)
        incrementNeuron('MDR16',4)
        incrementNeuron('VD4',4)
        incrementNeuron('VD5',3)
        incrementNeuron('VD6',3)

def DA7():
        incrementNeuron('AVAL',2)
        incrementNeuron('MDL15',4)
        incrementNeuron('MDL17',4)
        incrementNeuron('MDL18',4)
        incrementNeuron('MDR15',4)
        incrementNeuron('MDR17',4)
        incrementNeuron('MDR18',4)

def DA8():
        incrementNeuron('AVAR',1)
        incrementNeuron('DA9',1)
        incrementNeuron('MDL17',4)
        incrementNeuron('MDL19',4)
        incrementNeuron('MDL20',4)
        incrementNeuron('MDR17',4)
        incrementNeuron('MDR19',4)
        incrementNeuron('MDR20',4)

def DA9():
        incrementNeuron('DA8',1)
        incrementNeuron('DD6',1)
        incrementNeuron('MDL19',4)
        incrementNeuron('MDL21',4)
        incrementNeuron('MDL22',4)
        incrementNeuron('MDL23',4)
        incrementNeuron('MDL24',4)
        incrementNeuron('MDR19',4)
        incrementNeuron('MDR21',4)
        incrementNeuron('MDR22',4)
        incrementNeuron('MDR23',4)
        incrementNeuron('MDR24',4)
        incrementNeuron('PDA',1)
        incrementNeuron('PHCL',1)
        incrementNeuron('RID',1)
        incrementNeuron('VD13',1)

def DB1():
        incrementNeuron('AIBR',1)
        incrementNeuron('AS1',1)
        incrementNeuron('AS2',1)
        incrementNeuron('AS3',1)
        incrementNeuron('AVBR',3)
        incrementNeuron('DB2',1)
        incrementNeuron('DB4',1)
        incrementNeuron('DD1',10)
        incrementNeuron('DVA',1)
        incrementNeuron('MDL07',1)
        incrementNeuron('MDL08',1)
        incrementNeuron('MDR07',1)
        incrementNeuron('MDR08',1)
        incrementNeuron('RID',1)
        incrementNeuron('RIS',1)
        incrementNeuron('VB3',1)
        incrementNeuron('VB4',1)
        incrementNeuron('VD1',21)
        incrementNeuron('VD2',15)
        incrementNeuron('VD3',1)

def DB2():
        incrementNeuron('AVBR',1)
        incrementNeuron('DA3',5)
        incrementNeuron('DB1',1)
        incrementNeuron('DB3',6)
        incrementNeuron('DD2',3)
        incrementNeuron('MDL09',3)
        incrementNeuron('MDL10',3)
        incrementNeuron('MDL11',3)
        incrementNeuron('MDL12',3)
        incrementNeuron('MDR09',3)
        incrementNeuron('MDR10',3)
        incrementNeuron('MDR11',3)
        incrementNeuron('MDR12',3)
        incrementNeuron('VB1',2)
        incrementNeuron('VD3',23)
        incrementNeuron('VD4',14)
        incrementNeuron('VD5',1)

def DB3():
        incrementNeuron('AS4',1)
        incrementNeuron('AS5',1)
        incrementNeuron('AVBL',1)
        incrementNeuron('AVBR',1)
        incrementNeuron('DA4',1)
        incrementNeuron('DB2',6)
        incrementNeuron('DB4',1)
        incrementNeuron('DD2',4)
        incrementNeuron('DD3',10)
        incrementNeuron('MDL11',3)
        incrementNeuron('MDL12',3)
        incrementNeuron('MDL13',4)
        incrementNeuron('MDL14',3)
        incrementNeuron('MDR11',3)
        incrementNeuron('MDR12',3)
        incrementNeuron('MDR13',4)
        incrementNeuron('MDR14',3)
        incrementNeuron('VD4',9)
        incrementNeuron('VD5',26)
        incrementNeuron('VD6',7)

def DB4():
        incrementNeuron('AVBL',1)
        incrementNeuron('AVBR',1)
        incrementNeuron('DB1',1)
        incrementNeuron('DB3',1)
        incrementNeuron('DD3',3)
        incrementNeuron('MDL13',2)
        incrementNeuron('MDL14',2)
        incrementNeuron('MDL16',2)
        incrementNeuron('MDR13',2)
        incrementNeuron('MDR14',2)
        incrementNeuron('MDR16',2)
        incrementNeuron('VB2',1)
        incrementNeuron('VB4',1)
        incrementNeuron('VD6',13)

def DB5():
        incrementNeuron('AVAR',2)
        incrementNeuron('AVBL',1)
        incrementNeuron('AVBR',1)
        incrementNeuron('MDL15',2)
        incrementNeuron('MDL17',2)
        incrementNeuron('MDL18',2)
        incrementNeuron('MDR15',2)
        incrementNeuron('MDR17',2)
        incrementNeuron('MDR18',2)

def DB6():
        incrementNeuron('AVAL',3)
        incrementNeuron('AVBL',2)
        incrementNeuron('AVBR',1)
        incrementNeuron('MDL17',2)
        incrementNeuron('MDL19',2)
        incrementNeuron('MDL20',2)
        incrementNeuron('MDR17',2)
        incrementNeuron('MDR19',2)
        incrementNeuron('MDR20',2)

def DB7():
        incrementNeuron('AVBL',2)
        incrementNeuron('AVBR',1)
        incrementNeuron('MDL19',2)
        incrementNeuron('MDL21',2)
        incrementNeuron('MDL22',2)
        incrementNeuron('MDL23',2)
        incrementNeuron('MDL24',2)
        incrementNeuron('MDR19',2)
        incrementNeuron('MDR21',2)
        incrementNeuron('MDR22',2)
        incrementNeuron('MDR23',2)
        incrementNeuron('MDR24',2)
        incrementNeuron('VD13',2)

def DD1():
        incrementNeuron('AVBR',1)
        incrementNeuron('DD2',3)
        incrementNeuron('MDL07',-6)
        incrementNeuron('MDL08',-6)
        incrementNeuron('MDL09',-7)
        incrementNeuron('MDL10',-6)
        incrementNeuron('MDR07',-6)
        incrementNeuron('MDR08',-6)
        incrementNeuron('MDR09',-7)
        incrementNeuron('MDR10',-6)
        incrementNeuron('VD1',4)
        incrementNeuron('VD2',1)
        incrementNeuron('VD2',2)

def DD2():
        incrementNeuron('DA3',1)
        incrementNeuron('DD1',1)
        incrementNeuron('DD3',2)
        incrementNeuron('MDL09',-6)
        incrementNeuron('MDL11',-7)
        incrementNeuron('MDL12',-6)
        incrementNeuron('MDR09',-6)
        incrementNeuron('MDR11',-7)
        incrementNeuron('MDR12',-6)
        incrementNeuron('VD3',1)
        incrementNeuron('VD4',3)

def DD3():
        incrementNeuron('DD2',2)
        incrementNeuron('DD4',1)
        incrementNeuron('MDL11',-7)
        incrementNeuron('MDL13',-9)
        incrementNeuron('MDL14',-7)
        incrementNeuron('MDR11',-7)
        incrementNeuron('MDR13',-9)
        incrementNeuron('MDR14',-7)

def DD4():
        incrementNeuron('DD3',1)
        incrementNeuron('MDL13',-7)
        incrementNeuron('MDL15',-7)
        incrementNeuron('MDL16',-7)
        incrementNeuron('MDR13',-7)
        incrementNeuron('MDR15',-7)
        incrementNeuron('MDR16',-7)
        incrementNeuron('VC3',1)
        incrementNeuron('VD8',1)

def DD5():
        incrementNeuron('MDL17',-7)
        incrementNeuron('MDL18',-7)
        incrementNeuron('MDL20',-7)
        incrementNeuron('MDR17',-7)
        incrementNeuron('MDR18',-7)
        incrementNeuron('MDR20',-7)
        incrementNeuron('VB8',1)
        incrementNeuron('VD10',1)
        incrementNeuron('VD9',1)

def DD6():
        incrementNeuron('MDL19',-7)
        incrementNeuron('MDL21',-7)
        incrementNeuron('MDL22',-7)
        incrementNeuron('MDL23',-7)
        incrementNeuron('MDL24',-7)
        incrementNeuron('MDR19',-7)
        incrementNeuron('MDR21',-7)
        incrementNeuron('MDR22',-7)
        incrementNeuron('MDR23',-7)
        incrementNeuron('MDR24',-7)

def DVA():
        incrementNeuron('AIZL',3)
        incrementNeuron('AQR',4)
        incrementNeuron('AUAL',1)
        incrementNeuron('AUAR',1)
        incrementNeuron('AVAL',3)
        incrementNeuron('AVAR',1)
        incrementNeuron('AVBL',2)
        incrementNeuron('AVBR',1)
        incrementNeuron('AVEL',9)
        incrementNeuron('AVER',5)
        incrementNeuron('DB1',1)
        incrementNeuron('DB2',1)
        incrementNeuron('DB3',2)
        incrementNeuron('DB4',1)
        incrementNeuron('DB5',1)
        incrementNeuron('DB6',2)
        incrementNeuron('DB7',1)
        incrementNeuron('PDEL',3)
        incrementNeuron('PVCL',3)
        incrementNeuron('PVCL',1)
        incrementNeuron('PVCR',1)
        incrementNeuron('PVR',3)
        incrementNeuron('PVR',2)
        incrementNeuron('RIAL',1)
        incrementNeuron('RIAR',1)
        incrementNeuron('RIMR',1)
        incrementNeuron('RIR',3)
        incrementNeuron('SAADR',1)
        incrementNeuron('SAAVL',1)
        incrementNeuron('SAAVR',1)
        incrementNeuron('SABD',1)
        incrementNeuron('SMBDL',3)
        incrementNeuron('SMBDR',2)
        incrementNeuron('SMBVL',3)
        incrementNeuron('SMBVR',2)
        incrementNeuron('VA12',1)
        incrementNeuron('VA2',1)
        incrementNeuron('VB1',1)
        incrementNeuron('VB11',2)

def DVB():
        incrementNeuron('AS9',7)
        incrementNeuron('AVL',5)
        incrementNeuron('AVL',1)
        incrementNeuron('DA8',2)
        incrementNeuron('DD6',3)
        incrementNeuron('DVC',3)
        # incrementNeuron('MANAL',-5) - just not needed or used
        incrementNeuron('PDA',1)
        incrementNeuron('PHCL',1)
        incrementNeuron('PVPL',1)
        incrementNeuron('VA9',1)
        incrementNeuron('VB9',1)

def DVC():
        incrementNeuron('AIBL',2)
        incrementNeuron('AIBR',5)
        incrementNeuron('AVAL',5)
        incrementNeuron('AVAR',7)
        incrementNeuron('AVBL',1)
        incrementNeuron('AVKL',2)
        incrementNeuron('AVKR',1)
        incrementNeuron('AVL',9)
        incrementNeuron('PVPL',2)
        incrementNeuron('PVPR',13)
        incrementNeuron('PVT',1)
        incrementNeuron('RIBL',1)
        incrementNeuron('RIBR',1)
        incrementNeuron('RIGL',5)
        incrementNeuron('RIGR',5)
        incrementNeuron('RMFL',2)
        incrementNeuron('RMFR',4)
        incrementNeuron('VA9',1)
        incrementNeuron('VD1',5)
        incrementNeuron('VD10',4)

def FLPL():
        incrementNeuron('ADEL',2)
        incrementNeuron('ADER',2)
        incrementNeuron('AIBL',1)
        incrementNeuron('AIBR',2)
        incrementNeuron('AVAL',15)
        incrementNeuron('AVAR',17)
        incrementNeuron('AVBL',4)
        incrementNeuron('AVBR',5)
        incrementNeuron('AVDL',7)
        incrementNeuron('AVDR',13)
        incrementNeuron('DVA',1)
        incrementNeuron('FLPR',3)
        incrementNeuron('RIH',1)

def FLPR():
        incrementNeuron('ADER',1)
        incrementNeuron('AIBR',1)
        incrementNeuron('AVAL',12)
        incrementNeuron('AVAR',5)
        incrementNeuron('AVBL',5)
        incrementNeuron('AVBR',1)
        incrementNeuron('AVDL',10)
        incrementNeuron('AVDL',1)
        incrementNeuron('AVDR',2)
        incrementNeuron('AVEL',4)
        incrementNeuron('AVER',2)
        incrementNeuron('AVJR',1)
        incrementNeuron('DVA',1)
        incrementNeuron('FLPL',4)
        incrementNeuron('PVCL',2)
        incrementNeuron('VB1',1)

def HSNL():
        incrementNeuron('AIAL',1)
        incrementNeuron('AIZL',2)
        incrementNeuron('AIZR',1)
        incrementNeuron('ASHL',1)
        incrementNeuron('ASHR',2)
        incrementNeuron('ASJR',1)
        incrementNeuron('ASKL',1)
        incrementNeuron('AVDR',2)
        incrementNeuron('AVFL',6)
        incrementNeuron('AVJL',1)
        incrementNeuron('AWBL',1)
        incrementNeuron('AWBR',2)
        incrementNeuron('HSNR',3)
        incrementNeuron('HSNR',1)
        incrementNeuron('MVULVA',7)
        incrementNeuron('RIFL',3)
        incrementNeuron('RIML',2)
        incrementNeuron('SABVL',2)
        incrementNeuron('VC5',3)

def HSNR():
        incrementNeuron('AIBL',1)
        incrementNeuron('AIBR',1)
        incrementNeuron('AIZL',1)
        incrementNeuron('AIZR',1)
        incrementNeuron('AS5',1)
        incrementNeuron('ASHL',2)
        incrementNeuron('AVDR',1)
        incrementNeuron('AVFL',1)
        incrementNeuron('AVJL',1)
        incrementNeuron('AVL',1)
        incrementNeuron('AWBL',1)
        incrementNeuron('BDUR',1)
        incrementNeuron('DA5',1)
        incrementNeuron('DA6',1)
        incrementNeuron('HSNL',2)
        incrementNeuron('MVULVA',6)
        incrementNeuron('PVNR',2)
        incrementNeuron('PVQR',1)
        incrementNeuron('RIFR',4)
        incrementNeuron('RMGR',1)
        incrementNeuron('SABD',1)
        incrementNeuron('SABVR',1)
        incrementNeuron('VA6',1)
        incrementNeuron('VC2',3)
        incrementNeuron('VC3',1)
        incrementNeuron('VD4',2)

def I1L():
        incrementNeuron('I1R',1)
        incrementNeuron('I3',1)
        incrementNeuron('I5',1)
        incrementNeuron('RIPL',1)
        incrementNeuron('RIPR',1)

def I1R():
        incrementNeuron('I1L',1)
        incrementNeuron('I3',1)
        incrementNeuron('I5',1)
        incrementNeuron('RIPL',1)
        incrementNeuron('RIPR',1)

def I2L():
        incrementNeuron('I1L',1)
        incrementNeuron('I1R',1)
        incrementNeuron('M1',4)

def I2R():
        incrementNeuron('I1L',1)
        incrementNeuron('I1R',1)
        incrementNeuron('M1',4)

def I3():
        incrementNeuron('M1',4)
        incrementNeuron('M2L',2)
        incrementNeuron('M2R',2)

def I4():
        incrementNeuron('I2L',5)
        incrementNeuron('I2R',5)
        incrementNeuron('I5',2)
        incrementNeuron('M1',4)

def I5():
        incrementNeuron('I1L',4)
        incrementNeuron('I1R',3)
        incrementNeuron('M1',2)
        incrementNeuron('M5',2)
        incrementNeuron('MI',4)

def I6():
        incrementNeuron('I2L',2)
        incrementNeuron('I2R',2)
        incrementNeuron('I3',1)
        incrementNeuron('M4',1)
        incrementNeuron('M5',2)
        incrementNeuron('NSML',2)
        incrementNeuron('NSMR',2)

def IL1DL():
        incrementNeuron('IL1DR',1)
        incrementNeuron('IL1L',1)
        incrementNeuron('MDL01',1)
        incrementNeuron('MDL02',1)
        incrementNeuron('MDL04',2)
        incrementNeuron('OLLL',1)
        incrementNeuron('PVR',1)
        incrementNeuron('RIH',1)
        incrementNeuron('RIPL',2)
        incrementNeuron('RMDDR',1)
        incrementNeuron('RMDVL',4)
        incrementNeuron('RMEV',1)
        incrementNeuron('URYDL',1)

def IL1DR():
        incrementNeuron('IL1DL',1)
        incrementNeuron('IL1R',1)
        incrementNeuron('MDR01',4)
        incrementNeuron('MDR02',3)
        incrementNeuron('OLLR',1)
        incrementNeuron('RIPR',5)
        incrementNeuron('RMDVR',5)
        incrementNeuron('RMEV',1)

def IL1L():
        incrementNeuron('AVER',2)
        incrementNeuron('IL1DL',2)
        incrementNeuron('IL1VL',1)
        incrementNeuron('MDL01',3)
        incrementNeuron('MDL03',3)
        incrementNeuron('MDL05',4)
        incrementNeuron('MVL01',3)
        incrementNeuron('MVL03',3)
        incrementNeuron('RMDDL',5)
        incrementNeuron('RMDL',1)
        incrementNeuron('RMDR',3)
        incrementNeuron('RMDVL',4)
        incrementNeuron('RMDVR',2)
        incrementNeuron('RMER',1)

def IL1R():
        incrementNeuron('AVEL',1)
        incrementNeuron('AVER',1)
        incrementNeuron('IL1DR',2)
        incrementNeuron('IL1VR',1)
        incrementNeuron('MDR01',3)
        incrementNeuron('MDR03',3)
        incrementNeuron('MVR01',3)
        incrementNeuron('MVR03',3)
        incrementNeuron('RMDDL',3)
        incrementNeuron('RMDDR',2)
        incrementNeuron('RMDL',4)
        incrementNeuron('RMDR',2)
        incrementNeuron('RMDVL',1)
        incrementNeuron('RMDVR',4)
        incrementNeuron('RMEL',2)
        incrementNeuron('RMHL',1)
        incrementNeuron('URXR',2)

def IL1VL():
        incrementNeuron('IL1L',2)
        incrementNeuron('IL1VR',1)
        incrementNeuron('MVL01',5)
        incrementNeuron('MVL02',4)
        incrementNeuron('RIPL',4)
        incrementNeuron('RMDDL',5)
        incrementNeuron('RMED',1)
        incrementNeuron('URYVL',1)

def IL1VR():
        incrementNeuron('IL1R',2)
        incrementNeuron('IL1VL',1)
        incrementNeuron('IL2R',1)
        incrementNeuron('IL2VR',1)
        incrementNeuron('MVR01',5)
        incrementNeuron('MVR02',5)
        incrementNeuron('RIPR',6)
        incrementNeuron('RMDDR',10)
        incrementNeuron('RMER',1)

def IL2DL():
        incrementNeuron('AUAL',1)
        incrementNeuron('IL1DL',7)
        incrementNeuron('OLQDL',2)
        incrementNeuron('RIBL',1)
        incrementNeuron('RIPL',10)
        incrementNeuron('RMEL',4)
        incrementNeuron('RMER',3)
        incrementNeuron('URADL',3)

def IL2DR():
        incrementNeuron('CEPDR',1)
        incrementNeuron('IL1DR',7)
        incrementNeuron('RICR',1)
        incrementNeuron('RIPR',11)
        incrementNeuron('RMED',1)
        incrementNeuron('RMEL',2)
        incrementNeuron('RMER',2)
        incrementNeuron('RMEV',1)
        incrementNeuron('URADR',3)

def IL2L():
        incrementNeuron('ADEL',2)
        incrementNeuron('AVEL',1)
        incrementNeuron('IL1L',1)
        incrementNeuron('OLQDL',5)
        incrementNeuron('OLQVL',8)
        incrementNeuron('RICL',1)
        incrementNeuron('RIH',7)
        incrementNeuron('RMDL',3)
        incrementNeuron('RMDR',1)
        incrementNeuron('RMER',2)
        incrementNeuron('RMEV',2)
        incrementNeuron('RMGL',1)
        incrementNeuron('URXL',2)

def IL2R():
        incrementNeuron('ADER',1)
        incrementNeuron('IL1R',1)
        incrementNeuron('IL1VR',1)
        incrementNeuron('OLLR',1)
        incrementNeuron('OLQDR',2)
        incrementNeuron('OLQVR',7)
        incrementNeuron('RIH',6)
        incrementNeuron('RMDL',1)
        incrementNeuron('RMEL',2)
        incrementNeuron('RMEV',1)
        incrementNeuron('RMGR',1)
        incrementNeuron('URBR',1)
        incrementNeuron('URXR',1)

def IL2VL():
        incrementNeuron('BAGR',1)
        incrementNeuron('IL1VL',7)
        incrementNeuron('IL2L',1)
        incrementNeuron('OLQVL',1)
        incrementNeuron('RIAL',1)
        incrementNeuron('RIH',2)
        incrementNeuron('RIPL',1)
        incrementNeuron('RMEL',1)
        incrementNeuron('RMER',4)
        incrementNeuron('RMEV',1)
        incrementNeuron('URAVL',3)

def IL2VR():
        incrementNeuron('IL1VR',6)
        incrementNeuron('OLQVR',1)
        incrementNeuron('RIAR',2)
        incrementNeuron('RIH',3)
        incrementNeuron('RIPR',15)
        incrementNeuron('RMEL',3)
        incrementNeuron('RMER',2)
        incrementNeuron('RMEV',3)
        incrementNeuron('URAVR',4)
        incrementNeuron('URXR',1)

def LUAL():
        incrementNeuron('AVAL',6)
        incrementNeuron('AVAR',6)
        incrementNeuron('AVDL',4)
        incrementNeuron('AVDR',2)
        incrementNeuron('AVJL',1)
        incrementNeuron('PHBL',1)
        incrementNeuron('PLML',1)
        incrementNeuron('PVNL',1)
        incrementNeuron('PVR',1)
        incrementNeuron('PVWL',1)

def LUAR():
        incrementNeuron('AVAL',3)
        incrementNeuron('AVAR',7)
        incrementNeuron('AVDL',1)
        incrementNeuron('AVDR',3)
        incrementNeuron('AVJR',1)
        incrementNeuron('PLMR',1)
        incrementNeuron('PQR',1)
        incrementNeuron('PVCR',3)
        incrementNeuron('PVR',2)
        incrementNeuron('PVWL',1)

def M1():
        incrementNeuron('I2L',2)
        incrementNeuron('I2R',2)
        incrementNeuron('I3',1)
        incrementNeuron('I4',1)

def M2L():
        incrementNeuron('I1L',3)
        incrementNeuron('I1R',3)
        incrementNeuron('I3',3)
        incrementNeuron('M2R',1)
        incrementNeuron('M5',1)
        incrementNeuron('MI',4)

def M2R():
        incrementNeuron('I1L',3)
        incrementNeuron('I1R',3)
        incrementNeuron('I3',3)
        incrementNeuron('M3L',1)
        incrementNeuron('M3R',1)
        incrementNeuron('M5',1)
        incrementNeuron('MI',4)

def M3L():
        incrementNeuron('I1L',4)
        incrementNeuron('I1R',4)
        incrementNeuron('I4',2)
        incrementNeuron('I5',3)
        incrementNeuron('I6',1)
        incrementNeuron('M1',2)
        incrementNeuron('M3R',1)
        incrementNeuron('MCL',1)
        incrementNeuron('MCR',1)
        incrementNeuron('MI',2)
        incrementNeuron('NSML',2)
        incrementNeuron('NSMR',3)

def M3R():
        incrementNeuron('I1L',4)
        incrementNeuron('I1R',4)
        incrementNeuron('I3',2)
        incrementNeuron('I4',6)
        incrementNeuron('I5',3)
        incrementNeuron('I6',1)
        incrementNeuron('M1',2)
        incrementNeuron('M3L',1)
        incrementNeuron('MCL',1)
        incrementNeuron('MCR',1)
        incrementNeuron('MI',2)
        incrementNeuron('NSML',2)
        incrementNeuron('NSMR',3)

def M4():
        incrementNeuron('I3',1)
        incrementNeuron('I5',13)
        incrementNeuron('I6',3)
        incrementNeuron('M2L',1)
        incrementNeuron('M2R',1)
        incrementNeuron('M4',6)
        incrementNeuron('M5',1)
        incrementNeuron('NSML',1)
        incrementNeuron('NSMR',1)

def M5():
        incrementNeuron('I5',3)
        incrementNeuron('I5',1)
        incrementNeuron('I6',1)
        incrementNeuron('M1',2)
        incrementNeuron('M2L',2)
        incrementNeuron('M2R',2)
        incrementNeuron('M5',4)

def MCL():
        incrementNeuron('I1L',3)
        incrementNeuron('I1R',3)
        incrementNeuron('I2L',1)
        incrementNeuron('I2R',1)
        incrementNeuron('I3',1)
        incrementNeuron('M1',2)
        incrementNeuron('M2L',2)
        incrementNeuron('M2R',2)

def MCR():
        incrementNeuron('I1L',3)
        incrementNeuron('I1R',3)
        incrementNeuron('I3',1)
        incrementNeuron('M1',2)
        incrementNeuron('M2L',2)
        incrementNeuron('M2R',2)

def MI():
        incrementNeuron('I1L',1)
        incrementNeuron('I1R',1)
        incrementNeuron('I3',1)
        incrementNeuron('I4',1)
        incrementNeuron('I5',2)
        incrementNeuron('M1',1)
        incrementNeuron('M2L',2)
        incrementNeuron('M2R',2)
        incrementNeuron('M3L',1)
        incrementNeuron('M3R',1)
        incrementNeuron('MCL',2)
        incrementNeuron('MCR',2)

def NSML():
        incrementNeuron('I1L',1)
        incrementNeuron('I1R',2)
        incrementNeuron('I2L',6)
        incrementNeuron('I2R',6)
        incrementNeuron('I3',2)
        incrementNeuron('I4',3)
        incrementNeuron('I5',2)
        incrementNeuron('I6',2)
        incrementNeuron('M3L',2)
        incrementNeuron('M3R',2)

def NSMR():
        incrementNeuron('I1L',2)
        incrementNeuron('I1R',2)
        incrementNeuron('I2L',6)
        incrementNeuron('I2R',6)
        incrementNeuron('I3',2)
        incrementNeuron('I4',3)
        incrementNeuron('I5',2)
        incrementNeuron('I6',2)
        incrementNeuron('M3L',2)
        incrementNeuron('M3R',2)

def OLLL():
        incrementNeuron('AVER',21)
        incrementNeuron('CEPDL',3)
        incrementNeuron('CEPVL',4)
        incrementNeuron('IL1DL',1)
        incrementNeuron('IL1VL',2)
        incrementNeuron('OLLR',2)
        incrementNeuron('RIBL',8)
        incrementNeuron('RIGL',1)
        incrementNeuron('RMDDL',7)
        incrementNeuron('RMDL',2)
        incrementNeuron('RMDVL',1)
        incrementNeuron('RMEL',2)
        incrementNeuron('SMDDL',3)
        incrementNeuron('SMDDR',4)
        incrementNeuron('SMDVR',4)
        incrementNeuron('URYDL',1)

def OLLR():
        incrementNeuron('AVEL',16)
        incrementNeuron('CEPDR',1)
        incrementNeuron('CEPVR',6)
        incrementNeuron('IL1DR',3)
        incrementNeuron('IL1VR',1)
        incrementNeuron('IL2R',1)
        incrementNeuron('OLLL',2)
        incrementNeuron('RIBR',10)
        incrementNeuron('RIGR',1)
        incrementNeuron('RMDDR',10)
        incrementNeuron('RMDL',3)
        incrementNeuron('RMDVR',3)
        incrementNeuron('RMER',2)
        incrementNeuron('SMDDR',1)
        incrementNeuron('SMDVL',4)
        incrementNeuron('SMDVR',3)

def OLQDL():
        incrementNeuron('CEPDL',1)
        incrementNeuron('RIBL',2)
        incrementNeuron('RICR',1)
        incrementNeuron('RIGL',1)
        incrementNeuron('RMDDR',4)
        incrementNeuron('RMDVL',1)
        incrementNeuron('SIBVL',3)
        incrementNeuron('URBL',1)

def OLQDR():
        incrementNeuron('CEPDR',2)
        incrementNeuron('RIBR',2)
        incrementNeuron('RICL',1)
        incrementNeuron('RICR',1)
        incrementNeuron('RIGR',1)
        incrementNeuron('RIH',1)
        incrementNeuron('RMDDL',3)
        incrementNeuron('RMDVR',1)
        incrementNeuron('RMHR',1)
        incrementNeuron('SIBVR',2)
        incrementNeuron('URBR',1)

def OLQVL():
        incrementNeuron('ADLL',1)
        incrementNeuron('CEPVL',1)
        incrementNeuron('IL1VL',1)
        incrementNeuron('IL2VL',1)
        incrementNeuron('RIBL',1)
        incrementNeuron('RICL',1)
        incrementNeuron('RIGL',1)
        incrementNeuron('RIH',1)
        incrementNeuron('RIPL',1)
        incrementNeuron('RMDDL',1)
        incrementNeuron('RMDVR',4)
        incrementNeuron('SIBDL',3)
        incrementNeuron('URBL',1)

def OLQVR():
        incrementNeuron('CEPVR',1)
        incrementNeuron('IL1VR',1)
        incrementNeuron('RIBR',1)
        incrementNeuron('RICR',1)
        incrementNeuron('RIGR',1)
        incrementNeuron('RIH',2)
        incrementNeuron('RIPR',2)
        incrementNeuron('RMDDR',1)
        incrementNeuron('RMDVL',4)
        incrementNeuron('RMER',1)
        incrementNeuron('SIBDR',4)
        incrementNeuron('URBR',1)

def PDA():
        incrementNeuron('AS11',1)
        incrementNeuron('DA9',1)
        incrementNeuron('DD6',1)
        incrementNeuron('MDL21',2)
        incrementNeuron('PVNR',1)
        incrementNeuron('VD13',3)

def PDB():
        incrementNeuron('AS11',2)
        incrementNeuron('MVL22',1)
        incrementNeuron('MVR21',1)
        incrementNeuron('RID',2)
        incrementNeuron('VD13',2)

def PDEL():
        incrementNeuron('AVKL',6)
        incrementNeuron('DVA',24)
        incrementNeuron('PDER',1)
        incrementNeuron('PDER',3)
        incrementNeuron('PVCR',1)
        incrementNeuron('PVM',2)
        incrementNeuron('PVM',1)
        incrementNeuron('PVR',2)
        incrementNeuron('VA9',1)
        incrementNeuron('VD11',1)

def PDER():
        incrementNeuron('AVKL',16)
        incrementNeuron('DVA',35)
        incrementNeuron('PDEL',3)
        incrementNeuron('PVCL',1)
        incrementNeuron('PVCR',1)
        incrementNeuron('PVM',1)
        incrementNeuron('VA8',1)
        incrementNeuron('VD9',1)

def PHAL():
        incrementNeuron('AVDR',1)
        incrementNeuron('AVFL',3)
        incrementNeuron('AVG',5)
        incrementNeuron('AVHL',1)
        incrementNeuron('AVHR',1)
        incrementNeuron('DVA',2)
        incrementNeuron('PHAR',5)
        incrementNeuron('PHAR',2)
        incrementNeuron('PHBL',5)
        incrementNeuron('PHBR',5)
        incrementNeuron('PVQL',2)

def PHAR():
        incrementNeuron('AVG',3)
        incrementNeuron('AVHR',1)
        incrementNeuron('DA8',1)
        incrementNeuron('DVA',1)
        incrementNeuron('PHAL',6)
        incrementNeuron('PHAL',2)
        incrementNeuron('PHBL',1)
        incrementNeuron('PHBR',5)
        incrementNeuron('PVPL',3)
        incrementNeuron('PVQL',2)

def PHBL():
        incrementNeuron('AVAL',9)
        incrementNeuron('AVAR',6)
        incrementNeuron('AVDL',1)
        incrementNeuron('PHBR',1)
        incrementNeuron('PHBR',3)
        incrementNeuron('PVCL',13)
        incrementNeuron('VA12',1)

def PHBR():
        incrementNeuron('AVAL',7)
        incrementNeuron('AVAR',7)
        incrementNeuron('AVDL',1)
        incrementNeuron('AVDR',1)
        incrementNeuron('AVFL',1)
        incrementNeuron('AVHL',1)
        incrementNeuron('DA8',1)
        incrementNeuron('PHBL',1)
        incrementNeuron('PHBL',3)
        incrementNeuron('PVCL',6)
        incrementNeuron('PVCR',3)
        incrementNeuron('VA12',2)

def PHCL():
        incrementNeuron('AVAL',1)
        incrementNeuron('DA9',7)
        incrementNeuron('DA9',1)
        incrementNeuron('DVA',6)
        incrementNeuron('LUAL',1)
        incrementNeuron('PHCR',1)
        incrementNeuron('PLML',1)
        incrementNeuron('PVCL',2)
        incrementNeuron('VA12',3)

def PHCR():
        incrementNeuron('AVHR',1)
        incrementNeuron('DA9',2)
        incrementNeuron('DVA',8)
        incrementNeuron('LUAR',1)
        incrementNeuron('PHCL',2)
        incrementNeuron('PVCR',9)
        incrementNeuron('VA12',2)

def PLML():
        incrementNeuron('HSNL',1)
        incrementNeuron('LUAL',1)
        incrementNeuron('PHCL',1)
        incrementNeuron('PVCL',1)

def PLMR():
        incrementNeuron('AS6',1)
        incrementNeuron('AVAL',4)
        incrementNeuron('AVAR',1)
        incrementNeuron('AVDL',1)
        incrementNeuron('AVDR',4)
        incrementNeuron('DVA',5)
        incrementNeuron('HSNR',1)
        incrementNeuron('LUAR',1)
        incrementNeuron('PDEL',2)
        incrementNeuron('PDER',3)
        incrementNeuron('PVCL',2)
        incrementNeuron('PVCR',1)
        incrementNeuron('PVR',2)

def PLNL():
        incrementNeuron('SAADL',5)
        incrementNeuron('SMBVL',6)

def PLNR():
        incrementNeuron('SAADR',4)
        incrementNeuron('SMBVR',6)

def PQR():
        incrementNeuron('AVAL',8)
        incrementNeuron('AVAR',11)
        incrementNeuron('AVDL',7)
        incrementNeuron('AVDR',6)
        incrementNeuron('AVG',1)
        incrementNeuron('LUAR',1)
        incrementNeuron('PVNL',1)
        incrementNeuron('PVPL',4)

def PVCL():
        incrementNeuron('AS1',1)
        incrementNeuron('AVAL',3)
        incrementNeuron('AVAR',4)
        incrementNeuron('AVBL',5)
        incrementNeuron('AVBR',12)
        incrementNeuron('AVDL',5)
        incrementNeuron('AVDR',2)
        incrementNeuron('AVEL',3)
        incrementNeuron('AVER',1)
        incrementNeuron('AVJL',4)
        incrementNeuron('AVJR',2)
        incrementNeuron('DA2',1)
        incrementNeuron('DA5',1)
        incrementNeuron('DA6',1)
        incrementNeuron('DB2',3)
        incrementNeuron('DB3',4)
        incrementNeuron('DB4',3)
        incrementNeuron('DB5',2)
        incrementNeuron('DB6',2)
        incrementNeuron('DB7',3)
        incrementNeuron('DVA',5)
        incrementNeuron('PLML',1)
        incrementNeuron('PVCR',7)
        incrementNeuron('RID',5)
        incrementNeuron('RIS',2)
        incrementNeuron('SIBVL',2)
        incrementNeuron('VB10',3)
        incrementNeuron('VB11',1)
        incrementNeuron('VB3',1)
        incrementNeuron('VB4',1)
        incrementNeuron('VB5',1)
        incrementNeuron('VB6',2)
        incrementNeuron('VB8',1)
        incrementNeuron('VB9',2)

def PVCR():
        incrementNeuron('AQR',1)
        incrementNeuron('AS2',1)
        incrementNeuron('AVAL',12)
        incrementNeuron('AVAR',10)
        incrementNeuron('AVBL',8)
        incrementNeuron('AVBR',6)
        incrementNeuron('AVDL',5)
        incrementNeuron('AVDR',1)
        incrementNeuron('AVEL',1)
        incrementNeuron('AVER',1)
        incrementNeuron('AVJL',3)
        incrementNeuron('AVL',1)
        incrementNeuron('DA9',1)
        incrementNeuron('DB2',1)
        incrementNeuron('DB3',3)
        incrementNeuron('DB4',4)
        incrementNeuron('DB5',1)
        incrementNeuron('DB6',2)
        incrementNeuron('DB7',1)
        incrementNeuron('FLPL',1)
        incrementNeuron('LUAR',1)
        incrementNeuron('PDEL',2)
        incrementNeuron('PHCR',1)
        incrementNeuron('PLMR',1)
        incrementNeuron('PVCL',8)
        incrementNeuron('PVDL',1)
        incrementNeuron('PVR',1)
        incrementNeuron('PVWL',2)
        incrementNeuron('PVWR',2)
        incrementNeuron('RID',5)
        incrementNeuron('SIBVR',2)
        incrementNeuron('VA8',2)
        incrementNeuron('VA9',1)
        incrementNeuron('VB10',1)
        incrementNeuron('VB4',3)
        incrementNeuron('VB6',2)
        incrementNeuron('VB7',3)
        incrementNeuron('VB8',1)

def PVDL():
        incrementNeuron('AVAL',6)
        incrementNeuron('AVAR',6)
        incrementNeuron('DD5',1)
        incrementNeuron('PVCL',1)
        incrementNeuron('PVCR',6)
        incrementNeuron('VD10',6)

def PVDR():
        incrementNeuron('AVAL',6)
        incrementNeuron('AVAR',9)
        incrementNeuron('DVA',3)
        incrementNeuron('PVCL',13)
        incrementNeuron('PVCR',10)
        incrementNeuron('PVDL',1)
        incrementNeuron('VA9',1)

def PVM():
        incrementNeuron('AVKL',11)
        incrementNeuron('AVL',1)
        incrementNeuron('AVM',1)
        incrementNeuron('DVA',3)
        incrementNeuron('PDEL',7)
        incrementNeuron('PDEL',1)
        incrementNeuron('PDER',8)
        incrementNeuron('PDER',1)
        incrementNeuron('PVCL',2)
        incrementNeuron('PVR',1)

def PVNL():
        incrementNeuron('AVAL',2)
        incrementNeuron('AVBR',3)
        incrementNeuron('AVDL',3)
        incrementNeuron('AVDR',3)
        incrementNeuron('AVEL',1)
        incrementNeuron('AVFR',1)
        incrementNeuron('AVG',1)
        incrementNeuron('AVJL',5)
        incrementNeuron('AVJR',5)
        incrementNeuron('AVL',2)
        incrementNeuron('BDUL',1)
        incrementNeuron('BDUR',2)
        incrementNeuron('DD1',2)
        incrementNeuron('MVL09',3)
        incrementNeuron('PQR',1)
        incrementNeuron('PVCL',1)
        incrementNeuron('PVNR',5)
        incrementNeuron('PVQR',1)
        incrementNeuron('PVT',1)
        incrementNeuron('PVWL',1)
        incrementNeuron('RIFL',1)

def PVNR():
        incrementNeuron('AVAL',2)
        incrementNeuron('AVBL',1)
        incrementNeuron('AVBR',2)
        incrementNeuron('AVDR',1)
        incrementNeuron('AVEL',3)
        incrementNeuron('AVJL',4)
        incrementNeuron('AVJR',1)
        incrementNeuron('AVL',2)
        incrementNeuron('BDUL',1)
        incrementNeuron('BDUR',2)
        incrementNeuron('DD3',1)
        incrementNeuron('HSNR',2)
        incrementNeuron('MVL12',1)
        incrementNeuron('MVL13',2)
        incrementNeuron('PQR',2)
        incrementNeuron('PVCL',1)
        incrementNeuron('PVNL',1)
        incrementNeuron('PVT',2)
        incrementNeuron('PVWL',2)
        incrementNeuron('VC2',1)
        incrementNeuron('VC3',1)
        incrementNeuron('VD12',1)
        incrementNeuron('VD6',1)
        incrementNeuron('VD7',1)

def PVPL():
        incrementNeuron('ADAL',1)
        incrementNeuron('AQR',8)
        incrementNeuron('AVAL',2)
        incrementNeuron('AVAR',1)
        incrementNeuron('AVBL',5)
        incrementNeuron('AVBR',6)
        incrementNeuron('AVDR',2)
        incrementNeuron('AVER',1)
        incrementNeuron('AVHR',1)
        incrementNeuron('AVKL',1)
        incrementNeuron('AVKR',6)
        incrementNeuron('DVC',2)
        incrementNeuron('PHAR',3)
        incrementNeuron('PQR',4)
        incrementNeuron('PVCR',3)
        incrementNeuron('PVPR',1)
        incrementNeuron('PVT',1)
        incrementNeuron('RIGL',2)
        incrementNeuron('VD13',2)
        incrementNeuron('VD3',1)

def PVPR():
        incrementNeuron('ADFR',1)
        incrementNeuron('AQR',11)
        incrementNeuron('ASHR',1)
        incrementNeuron('AVAL',1)
        incrementNeuron('AVAR',2)
        incrementNeuron('AVBL',4)
        incrementNeuron('AVBR',5)
        incrementNeuron('AVHL',3)
        incrementNeuron('AVKL',1)
        incrementNeuron('AVL',4)
        incrementNeuron('DD2',1)
        incrementNeuron('DVC',14)
        incrementNeuron('PVCL',4)
        incrementNeuron('PVCR',7)
        incrementNeuron('PVPL',1)
        incrementNeuron('PVQR',1)
        incrementNeuron('RIAR',2)
        incrementNeuron('RIGR',1)
        incrementNeuron('RIMR',1)
        incrementNeuron('RMGR',1)
        incrementNeuron('VD4',1)
        incrementNeuron('VD5',1)

def PVQL():
        incrementNeuron('ADAL',1)
        incrementNeuron('AIAL',3)
        incrementNeuron('ASJL',1)
        incrementNeuron('ASKL',4)
        incrementNeuron('ASKL',5)
        incrementNeuron('HSNL',2)
        incrementNeuron('PVQR',2)
        incrementNeuron('RMGL',1)

def PVQR():
        incrementNeuron('ADAR',1)
        incrementNeuron('AIAR',7)
        incrementNeuron('ASER',1)
        incrementNeuron('ASKR',8)
        incrementNeuron('AVBL',1)
        incrementNeuron('AVFL',1)
        incrementNeuron('AVFR',1)
        incrementNeuron('AVL',1)
        incrementNeuron('AWAR',2)
        incrementNeuron('DD1',1)
        incrementNeuron('DVC',1)
        incrementNeuron('HSNR',1)
        incrementNeuron('PVNL',1)
        incrementNeuron('PVQL',1)
        incrementNeuron('PVT',1)
        incrementNeuron('RIFR',1)
        incrementNeuron('VD1',1)

def PVR():
        incrementNeuron('ADAL',1)
        incrementNeuron('ALML',1)
        incrementNeuron('AS6',1)
        incrementNeuron('AVBL',4)
        incrementNeuron('AVBR',4)
        incrementNeuron('AVJL',3)
        incrementNeuron('AVJR',2)
        incrementNeuron('AVKL',1)
        incrementNeuron('DA9',1)
        incrementNeuron('DB2',1)
        incrementNeuron('DB3',1)
        incrementNeuron('DVA',3)
        incrementNeuron('IL1DL',1)
        incrementNeuron('IL1DR',1)
        incrementNeuron('IL1VL',1)
        incrementNeuron('IL1VR',1)
        incrementNeuron('LUAL',1)
        incrementNeuron('LUAR',1)
        incrementNeuron('PDEL',1)
        incrementNeuron('PDER',1)
        incrementNeuron('PLMR',2)
        incrementNeuron('PVCR',1)
        incrementNeuron('RIPL',3)
        incrementNeuron('RIPR',3)
        incrementNeuron('SABD',1)
        incrementNeuron('URADL',1)

def PVT():
        incrementNeuron('AIBL',3)
        incrementNeuron('AIBR',5)
        incrementNeuron('AVKL',9)
        incrementNeuron('AVKR',7)
        incrementNeuron('AVL',2)
        incrementNeuron('DVC',2)
        incrementNeuron('PVPL',1)
        incrementNeuron('RIBL',1)
        incrementNeuron('RIBR',1)
        incrementNeuron('RIGL',2)
        incrementNeuron('RIGR',3)
        incrementNeuron('RIH',1)
        incrementNeuron('RMEV',1)
        incrementNeuron('RMFL',2)
        incrementNeuron('RMFR',3)
        incrementNeuron('SMBDR',1)

def PVWL():
        incrementNeuron('AVJL',1)
        incrementNeuron('PVCR',2)
        incrementNeuron('PVT',2)
        incrementNeuron('PVWR',1)
        incrementNeuron('VA12',1)


def PVWR():
        incrementNeuron('AVAR',1)
        incrementNeuron('AVDR',1)
        incrementNeuron('PVCR',2)
        incrementNeuron('PVT',1)
        incrementNeuron('VA12',1)

def RIAL():
        incrementNeuron('CEPVL',1)
        incrementNeuron('RIAR',1)
        incrementNeuron('RIVL',2)
        incrementNeuron('RIVR',4)
        incrementNeuron('RMDDL',12)
        incrementNeuron('RMDDR',7)
        incrementNeuron('RMDL',6)
        incrementNeuron('RMDR',6)
        incrementNeuron('RMDVL',9)
        incrementNeuron('RMDVR',11)
        incrementNeuron('SIADL',2)
        incrementNeuron('SMDDL',8)
        incrementNeuron('SMDDR',10)
        incrementNeuron('SMDVL',6)
        incrementNeuron('SMDVR',11)

def RIAR():
        incrementNeuron('CEPVR',1)
        incrementNeuron('IL1R',1)
        incrementNeuron('RIAL',4)
        incrementNeuron('RIVL',1)
        incrementNeuron('RMDDL',10)
        incrementNeuron('RMDDR',11)
        incrementNeuron('RMDL',3)
        incrementNeuron('RMDR',8)
        incrementNeuron('RMDVL',12)
        incrementNeuron('RMDVR',10)
        incrementNeuron('SAADR',1)
        incrementNeuron('SIADL',1)
        incrementNeuron('SIADR',1)
        incrementNeuron('SIAVL',1)
        incrementNeuron('SMDDL',7)
        incrementNeuron('SMDDR',7)
        incrementNeuron('SMDVL',13)
        incrementNeuron('SMDVR',7)

def RIBL():
        incrementNeuron('AIBR',2)
        incrementNeuron('AUAL',1)
        incrementNeuron('AVAL',1)
        incrementNeuron('AVBL',1)
        incrementNeuron('AVBR',2)
        incrementNeuron('AVDR',1)
        incrementNeuron('AVEL',1)
        incrementNeuron('AVER',5)
        incrementNeuron('BAGR',1)
        incrementNeuron('OLQDL',2)
        incrementNeuron('OLQVL',1)
        incrementNeuron('PVT',1)
        incrementNeuron('RIAL',3)
        incrementNeuron('RIBL',1)
        incrementNeuron('RIBR',3)
        incrementNeuron('RIGL',1)
        incrementNeuron('SIADL',1)
        incrementNeuron('SIAVL',1)
        incrementNeuron('SIBDL',1)
        incrementNeuron('SIBVL',1)
        incrementNeuron('SIBVR',1)
        incrementNeuron('SMBDL',1)
        incrementNeuron('SMDDL',1)
        incrementNeuron('SMDVR',4)

def RIBR():
        incrementNeuron('AIBL',1)
        incrementNeuron('AIZR',1)
        incrementNeuron('AVAR',2)
        incrementNeuron('AVBL',1)
        incrementNeuron('AVBR',1)
        incrementNeuron('AVEL',3)
        incrementNeuron('AVER',1)
        incrementNeuron('BAGL',1)
        incrementNeuron('OLQDR',2)
        incrementNeuron('OLQVR',1)
        incrementNeuron('PVT',1)
        incrementNeuron('RIAR',2)
        incrementNeuron('RIBL',3)
        incrementNeuron('RIBR',1)
        incrementNeuron('RIGR',2)
        incrementNeuron('RIH',1)
        incrementNeuron('SIADR',1)
        incrementNeuron('SIAVR',1)
        incrementNeuron('SIBDR',1)
        incrementNeuron('SIBVR',1)
        incrementNeuron('SMBDR',1)
        incrementNeuron('SMDDL',2)
        incrementNeuron('SMDDR',1)
        incrementNeuron('SMDVL',2)

def RICL():
        incrementNeuron('ADAR',1)
        incrementNeuron('ASHL',2)
        incrementNeuron('AVAL',5)
        incrementNeuron('AVAR',6)
        incrementNeuron('AVKL',1)
        incrementNeuron('AVKR',2)
        incrementNeuron('AWBR',1)
        incrementNeuron('RIML',1)
        incrementNeuron('RIMR',3)
        incrementNeuron('RIVR',1)
        incrementNeuron('RMFR',1)
        incrementNeuron('SMBDL',2)
        incrementNeuron('SMDDL',3)
        incrementNeuron('SMDDR',3)
        incrementNeuron('SMDVR',1)

def RICR():
        incrementNeuron('ADAR',1)
        incrementNeuron('ASHR',2)
        incrementNeuron('AVAL',5)
        incrementNeuron('AVAR',5)
        incrementNeuron('AVKL',1)
        incrementNeuron('SMBDR',1)
        incrementNeuron('SMDDL',4)
        incrementNeuron('SMDDR',3)
        incrementNeuron('SMDVL',2)
        incrementNeuron('SMDVR',1)

def RID():
        incrementNeuron('ALA',1)
        incrementNeuron('AS2',1)
        incrementNeuron('AVBL',1)
        incrementNeuron('AVBR',2)
        incrementNeuron('DA6',3)
        incrementNeuron('DA9',1)
        incrementNeuron('DB1',1)
        incrementNeuron('DD1',4)
        incrementNeuron('DD2',4)
        incrementNeuron('DD3',3)
        incrementNeuron('MDL14',-2)
        incrementNeuron('MDL21',-3)
        incrementNeuron('PDB',2)
        incrementNeuron('VD13',1)
        incrementNeuron('VD5',1)

def RIFL():
        incrementNeuron('ALML',2)
        incrementNeuron('AVBL',10)
        incrementNeuron('AVBR',1)
        incrementNeuron('AVG',1)
        incrementNeuron('AVHR',1)
        incrementNeuron('AVJR',2)
        incrementNeuron('PVPL',3)
        incrementNeuron('RIML',4)
        incrementNeuron('VD1',1)

def RIFR():
        incrementNeuron('ASHR',2)
        incrementNeuron('AVBL',1)
        incrementNeuron('AVBR',17)
        incrementNeuron('AVFL',1)
        incrementNeuron('AVG',1)
        incrementNeuron('AVHL',1)
        incrementNeuron('AVJL',1)
        incrementNeuron('AVJR',2)
        incrementNeuron('HSNR',1)
        incrementNeuron('PVCL',1)
        incrementNeuron('PVCR',1)
        incrementNeuron('PVPR',4)
        incrementNeuron('RIMR',4)
        incrementNeuron('RIPR',1)

def RIGL():
        incrementNeuron('AIBR',3)
        incrementNeuron('AIZR',1)
        incrementNeuron('ALNL',1)
        incrementNeuron('AQR',2)
        incrementNeuron('AVEL',1)
        incrementNeuron('AVER',1)
        incrementNeuron('AVKL',1)
        incrementNeuron('AVKR',2)
        incrementNeuron('BAGR',2)
        incrementNeuron('DVC',1)
        incrementNeuron('OLLL',1)
        incrementNeuron('OLQDL',1)
        incrementNeuron('OLQVL',1)
        incrementNeuron('RIBL',2)
        incrementNeuron('RIGR',3)
        incrementNeuron('RIR',2)
        incrementNeuron('RMEL',2)
        incrementNeuron('RMHR',3)
        incrementNeuron('URYDL',1)
        incrementNeuron('URYVL',1)
        incrementNeuron('VB2',1)
        incrementNeuron('VD1',2)

def RIGR():
        incrementNeuron('AIBL',3)
        incrementNeuron('ALNR',1)
        incrementNeuron('AQR',1)
        incrementNeuron('AVER',2)
        incrementNeuron('AVKL',4)
        incrementNeuron('AVKR',2)
        incrementNeuron('BAGL',1)
        incrementNeuron('OLLR',1)
        incrementNeuron('OLQDR',1)
        incrementNeuron('OLQVR',1)
        incrementNeuron('RIBR',2)
        incrementNeuron('RIGL',3)
        incrementNeuron('RIR',1)
        incrementNeuron('RMHL',4)
        incrementNeuron('URYDR',1)
        incrementNeuron('URYVR',1)

def RIH():
        incrementNeuron('ADFR',1)
        incrementNeuron('AIZL',4)
        incrementNeuron('AIZR',4)
        incrementNeuron('AUAR',1)
        incrementNeuron('BAGR',1)
        incrementNeuron('CEPDL',2)
        incrementNeuron('CEPDR',2)
        incrementNeuron('CEPVL',2)
        incrementNeuron('CEPVR',2)
        incrementNeuron('FLPL',1)
        incrementNeuron('IL2L',2)
        incrementNeuron('IL2R',1)
        incrementNeuron('OLQDL',4)
        incrementNeuron('OLQDR',2)
        incrementNeuron('OLQVL',1)
        incrementNeuron('OLQVR',6)
        incrementNeuron('RIAL',10)
        incrementNeuron('RIAR',8)
        incrementNeuron('RIBL',5)
        incrementNeuron('RIBR',4)
        incrementNeuron('RIPL',4)
        incrementNeuron('RIPR',6)
        incrementNeuron('RMER',2)
        incrementNeuron('RMEV',1)
        incrementNeuron('URYVR',1)

def RIML():
        incrementNeuron('AIBR',1)
        incrementNeuron('AIYL',1)
        incrementNeuron('AVAL',1)
        incrementNeuron('AVAR',2)
        incrementNeuron('AVBL',2)
        incrementNeuron('AVBR',3)
        incrementNeuron('AVEL',2)
        incrementNeuron('AVER',3)
        incrementNeuron('MDR05',2)
        incrementNeuron('MVR05',2)
        incrementNeuron('RIBL',1)
        incrementNeuron('RIS',1)
        incrementNeuron('RMDL',1)
        incrementNeuron('RMDR',1)
        incrementNeuron('RMFR',1)
        incrementNeuron('SAADR',1)
        incrementNeuron('SAAVL',3)
        incrementNeuron('SAAVR',2)
        incrementNeuron('SMDDR',5)
        incrementNeuron('SMDVL',1)

def RIMR():
        incrementNeuron('ADAR',1)
        incrementNeuron('AIBL',4)
        incrementNeuron('AIBL',1)
        incrementNeuron('AIYR',1)
        incrementNeuron('AVAL',5)
        incrementNeuron('AVAR',1)
        incrementNeuron('AVBL',2)
        incrementNeuron('AVBR',5)
        incrementNeuron('AVEL',3)
        incrementNeuron('AVER',2)
        incrementNeuron('AVJL',1)
        incrementNeuron('AVKL',1)
        incrementNeuron('MDL05',1)
        incrementNeuron('MDL07',1)
        incrementNeuron('MVL05',1)
        incrementNeuron('MVL07',1)
        incrementNeuron('RIBR',1)
        incrementNeuron('RIS',2)
        incrementNeuron('RMDL',1)
        incrementNeuron('RMDR',1)
        incrementNeuron('RMFL',1)
        incrementNeuron('RMFR',1)
        incrementNeuron('SAAVL',3)
        incrementNeuron('SAAVR',3)
        incrementNeuron('SMDDL',2)
        incrementNeuron('SMDDR',4)

def RIPL():
        incrementNeuron('OLQDL',1)
        incrementNeuron('OLQDR',1)
        incrementNeuron('RMED',1)

def RIPR():
        incrementNeuron('OLQDL',1)
        incrementNeuron('OLQDR',1)
        incrementNeuron('RMED',1)

def RIR():
        incrementNeuron('AFDR',1)
        incrementNeuron('AIZL',3)
        incrementNeuron('AIZR',5)
        incrementNeuron('AUAL',1)
        incrementNeuron('AWBR',1)
        incrementNeuron('BAGL',1)
        incrementNeuron('BAGR',2)
        incrementNeuron('DVA',2)
        incrementNeuron('HSNL',1)
        incrementNeuron('PVPL',1)
        incrementNeuron('RIAL',5)
        incrementNeuron('RIAR',1)
        incrementNeuron('RIGL',1)
        incrementNeuron('URXL',5)
        incrementNeuron('URXR',1)

def RIS():
        incrementNeuron('AIBR',1)
        incrementNeuron('AVEL',7)
        incrementNeuron('AVER',7)
        incrementNeuron('AVJL',1)
        incrementNeuron('AVKL',1)
        incrementNeuron('AVKR',4)
        incrementNeuron('AVL',2)
        incrementNeuron('CEPDR',1)
        incrementNeuron('CEPVL',2)
        incrementNeuron('CEPVR',1)
        incrementNeuron('DB1',1)
        incrementNeuron('OLLR',1)
        incrementNeuron('RIBL',3)
        incrementNeuron('RIBR',5)
        incrementNeuron('RIML',2)
        incrementNeuron('RIMR',5)
        incrementNeuron('RMDDL',1)
        incrementNeuron('RMDL',2)
        incrementNeuron('RMDR',4)
        incrementNeuron('SMDDL',1)
        incrementNeuron('SMDDR',3)
        incrementNeuron('SMDVL',1)
        incrementNeuron('SMDVR',1)
        incrementNeuron('URYVR',1)

def RIVL():
        incrementNeuron('AIBL',1)
        incrementNeuron('MVR05',-2)
        incrementNeuron('MVR06',-2)
        incrementNeuron('MVR08',-3)
        incrementNeuron('RIAL',1)
        incrementNeuron('RIAR',1)
        incrementNeuron('RIVR',2)
        incrementNeuron('RMDL',2)
        incrementNeuron('SAADR',3)
        incrementNeuron('SDQR',2)
        incrementNeuron('SIAVR',2)
        incrementNeuron('SMDDR',1)
        incrementNeuron('SMDVL',1)

def RIVR():
        incrementNeuron('AIBR',1)
        incrementNeuron('MVL05',-2)
        incrementNeuron('MVL06',-2)
        incrementNeuron('MVL08',-2)
        incrementNeuron('MVR04',-2)
        incrementNeuron('MVR06',-2)
        incrementNeuron('RIAL',2)
        incrementNeuron('RIAR',1)
        incrementNeuron('RIVL',2)
        incrementNeuron('RMDDL',1)
        incrementNeuron('RMDR',1)
        incrementNeuron('RMDVR',1)
        incrementNeuron('RMEV',1)
        incrementNeuron('SAADL',2)
        incrementNeuron('SDQR',2)
        incrementNeuron('SIAVL',2)
        incrementNeuron('SMDDL',2)
        incrementNeuron('SMDVR',4)

def RMDDL():
        incrementNeuron('MDR01',1)
        incrementNeuron('MDR02',1)
        incrementNeuron('MDR03',1)
        incrementNeuron('MDR04',1)
        incrementNeuron('MDR08',2)
        incrementNeuron('MVR01',1)
        incrementNeuron('OLQVL',1)
        incrementNeuron('RMDL',1)
        incrementNeuron('RMDVL',1)
        incrementNeuron('RMDVR',7)
        incrementNeuron('SMDDL',1)

def RMDDR():
        incrementNeuron('MDL01',1)
        incrementNeuron('MDL02',1)
        incrementNeuron('MDL03',2)
        incrementNeuron('MDL04',1)
        incrementNeuron('MDR04',1)
        incrementNeuron('MVR01',1)
        incrementNeuron('MVR02',1)
        incrementNeuron('OLQVR',1)
        incrementNeuron('RMDVL',12)
        incrementNeuron('RMDVR',1)
        incrementNeuron('SAADR',1)
        incrementNeuron('SMDDR',1)
        incrementNeuron('URYDL',1)

def RMDL():
        incrementNeuron('MDL03',1)
        incrementNeuron('MDL05',2)
        incrementNeuron('MDR01',1)
        incrementNeuron('MDR03',1)
        incrementNeuron('MVL01',1)
        incrementNeuron('MVR01',1)
        incrementNeuron('MVR03',1)
        incrementNeuron('MVR05',2)
        incrementNeuron('MVR07',1)
        incrementNeuron('OLLR',2)
        incrementNeuron('RIAL',4)
        incrementNeuron('RIAR',3)
        incrementNeuron('RMDDL',1)
        incrementNeuron('RMDDR',1)
        incrementNeuron('RMDR',3)
        incrementNeuron('RMDVL',1)
        incrementNeuron('RMER',1)
        incrementNeuron('RMFL',1)

def RMDR():
        incrementNeuron('AVKL',1)
        incrementNeuron('MDL03',1)
        incrementNeuron('MDL05',1)
        incrementNeuron('MDR05',1)
        incrementNeuron('MVL03',1)
        incrementNeuron('MVL05',1)
        incrementNeuron('RIAL',3)
        incrementNeuron('RIAR',7)
        incrementNeuron('RIMR',2)
        incrementNeuron('RIS',1)
        incrementNeuron('RMDDL',1)
        incrementNeuron('RMDL',1)
        incrementNeuron('RMDVR',1)

def RMDVL():
        incrementNeuron('AVER',1)
        incrementNeuron('MDR01',1)
        incrementNeuron('MVL04',1)
        incrementNeuron('MVR01',1)
        incrementNeuron('MVR02',1)
        incrementNeuron('MVR03',1)
        incrementNeuron('MVR04',1)
        incrementNeuron('MVR05',1)
        incrementNeuron('MVR06',1)
        incrementNeuron('MVR08',1)
        incrementNeuron('OLQDL',1)
        incrementNeuron('RMDDL',1)
        incrementNeuron('RMDDR',6)
        incrementNeuron('RMDL',1)
        incrementNeuron('RMDVR',1)
        incrementNeuron('SAAVL',1)
        incrementNeuron('SMDVL',1)

def RMDVR():
        incrementNeuron('AVEL',1)
        incrementNeuron('AVER',1)
        incrementNeuron('MDL01',1)
        incrementNeuron('MVL01',1)
        incrementNeuron('MVL02',1)
        incrementNeuron('MVL03',1)
        incrementNeuron('MVL04',1)
        incrementNeuron('MVL05',1)
        incrementNeuron('MVL06',1)
        incrementNeuron('MVL08',1)
        incrementNeuron('MVR04',1)
        incrementNeuron('MVR06',1)
        incrementNeuron('MVR08',1)
        incrementNeuron('OLQDR',1)
        incrementNeuron('RMDDL',4)
        incrementNeuron('RMDDR',1)
        incrementNeuron('RMDR',1)
        incrementNeuron('RMDVL',1)
        incrementNeuron('SAAVR',1)
        incrementNeuron('SIBDR',1)
        incrementNeuron('SIBVR',1)
        incrementNeuron('SMDVR',1)

def RMED():
        incrementNeuron('IL1VL',1)
        incrementNeuron('MVL02',-4)
        incrementNeuron('MVL04',-4)
        incrementNeuron('MVL06',-4)
        incrementNeuron('MVR02',-4)
        incrementNeuron('MVR04',-4)
        incrementNeuron('RIBL',1)
        incrementNeuron('RIBR',1)
        incrementNeuron('RIPL',1)
        incrementNeuron('RIPR',1)
        incrementNeuron('RMEV',2)

def RMEL():
        incrementNeuron('MDR01',-5)
        incrementNeuron('MDR03',-5)
        incrementNeuron('MVR01',-5)
        incrementNeuron('MVR03',-5)
        incrementNeuron('RIGL',1)
        incrementNeuron('RMEV',1)

def RMER():
        incrementNeuron('MDL01',-7)
        incrementNeuron('MDL03',-7)
        incrementNeuron('MVL01',-7)
        incrementNeuron('RMEV',1)

def RMEV():
        incrementNeuron('AVEL',1)
        incrementNeuron('AVER',1)
        incrementNeuron('IL1DL',1)
        incrementNeuron('IL1DR',1)
        incrementNeuron('MDL02',-3)
        incrementNeuron('MDL04',-3)
        incrementNeuron('MDL06',-3)
        incrementNeuron('MDR02',-3)
        incrementNeuron('MDR04',-3)
        incrementNeuron('RMED',2)
        incrementNeuron('RMEL',1)
        incrementNeuron('RMER',1)
        incrementNeuron('SMDDR',1)

def RMFL():
        incrementNeuron('AVKL',4)
        incrementNeuron('AVKR',4)
        incrementNeuron('MDR03',1)
        incrementNeuron('MVR01',1)
        incrementNeuron('MVR03',1)
        incrementNeuron('PVT',1)
        incrementNeuron('RIGR',1)
        incrementNeuron('RMDR',3)
        incrementNeuron('RMGR',1)
        incrementNeuron('URBR',1)

def RMFR():
        incrementNeuron('AVKL',3)
        incrementNeuron('AVKR',3)
        incrementNeuron('RMDL',2)

def RMGL():
        incrementNeuron('ADAL',1)
        incrementNeuron('ADLL',1)
        incrementNeuron('AIBR',1)
        incrementNeuron('ALML',1)
        incrementNeuron('ALNL',1)
        incrementNeuron('ASHL',2)
        incrementNeuron('ASKL',2)
        incrementNeuron('AVAL',1)
        incrementNeuron('AVBR',2)
        incrementNeuron('AVEL',2)
        incrementNeuron('AWBL',1)
        incrementNeuron('CEPDL',1)
        incrementNeuron('IL2L',1)
        incrementNeuron('MDL05',2)
        incrementNeuron('MVL05',2)
        incrementNeuron('RID',1)
        incrementNeuron('RMDL',1)
        incrementNeuron('RMDR',3)
        incrementNeuron('RMDVL',3)
        incrementNeuron('RMHL',3)
        incrementNeuron('RMHR',1)
        incrementNeuron('SIAVL',1)
        incrementNeuron('SIBVL',3)
        incrementNeuron('SIBVR',1)
        incrementNeuron('SMBVL',1)
        incrementNeuron('URXL',2)

def RMGR():
        incrementNeuron('ADAR',1)
        incrementNeuron('AIMR',1)
        incrementNeuron('ALNR',1)
        incrementNeuron('ASHR',2)
        incrementNeuron('ASKR',1)
        incrementNeuron('AVAR',1)
        incrementNeuron('AVBR',1)
        incrementNeuron('AVDL',1)
        incrementNeuron('AVER',3)
        incrementNeuron('AVJL',1)
        incrementNeuron('AWBR',1)
        incrementNeuron('IL2R',1)
        incrementNeuron('MDR05',1)
        incrementNeuron('MVR05',1)
        incrementNeuron('MVR07',1)
        incrementNeuron('RIR',1)
        incrementNeuron('RMDL',4)
        incrementNeuron('RMDR',2)
        incrementNeuron('RMDVR',5)
        incrementNeuron('RMHR',1)
        incrementNeuron('URXR',2)

def RMHL():
        incrementNeuron('MDR01',2)
        incrementNeuron('MDR03',3)
        incrementNeuron('MVR01',2)
        incrementNeuron('RMDR',1)
        incrementNeuron('RMGL',3)
        incrementNeuron('SIBVR',1)

def RMHR():
        incrementNeuron('MDL01',2)
        incrementNeuron('MDL03',2)
        incrementNeuron('MDL05',2)
        incrementNeuron('MVL01',2)
        incrementNeuron('RMER',1)
        incrementNeuron('RMGL',1)
        incrementNeuron('RMGR',1)

def SAADL():
        incrementNeuron('AIBL',1)
        incrementNeuron('AVAL',6)
        incrementNeuron('RIML',3)
        incrementNeuron('RIMR',6)
        incrementNeuron('RMGR',1)
        incrementNeuron('SMBDL',1)

def SAADR():
        incrementNeuron('AIBR',1)
        incrementNeuron('AVAR',3)
        incrementNeuron('OLLL',1)
        incrementNeuron('RIML',4)
        incrementNeuron('RIMR',5)
        incrementNeuron('RMDDR',1)
        incrementNeuron('RMFL',1)
        incrementNeuron('RMGL',1)

def SAAVL():
        incrementNeuron('AIBL',1)
        incrementNeuron('ALNL',1)
        incrementNeuron('AVAL',16)
        incrementNeuron('OLLR',1)
        incrementNeuron('RIML',2)
        incrementNeuron('RIMR',12)
        incrementNeuron('RMDVL',2)
        incrementNeuron('RMFR',2)
        incrementNeuron('SMBVR',3)
        incrementNeuron('SMDDR',8)

def SAAVR():
        incrementNeuron('AVAR',13)
        incrementNeuron('RIML',5)
        incrementNeuron('RIMR',2)
        incrementNeuron('RMDVR',1)
        incrementNeuron('SMBVL',2)
        incrementNeuron('SMDDL',6)

def SABD():
        incrementNeuron('AVAL',4)
        incrementNeuron('VA2',4)
        incrementNeuron('VA3',2)
        incrementNeuron('VA4',1)

def SABVL():
        incrementNeuron('AVAR',3)
        incrementNeuron('DA1',2)
        incrementNeuron('DA2',1)

def SABVR():
        incrementNeuron('AVAL',1)
        incrementNeuron('AVAR',1)
        incrementNeuron('DA1',3)

def SDQL():
        incrementNeuron('ALML',2)
        incrementNeuron('AVAL',1)
        incrementNeuron('AVAR',3)
        incrementNeuron('AVEL',1)
        incrementNeuron('FLPL',1)
        incrementNeuron('RICR',1)
        incrementNeuron('RIS',3)
        incrementNeuron('RMFL',1)
        incrementNeuron('SDQR',1)

def SDQR():
        incrementNeuron('ADLL',1)
        incrementNeuron('AIBL',2)
        incrementNeuron('AVAL',3)
        incrementNeuron('AVBL',7)
        incrementNeuron('AVBR',4)
        incrementNeuron('DVA',3)
        incrementNeuron('RICR',1)
        incrementNeuron('RIVL',2)
        incrementNeuron('RIVR',2)
        incrementNeuron('RMHL',2)
        incrementNeuron('RMHR',1)
        incrementNeuron('SDQL',1)
        incrementNeuron('SIBVL',1)

def SIADL():
        incrementNeuron('RIBL',1)

def SIADR():
        incrementNeuron('RIBR',1)

def SIAVL():
        incrementNeuron('RIBL',1)

def SIAVR():
        incrementNeuron('RIBR',1)

def SIBDL():
        incrementNeuron('RIBL',1)
        incrementNeuron('SIBVL',1)

def SIBDR():
        incrementNeuron('AIML',1)
        incrementNeuron('RIBR',1)
        incrementNeuron('SIBVR',1)

def SIBVL():
        incrementNeuron('AVBL',1)
        incrementNeuron('AVBR',1)
        incrementNeuron('RIBL',1)
        incrementNeuron('SDQR',1)
        incrementNeuron('SIBDL',1)

def SIBVR():
        incrementNeuron('RIBL',1)
        incrementNeuron('RIBR',1)
        incrementNeuron('RMHL',1)
        incrementNeuron('SIBDR',1)

def SMBDL():
        incrementNeuron('AVAR',1)
        incrementNeuron('AVKL',1)
        incrementNeuron('AVKR',1)
        incrementNeuron('MDR01',2)
        incrementNeuron('MDR02',2)
        incrementNeuron('MDR03',2)
        incrementNeuron('MDR04',2)
        incrementNeuron('MDR06',3)
        incrementNeuron('RIBL',1)
        incrementNeuron('RMED',3)
        incrementNeuron('SAADL',1)
        incrementNeuron('SAAVR',1)

def SMBDR():
        incrementNeuron('ALNL',1)
        incrementNeuron('AVAL',1)
        incrementNeuron('AVKL',1)
        incrementNeuron('AVKR',2)
        incrementNeuron('MDL02',1)
        incrementNeuron('MDL03',1)
        incrementNeuron('MDL04',1)
        incrementNeuron('MDL06',2)
        incrementNeuron('MDR04',1)
        incrementNeuron('MDR08',1)
        incrementNeuron('RIBR',1)
        incrementNeuron('RMED',4)
        incrementNeuron('SAAVL',3)

def SMBVL():
        incrementNeuron('MVL01',1)
        incrementNeuron('MVL02',1)
        incrementNeuron('MVL03',1)
        incrementNeuron('MVL04',1)
        incrementNeuron('MVL05',1)
        incrementNeuron('MVL06',1)
        incrementNeuron('MVL08',1)
        incrementNeuron('PLNL',1)
        incrementNeuron('RMEV',5)
        incrementNeuron('SAADL',3)
        incrementNeuron('SAAVR',2)

def SMBVR():
        incrementNeuron('AVKL',1)
        incrementNeuron('AVKR',1)
        incrementNeuron('MVR01',1)
        incrementNeuron('MVR02',1)
        incrementNeuron('MVR03',1)
        incrementNeuron('MVR04',1)
        incrementNeuron('MVR06',1)
        incrementNeuron('MVR07',1)
        incrementNeuron('RMEV',3)
        incrementNeuron('SAADR',4)
        incrementNeuron('SAAVL',3)

def SMDDL():
        incrementNeuron('MDL04',1)
        incrementNeuron('MDL06',1)
        incrementNeuron('MDL08',1)
        incrementNeuron('MDR02',1)
        incrementNeuron('MDR03',1)
        incrementNeuron('MDR04',1)
        incrementNeuron('MDR05',1)
        incrementNeuron('MDR06',1)
        incrementNeuron('MDR07',1)
        incrementNeuron('MVL02',1)
        incrementNeuron('MVL04',1)
        incrementNeuron('RIAL',1)
        incrementNeuron('RIAR',1)
        incrementNeuron('RIBL',1)
        incrementNeuron('RIBR',1)
        incrementNeuron('RIS',1)
        incrementNeuron('RMDDL',1)
        incrementNeuron('SMDVR',2)

def SMDDR():
        incrementNeuron('MDL04',1)
        incrementNeuron('MDL05',1)
        incrementNeuron('MDL06',1)
        incrementNeuron('MDL08',1)
        incrementNeuron('MDR04',1)
        incrementNeuron('MDR06',1)
        incrementNeuron('MVR02',1)
        incrementNeuron('RIAL',2)
        incrementNeuron('RIAR',1)
        incrementNeuron('RIBR',1)
        incrementNeuron('RIS',1)
        incrementNeuron('RMDDR',1)
        incrementNeuron('VD1',1)

def SMDVL():
        incrementNeuron('MVL03',1)
        incrementNeuron('MVL06',1)
        incrementNeuron('MVR02',1)
        incrementNeuron('MVR03',1)
        incrementNeuron('MVR04',1)
        incrementNeuron('MVR06',1)
        incrementNeuron('PVR',1)
        incrementNeuron('RIAL',3)
        incrementNeuron('RIAR',8)
        incrementNeuron('RIBR',2)
        incrementNeuron('RIS',1)
        incrementNeuron('RIVL',2)
        incrementNeuron('RMDDR',1)
        incrementNeuron('RMDVL',1)
        incrementNeuron('SMDDR',4)
        incrementNeuron('SMDVR',1)

def SMDVR():
        incrementNeuron('MVL02',1)
        incrementNeuron('MVL03',1)
        incrementNeuron('MVL04',1)
        incrementNeuron('MVR07',1)
        incrementNeuron('RIAL',7)
        incrementNeuron('RIAR',5)
        incrementNeuron('RIBL',2)
        incrementNeuron('RIVR',1)
        incrementNeuron('RIVR',2)
        incrementNeuron('RMDDL',1)
        incrementNeuron('RMDVR',1)
        incrementNeuron('SMDDL',2)
        incrementNeuron('SMDVL',1)
        incrementNeuron('VB1',1)

def URADL():
        incrementNeuron('IL1DL',2)
        incrementNeuron('MDL02',2)
        incrementNeuron('MDL03',2)
        incrementNeuron('MDL04',2)
        incrementNeuron('RIPL',3)
        incrementNeuron('RMEL',1)

def URADR():
        incrementNeuron('IL1DR',1)
        incrementNeuron('MDR01',3)
        incrementNeuron('MDR02',2)
        incrementNeuron('MDR03',3)
        incrementNeuron('RIPR',3)
        incrementNeuron('RMDVR',1)
        incrementNeuron('RMED',1)
        incrementNeuron('RMER',1)
        incrementNeuron('URYDR',1)

def URAVL():
        incrementNeuron('MVL01',2)
        incrementNeuron('MVL02',2)
        incrementNeuron('MVL03',3)
        incrementNeuron('MVL04',2)
        incrementNeuron('RIPL',3)
        incrementNeuron('RMEL',1)
        incrementNeuron('RMER',1)
        incrementNeuron('RMEV',2)

def URAVR():
        incrementNeuron('IL1R',1)
        incrementNeuron('MVR01',2)
        incrementNeuron('MVR02',2)
        incrementNeuron('MVR03',2)
        incrementNeuron('MVR04',2)
        incrementNeuron('RIPR',3)
        incrementNeuron('RMDVL',1)
        incrementNeuron('RMER',2)
        incrementNeuron('RMEV',2)

def URBL():
        incrementNeuron('AVBL',1)
        incrementNeuron('CEPDL',1)
        incrementNeuron('IL1L',1)
        incrementNeuron('OLQDL',1)
        incrementNeuron('OLQVL',1)
        incrementNeuron('RICR',1)
        incrementNeuron('RMDDR',1)
        incrementNeuron('SIAVL',1)
        incrementNeuron('SMBDR',1)
        incrementNeuron('URXL',2)

def URBR():
        incrementNeuron('ADAR',1)
        incrementNeuron('AVBR',1)
        incrementNeuron('CEPDR',1)
        incrementNeuron('IL1R',3)
        incrementNeuron('IL2R',1)
        incrementNeuron('OLQDR',1)
        incrementNeuron('OLQVR',1)
        incrementNeuron('RICR',1)
        incrementNeuron('RMDL',1)
        incrementNeuron('RMDR',1)
        incrementNeuron('RMFL',1)
        incrementNeuron('SIAVR',2)
        incrementNeuron('SMBDL',1)
        incrementNeuron('URXR',4)

def URXL():
        incrementNeuron('ASHL',1)
        incrementNeuron('AUAL',5)
        incrementNeuron('AVBL',1)
        incrementNeuron('AVEL',4)
        incrementNeuron('AVJR',1)
        incrementNeuron('RIAL',8)
        incrementNeuron('RICL',1)
        incrementNeuron('RIGL',3)
        incrementNeuron('RMGL',2)
        incrementNeuron('RMGL',1)

def URXR():
        incrementNeuron('AUAR',4)
        incrementNeuron('AVBL',1)
        incrementNeuron('AVBR',2)
        incrementNeuron('AVER',2)
        incrementNeuron('IL2R',1)
        incrementNeuron('OLQVR',1)
        incrementNeuron('RIAR',3)
        incrementNeuron('RIGR',2)
        incrementNeuron('RIPR',3)
        incrementNeuron('RMDR',1)
        incrementNeuron('RMGR',2)
        incrementNeuron('SIAVR',1)

def URYDL():
        incrementNeuron('AVAL',1)
        incrementNeuron('AVER',2)
        incrementNeuron('RIBL',1)
        incrementNeuron('RIGL',1)
        incrementNeuron('RMDDR',4)
        incrementNeuron('RMDVL',6)
        incrementNeuron('SMDDL',1)
        incrementNeuron('SMDDR',1)

def URYDR():
        incrementNeuron('AVAR',1)
        incrementNeuron('AVEL',2)
        incrementNeuron('AVER',2)
        incrementNeuron('RIBR',1)
        incrementNeuron('RIGR',1)
        incrementNeuron('RMDDL',3)
        incrementNeuron('RMDVR',5)
        incrementNeuron('SMDDL',4)

def URYVL():
        incrementNeuron('AVAR',1)
        incrementNeuron('AVBR',1)
        incrementNeuron('AVER',5)
        incrementNeuron('IL1VL',1)
        incrementNeuron('RIAL',1)
        incrementNeuron('RIBL',2)
        incrementNeuron('RIGL',1)
        incrementNeuron('RIH',1)
        incrementNeuron('RIS',1)
        incrementNeuron('RMDDL',4)
        incrementNeuron('RMDVR',2)
        incrementNeuron('SIBVR',1)
        incrementNeuron('SMDVR',4)

def URYVR():
        incrementNeuron('AVAL',2)
        incrementNeuron('AVEL',6)
        incrementNeuron('IL1VR',1)
        incrementNeuron('RIAR',1)
        incrementNeuron('RIBR',1)
        incrementNeuron('RIGR',1)
        incrementNeuron('RMDDR',6)
        incrementNeuron('RMDVL',4)
        incrementNeuron('SIBDR',1)
        incrementNeuron('SIBVL',1)
        incrementNeuron('SMDVL',3)

def VA1():
        incrementNeuron('AVAL',3)
        incrementNeuron('DA2',2)
        incrementNeuron('DD1',9)
        incrementNeuron('MVL07',3)
        incrementNeuron('MVL08',3)
        incrementNeuron('MVR07',3)
        incrementNeuron('MVR08',3)
        incrementNeuron('VD1',2)

def VA2():
        incrementNeuron('AVAL',5)
        incrementNeuron('DD1',13)
        incrementNeuron('MVL07',5)
        incrementNeuron('MVL10',5)
        incrementNeuron('MVR07',5)
        incrementNeuron('MVR10',5)
        incrementNeuron('SABD',3)
        incrementNeuron('VA3',2)
        incrementNeuron('VB1',2)
        incrementNeuron('VD1',2)
        incrementNeuron('VD1',1)
        incrementNeuron('VD2',11)

def VA3():
        incrementNeuron('AS1',1)
        incrementNeuron('AVAL',1)
        incrementNeuron('AVAR',2)
        incrementNeuron('DD1',18)
        incrementNeuron('DD2',11)
        incrementNeuron('MVL09',5)
        incrementNeuron('MVL10',5)
        incrementNeuron('MVL12',5)
        incrementNeuron('MVR09',5)
        incrementNeuron('MVR10',5)
        incrementNeuron('MVR12',5)
        incrementNeuron('SABD',2)
        incrementNeuron('VA4',1)
        incrementNeuron('VD2',3)
        incrementNeuron('VD3',3)

def VA4():
        incrementNeuron('AS2',2)
        incrementNeuron('AVAL',1)
        incrementNeuron('AVAR',2)
        incrementNeuron('AVDL',1)
        incrementNeuron('DA5',1)
        incrementNeuron('DD2',21)
        incrementNeuron('MVL11',6)
        incrementNeuron('MVL12',6)
        incrementNeuron('MVR11',6)
        incrementNeuron('MVR12',6)
        incrementNeuron('SABD',1)
        incrementNeuron('VB3',2)
        incrementNeuron('VD4',3)
        
def VA5():
        incrementNeuron('AS3',2)
        incrementNeuron('AVAL',5)
        incrementNeuron('AVAR',3)
        incrementNeuron('DA5',2)
        incrementNeuron('DD2',5)
        incrementNeuron('DD3',13)
        incrementNeuron('MVL11',5)
        incrementNeuron('MVL14',5)
        incrementNeuron('MVR11',5)
        incrementNeuron('MVR14',5)
        incrementNeuron('VD5',2)

def VA6():
        incrementNeuron('AVAL',6)
        incrementNeuron('AVAR',2)
        incrementNeuron('DD3',24)
        incrementNeuron('MVL13',5)
        incrementNeuron('MVL14',5)
        incrementNeuron('MVR13',5)
        incrementNeuron('MVR14',5)
        incrementNeuron('VB5',2)
        incrementNeuron('VD5',1)
        incrementNeuron('VD6',2)

def VA7():
        incrementNeuron('AS5',1)
        incrementNeuron('AVAL',2)
        incrementNeuron('AVAR',4)
        incrementNeuron('DD3',3)
        incrementNeuron('DD4',12)
        incrementNeuron('MVL13',4)
        incrementNeuron('MVL15',4)
        incrementNeuron('MVL16',4)
        incrementNeuron('MVR13',4)
        incrementNeuron('MVR15',4)
        incrementNeuron('MVR16',4)
        incrementNeuron('MVULVA',4)
        incrementNeuron('VB3',1)
        incrementNeuron('VD7',9)

def VA8():
        incrementNeuron('AS6',1)
        incrementNeuron('AVAL',10)
        incrementNeuron('AVAR',4)
        incrementNeuron('AVBR',1)
        incrementNeuron('DD4',21)
        incrementNeuron('MVL15',6)
        incrementNeuron('MVL16',6)
        incrementNeuron('MVR15',6)
        incrementNeuron('MVR16',6)
        incrementNeuron('PDER',1)
        incrementNeuron('PVCR',2)
        incrementNeuron('VA8',1)
        incrementNeuron('VA9',1)
        incrementNeuron('VB6',1)
        incrementNeuron('VB8',1)
        incrementNeuron('VB8',3)
        incrementNeuron('VB9',3)
        incrementNeuron('VD7',5)
        incrementNeuron('VD8',5)
        incrementNeuron('VD8',1)

def VA9():
        incrementNeuron('AVAL',1)
        incrementNeuron('AVBR',1)
        incrementNeuron('DD4',3)
        incrementNeuron('DD5',15)
        incrementNeuron('DVB',1)
        incrementNeuron('DVC',1)
        incrementNeuron('MVL15',5)
        incrementNeuron('MVL18',5)
        incrementNeuron('MVR15',5)
        incrementNeuron('MVR18',5)
        incrementNeuron('PVCR',1)
        incrementNeuron('PVT',1)
        incrementNeuron('VB8',6)
        incrementNeuron('VB8',1)
        incrementNeuron('VB9',4)
        incrementNeuron('VD7',1)
        incrementNeuron('VD9',10)


def VA10():
        incrementNeuron('AVAL',1)
        incrementNeuron('AVAR',1)
        incrementNeuron('MVL17',5)
        incrementNeuron('MVL18',5)
        incrementNeuron('MVR17',5)
        incrementNeuron('MVR18',5)

def VA11():
        incrementNeuron('AVAL',1)
        incrementNeuron('AVAR',7)
        incrementNeuron('DD6',10)
        incrementNeuron('MVL19',5)
        incrementNeuron('MVL20',5)
        incrementNeuron('MVR19',5)
        incrementNeuron('MVR20',5)
        incrementNeuron('PVNR',2)
        incrementNeuron('VB10',1)
        incrementNeuron('VD12',4)

def VA12():
        incrementNeuron('AS11',2)
        incrementNeuron('AVAR',1)
        incrementNeuron('DA8',3)
        incrementNeuron('DA9',5)
        incrementNeuron('DB7',4)
        incrementNeuron('DD6',2)
        incrementNeuron('LUAL',2)
        incrementNeuron('MVL21',5)
        incrementNeuron('MVL22',5)
        incrementNeuron('MVL23',5)
        incrementNeuron('MVR21',5)
        incrementNeuron('MVR22',5)
        incrementNeuron('MVR23',5)
        incrementNeuron('MVR24',5)
        incrementNeuron('PHCL',1)
        incrementNeuron('PHCR',1)
        incrementNeuron('PVCL',2)
        incrementNeuron('PVCR',3)
        incrementNeuron('VA11',1)
        incrementNeuron('VB11',1)
        incrementNeuron('VD12',3)
        incrementNeuron('VD13',11)

def VB1():
        incrementNeuron('AIBR',1)
        incrementNeuron('AVBL',1)
        incrementNeuron('AVKL',4)
        incrementNeuron('DB2',2)
        incrementNeuron('DD1',1)
        incrementNeuron('DVA',1)
        incrementNeuron('MVL07',1)
        incrementNeuron('MVL08',1)
        incrementNeuron('MVR07',1)
        incrementNeuron('MVR08',1)
        incrementNeuron('RIML',2)
        incrementNeuron('RMFL',2)
        incrementNeuron('SAADL',9)
        incrementNeuron('SAADR',2)
        incrementNeuron('SABD',1)
        incrementNeuron('SMDVR',1)
        incrementNeuron('VA1',3)
        incrementNeuron('VA3',1)
        incrementNeuron('VB2',4)
        incrementNeuron('VD1',3)
        incrementNeuron('VD2',1)

def VB2():
        incrementNeuron('AVBL',3)
        incrementNeuron('AVBR',1)
        incrementNeuron('DB4',1)
        incrementNeuron('DD1',20)
        incrementNeuron('DD2',1)
        incrementNeuron('MVL07',4)
        incrementNeuron('MVL09',4)
        incrementNeuron('MVL10',4)
        incrementNeuron('MVL12',4)
        incrementNeuron('MVR07',4)
        incrementNeuron('MVR09',4)
        incrementNeuron('MVR10',4)
        incrementNeuron('MVR12',4)
        incrementNeuron('RIGL',1)
        incrementNeuron('VA2',1)
        incrementNeuron('VB1',4)
        incrementNeuron('VB3',1)
        incrementNeuron('VB5',1)
        incrementNeuron('VB7',2)
        incrementNeuron('VC2',1)
        incrementNeuron('VD2',9)
        incrementNeuron('VD3',3)

def VB3():
        incrementNeuron('AVBR',1)
        incrementNeuron('DB1',1)
        incrementNeuron('DD2',37)
        incrementNeuron('MVL11',6)
        incrementNeuron('MVL12',6)
        incrementNeuron('MVL14',6)
        incrementNeuron('MVR11',6)
        incrementNeuron('MVR12',6)
        incrementNeuron('MVR14',6)
        incrementNeuron('VA4',1)
        incrementNeuron('VA7',1)
        incrementNeuron('VB2',1)

def VB4():
        incrementNeuron('AVBL',1)
        incrementNeuron('AVBR',1)
        incrementNeuron('DB1',1)
        incrementNeuron('DB4',1)
        incrementNeuron('DD2',6)
        incrementNeuron('DD3',16)
        incrementNeuron('MVL11',5)
        incrementNeuron('MVL14',5)
        incrementNeuron('MVR11',5)
        incrementNeuron('MVR14',5)
        incrementNeuron('VB5',1)

def VB5():
        incrementNeuron('AVBL',1)
        incrementNeuron('DD3',27)
        incrementNeuron('MVL13',6)
        incrementNeuron('MVL14',6)
        incrementNeuron('MVR13',6)
        incrementNeuron('MVR14',6)
        incrementNeuron('VB2',1)
        incrementNeuron('VB4',1)
        incrementNeuron('VB6',8)

def VB6():
        incrementNeuron('AVBL',1)
        incrementNeuron('AVBR',2)
        incrementNeuron('DA4',1)
        incrementNeuron('DD4',30)
        incrementNeuron('MVL15',6)
        incrementNeuron('MVL16',6)
        incrementNeuron('MVR15',6)
        incrementNeuron('MVR16',6)
        incrementNeuron('MVULVA',6)
        incrementNeuron('VA8',1)
        incrementNeuron('VB5',1)
        incrementNeuron('VB7',1)
        incrementNeuron('VD6',1)
        incrementNeuron('VD7',8)

def VB7():
        incrementNeuron('AVBL',2)
        incrementNeuron('AVBR',2)
        incrementNeuron('DD4',2)
        incrementNeuron('MVL15',5)
        incrementNeuron('MVR15',5)
        incrementNeuron('VB2',2)

def VB8():
        incrementNeuron('AVBL',7)
        incrementNeuron('AVBR',3)
        incrementNeuron('DD5',30)
        incrementNeuron('MVL17',5)
        incrementNeuron('MVL18',5)
        incrementNeuron('MVL20',5)
        incrementNeuron('MVR17',5)
        incrementNeuron('MVR18',5)
        incrementNeuron('MVR20',5)
        incrementNeuron('VA8',3)
        incrementNeuron('VA9',9)
        incrementNeuron('VA9',1)
        incrementNeuron('VB9',6)
        incrementNeuron('VD10',1)
        incrementNeuron('VD9',10)

def VB9():
        incrementNeuron('AVAL',5)
        incrementNeuron('AVAR',4)
        incrementNeuron('AVBL',1)
        incrementNeuron('AVBR',6)
        incrementNeuron('DD5',8)
        incrementNeuron('DVB',1)
        incrementNeuron('MVL17',6)
        incrementNeuron('MVL20',6)
        incrementNeuron('MVR17',6)
        incrementNeuron('MVR20',6)
        incrementNeuron('PVCL',2)
        incrementNeuron('VA8',3)
        incrementNeuron('VA9',4)
        incrementNeuron('VB8',1)
        incrementNeuron('VB8',3)
        incrementNeuron('VD10',5)

def VB10():
        incrementNeuron('AVBL',2)
        incrementNeuron('AVBR',1)
        incrementNeuron('AVKL',1)
        incrementNeuron('DD6',9)
        incrementNeuron('MVL19',5)
        incrementNeuron('MVL20',5)
        incrementNeuron('MVR19',5)
        incrementNeuron('MVR20',5)
        incrementNeuron('PVCL',1)
        incrementNeuron('PVT',1)
        incrementNeuron('VD11',1)
        incrementNeuron('VD12',2)

def VB11():
        incrementNeuron('AVBL',2)
        incrementNeuron('AVBR',1)
        incrementNeuron('DD6',7)
        incrementNeuron('MVL21',5)
        incrementNeuron('MVL22',5)
        incrementNeuron('MVL23',5)
        incrementNeuron('MVR21',5)
        incrementNeuron('MVR22',5)
        incrementNeuron('MVR23',5)
        incrementNeuron('MVR24',5)
        incrementNeuron('PVCR',1)
        incrementNeuron('VA12',2)

def VC1():
        incrementNeuron('AVL',2)
        incrementNeuron('DD1',7)
        incrementNeuron('DD2',6)
        incrementNeuron('DD3',6)
        incrementNeuron('DVC',1)
        incrementNeuron('MVULVA',6)
        incrementNeuron('PVT',2)
        incrementNeuron('VC2',9)
        incrementNeuron('VC3',3)
        incrementNeuron('VD1',5)
        incrementNeuron('VD2',1)
        incrementNeuron('VD3',1)
        incrementNeuron('VD4',2)
        incrementNeuron('VD5',5)
        incrementNeuron('VD6',1)

def VC2():
        incrementNeuron('DB4',1)
        incrementNeuron('DD1',6)
        incrementNeuron('DD2',4)
        incrementNeuron('DD3',9)
        incrementNeuron('DVC',1)
        incrementNeuron('MVULVA',10)
        incrementNeuron('PVCR',1)
        incrementNeuron('PVQR',1)
        incrementNeuron('PVT',2)
        incrementNeuron('VC1',10)
        incrementNeuron('VC3',6)
        incrementNeuron('VD1',2)
        incrementNeuron('VD2',2)
        incrementNeuron('VD4',5)
        incrementNeuron('VD5',5)
        incrementNeuron('VD6',1)

def VC3():
        incrementNeuron('AVL',1)
        incrementNeuron('DD1',2)
        incrementNeuron('DD2',4)
        incrementNeuron('DD3',5)
        incrementNeuron('DD4',13)
        incrementNeuron('DVC',1)
        incrementNeuron('HSNR',1)
        incrementNeuron('MVULVA',11)
        incrementNeuron('PVNR',1)
        incrementNeuron('PVPR',1)
        incrementNeuron('PVQR',4)
        incrementNeuron('VC1',4)
        incrementNeuron('VC2',3)
        incrementNeuron('VC4',1)
        incrementNeuron('VC5',2)
        incrementNeuron('VD1',1)
        incrementNeuron('VD2',1)
        incrementNeuron('VD3',1)
        incrementNeuron('VD4',2)
        incrementNeuron('VD5',4)
        incrementNeuron('VD6',4)
        incrementNeuron('VD7',5)

def VC4():
        incrementNeuron('AVBL',1)
        incrementNeuron('AVFR',1)
        incrementNeuron('AVHR',1)
        incrementNeuron('MVULVA',7)
        incrementNeuron('VC1',1)
        incrementNeuron('VC3',5)
        incrementNeuron('VC5',2)

def VC5():
        incrementNeuron('AVFL',1)
        incrementNeuron('AVFR',1)
        incrementNeuron('DVC',2)
        incrementNeuron('HSNL',1)
        incrementNeuron('MVULVA',2)
        incrementNeuron('OLLR',1)
        incrementNeuron('PVT',1)
        incrementNeuron('URBL',3)
        incrementNeuron('VC3',3)
        incrementNeuron('VC4',2)

def VC6():
        incrementNeuron('MVULVA',1)
           
def VD1():
        incrementNeuron('DD1',5)
        incrementNeuron('DVC',5)
        incrementNeuron('MVL05',-5)
        incrementNeuron('MVL08',-5)
        incrementNeuron('MVR05',-5)
        incrementNeuron('MVR08',-5)
        incrementNeuron('RIFL',1)
        incrementNeuron('RIGL',2)
        incrementNeuron('SMDDR',1)
        incrementNeuron('VA1',2)
        incrementNeuron('VA2',1)
        incrementNeuron('VC1',1)
        incrementNeuron('VD2',7)

def VD2():
        incrementNeuron('AS1',1)
        incrementNeuron('DD1',3)
        incrementNeuron('MVL07',-7)
        incrementNeuron('MVL10',-7)
        incrementNeuron('MVR07',-7)
        incrementNeuron('MVR10',-7)
        incrementNeuron('VA2',9)
        incrementNeuron('VB2',3)
        incrementNeuron('VD1',7)
        incrementNeuron('VD3',2)

def VD3():
        incrementNeuron('MVL09',-7)
        incrementNeuron('MVL12',-9)
        incrementNeuron('MVR09',-7)
        incrementNeuron('MVR12',-7)
        incrementNeuron('PVPL',1)
        incrementNeuron('VA3',2)
        incrementNeuron('VB2',2)
        incrementNeuron('VD2',2)
        incrementNeuron('VD4',1)

def VD4():
        incrementNeuron('DD2',2)
        incrementNeuron('MVL11',-9)
        incrementNeuron('MVL12',-9)
        incrementNeuron('MVR11',-9)
        incrementNeuron('MVR12',-9)
        incrementNeuron('PVPR',1)
        incrementNeuron('VD3',1)
        incrementNeuron('VD5',1)

def VD5():
        incrementNeuron('AVAR',1)
        incrementNeuron('MVL14',-17)
        incrementNeuron('MVR14',-17)
        incrementNeuron('PVPR',1)
        incrementNeuron('VA5',2)
        incrementNeuron('VB4',2)
        incrementNeuron('VD4',1)
        incrementNeuron('VD6',2)

def VD6():
        incrementNeuron('AVAL',1)
        incrementNeuron('MVL13',-7)
        incrementNeuron('MVL14',-7)
        incrementNeuron('MVL16',-7)
        incrementNeuron('MVR13',-7)
        incrementNeuron('MVR14',-7)
        incrementNeuron('MVR16',-7)
        incrementNeuron('VA6',1)
        incrementNeuron('VB5',2)
        incrementNeuron('VD5',2)
        incrementNeuron('VD7',1)

def VD7():
        incrementNeuron('MVL15',-7)
        incrementNeuron('MVL16',-7)
        incrementNeuron('MVR15',-7)
        incrementNeuron('MVR16',-7)
        incrementNeuron('MVULVA',-15)
        incrementNeuron('VA9',1)
        incrementNeuron('VD6',1)

def VD8():
        incrementNeuron('DD4',2)
        incrementNeuron('MVL15',-18)
        incrementNeuron('MVR15',-18)
        incrementNeuron('VA8',5)

def VD9():
        incrementNeuron('MVL17',-10)
        incrementNeuron('MVL18',-10)
        incrementNeuron('MVR17',-10)
        incrementNeuron('MVR18',-10)
        incrementNeuron('PDER',1)
        incrementNeuron('VD10',5)

def VD10():
        incrementNeuron('AVBR',1)
        incrementNeuron('DD5',2)
        incrementNeuron('DVC',4)
        incrementNeuron('MVL17',-9)
        incrementNeuron('MVL20',-9)
        incrementNeuron('MVR17',-9)
        incrementNeuron('MVR20',-9)
        incrementNeuron('VB9',2)
        incrementNeuron('VD9',5)

def VD11():
        incrementNeuron('AVAR',2)
        incrementNeuron('MVL19',-9)
        incrementNeuron('MVL20',-9)
        incrementNeuron('MVR19',-9)
        incrementNeuron('MVR20',-9)
        incrementNeuron('VA11',1)
        incrementNeuron('VB10',1)

def VD12():
        incrementNeuron('MVL19',-5)
        incrementNeuron('MVL21',-5)
        incrementNeuron('MVR19',-5)
        incrementNeuron('MVR22',-5)
        incrementNeuron('VA11',3)
        incrementNeuron('VA12',2)
        incrementNeuron('VB10',1)
        incrementNeuron('VB11',1)

def VD13():
        incrementNeuron('AVAR',2)
        incrementNeuron('MVL21',-9)
        incrementNeuron('MVL22',-9)
        incrementNeuron('MVL23',-9)
        incrementNeuron('MVR21',-9)
        incrementNeuron('MVR22',-9)
        incrementNeuron('MVR23',-9)
        incrementNeuron('MVR24',-9)
        incrementNeuron('PVCL',1)
        incrementNeuron('PVCR',1)
        incrementNeuron('PVPL',2)
        incrementNeuron('VA12',1)
        
        
def createpostsynaptic():
        # The PostSynaptic dictionary maintains the accumulated values for
        # each neuron and muscle. The Accumulated values are initialized to Zero
        postsynaptic['ADAL'] = [0,0,False]
        postsynaptic['ADAR'] = [0,0,False]
        postsynaptic['ADEL'] = [0,0,False]
        postsynaptic['ADER'] = [0,0,False]
        postsynaptic['ADFL'] = [0,0,False]
        postsynaptic['ADFR'] = [0,0,False]
        postsynaptic['ADLL'] = [0,0,False]
        postsynaptic['ADLR'] = [0,0,False]
        postsynaptic['AFDL'] = [0,0,False]
        postsynaptic['AFDR'] = [0,0,False]
        postsynaptic['AIAL'] = [0,0,False]
        postsynaptic['AIAR'] = [0,0,False]
        postsynaptic['AIBL'] = [0,0,False]
        postsynaptic['AIBR'] = [0,0,False]
        postsynaptic['AIML'] = [0,0,False]
        postsynaptic['AIMR'] = [0,0,False]
        postsynaptic['AINL'] = [0,0,False]
        postsynaptic['AINR'] = [0,0,False]
        postsynaptic['AIYL'] = [0,0,False]
        postsynaptic['AIYR'] = [0,0,False]
        postsynaptic['AIZL'] = [0,0,False]
        postsynaptic['AIZR'] = [0,0,False]
        postsynaptic['ALA'] = [0,0,False]
        postsynaptic['ALML'] = [0,0,False]
        postsynaptic['ALMR'] = [0,0,False]
        postsynaptic['ALNL'] = [0,0,False]
        postsynaptic['ALNR'] = [0,0,False]
        postsynaptic['AQR'] = [0,0,False]
        postsynaptic['AS1'] = [0,0,False]
        postsynaptic['AS10'] = [0,0,False]
        postsynaptic['AS11'] = [0,0,False]
        postsynaptic['AS2'] = [0,0,False]
        postsynaptic['AS3'] = [0,0,False]
        postsynaptic['AS4'] = [0,0,False]
        postsynaptic['AS5'] = [0,0,False]
        postsynaptic['AS6'] = [0,0,False]
        postsynaptic['AS7'] = [0,0,False]
        postsynaptic['AS8'] = [0,0,False]
        postsynaptic['AS9'] = [0,0,False]
        postsynaptic['ASEL'] = [0,0,False]
        postsynaptic['ASER'] = [0,0,False]
        postsynaptic['ASGL'] = [0,0,False]
        postsynaptic['ASGR'] = [0,0,False]
        postsynaptic['ASHL'] = [0,0,False]
        postsynaptic['ASHR'] = [0,0,False]
        postsynaptic['ASIL'] = [0,0,False]
        postsynaptic['ASIR'] = [0,0,False]
        postsynaptic['ASJL'] = [0,0,False]
        postsynaptic['ASJR'] = [0,0,False]
        postsynaptic['ASKL'] = [0,0,False]
        postsynaptic['ASKR'] = [0,0,False]
        postsynaptic['AUAL'] = [0,0,False]
        postsynaptic['AUAR'] = [0,0,False]
        postsynaptic['AVAL'] = [0,0,False]
        postsynaptic['AVAR'] = [0,0,False]
        postsynaptic['AVBL'] = [0,0,False]
        postsynaptic['AVBR'] = [0,0,False]
        postsynaptic['AVDL'] = [0,0,False]
        postsynaptic['AVDR'] = [0,0,False]
        postsynaptic['AVEL'] = [0,0,False]
        postsynaptic['AVER'] = [0,0,False]
        postsynaptic['AVFL'] = [0,0,False]
        postsynaptic['AVFR'] = [0,0,False]
        postsynaptic['AVG'] = [0,0,False]
        postsynaptic['AVHL'] = [0,0,False]
        postsynaptic['AVHR'] = [0,0,False]
        postsynaptic['AVJL'] = [0,0,False]
        postsynaptic['AVJR'] = [0,0,False]
        postsynaptic['AVKL'] = [0,0,False]
        postsynaptic['AVKR'] = [0,0,False]
        postsynaptic['AVL'] = [0,0,False]
        postsynaptic['AVM'] = [0,0,False]
        postsynaptic['AWAL'] = [0,0,False]
        postsynaptic['AWAR'] = [0,0,False]
        postsynaptic['AWBL'] = [0,0,False]
        postsynaptic['AWBR'] = [0,0,False]
        postsynaptic['AWCL'] = [0,0,False]
        postsynaptic['AWCR'] = [0,0,False]
        postsynaptic['BAGL'] = [0,0,False]
        postsynaptic['BAGR'] = [0,0,False]
        postsynaptic['BDUL'] = [0,0,False]
        postsynaptic['BDUR'] = [0,0,False]
        postsynaptic['CEPDL'] = [0,0,False]
        postsynaptic['CEPDR'] = [0,0,False]
        postsynaptic['CEPVL'] = [0,0,False]
        postsynaptic['CEPVR'] = [0,0,False]
        postsynaptic['DA1'] = [0,0,False]
        postsynaptic['DA2'] = [0,0,False]
        postsynaptic['DA3'] = [0,0,False]
        postsynaptic['DA4'] = [0,0,False]
        postsynaptic['DA5'] = [0,0,False]
        postsynaptic['DA6'] = [0,0,False]
        postsynaptic['DA7'] = [0,0,False]
        postsynaptic['DA8'] = [0,0,False]
        postsynaptic['DA9'] = [0,0,False]
        postsynaptic['DB1'] = [0,0,False]
        postsynaptic['DB2'] = [0,0,False]
        postsynaptic['DB3'] = [0,0,False]
        postsynaptic['DB4'] = [0,0,False]
        postsynaptic['DB5'] = [0,0,False]
        postsynaptic['DB6'] = [0,0,False]
        postsynaptic['DB7'] = [0,0,False]
        postsynaptic['DD1'] = [0,0,False]
        postsynaptic['DD2'] = [0,0,False]
        postsynaptic['DD3'] = [0,0,False]
        postsynaptic['DD4'] = [0,0,False]
        postsynaptic['DD5'] = [0,0,False]
        postsynaptic['DD6'] = [0,0,False]
        postsynaptic['DVA'] = [0,0,False]
        postsynaptic['DVB'] = [0,0,False]
        postsynaptic['DVC'] = [0,0,False]
        postsynaptic['FLPL'] = [0,0,False]
        postsynaptic['FLPR'] = [0,0,False]
        postsynaptic['HSNL'] = [0,0,False]
        postsynaptic['HSNR'] = [0,0,False]
        postsynaptic['I1L'] = [0,0,False]
        postsynaptic['I1R'] = [0,0,False]
        postsynaptic['I2L'] = [0,0,False]
        postsynaptic['I2R'] = [0,0,False]
        postsynaptic['I3'] = [0,0,False]
        postsynaptic['I4'] = [0,0,False]
        postsynaptic['I5'] = [0,0,False]
        postsynaptic['I6'] = [0,0,False]
        postsynaptic['IL1DL'] = [0,0,False]
        postsynaptic['IL1DR'] = [0,0,False]
        postsynaptic['IL1L'] = [0,0,False]
        postsynaptic['IL1R'] = [0,0,False]
        postsynaptic['IL1VL'] = [0,0,False]
        postsynaptic['IL1VR'] = [0,0,False]
        postsynaptic['IL2L'] = [0,0,False]
        postsynaptic['IL2R'] = [0,0,False]
        postsynaptic['IL2DL'] = [0,0,False]
        postsynaptic['IL2DR'] = [0,0,False]
        postsynaptic['IL2VL'] = [0,0,False]
        postsynaptic['IL2VR'] = [0,0,False]
        postsynaptic['LUAL'] = [0,0,False]
        postsynaptic['LUAR'] = [0,0,False]
        postsynaptic['M1'] = [0,0,False]
        postsynaptic['M2L'] = [0,0,False]
        postsynaptic['M2R'] = [0,0,False]
        postsynaptic['M3L'] = [0,0,False]
        postsynaptic['M3R'] = [0,0,False]
        postsynaptic['M4'] = [0,0,False]
        postsynaptic['M5'] = [0,0,False]
        postsynaptic['MANAL'] = [0,0,False]
        postsynaptic['MCL'] = [0,0,False]
        postsynaptic['MCR'] = [0,0,False]
        postsynaptic['MDL01'] = [0,0,False]
        postsynaptic['MDL02'] = [0,0,False]
        postsynaptic['MDL03'] = [0,0,False]
        postsynaptic['MDL04'] = [0,0,False]
        postsynaptic['MDL05'] = [0,0,False]
        postsynaptic['MDL06'] = [0,0,False]
        postsynaptic['MDL07'] = [0,0,False]
        postsynaptic['MDL08'] = [0,0,False]
        postsynaptic['MDL09'] = [0,0,False]
        postsynaptic['MDL10'] = [0,0,False]
        postsynaptic['MDL11'] = [0,0,False]
        postsynaptic['MDL12'] = [0,0,False]
        postsynaptic['MDL13'] = [0,0,False]
        postsynaptic['MDL14'] = [0,0,False]
        postsynaptic['MDL15'] = [0,0,False]
        postsynaptic['MDL16'] = [0,0,False]
        postsynaptic['MDL17'] = [0,0,False]
        postsynaptic['MDL18'] = [0,0,False]
        postsynaptic['MDL19'] = [0,0,False]
        postsynaptic['MDL20'] = [0,0,False]
        postsynaptic['MDL21'] = [0,0,False]
        postsynaptic['MDL22'] = [0,0,False]
        postsynaptic['MDL23'] = [0,0,False]
        postsynaptic['MDL24'] = [0,0,False]
        postsynaptic['MDR01'] = [0,0,False]
        postsynaptic['MDR02'] = [0,0,False]
        postsynaptic['MDR03'] = [0,0,False]
        postsynaptic['MDR04'] = [0,0,False]
        postsynaptic['MDR05'] = [0,0,False]
        postsynaptic['MDR06'] = [0,0,False]
        postsynaptic['MDR07'] = [0,0,False]
        postsynaptic['MDR08'] = [0,0,False]
        postsynaptic['MDR09'] = [0,0,False]
        postsynaptic['MDR10'] = [0,0,False]
        postsynaptic['MDR11'] = [0,0,False]
        postsynaptic['MDR12'] = [0,0,False]
        postsynaptic['MDR13'] = [0,0,False]
        postsynaptic['MDR14'] = [0,0,False]
        postsynaptic['MDR15'] = [0,0,False]
        postsynaptic['MDR16'] = [0,0,False]
        postsynaptic['MDR17'] = [0,0,False]
        postsynaptic['MDR18'] = [0,0,False]
        postsynaptic['MDR19'] = [0,0,False]
        postsynaptic['MDR20'] = [0,0,False]
        postsynaptic['MDR21'] = [0,0,False]
        postsynaptic['MDR22'] = [0,0,False]
        postsynaptic['MDR23'] = [0,0,False]
        postsynaptic['MDR24'] = [0,0,False]
        postsynaptic['MI'] = [0,0,False]
        postsynaptic['MVL01'] = [0,0,False]
        postsynaptic['MVL02'] = [0,0,False]
        postsynaptic['MVL03'] = [0,0,False]
        postsynaptic['MVL04'] = [0,0,False]
        postsynaptic['MVL05'] = [0,0,False]
        postsynaptic['MVL06'] = [0,0,False]
        postsynaptic['MVL07'] = [0,0,False]
        postsynaptic['MVL08'] = [0,0,False]
        postsynaptic['MVL09'] = [0,0,False]
        postsynaptic['MVL10'] = [0,0,False]
        postsynaptic['MVL11'] = [0,0,False]
        postsynaptic['MVL12'] = [0,0,False]
        postsynaptic['MVL13'] = [0,0,False]
        postsynaptic['MVL14'] = [0,0,False]
        postsynaptic['MVL15'] = [0,0,False]
        postsynaptic['MVL16'] = [0,0,False]
        postsynaptic['MVL17'] = [0,0,False]
        postsynaptic['MVL18'] = [0,0,False]
        postsynaptic['MVL19'] = [0,0,False]
        postsynaptic['MVL20'] = [0,0,False]
        postsynaptic['MVL21'] = [0,0,False]
        postsynaptic['MVL22'] = [0,0,False]
        postsynaptic['MVL23'] = [0,0,False]
        postsynaptic['MVR01'] = [0,0,False]
        postsynaptic['MVR02'] = [0,0,False]
        postsynaptic['MVR03'] = [0,0,False]
        postsynaptic['MVR04'] = [0,0,False]
        postsynaptic['MVR05'] = [0,0,False]
        postsynaptic['MVR06'] = [0,0,False]
        postsynaptic['MVR07'] = [0,0,False]
        postsynaptic['MVR08'] = [0,0,False]
        postsynaptic['MVR09'] = [0,0,False]
        postsynaptic['MVR10'] = [0,0,False]
        postsynaptic['MVR11'] = [0,0,False]
        postsynaptic['MVR12'] = [0,0,False]
        postsynaptic['MVR13'] = [0,0,False]
        postsynaptic['MVR14'] = [0,0,False]
        postsynaptic['MVR15'] = [0,0,False]
        postsynaptic['MVR16'] = [0,0,False]
        postsynaptic['MVR17'] = [0,0,False]
        postsynaptic['MVR18'] = [0,0,False]
        postsynaptic['MVR19'] = [0,0,False]
        postsynaptic['MVR20'] = [0,0,False]
        postsynaptic['MVR21'] = [0,0,False]
        postsynaptic['MVR22'] = [0,0,False]
        postsynaptic['MVR23'] = [0,0,False]
        postsynaptic['MVR24'] = [0,0,False]
        postsynaptic['MVULVA'] = [0,0,False]
        postsynaptic['NSML'] = [0,0,False]
        postsynaptic['NSMR'] = [0,0,False]
        postsynaptic['OLLL'] = [0,0,False]
        postsynaptic['OLLR'] = [0,0,False]
        postsynaptic['OLQDL'] = [0,0,False]
        postsynaptic['OLQDR'] = [0,0,False]
        postsynaptic['OLQVL'] = [0,0,False]
        postsynaptic['OLQVR'] = [0,0,False]
        postsynaptic['PDA'] = [0,0,False]
        postsynaptic['PDB'] = [0,0,False]
        postsynaptic['PDEL'] = [0,0,False]
        postsynaptic['PDER'] = [0,0,False]
        postsynaptic['PHAL'] = [0,0,False]
        postsynaptic['PHAR'] = [0,0,False]
        postsynaptic['PHBL'] = [0,0,False]
        postsynaptic['PHBR'] = [0,0,False]
        postsynaptic['PHCL'] = [0,0,False]
        postsynaptic['PHCR'] = [0,0,False]
        postsynaptic['PLML'] = [0,0,False]
        postsynaptic['PLMR'] = [0,0,False]
        postsynaptic['PLNL'] = [0,0,False]
        postsynaptic['PLNR'] = [0,0,False]
        postsynaptic['PQR'] = [0,0,False]
        postsynaptic['PVCL'] = [0,0,False]
        postsynaptic['PVCR'] = [0,0,False]
        postsynaptic['PVDL'] = [0,0,False]
        postsynaptic['PVDR'] = [0,0,False]
        postsynaptic['PVM'] = [0,0,False]
        postsynaptic['PVNL'] = [0,0,False]
        postsynaptic['PVNR'] = [0,0,False]
        postsynaptic['PVPL'] = [0,0,False]
        postsynaptic['PVPR'] = [0,0,False]
        postsynaptic['PVQL'] = [0,0,False]
        postsynaptic['PVQR'] = [0,0,False]
        postsynaptic['PVR'] = [0,0,False]
        postsynaptic['PVT'] = [0,0,False]
        postsynaptic['PVWL'] = [0,0,False]
        postsynaptic['PVWR'] = [0,0,False]
        postsynaptic['RIAL'] = [0,0,False]
        postsynaptic['RIAR'] = [0,0,False]
        postsynaptic['RIBL'] = [0,0,False]
        postsynaptic['RIBR'] = [0,0,False]
        postsynaptic['RICL'] = [0,0,False]
        postsynaptic['RICR'] = [0,0,False]
        postsynaptic['RID'] = [0,0,False]
        postsynaptic['RIFL'] = [0,0,False]
        postsynaptic['RIFR'] = [0,0,False]
        postsynaptic['RIGL'] = [0,0,False]
        postsynaptic['RIGR'] = [0,0,False]
        postsynaptic['RIH'] = [0,0,False]
        postsynaptic['RIML'] = [0,0,False]
        postsynaptic['RIMR'] = [0,0,False]
        postsynaptic['RIPL'] = [0,0,False]
        postsynaptic['RIPR'] = [0,0,False]
        postsynaptic['RIR'] = [0,0,False]
        postsynaptic['RIS'] = [0,0,False]
        postsynaptic['RIVL'] = [0,0,False]
        postsynaptic['RIVR'] = [0,0,False]
        postsynaptic['RMDDL'] = [0,0,False]
        postsynaptic['RMDDR'] = [0,0,False]
        postsynaptic['RMDL'] = [0,0,False]
        postsynaptic['RMDR'] = [0,0,False]
        postsynaptic['RMDVL'] = [0,0,False]
        postsynaptic['RMDVR'] = [0,0,False]
        postsynaptic['RMED'] = [0,0,False]
        postsynaptic['RMEL'] = [0,0,False]
        postsynaptic['RMER'] = [0,0,False]
        postsynaptic['RMEV'] = [0,0,False]
        postsynaptic['RMFL'] = [0,0,False]
        postsynaptic['RMFR'] = [0,0,False]
        postsynaptic['RMGL'] = [0,0,False]
        postsynaptic['RMGR'] = [0,0,False]
        postsynaptic['RMHL'] = [0,0,False]
        postsynaptic['RMHR'] = [0,0,False]
        postsynaptic['SAADL'] = [0,0,False]
        postsynaptic['SAADR'] = [0,0,False]
        postsynaptic['SAAVL'] = [0,0,False]
        postsynaptic['SAAVR'] = [0,0,False]
        postsynaptic['SABD'] = [0,0,False]
        postsynaptic['SABVL'] = [0,0,False]
        postsynaptic['SABVR'] = [0,0,False]
        postsynaptic['SDQL'] = [0,0,False]
        postsynaptic['SDQR'] = [0,0,False]
        postsynaptic['SIADL'] = [0,0,False]
        postsynaptic['SIADR'] = [0,0,False]
        postsynaptic['SIAVL'] = [0,0,False]
        postsynaptic['SIAVR'] = [0,0,False]
        postsynaptic['SIBDL'] = [0,0,False]
        postsynaptic['SIBDR'] = [0,0,False]
        postsynaptic['SIBVL'] = [0,0,False]
        postsynaptic['SIBVR'] = [0,0,False]
        postsynaptic['SMBDL'] = [0,0,False]
        postsynaptic['SMBDR'] = [0,0,False]
        postsynaptic['SMBVL'] = [0,0,False]
        postsynaptic['SMBVR'] = [0,0,False]
        postsynaptic['SMDDL'] = [0,0,False]
        postsynaptic['SMDDR'] = [0,0,False]
        postsynaptic['SMDVL'] = [0,0,False]
        postsynaptic['SMDVR'] = [0,0,False]
        postsynaptic['URADL'] = [0,0,False]
        postsynaptic['URADR'] = [0,0,False]
        postsynaptic['URAVL'] = [0,0,False]
        postsynaptic['URAVR'] = [0,0,False]
        postsynaptic['URBL'] = [0,0,False]
        postsynaptic['URBR'] = [0,0,False]
        postsynaptic['URXL'] = [0,0,False]
        postsynaptic['URXR'] = [0,0,False]
        postsynaptic['URYDL'] = [0,0,False]
        postsynaptic['URYDR'] = [0,0,False]
        postsynaptic['URYVL'] = [0,0,False]
        postsynaptic['URYVR'] = [0,0,False]
        postsynaptic['VA1'] = [0,0,False]
        postsynaptic['VA10'] = [0,0,False]
        postsynaptic['VA11'] = [0,0,False]
        postsynaptic['VA12'] = [0,0,False]
        postsynaptic['VA2'] = [0,0,False]
        postsynaptic['VA3'] = [0,0,False]
        postsynaptic['VA4'] = [0,0,False]
        postsynaptic['VA5'] = [0,0,False]
        postsynaptic['VA6'] = [0,0,False]
        postsynaptic['VA7'] = [0,0,False]
        postsynaptic['VA8'] = [0,0,False]
        postsynaptic['VA9'] = [0,0,False]
        postsynaptic['VB1'] = [0,0,False]
        postsynaptic['VB10'] = [0,0,False]
        postsynaptic['VB11'] = [0,0,False]
        postsynaptic['VB2'] = [0,0,False]
        postsynaptic['VB3'] = [0,0,False]
        postsynaptic['VB4'] = [0,0,False]
        postsynaptic['VB5'] = [0,0,False]
        postsynaptic['VB6'] = [0,0,False]
        postsynaptic['VB7'] = [0,0,False]
        postsynaptic['VB8'] = [0,0,False]
        postsynaptic['VB9'] = [0,0,False]
        postsynaptic['VC1'] = [0,0,False]
        postsynaptic['VC2'] = [0,0,False]
        postsynaptic['VC3'] = [0,0,False]
        postsynaptic['VC4'] = [0,0,False]
        postsynaptic['VC5'] = [0,0,False]
        postsynaptic['VC6'] = [0,0,False]
        postsynaptic['VD1'] = [0,0,False]
        postsynaptic['VD10'] = [0,0,False]
        postsynaptic['VD11'] = [0,0,False]
        postsynaptic['VD12'] = [0,0,False]
        postsynaptic['VD13'] = [0,0,False]
        postsynaptic['VD2'] = [0,0,False]
        postsynaptic['VD3'] = [0,0,False]
        postsynaptic['VD4'] = [0,0,False]
        postsynaptic['VD5'] = [0,0,False]
        postsynaptic['VD6'] = [0,0,False]
        postsynaptic['VD7'] = [0,0,False]
        postsynaptic['VD8'] = [0,0,False]
        postsynaptic['VD9'] = [0,0,False]

#global postsynapticNext = copy.deepcopy(postsynaptic)

def motorcontrol():
        global accumright
        global accumleft

        # accumulate left and right muscles and the accumulated values are
        # used to move the left and right motors of the robot
        for pscheck in postsynaptic:
                if pscheck in musDleft or pscheck in musVleft:
                   accumleft += postsynaptic[pscheck][thisState]
                   postsynaptic[pscheck][thisState] = 0                 #Only thisState weight is reset to 0, because nextState weight
                   #postsynaptic[pscheck][nextState] = 0                # equals weight to accumulate plus thisState weight
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
        print("Left: ", accumleft, "Right:", accumright, "Speed: ", new_speed)
        ## Start Commented section
        gpg.set_speed(new_speed)
        print("Speed set: ", new_speed)
        if accumleft == 0 and accumright == 0:
                gpg.stop()
        elif accumright <= 0 and accumleft < 0:
                gpg.set_speed(150)
                turnratio = float(accumright) / float(accumleft)
                # print "Turn Ratio: ", turnratio
                if turnratio <= 0.6:
                         gpg.left()
                         time.sleep(0.8)
                elif turnratio >= 2:
                         gpg.right()
                         time.sleep(0.8)
                gpg.backward()
                time.sleep(0.5)
        elif accumright <= 0 and accumleft >= 0:
                gpg.right()
                time.sleep(.8)
        elif accumright >= 0 and accumleft <= 0:
                gpg.left()
                time.sleep(.8)
        elif accumright >= 0 and accumleft > 0:
                turnratio = float(accumright) / float(accumleft)
                # print "Turn Ratio: ", turnratio
                if turnratio <= 0.6:
                         gpg.left()
                         time.sleep(0.8)
                elif turnratio >= 2:
                         gpg.right()
                         time.sleep(0.8)
                gpg.forward()
                time.sleep(0.5)
        else:
                gpg.stop()
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
                #print "Function: " + fneuron
                #postsynaptic[fneuron][2] = False

def runconnectome():
        # Each time a set of neuron is stimulated, this method will execute
        # The weigted values are accumulated in the PostSynaptic array
        # Once the accumulation is read, we see what neurons are greater
        # then the threshold and fire the neuron or muscle that has exceeded
        # the threshold 
        global thisState
        global nextState
        for ps in nextNeurons:
                #print ps
                if ps[:3] not in muscles: #and abs(postsynaptic[ps][thisState]) > threshold:
                        fireNeuron(ps)                                  #IS THIS ADDING TO NEXTNEURONS IN REAL TIME???
                        postsynaptic[ps] = [0,0,False]
                        nextNeurons.remove(ps)
        motorcontrol()
        thisState,nextState=nextState,thisState
        #nextNeurons[:] = []    #List of neurons to fire next is reset to blank array after they are fired.
                         

# Create the dictionary      
createpostsynaptic()
dist=0
## Start comment
gpg.set_speed(120)
print("Voltage: ", gpg.volt())
## End comment
tfood = 0
try:
### Here is where you would put in a method to stimulate the neurons ###
### We stimulate chemosensory neurons constantly unless nose touch   ###
### (sonar) is stimulated and then we fire nose touch neurites       ###
### Use CNTRL-C to stop the program
    while True:
        ## Start comment - use a fixed value if you want to stimulte nose touch
        ## use something like "dist = 27" if you want to stop nose stimulation
        # print("Distance Sensor Reading: {} mm ".format(my_distance_sensor.read_mm()))
        dist = my_distance_sensor.read_mm()
        ## End Comment

        #Do we need to switch states at the end of each loop? No, this is done inside the runconnectome()
        #function, called inside each loop.
        if dist>0 and dist<100:
            print("OBSTACLE (Nose Touch)", dist)
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
                    print("FOOD")
                    print(thisState)
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
    gpg.stop()
    ## End Comment
    print("Ctrl+C detected. Program Stopped!")