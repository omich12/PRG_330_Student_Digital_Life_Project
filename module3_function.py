
# Module 3: Custom Function  --  Daily_Social_Media_Hours

def social_media_category(hours):
    
    if hours < 3:
        return "Low Usage"
    
    elif hours <= 6:
        return "Moderate Usage"
    
    else:
        return "High Usage"
