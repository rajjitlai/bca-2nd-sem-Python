# Python program to find the total sales of a Salesman

def salesReport(salesRecord):
          totalSales = sum(salesRecord)
    
          if totalSales >= 80000:
                    remarks = "Excellent"
          elif totalSales >= 60000:
                    remarks = "Good"
          elif totalSales >= 40000:
                    remarks = "Average"
          else:
                    remarks = "Work Hard"
        
          if totalSales >= 50000:
                    commission = totalSales * 0.05
          else:
                    commission = 0
        
          return totalSales, commission, remarks

salesRecord = [15000, 20000, 25000, 30000]

# Call the function
totalSales, commission, remarks = salesReport(salesRecord)

print("Total Sales: ", totalSales)
print("Commission: ", commission)

if remarks == "Excellent":
    print("Great job! You exceeded your sales target.")
elif remarks == "Good":
    print("Well done! You made good sales this month.")
elif remarks == "Average":
    print("Good effort! Keep working to improve your sales.")
else:
    print("You need to work harder to meet your sales targets.")
