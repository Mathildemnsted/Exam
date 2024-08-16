# A

data1 = {
    'salesTarget': input("type performance of Sales Target: Less than 80%: Poor\n80% to 100%: Average\n 100% to 120%: Good\nAbove 120%: Excellent\n"),
    'customerSatisfaction': input("type performance of Customer Satisfaction:\nLess than 6: Poor\n6 to 7: Average\n8 to 9: Good\n10: Excellent\n"),
    'attendance': input("type performance of attendance:\nLess than 20 days: Poor\n20 to 24 days: Average\n25 to 27 days: Good\n28 and more days: Excellent\n"),
    'peerFeedback': input("Type performance of Peer Feedback:\nLess than 4: Poor\n4 to 6: Average\n7 to 8: Good\n9 to 10: Excellent\n")
}

def evaluate_performance(data):
    #store performance in list: 
    performanceList = [data['salesTarget'], data['customerSatisfaction'], data['attendance'], data['peerFeedback']]

    #add performance parameters: 
    poor = 0
    average = 0
    good = 0
    excellent = 0 

    #loop through list to check the rating
    for rating in performanceList:
        if rating == 'poor':
            poor += 1
        elif rating == 'average':
            average += 1
        elif rating == 'good':
            good +=1 
        else: 
            excellent += 1
    
    #give final score 
    if excellent == 4: 
        overallRating = 'Outstanding'
    elif poor >= 2: 
        overallRating = 'Needs improvement'
    elif good == 1:
        if excellent >= 2: 
            overallRating = 'Strong performance'
        else: 
            overallRating = 'Satisfactory'
    elif good == 2:
        if excellent >= 1: 
            overallRating == "Strong performance"
        else: 
            overallRating = 'Satisfactory'
    elif good >= 3: 
        overallRating = 'Strong performance'
    else: 
        overallRating = 'Satisfactory'
  
    return overallRating

print(f"The overall rating of employee is: {evaluate_performance(data1)}")

#b 

data2 = { 
    'performanceRating': evaluate_performance(data1),
    'yearsOfService': int(input("How many years of service?\n")) 
}
def calculate_bonus(data2): 
    bonus = 0
    #Calculate basebonus based on performance 
    if data2['performanceRating'] == 'Outstanding':
        bonus += 1000
    elif data2['performanceRating'] == 'Strong performance':
        bonus += 800
    elif data2['performanceRating'] == 'Satisfactory': 
        bonus += 500 
    else: 
        bonus += 200 

    #calculate final bonus based on years of service 
    if data2['yearsOfService'] < 2: 
        bonus *= 1
    elif data2['yearsOfService'] <= 5: 
        bonus *= 1.5
    else: 
        bonus *= 2
    return bonus

print(f"the final bonus is: {calculate_bonus(data2)}")







        
         



