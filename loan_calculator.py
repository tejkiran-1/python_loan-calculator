# Loan Calculator
import math
import argparse

parser = argparse.ArgumentParser(description='What do you want to calculate?\n'
                                             'type "n" for number of monthly payments\n'
                                             'type "a" for the annuity monthly payment\n'
                                             'type "p" for loan principal\n'
                                             'type "d" for differential payment: ')

parser.add_argument('--type', metavar='type', help='indicates the type of payment', required=True,
                    choices=['annuity', 'diff'])
parser.add_argument('--payment', metavar='payment', type=int, help='is the monthly payment amount')
parser.add_argument('--principal', metavar='principal', type=int, help='loan principal')
parser.add_argument('--periods', metavar='periods', type=int, help='number of months')
parser.add_argument('--interest', type=float)

args = parser.parse_args()

calc_type = args.type

# Calculating the annuity monthly payment
if calc_type == "annuity":
    if args.principal is None:
        a = args.payment
        n = args.periods
        interest_rate = args.interest
        i = interest_rate / 100 / 12
        p = int(a / ((i * math.pow(1 + i, n)) / (math.pow(1 + i, n) - 1)))
        print("Your loan principal = " + str(p) + "!")

    elif args.payment is None:
        p = args.principal
        n = args.periods
        interest_rate = args.interest
        i = interest_rate / 100 / 12

        a = math.ceil(p * i * (math.pow(1 + i, n)) / (math.pow(1 + i, n) - 1))
        print(f'Your annuity payment ={a}!')
        Total_payment = a * n
        Overpayment = Total_payment - p
        print(f'Overpayment={Overpayment}')

    elif args.periods is None:
        if args.interest is None:  # interest value always needed
            print("Incorrect parameters")
        else:
            p = args.principal
            a = args.payment
            interest_rate = args.interest
            i = interest_rate / 100 / 12
            n = math.ceil(math.log((a / (a - i * p)), 1 + i))
            Total_payment = a * n
            Overpayment = Total_payment - p
            if n < 12:
                print(f'It will take {n} months to repay this loan!')
                print(f'Overpayment = {Overpayment}')
            elif n == 12:
                print(f'It will take 1 year to repay this loan!')
                print(f'Overpayment = {Overpayment}')
            else:
                y = n // 12
                r = n % 12
                if r != 1:
                    print(f'it will take {y} years and {r} months to repay this loan!')
                    print(f'Overpayment = {Overpayment}')

                else:
                    print(f'it will take {y} years and {r} month to repay this loan!')
                    print(f'Overpayment = {Overpayment}')

# print("Your monthly payment = " + str(math.ceil(a)) + "!")

# Calculating differentiated payments
elif calc_type == "diff":
    if args.interest is None:  # interest value always needed
        print("Incorrect parameters")
    else:
        p = args.principal
        n = args.periods
        interest_rate = args.interest
        i = float(interest_rate / 100 / 12)
        m = n
        a = math.ceil(p * i * (math.pow(1 + i, n)) / (math.pow(1 + i, n) - 1))
        Total_payment = 0

        for m in range(1, n+1):
            dm = (p / n) + i * (p - (p * (m - 1)) / n)
            print(f'Month {m} : payment is {math.ceil(dm)}')
            Total_payment += math.ceil(dm)
        Overpayment = Total_payment - p
        print(f'with overpayment = {math.floor(Overpayment)}')


elif calc_type != "annuity" or "diff":
    print('Incorrect parameters')
