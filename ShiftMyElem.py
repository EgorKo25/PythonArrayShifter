# !/usr/bin/pyhon
import mymodule.MatrixCreator as mcreator
import mymodule.DataCollector as dcollector
import mymodule.ValueShifter as vshifter


def main():
    temp_arr    =   dcollector.CheckMyData()
    n           =   temp_arr[0]
    k           =   temp_arr[1]
    shift       =   temp_arr[2]

    
    array = mcreator.GetMeMatrix(n, k)
    array = vshifter.ShiftMyValue(array, shift, n, k)

if __name__ == '__main__':
    main()
