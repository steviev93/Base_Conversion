import math

above_ten = {"A":10,"B":11,"C":12,"D":13,"E":14,"F":15,"G":16,"H":17,"I":18,"J":19,"K":20,
             "L":21,"M":22,"N":23,"O":24,"P":25,"Q":26,"R":27,"S":28,"T":29,"U":30,"V":31,
             "W":32,"X":33,"Y":34,"Z":35}

def ten2we(o_num,base,bits):
    above_ten = {"A":10,"B":11,"C":12,"D":13,"E":14,"F":15,"G":16,"H":17,"I":18,"J":19,"K":20,
                 "L":21,"M":22,"N":23,"O":24,"P":25,"Q":26,"R":27,"S":28,"T":29,"U":30,"V":31,
                 "W":32,"X":33,"Y":34,"Z":35}
    num = ""
    bits = bits
    mod = 0
    num_left = o_num
    while bits != -1:
        mod = num_left % (base**bits)
        num_left = math.floor(num_left/(base**bits))
        if num_left in above_ten.values():
            key_list = list(above_ten.keys())
            val_list = list(above_ten.values())
            position = val_list.index(num_left)
            num += str(key_list[position])
        else:
            num += str(num_left)
        num_left = mod
        bits -= 1
        
    return(num)


def we2decimal(o_num,base):
    above_ten = {"A":10,"B":11,"C":12,"D":13,"E":14,"F":15,"G":16,"H":17,"I":18,"J":19,"K":20,
                 "L":21,"M":22,"N":23,"O":24,"P":25,"Q":26,"R":27,"S":28,"T":29,"U":30,"V":31,
                 "W":32,"X":33,"Y":34,"Z":35}
    num = 0
    bits = len(o_num)-1

    for i in range(bits+1):
        if " " in o_num:
            print("NO SPACES ALLOWED")
            return
        
        else:
            if o_num[i] in above_ten.keys():
                num += above_ten[o_num[i]] * (base**bits)
                if (above_ten[o_num[i]] > base) or (str(base) in o_num[i]):
                    print("INVALID NUMBER")
                    return
            else:
                num += int(o_num[i]) * (base**bits)
        bits -= 1
    return num

def we2we(num, base, base_desired):
    dec_num = we2decimal(num,base)
    desired_num = ten2we(dec_num,base_desired,16)
    return desired_num

num = input("Enter any base number, no spaces: ").upper()
base = int(input("Enter the base: "))
base_desired = int(input("Enter the base desired: "))

new_num = we2we(num,base,base_desired)
for digit in range(len(new_num)):
    if int(new_num[digit]) > 0 or new_num[digit] in above_ten.keys():
        new_num = new_num[digit:]
        break


print(num + " base " + str(base) + " in base " + str(base_desired) + ": " + new_num )
