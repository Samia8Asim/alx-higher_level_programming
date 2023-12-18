#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    div_result = 0
    for i in range(list_length):
        try:
            div_result = my_list_1[i] / my_list_2[i]
            new_list.append(my_list_1[i] / my_list_2[i])
        except (ValueError, TypeError):
            print("wrong type")
            new_list.append(0)
        except ZeroDivisionError:
            print("division by 0")
            new_list.append(0)
        except IndexError:
            print("out of range")
            new_list.extend([0] * (list_length - len(new_list)))
        finally:
            pass
    return new_list
