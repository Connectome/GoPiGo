"""GoPiGo Connectome

Written by Timothy Busbice, Gabriel Garrett, Geoffrey Churchill (c) 2014, in Python 2.7
The GoPiGo Connectome uses a postSynaptic dictionary based on the C Elegans Connectome Model
This application can be ran on the Raspberry Pi GoPiGo robot with a Sonar that represents Nose Touch when activated
To run standalone without a GoPiGo robot, simply comment out the sections with Start and End comments 

#TIME STATE EXPERIMENTAL OPTIMIZATION
The previous version had a logic error whereby if more than one neuron fired into the same neuron in the next time state,
it would overwrite the contribution from the previous neuron. Thus, only one neuron could fire into the same neuron at any given time state.
This version also explicitly lists all left and right muscles, so that during the muscle checks for the motor control function, instead of 
iterating through each neuron, we now iterate only through the relevant muscle neurons.
"""

## Start Comment
#from gopigo import *
## End Comment
import time
import copy

# The postSynaptic dictionary contains the accumulated weighted values as the
# connectome is executed
from synapse_dict import createpostSynaptic
postSynaptic = createpostSynaptic()

global thisState
global nextState
thisState = 0 
nextState = 1
timestep = 1

# The Threshold is the maximum sccumulated value that must be exceeded before
# the Neurite will fire
threshold = 30

# Accumulators are used to decide the value to send to the Left and Right motors
# of the GoPiGo robot
accumleft = 0
accumright = 0

from muscle_list import muscles, muscleList, mLeft, mRight, musDleft, musVleft, musDright, musVright

from neuron_functions import ADAL, ADAR, ADEL, ADER, ADFL, ADFR, ADLL, ADLR, AFDL, AFDR, AIAL, AIAR, AIBL, AIBR, AIML, AIMR, AINL, AINR, AIYL, AIYR, AIZL, AIZR, ALA, ALML, ALMR, ALNL, ALNR, AQR, AS1, AS2, AS3, AS4, AS5, AS6, AS7, AS8, AS9, AS10, AS11, ASEL, ASER, ASGL, ASGR, ASHL, ASHR, ASIL, ASIR, ASJL, ASJR, ASKL, ASKR, AUAL, AUAR, AVAL, AVAR, AVBL, AVBR, AVDL, AVDR, AVEL, AVER, AVFL, AVFR, AVG, AVHL, AVHR, AVJL, AVJR, AVKL, AVKR, AVL, AVM, AWAL, AWAR, AWBL, AWBR, AWCL, AWCR, BAGL, BAGR, BDUL, BDUR, CEPDL, CEPDR, CEPVL, CEPVR, DA1, DA2, DA3, DA4, DA5, DA6, DA7, DA8, DA9, DB1, DB2, DB3, DB4, DB5, DB6, DB7, DD1, DD2, DD3, DD4, DD5, DD6, DVA, DVB, DVC, FLPL, FLPR, HSNL, HSNR, I1L, I1R, I2L, I2R, I3, I4, I5, I6, IL1DL, IL1DR, IL1L, IL1R, IL1VL, IL1VR, IL2DL, IL2DR, IL2L, IL2R, IL2VL, IL2VR, LUAL, LUAR, M1, M2L, M2R, M3L, M3R, M4, M5, MCL, MCR, MI, NSML, NSMR, OLLL, OLLR, OLQDL, OLQDR, OLQVL, OLQVR, PDA, PDB, PDEL, PDER, PHAL, PHAR, PHBL, PHBR, PHCL, PHCR, PLML, PLMR, PLNL, PLNR, PQR, PVCL, PVCR, PVDL, PVDR, PVM, PVNL, PVNR, PVPL, PVPR, PVQL, PVQR, PVR, PVT, PVWL, PVWR, RIAL, RIAR, RIBL, RIBR, RICL, RICR, RID, RIFL, RIFR, RIGL, RIGR, RIH, RIML, RIMR, RIPL, RIPR, RIR, RIS, RIVL, RIVR, RMDDL, RMDDR, RMDL, RMDR, RMDVL, RMDVR, RMED, RMEL, RMER, RMEV, RMFL, RMFR, RMGL, RMGR, RMHL, RMHR, SAADL, SAADR, SAAVL, SAAVR, SABD, SABVL, SABVR, SDQL, SDQR, SIADL, SIADR, SIAVL, SIAVR, SIBDL, SIBDR, SIBVL, SIBVR, SMBDL, SMBDR, SMBVL, SMBVR, SMDDL, SMDDR, SMDVL, SMDVR, URADL, URADR, URAVL, URAVR, URBL, URBR, URXL, URXR, URYDL, URYDR, URYVL, URYVR, VA1, VA2, VA3, VA4, VA5, VA6, VA7, VA8, VA9, VA10, VA11, VA12, VB1, VB2, VB3, VB4, VB5, VB6, VB7, VB8, VB9, VB10, VB11, VC1, VC2, VC3, VC4, VC5, VC6, VD1, VD2, VD3, VD4, VD5, VD6, VD7, VD8, VD9, VD10, VD11, VD12, VD13

