from calculator.model import CalculatorModel
import os
if __name__ == '__main__':
    calc = CalculatorModel()
    #리눅스에서 돌아간다
    #모델이 존재하지 않을경우만 실행한다.
    if not os.path.exists('saved_add_model/checkpoint'):
        calc.create_add_model()
    if not os.path.exists('saved_min_model/checkpoint'):
        calc.create_min_model()
    if not os.path.exists('saved_mul_model/checkpoint'):
        calc.create_mul_model()
    if not os.path.exists('saved_div_model/checkpoint'):
        calc.create_div_model()
