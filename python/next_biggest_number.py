#!/usr/bin/python3
import sys


def main():
    #next_biggest_number(sys.argv[1])
    next_biggest_number(-21)
    next_biggest_number(123987)
    next_biggest_number(52210)


def next_biggest_number(num):
    int_num = int(num)
    if int_num >= 0:
        list_of_digits = [int(d) for d in str(num)]
        print(list_of_digits)
        sorted_list = sorted(list_of_digits, reverse = True)
        print(sorted_list)
        if list_of_digits == sorted_list:
            print(-1)
            return -1
        else:  # I need to be reordered
            index_count = len(list_of_digits) - 1
            ones_place = list_of_digits.pop()
            print(ones_place)
            counter = index_count
            while counter > 0:
                if list_of_digits[counter - 1] < ones_place:
                    replace_me = list_of_digits[counter - 1]
                    print(replace_me)
                    first_half = list_of_digits[:counter - 1]
                    second_half = list_of_digits[counter - 1:]
                    print(first_half)
                    print(second_half)
                    first_half.append(ones_place)
                    second_half.sort()
                    first_half.extend(second_half)
                    print(first_half)
                    print(list_ints_to_int(first_half))
                    return list_ints_to_int(first_half)
                counter -= 1
            return "I need to be reordered - but the code broke"
    else:  # I am a negative number
        abs_num = abs(int_num)
        list_of_digits = [int(d) for d in str(abs_num)]
        print(list_of_digits)
        sorted_list = sorted(list_of_digits)
        print(sorted_list)
        if list_of_digits == sorted_list:
            print(-1)
            return -1
        else:  # I need to be reordered
            index_count = len(list_of_digits) - 1
            ones_place = list_of_digits.pop()
            print(ones_place)
            counter = index_count
            while counter > 0:
                if list_of_digits[counter - 1] > ones_place:
                    replace_me = list_of_digits[counter - 1]
                    print(replace_me)
                    first_half = list_of_digits[:counter - 1]
                    second_half = list_of_digits[counter - 1:]
                    print(first_half)
                    print(second_half)
                    first_half.append(ones_place)
                    second_half.sort()
                    first_half.extend(second_half)
                    print(first_half)
                    print(list_ints_to_int(first_half))
                    return list_ints_to_int(first_half)
                counter -= 1
            return "I need to be reordered - but the code broke"


def list_ints_to_int(list_of_ints):
    str_list = [str(integer) for integer in list_of_ints]
    str_final_int = "". join(str_list)
    final_int = int(str_final_int)
    return final_int


if __name__ == "__main__":
    main()



