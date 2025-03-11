## This function opens the CSV for You!
def csv_to_list(file_path):
    data_list = []
    
    with open(file_path, 'r') as file:
        for line in file:
            row = line.strip().split(',')
            row = [int(value) if value.isdigit() else value for value in row]
            data_list.append(row)

    return data_list


file_path = "SalesData.csv"  
data = csv_to_list(file_path)

#1  //every store all 30 days
"""def avgSalesPerDay(data):    row_totals = {}
    for row in data[1:]:
        store_name = row[0]
        sales = map(int, row[1:])
        row_totals[store_name] = round(sum(sales) / 30,2)
    return row_totals
print(avgSalesPerDay(data))"""

#2
"""def mostProfitable(data):
    row_totals = []
    for row in data[1:]:
        sales = map(int, row[1:])
        row_totals.append(sum(sales))
        row_totals.sort()
    return row_totals
print(mostProfitable(data))"""


#3 every store every day
def allStoresAvgSales(data):
    row_totals = []
    for row in data[1:]:
        sales = map(int, row[1:])
        row_totals.append(sum(sales))
    avg = sum(row_totals) / len(row_totals)        
    return avg

#4
def closingStores(data):
    twentyPercentOfAverage = allStoresAvgSales(data) * .2
    return 
closingStores(data)
