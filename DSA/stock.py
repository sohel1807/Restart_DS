def stock_profit(list):
    min_price=float("inf")
    max_profit=0
    
    for stock in list:
        min_price=min(min_price,stock)
        max_profit=max(max_profit,stock-min_price)
        
    return min_price,max_profit

print(stock_profit([7,-1,3,0,6]))    