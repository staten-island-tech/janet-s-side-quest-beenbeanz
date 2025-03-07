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

#1
def avgSalesPerDay(data):
    row_totals = {}
    
    for row in data[1:]:
        store_name = row[0]
        sales = map(int, row[1:])
        row_totals[store_name] = sum(sales) / 30

    return row_totals

print(avgSalesPerDay(data))




#3
def allStoresAvgSales(data):
    row_totals = []
    
    for row in data[1:]:
        store_name = row[0]
        sales = map(int, row[1:])
        row_totals.append(sum(sales))

   # for i in row_totals:
        
    return row_totals

allStoresAvgSalesList = allStoresAvgSales(data)
print(allStoresAvgSalesList)

