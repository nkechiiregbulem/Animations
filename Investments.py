XRP_Price = 0.46
Bitcoin_Price = 6474
Ethereum_Price = 202.78
Cardano = 0.07
Tron = 0.02
Kin = 0.000056
Investment_Quantity_XRP = int(input("How much XRP do you hold? "))
Investment_Quantity_BTC = int(input("How much BTC do you hold? "))
Investment_Quantity_ETH = int(input("How much ETH do you hold? "))
Investment_Quantity_ADA = int(input("How much ADA do you hold? "))
Investment_Quantity_TRX = int(input("How much TRX do you hold? "))
Investment_Quantity_KIN = int(input("How much KIN do you hold? "))
Investment_Status = input("Are you invested?")
value = XRP_Price * Investment_Quantity_XRP +Bitcoin_Price * Investment_Quantity_BTC +Ethereum_Price * Investment_Quantity_ETH+Cardano * Investment_Quantity_ADA+Tron * Investment_Quantity_TRX+Kin * Investment_Quantity_KIN

def getPortfolio():
    if Investment_Status == "Yes":
        print(value)
    else:
        print("Portfolio Value: 0")
PortfolioValue = [
    {"Name": "XRP", "Price": 0.46},
    {"Name":"Bitcoin","Price":6474},
    {"Name":"Ethereum","Price": 202.78},
    {"Name":"Cardano", "Price": 0.07},
    {"Name":"Tron","Price": 0.02},
    {"Name":"Kin","Price": 0.000056},
]
def getPortfolioValue(getPortfolio):
    for value in getPortfolio:
        if Investment_Status == "Yes":
            return value
if __name__ == "__main__":
    print("$", value)