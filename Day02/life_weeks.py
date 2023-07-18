#calcular la cantidad de días, semanas y meses que le queda hasta los 90 años

#365 días
#52 semanas
#12 meses

get_age = input("What is your current age? ")
age = int(get_age)

years_remaining = 90 - age
days_remainig = years_remaining * 365
weeks_remainig = years_remaining * 52
months_remainig = years_remaining * 12

print(f"You have {days_remainig} days, {weeks_remainig} weeks, and {months_remainig} left.")