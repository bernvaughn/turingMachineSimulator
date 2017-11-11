# turingMachineSimulator
A console-based Turing Machine Simulator for Linux

I started this project because the Turing Machine simulator we were using for class was found to sneakily run cryptocurrency mining scripts on computers using the site.

Desinged to take in a file with this structure:
qState1
0:0>,qState1
1:0-,qState2
qState2
0:0<,qState2
1:0-,qState1

And output the steps of the Turing machine
