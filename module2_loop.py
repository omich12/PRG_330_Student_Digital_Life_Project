
# Module 2: Loop Statement -- Burnout_Level

def count_burnout(burnout_data):
    
    low = 0
    moderate = 0
    high = 0
    severe = 0
    
    for level in burnout_data:
        
        if level == "Low":
            low += 1
            
        elif level == "Moderate":
            moderate += 1
            
        elif level == "High":
            high += 1
            
        elif level == "Severe":
            severe += 1
    
    return low, moderate, high, severe
