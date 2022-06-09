#Nicko Ilham Pramudya
#L200200252

#NOMOR 1
import re

pola1 = r'@[A-Za-z]+[0-9]' 
pola2 = r'@[A-Za-z]+[0-9]+_' 

def check(instagram):   
  
    if(re.findall(pola1,instagram)):   
        print("PASS")
    elif(re.findall(pola2,instagram)):   
        print("PASS")
    else:   
        print("FAILED")

if __name__ == '__main__':
 
    instagram = "@nicko52"
    check(instagram)

    instagram = "@nicko52_"
    check(instagram)

    instagram = "@nicko_52"
    check(instagram)

#NOMOR 2
import re
paragraf = """We are hiring Test/QA Engineers with 1-3 years of experience in Manual Testing(Web, Mobile & API).
If anyone((Especially who lost the job due to COVID) looking for a change, please share me the resume at mailmesiva25@gmail.com
Company:Open Financial Technologies
Location: Bangalore
Note: Fintech Experience would be a higher priority"""

pola = r'[\w\d.-]+@[\w\d.]+\.\w+'
email = re.findall(pola,paragraf)
print(email[0])