def motorcontrol():
        global accumright
        global accumleft

        # accumulate left and right muscles and the accumulated values are
        # used to move the left and right motors of the robot
        for muscle in muscleList:
                if muscle in mLeft:
                   accumleft += postSynaptic[muscle][nextState]
                   #accumleft = accumleft + postSynaptic[muscle][thisState] #what???  For some reason, thisState weight is always 0.
                   #postSynaptic[muscle][thisState] = 0
                   print muscle, "Before", postSynaptic[muscle][thisState], accumleft                #Both states have to be set to 0 once the muscle is fired, or
                   postSynaptic[muscle][nextState] = 0
                   print muscle, "After", postSynaptic[muscle][thisState], accumleft                   # it will keep returning beyond the threshold within one iteration.
                elif muscle in mRight:
                   accumright += postSynaptic[muscle][nextState]
                   #accumleft = accumright + postSynaptic[muscle][thisState] #what???
                   #postSynaptic[muscle][thisState] = 0
                   postSynaptic[muscle][nextState] = 0

        # We turn the wheels according to the motor weight accumulation
        new_speed = abs(accumleft) + abs(accumright)
        if new_speed > 150:
                new_speed = 150
        elif new_speed < 75:
                new_speed = 75
        print "Left: ", accumleft, "Right:", accumright, "Speed: ", new_speed
        accumleft = 0
        accumright = 0
        time.sleep(0.5)

def dendriteAccumulate(dneuron):
    f = eval(dneuron)
    f(postSynaptic, nextState)

def fireNeuron(fneuron):
    # The threshold has been exceeded and we fire the neurite
    if fneuron != "MVULVA":
        f = eval(fneuron)
        f(postSynaptic, nextState)
        #postSynaptic[fneuron][nextState] = 0
        #postSynaptic[fneuron][thisState] = 0
        postSynaptic[fneuron][nextState] = 0

def runconnectome():
    # Each time a set of neuron is stimulated, this method will execute
    # The weigted values are accumulated in the postSynaptic array
    # Once the accumulation is read, we see what neurons are greater
    # then the threshold and fire the neuron or muscle that has exceeded
    # the threshold 
    global thisState
    global nextState
    global timestep

    for ps in postSynaptic:
        if ps[:3] not in muscles and abs(postSynaptic[ps][thisState]) > threshold:
            fireNeuron(ps)
            #print ps
            #print (ps)
            #postSynaptic[ps][nextState] = 0
    motorcontrol()
    for ps in postSynaptic:
        #if postSynaptic[ps][thisState] != 0:
        #print ps
        #print "Before Clone: ", postSynaptic[ps][thisState]
        postSynaptic[ps][thisState] = copy.deepcopy(postSynaptic[ps][nextState]) #fired neurons keep getting reset to previous weight
        #print "After Clone: ", postSynaptic[ps][thisState]
    thisState,nextState=nextState,thisState 
    timestep += 1              

dist=0

tfood = 0

def main():
    global tfood
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
        #stop()
        ## End Comment
        print "Ctrl+C detected. Program Stopped!"
        for pscheck in postSynaptic:
            print (pscheck,' ',postSynaptic[pscheck][0],' ',postSynaptic[pscheck][1])

if __name__ == '__main__':
    main()