# Agrs and Kwargs for arbitary number of agruements

def an_agrs_func(*agrs):
    val=0
    for a in agrs:
        val+=a
    return val

print(an_agrs_func(3,4,5))