# !/usr/bin/pyhon

from multiprocessing.dummy import Array


def CheckMyData():
    """Check the input data on the type of data

    Args:
        n (int): Length
        k (int): Width
        shift (int): Shift

    Returns:
        int: Three entered values
    """
    print("""Enter the entire and positive values of the future matrix.\nNegative values will be automatically converted to positive""")
    print("\t\t\t(enter \"q\" to exit)\t\t\t")
    try:
        temp_arr = []
        temp_arr.append(int(input("Enter a width of Array: ")))
        temp_arr.append(int(input("Enter a hieght of Array: ")))
        temp_arr.append(int(input("Enter a shift value: ")))
        return temp_arr

    except:
        print("Error in entered data. Please try again\n")
        CheckMyData()


def main():
    CheckMyData()
