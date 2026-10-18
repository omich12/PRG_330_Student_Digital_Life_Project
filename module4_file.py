
# Module 4: File I/O

def save_report(report):
    
    file = open("student_analysis_report.txt", "w")
    
    file.write(report)
    
    file.close()
