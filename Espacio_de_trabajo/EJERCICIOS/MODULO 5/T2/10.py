import pandas as pd

Car_Price = pd.DataFrame({'Company': ['Toyota', 'Honda', 'BMW', 'Audi'], 'Price': [23845, 17995, 135925, 71400]})  
car_Horsepower = pd.DataFrame({'Company': ['Toyota', 'Honda', 'BMW', 'Audi'], 'horsepower': [141, 80, 182, 160]})  


df = pd.merge(Car_Price,car_Horsepower, on='Company')
print(df)