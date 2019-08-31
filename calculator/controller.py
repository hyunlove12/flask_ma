import tensorflow as tf

class CalculatorController:
    def __init__(self, num1, num2, opcode):
        self._num1 = num1
        self._num2 = num2
        self._opconde = opcode

    def calc(self):
        n1 = self._num1
        n2 = self._num2
        opcode = self._opconde
        print('app.py에서 받은 n1 = {}. n2 = {}, opcode = {}'.format(n1, n2, opcode))