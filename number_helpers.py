def to_int_tuple(input_str):
    if input_str is not None:
        num_str = input_str.strip()
        if num_str.isnumeric() or num_str.isdigit():
            int_num = int(num_str)
            return True, int_num

        # only if isnumeric and isdigit couldn't figure out whether it's a number
        # then try the approach which may cause an exception
        # to relieve performance reduction caused by the exception stack
        try:
            num = int(num_str)
            return True, num
        except:
            pass

    return False, -1


def to_float_tuple(input_str):
    if input_str is not None:
        num_str = input_str.strip()
        if num_str.isnumeric() or num_str.isdigit():
            float_num = float(num_str)
            return True, float_num

        # only if isnumeric and isdigit couldn't figure out whether it's a number
        # then try the approach which may cause an exception
        # to relieve performance reduction caused by the exception stack
        try:
            num = float(num_str)
            return True, num
        except:
            pass

    return False, -1.0
