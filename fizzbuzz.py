def fizzbuzz(number):
    if type(number)==int:
        #if number %15==0:
        if number %3==0 and number%5==0:
            return 'fizzbuzz'
        elif number % 3==0:
            return 'fizz'
        elif number %5==0:
            return 'buzz'
        else:
            return number
