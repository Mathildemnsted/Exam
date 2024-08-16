import numpy as np
import matplotlib.pyplot as plt

price = 15
lostSale = 10
avgDemand = 800
maxProduction = 1200

def simulate_production(productionCost):
    productionQuantities = list(range(maxProduction + 1)) #i make the lists so i can use it to plot the figure 
    avgProfits = []

    for production in productionQuantities:
        totalProfit = 0
        
        for i in range(1000):
            demand = np.random.poisson(avgDemand)
            if demand <= production:
                revenue = price * demand
                costs = productionCost * production
            else:
                revenue = price * production
                costs = productionCost * production + lostSale * (demand - production)
            profit = revenue - costs
            totalProfit += profit
        
        # Average profit over the 1000 simulations
        avgProfits.append(totalProfit/1000)
    
    bestProfit = max(avgProfits)
    bestProduction = productionQuantities[avgProfits.index(bestProfit)]

    print(f"With production cost of {productionCost}, the best quantity to produce is: {bestProduction}, which results in an average profit of: {bestProfit}")
    #plot the figure 
    plt.figure()
    plt.plot(productionQuantities, avgProfits, label=f'Production Cost: {productionCost}')
    plt.title('Average Profit at Production Quantity')
    plt.xlabel('Production Quantity')
    plt.ylabel('Average Profit')
    plt.savefig(f'prodCost{productionCost}.png')
    
    return productionQuantities, avgProfits
    
#Production cost = 4 
simulate_production(productionCost=4)
#Production cast = 5 
simulate_production(productionCost=5)



