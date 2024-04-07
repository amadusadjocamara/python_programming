name_titan = input ("Who was in the Titanic: ")
year = (input("What year is it currently: "))
def titanic_fun (name_titan, year):
    year = 2024 - int (year)
    print(f"{name_titan} were on the Titanic, was {year} year ago")
titanic_fun(name_titan, year)
