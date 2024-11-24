
def get_date_of_birth(id_number:str): 
    """
    STEP 2: Extract the date of birth from the ID number and return it as a string

    return format: DD/MM/YY: 
     """
         
    day = id_number[4:6]
    month = id_number[2:4]
    year = id_number[:2]

    return f'{day}/{month}/{year}'

#Question 2    
def get_gender(id_number):
    """
    STEP 3: Extract the gender from the ID number using the formula below and return it as a string

    Formula: 1 if the ID number's 7th to 10th digit is less than 5000, the person is female and if it is greater than 4999, the person is male.
                                                            """

    gender = id_number[6:10]
    return 'Female' if int(gender) < 5000 else 'Male'

#Question 3
def get_citizenship(id_number):                     
    """
                                                            STEP 4: Extract the citizenship from the ID number using the formula below and return it as a string

                                                            Formula: 1 if the ID number's 11th to 12th digit is less than 01, the person is a South African citizen and if it is greater than 01, the person is a non-South African citizen.
                                                            """

    citizenship = id_number[10]
                                                    
    return 'South African' if int(citizenship) == 0 else 'Non-South African'
                                                        #Question 4
    """
    Fizzbuzz is a programme that prints the numbers from 1 to n, but for multiples of 3, it prints "Fizz" instead of the number, and for multiples of 5, it prints "Buzz" instead of the number. For numbers that are multiples of both 3 and 5, it prints "FizzBuzz.

    TODO: define a function called fizzbuzz and implement the fucntionality above.
                                                           """                                                

def fizzbuzz(n):
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0: print('FizzBuzz')
        elif i % 3 == 0: print('Fizz')
        elif i % 5 == 0: print('Buzz')
        else: print(i)

                                                        #Question 5
def check_number(n:int):
    is_odd = lambda n: n & 1  

    if n < 0 and not is_odd(n): return 'Very Weird'
    if n < 0 and is_odd(n): return 'Extremely Weird'

    if is_odd(n): return 'Weird'
    if not is_odd(n) and n >= 2 and n <= 5: return 'Not Weird'
    if not is_odd(n) and n >= 6 and n <= 20: return 'Weird'
    if not is_odd(n) and n > 20: return 'Not Weird'
    return 'Neutral'

