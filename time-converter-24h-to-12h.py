def time_converter(time):
    #replace this for solution
    h1 = time[:2]
    h2 = time[3:]
    
         
    if int(h1) == 0:
        time = "12" + ":" + h2 + " a.m."
        print(time)
        return time
    elif int(h1) < 12:
        time = h1[1:] + ":" + h2 + " a.m."
        print(time)
        return time
   # elif int(h1) == 12 and int(h2) == 00:
   #     time = h1 + ":" + h2 + " a.m."
   #     print(time)
    
    elif int(h1) == 12:
        time = h1 + ":" + h2 + " p.m."
        print(time)
        return time
    elif int(h1) > 12:
        h3 = str(int(h1) - 12)
        time = h3 + ":" + h2 + " p.m."
        print(time)
        return time
    else:
        print("this isn't a time")
    

if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30') == '12:30 p.m.'
    assert time_converter('09:00') == '9:00 a.m.'
    assert time_converter('23:15') == '11:15 p.m.'
    print("Coding complete? Click 'Check' to earn cool rewards!")
