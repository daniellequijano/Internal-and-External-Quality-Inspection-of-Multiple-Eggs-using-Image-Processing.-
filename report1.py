from prettytable import PrettyTable
from prettytable import from_csv


#table from csv
path="/Users/Danielle/Desktop/EggIE_ver2_SOFTENG/resultegg.csv"
csv_file = open(path)
x = from_csv(csv_file)
print(x)
    