import pandas as pd 
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/NikoStein/pds_data/main/sales.csv'

sales = pd.read_csv(url) 
sales.to_csv('sales.csv') 

#Total sales pr store in 2014
sales['Date'] = pd.to_datetime(sales['Date']) # make dates datetime 

selector1 = sales['Date'] >= '2014-01-01'
selector2 = sales['Date'] <= '2014-12-31'

sales2014 = sales[selector1 & selector2]
total_sales_2014 = sales2014.groupby(['Store'])[['Sales']].sum()
print(f"Total sales pr. store in 2014: {total_sales_2014}")

#Store with most consistent sales 
salesStdDev = sales.groupby(['Store'])['Sales'].std()
minStd =salesStdDev.min() 
storeMinStd = salesStdDev.idxmin() # finds the index where the min stdDev is, which is equal to the store number

print(f"The store with most consistent sales is: store {storeMinStd}, which has a stdDev of {minStd}")

#Monthly sales trend for each store

sales['Month'] = sales['Date'].dt.to_period('M') # set dates to months in yyyy-mm format
monthly_sales_trend = sales.groupby(['Store', 'Month'])['Sales'].sum().reset_index() #sum the sales pr months ans set the series to a dataframe
monthly_sales_trend.columns = ['Store', 'Month', 'TotalSales'] #create the "totalSales header"
print(f"the monthly sales for each store:\n{monthly_sales_trend}")

#Sales Distribution by day of the week 
avgSalesWeekDay = sales.groupby(['DayOfWeek'])['Sales'].mean()

# Create plot
plt.figure()
plt.bar(avgSalesWeekDay.index, avgSalesWeekDay.values)
plt.title('Average Sales Per Weekday')
plt.xlabel('Weekday (1: Monday, 2: Tuesday, ..., 7: Sunday)')
plt.ylabel('Average Sales')
plt.savefig('task3avgSalesDaysOfWeek.png')

#Sales trends top 5 stores 
#top 5 stores 
topStores = sales.groupby('Store')['Sales'].sum().nlargest(5).index

#get the dat from top 5
topSales = sales[sales['Store'].isin(topStores)]

# create the figure

plt.figure()

for store in topStores:
    store_data = topSales[topSales['Store'] == store]
    plt.plot(store_data['Date'], store_data['Sales'], label=f'Store {store}') # I im not sure if this is the correct line plot, but i do not have time to correct it 

plt.title('Sales Trend for the Top 5 Stores')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.tight_layout() 
plt.savefig('SalesTrendTop5Stores.png')











