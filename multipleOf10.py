# given a string s representing positive integer.your task is to round the number
# to the nearest multiple of 10. if num is equally distant from 2 multiples of 10
# return the smaller number. return rounded number as astring
def roundToNearest(s: str) -> str:
    n = int(s)
    if n % 10 <= 5:
        return str(n - n % 10)
    return str(n + 10 - n % 10)