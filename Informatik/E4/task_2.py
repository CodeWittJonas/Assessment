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
	# Here you can write code to test your function. Code you write here is solely for testing and will not be evaluated.

    print(gcd(16, 12))
    print(gcd(12, 16))
    print(gcd(72, 36))
    print(gcd(12, 68))

