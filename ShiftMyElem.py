# !/usr/bin/pyhon
import mymodule.MatrixCreator  as mcreator
import mymodule.DataCollector  as dcollector
import mymodule.ValueShifter   as vshifter
import tests.test              as utest


def main():
    """
    temp_arr    =   dcollector.CheckMyData()
    n           =   temp_arr[0]
    k           =   temp_arr[1]
    shift       =   temp_arr[2]

    
    array = mcreator.GetMeMatrix(n, k)
    """
    i = 0
    if utest.solution_test.M2X2 == vshifter.ShiftMyValue(utest.test.M2X2, utest.solution_test.shift_2x2):
        i += 1
    if utest.solution_test.M2X3 == vshifter.ShiftMyValue(utest.test.M2X3, utest.solution_test.shift_2x3):
        i += 1
    if utest.solution_test.M3X2 == vshifter.ShiftMyValue(utest.test.M3X2, utest.solution_test.shift_3x2):
        i += 1
    if utest.solution_test.M3X3 == vshifter.ShiftMyValue(utest.test.M3X3, utest.solution_test.shift_3x3):
        i += 1
    if utest.solution_test.M4X3 == vshifter.ShiftMyValue(utest.test.M4X3, utest.solution_test.shift_4x3):
        i += 1
    if utest.solution_test.M3X4 == vshifter.ShiftMyValue(utest.test.M3X4, utest.solution_test.shift_3x4):
        i += 1
    if utest.solution_test.M4X4 == vshifter.ShiftMyValue(utest.test.M4X4, utest.solution_test.shift_4x4):
        i += 1
    print(f"Tests is right: {i}")
if __name__ == '__main__':
    main()
