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
            raise AttributeError(str(symbol)+" already known in this state.")
        self.setTransition(self,symbol,transition)

    def setTransition(self,symbol,transition):
        '''in: symbol as character
        in: transition as string. ex: 0>newState
        '''
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

    def __init__(self,tapestring):
        # TODO: make tapestring optional, default to blank tape
        self._tape = collections.deque(tapestring)
        self._currentPosition = 0

    # TODO: add tape functions

    # TODO: add tape load function
    def load(self,tapestring):
        self._tape = collections.deque(tapestring)
        self._currentPosition = 0

# TODO: add main
    
