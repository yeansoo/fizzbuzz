def fizzbuzz(number):
    if type(number)==int:
        if str (number).find('7')>=0:
            return 'github'
        elif number %3==0 and number%5==0:
            return 'fizzbuzz'
        elif number % 3==0:
            return 'fizz'
        elif number %5==0:
            return 'buzz'
        else:
            return number
