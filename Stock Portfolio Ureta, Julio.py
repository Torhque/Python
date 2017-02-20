## Julio Ureta CSC102

## Create Names dictionary.
Names = {}

####Names["GM"] = "General Motors"

## Create Prices dictionary.
Prices = {}

## Create Exposure dictionary.
Exposure = {}


## Asks the user for a Stock Symbol and Name pairing then adds it to the Names dictionary.
def AddName():
    stock_symbol = input("Please enter a Stock Symbol: ")
    company_name = input("Please enter Name of the stock: ")

    Names[stock_symbol] = company_name

    return stock_symbol

## Takes a Stock Symbol as an input parameter, then asks the user for the Buy price
## and the Current price of the corresponding stock, adding them to the Prices dictionary.
def AddPrices(stock_symbol):
    buy_price = input("Please enter the Buy Price of the stock: ")
    buy_price = float(buy_price)
    
    current_price = input("Please enter the Current Price of the stock: ")
    current_price = float(current_price)

    Prices[stock_symbol] = [buy_price, current_price]
    
## Takes a Stock Symbol as an input parameter, then asks the user for the Risk and
## Shares of the corresponding stock, adding them to the Exposure dictionary.
def AddExposure(stock_symbol):
    stock_risk = input("Please enter the Risk of the stock: ")
    stock_risk = float(stock_risk)

    stock_shares = input("Please enter the Shares of the stock: ")
    stock_shares = float(stock_shares)

    Exposure[stock_symbol] = [stock_risk, stock_shares]

## Calls AddName, AddPrices, and AddExposure to add a new stock to the portfolio.
def AddStock():
    stock_symbol = AddName()
    AddPrices(stock_symbol)
    AddExposure(stock_symbol)

def ExpectedSaleValue(stock_symbol):
    expected_sale_value = (((Prices[stock_symbol][1] - Prices[stock_symbol][0])
                           - Exposure[stock_symbol][0] * Prices[stock_symbol][1])
                           * Exposure[stock_symbol][1])
    
    return float(expected_sale_value)

## Finds the maximum expected value of selling a stock. The expected sale value of
## a stock is the current profit minus the future value of the stock:
##  Expected Sale value = ( ( Current Price - Buy Price ) - Risk * CurrentPrice ) * Shares
def GetSale():

    for key in Names:
        biggest = ExpectedSaleValue(key)
        
    for key in Names:
        if biggest < ExpectedSaleValue(key):
            biggest = ExpectedSaleValue(key)
           
    print(key)

## Should take no arguments, but present a menu item consisting of "1. Add Stock", "2.
## Recommend Sale" and "3. Exit". If the user selects '1,' the Add Stock function is called,
## and when it is complete, the menu is presented again. If the user selects '2,' the Symbol
## of the stock corresponding to the highest expected value (returned by GetSale) should be
## displayed, and the menu presented after completion. If the user selects '3', the program should end.
def Main():

    quit_program = False
    
    print("Main Menu")
    user_input = input("Enter 1 to add a stock, enter 2 to receive a sale recommendation," +
                       " or press 3 to exit the program. ")
    user_input = int(user_input)

    while(quit_program == False):
        
        while user_input < 1 or user_input > 3:
            user_input = input("Enter 1 to add a stock, enter 2 to receive a sale recommendation," +
                           " or press 3 to exit. ")
            user_input = int(user_input)

        if user_input == 1:
            AddStock()
            user_input -= 1
        elif user_input == 2:
            GetSale()
            user_input -= 2
        else:
            quit_program = True

Main()
