import math
import argparse


def diff(p, n, i):
    total = 0
    for m in range(1, n + 1):
        d = math.ceil((p / n) + (i * (p - (p * (m - 1) / n))))
        total += d
        print(f'Month {m}: payment is {d}')
    print(f'\nOverpayment = {total - p}')


def monthly_payment_amount(p, i, n):
    magic_value = magic_box(i, n)
    annuity = math.ceil(p * magic_value)
    overpayment = (n * annuity) - p
    print(f"Your annuity payment = {annuity}!")
    print(f"Overpayment = {overpayment}")


def loan_principal(i, n, a):
    magic_value = magic_box(i, n)
    p = math.ceil(a / magic_value)
    overpayment = (n * a) - p
    print(f"Your loan principal = {p}!")
    print(f'Overpayment = {overpayment}')


def magic_box(i, n):
    # processes that hot mess of a fraction
    # returns value needed to calculate for
    # monthly_payment_amount or
    # loan_principal
    temp = (1 + i) ** n
    magic_value = i * temp / (temp - 1)
    return magic_value


def total_duration(n):
    y = n // 12
    m = n % 12
    answer = f'It will take {y} years '
    if m:
        answer += f'and {m} months '
    answer += 'to repay this loan!'
    print(answer)


def num_of_payments(p, i, a):
    arg = a / (a - i * p)
    n = math.log(arg, 1 + i)
    n = math.ceil(n)
    overpayment = (n * a) - p
    total_duration(n)
    print(f'Overpayment = {overpayment}')


def prep_values(p, i, n, a):
    p = int(principal) if p else 0
    i = float(interest) / (12 * 100) if i else 0
    n = int(months) if n else 0
    a = int(a) if a else 0
    return [p, i, n, a]


parser = argparse.ArgumentParser()
parser.add_argument("--type")
parser.add_argument("--principal")
parser.add_argument("--periods")
parser.add_argument("--interest")
parser.add_argument("--payment")

args = parser.parse_args()

type_choice = args.type
principal = args.principal
interest = args.interest
months = args.periods
payment = args.payment

[principal, interest, months, payment] =\
    prep_values(principal, interest, months, payment)

if type_choice == "diff":
    if not all([principal, interest, months]):
        print("Incorrect parameters.")
    else:
        diff(principal, months, interest)
if type_choice == "annuity":
    if not months:
        if interest:
            num_of_payments(principal, interest, payment)
        else:
            print("Incorrect parameters.")
    if not principal:
        loan_principal(interest, months, payment)
    if not payment:
        monthly_payment_amount(principal, interest, months)
