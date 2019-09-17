# ======== You can define the gcd function here. Do not write any code other than your solution here! ================
def gcd(x, y):
    zwischenresultat = 0
    if x > y:
        zwischenresultat = x % y
        if zwischenresultat == 0:
            return y
        elif zwischenresultat == 1:
            return 1
        else:
            return gcd(y, zwischenresultat)
    elif x < y:
        zwischenresultat = y % x
        if zwischenresultat == 0:
            return x
        elif zwischenresultat == 1:
            return 1
        else:
            return gcd(x, zwischenresultat)


# ====================================================================================================================================


if __name__ == '__main__':

    list_of_pairs = []

    for i in range(2, 100):
        for j in range(i+1, 103):
            if gcd(i, j) < i:
                    list_of_pairs.append((i, j))




