# GoPiGo C. elegans Connectome Code

The GoPiGoConnectomev(n).py Python program provided here can be used with a Raspberry Pi GoPiGo robotic kit created by Dexter Industries.

To run this code, from the Pi directory, type 
```
sudo python connectome.py
```

The tiny worm Caenorhabditis elegans has only 302 neurons but exhibits some complex behaviors. When the worm senses food through a variety of sensory neurons, the worm will move forward towards that food source. When the worm’s nose senses a blocking object, the worm will stop, backup and change direction to move around the object or avoid it all together. After successfully simulating the worm’s brain in a more complex environment, I wanted to see if a similar application could be created in a much simpler environment and the GoPiGo with a Raspberry Pi was the perfect answer. 

## Combining Worm and GoPiGo Robot

I created the connectome of the worm in a Python 2.7 program utilizing the GoPiGo commands for sensory input and motor output. The program essentially does the following:

 * If no other sensory input is happening, stimulate food sensing neurons
 * If an object is within 25cm of the sonar sensor, stimulate nose touch sensory neurons
 * Each stimulation of sensory neurons, runs the connectome whereby each sensory neuron has added weights within a dictionary of the entire worms neural structure (i.e. dendriteAccumulate function). After each sensory neuron is activated and weights added, the programs run through all the neurons (i.e. runnconnectome function) and anywhere the accumulated weights of a neuron is greater than a predefined threshold, the neuron fires (i.e. fireNeuron function) and additional weights are added throughout the connectome which include neurons and muscles. 
 * Each time the Connectome is ran, muscles, which are part of the same dictionary as the neurons, are accumulated as Right and Left muscle weights (weights for muscles can be negative as well as positive) and the wheels on the robot are activated according to the weighted values. 
 * Each time a neuron or muscle is activated, the weights are set to zero so that accumulation can start again. 

### Worm’s Brain Controls the GoPiGo Robot

To be clear, there is no programming that is directing the robot to stop or rotate a wheel in one direction or another. It is only the collective weighted values being generated from the simulated worm connectome that guides the actions of the robot. It was very difficult to contain the connectome into a single application and make it run on a Raspberry Pi but this is a good attempt from the evidence I have seen. This is truly a totally autonomous robot that is reacting to its environment through a simulated brain of a nematode. 

I encourage others to use the connectome program and try to change the methods to make the program run more efficiently and react better to the environment. However, I do not encourage any changes to the connectomic structure of the program itself if you are interested in studying the nervous system of the C elegans nematode. Changes to the connectome, means you are creating your own simulated nervous system and away from the worms nervous system, which might be fun to explore as well. 
