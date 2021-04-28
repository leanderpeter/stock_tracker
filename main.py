
from BO.stockBO import Stock
import pandas as pd

# list of all stock BO's in portfolio
stocks = []

# read stock csv from unicredit Hypovereinsbank
df = pd.read_csv('original_depot.csv', sep=';', encoding='utf_16_le')

# print(df.to_string())

print('==============================================')

def stk_to_float(String):
	amount = String
	amount = amount.split('Stk. ')[1]
	amount = amount.split(',')[0]
	amount = float(amount)
	return amount

for index, row in df.iterrows():
	stockBO = Stock()
	stockBO.set_name(row[1])
	stockBO.set_wkn(row[2])
	stockBO.set_bought_at(row[4])
	stockBO.set_currency(row[5])
	# amount in pieces/stocks
	amount = stk_to_float(row[3])
	stockBO.set_amount(amount)
	# stockBO.set_date()
	

import requests
import pandas as pd
import matplotlib.pyplot as plt



companies = ['AAPL', 'TSLA']
i = 0
listofdf = []
for item in companies:
    histprices = requests.get(f"https://financialmodelingprep.com/api/v3/historical-price-full/{item}?serietype=line&apikey=f1b1363d36fec2f64645c8c1a7939609")
    histprices = histprices.json()

	#Parse the API response and select only last 600 days of prices
    histprices = histprices["historical"][-50:]

	#Convert from dict to pandas datafram

    histpricesdf = pd.DataFrame.from_dict(histprices)

	#rename column
    histpricesdf = histpricesdf.rename({'close': item}, axis=1)
    
	#append all dfs to list
    listofdf.append(histpricesdf)
    i += 1




#set index of each DataFrame by common column before concatinatinghtem
dfs = [df.set_index('date') for df in listofdf]

histpriceconcat = pd.concat(dfs,axis=1)

#divide all dataframe by first line of data to enable comparison
# histpriceconcat = histpriceconcat/histpriceconcat.iloc[0]



for i, col in enumerate(histpriceconcat.columns):
    histpriceconcat[col].plot()

plt.title('Price Evolution Comparison')

plt.xticks(rotation=70)
plt.legend(histpriceconcat.columns)
plt.savefig('foo1.png', bbox_inches='tight')