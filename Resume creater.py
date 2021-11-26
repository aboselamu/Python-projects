""" Simple Resame creater """ 
import re
# Making a small resume
def input_fun(dicValue):
    for val in dicValue:
        dicValue[val] = re.sub(' +', ' ', input("Please Enter " + val).lower())
    return dicValue

user_info = {"fullname ":"","Name_pro_langu ": "","Name_of_company ": "","Level_of_study ":"",
             "field_of_study ": "","Name_of_Institution ":"","Grade_poin t":"0","Previous_organization ":"",
             "years_of_experiance ":"0"}

def resumeFun(var):
    print("Do you want to creat the best resume just in one minute\n")
    willing = input("Enter yes to continue:")
    if willing.lower().strip() == "yes":
        data = input_fun(user_info)
        infos= [value for value in data.values()]

        print("\nMy name is " + infos[0].title().strip() +" and I am very good at " + infos[1].upper().strip() + " and " +
                  " I want to apply for the position your company," + infos[2].title().rstrip() + ", offering.\nI have " + 
                   infos[3].upper().strip() +" in " + infos[4].title().strip()+ " from " + infos[5].title().strip() + " with " + 
              infos[6].strip() + ". I previously worked at " + infos[7].title().strip() +" for " + 
                  infos[8].strip() + " years" + ". If you give me the opportunity you will not regret." +
                  " I look forward hearing from you.\nThank you very much.") 
            
    else:
        print("Goodby")
#         break
resumeFun(user_info)