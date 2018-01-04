#! /usr/bin/env python3

import sys
import collections

class State:
    ''''''
    # TODO: add info for State class

    def __init__(self):
        self._recognizedSymbols = dict() # ex: 0:0>newState

    def getTransition(self,symbol):
        '''in: symbol as character read
        out: -1 if unrecognized
        out: string of two characters and a new state.
            ex: 0>newState
        '''
        if not symbol in _recognizedSymbols:
            return -1
        return _recognizedSymbols[symbol]
    
    def addTransition(self,symbol,transition):
        '''in: symbol as character
        in: transition as string. ex: 0>newState
        exception: AttributeError if symbol is already known to state
        '''
        if symbol in _recognizedSymbols:
            raise AttributeError(symbol+" already known in this state.")
        _checkTransition(transition)
        self.setTransition(self,symbol,transition)

    def setTransition(self,symbol,transition):
        '''in: symbol as character
        in: transition as string. ex: 0>newState
        '''
        _checkTransition(transition)
        _recognizedSymbols[symbol] = transition

    def _checkTransition(self,transition):
        '''in: transition as string to check
        exception: SyntaxError if the string does not qualify
        '''
        if len(transition) < 3:
            raise SyntaxError('Transition string is not long enough')
        if not transition[1] in [-,<,>]:
            raise SyntaxError('Transition string does not have a valid ' +
                              'move character (-,<,>)')

class Tape:
    ''''''
    # TODO: add info for Tape class
    
    _tape = collections.deque('') # placeholder
    _currentPosition = 0

    def __init__(self,tapestring=''):
        self._tape = collections.deque(tapestring)
        self._currentPosition = 0

    # TODO: add tape functions: write, read, move
    def move(self,direction):
        '''Updates currentPosition
        in: direction as either -1,0,1
        -1 is left, 1 is right, 0 is no move
        '''
        self._currentPosition+=direction

    def read(self):
        '''returns the symbol at the currentPosition
        out: character that has been read
        '''
        return self._tape[self._currentPosition]

    def write(self,newCharacter):
        '''updates the character at currentPosition.
        in: newCharacter as character
        '''
        self._tape[self._currentPosition] = newCharacter

    # TODO: verify that this does what i want
    def load(self,tapestring):
        self._tape = collections.deque(tapestring)
        self._currentPosition = 0

# TODO: add main
    
