def base_converter(dec_num, base):
    digits = "0123456789ABCDEF"
    if dec_num < base:
        return digits[dec_num]
    else:
        return base_converter(dec_num//base) + digits[dec_num % base]
