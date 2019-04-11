'''IT is Banking Application for:
1. Create Account in Bank for Customer
2. Withdraw , Deposit ,Mobile Number Update And Aadhar Update Facility Provide by Bank.
3. Loan Facility Provided by bank
4. View Account Details For Customer
'''
import json

from time import sleep             #We import sleep from time Module which is useful for sleep program for Allocated time.
import os                          # In This Application we import os Module to perform clear screen Task(os.system("cls"))
from getpass import getpass        #we use getpass Module for invisible password
'''Total_Accounts :---->It is A Dictionary Which Hold Account Details For Customer such as customer Account Number as
key,Customer mobile number,Customer Aadhar Number,Username,Password as values'''

''''when A person create a New Account ,The New Account will be Added to the Dictionary'''



'''Function For Create A New Account'''
def Create_Account():
    
    @dec
    def Decorator_For_Create_Account():
        print("#"," "*50,"Create Account"," "*50,"#",sep="")
    varify(Total_Accounts)        #Function Calling For Varify Documents    
'''Function For Varify Documents and Check You are Eligible or not for Create A New Account''' 
def varify(Total_Accounts):
    Documents=[]
    try:
        Age=int(input("Enter your Age---->"))
        if Age>18:
            PAN_NO=input("Press yes if you have a PAN Card else no---->")
            Driving_licence=input("Press yes if you have a Driving licence else no-->")
            
            if PAN_NO.casefold()=="yes" and Driving_licence.casefold()=="yes":
            
                print("*"*30,"You Are Eligible For Create Account","*"*30)
                acc_list=list(Total_Accounts)
                acc_list=list(map(int,acc_list))
                acc_no=acc_list[-1]+1
                print("your Account Number is--------------> ",acc_no)
                
                mobile_no=int(input("Enter your 10 Digit Mobile number--------------> "))
                Aadhar_no=int(input("Enter your 12 Digit Aadhar number----> "))
                if len(str(mobile_no))==10 and len(str(Aadhar_no))==12: 
                    Documents.append(mobile_no)
                    Documents.append(Aadhar_no)
                    Documents.append(int(input("Enter Balance -----------------------> ")))
                    Name=input("Enter Your User Name-----------------> ")
                    print("*"*30,"Conditions For PassWord","*"*30)
                    print("1. password length must be less than 12")
                    print("2. At least 2 Digits in password")
                    pass_word=getpass("Enter your Password-------------------> ")
                    confirm_password=getpass("Enter your Password for Confirm------------> ")
                    def digit(pass_word):
                        count=0
                        for i in pass_word:
                            if i.isdigit():
                                count+=1
                            else:
                                pass
                        else:
                            if count>=2:
                                return True
                            else:
                                return False
                    if pass_word==confirm_password and len(pass_word)<12 and digit(pass_word):
                        
                        dict_value=(Documents,(Name,pass_word))
                        Total_Accounts[acc_no]=dict_value
                        print("*"*40,"Account Created","*"*40)
                    else:
                        print("Conditions For Password Are Not Fulfill")
                else:
                    print("Invalid Details")
            else:
                print("You Are Not Eligible For Create Account")
        else:
            print("Above 18 Are Eligible For Create Account")
    except ValueError as e:
        print(" ValueError---->",e)     
'''Function which Provide Banking Facility'''
def Banking(Total_Accounts):
    @dec
    def Decorator_For_Banking():
        print("#"," "*53,"Banking"," "*54,"#",sep="")
    Decorator_For_Banking()

    try:
        acc_no=int(input("Enter Your Account Number"))
        user_name=input("Enter your User Name--> ")
        password=getpass("Enter your password--> ")
        if user_name==Total_Accounts[acc_no][1][0] and password==Total_Accounts[acc_no][1][1]:
            ch=int(input("Enter Your Choice--> 1:withdraw 2:Deposit 3:Aadhar update 4:Mobile update"))
            if ch==1:
                WithDraw(Total_Accounts,acc_no)
            elif ch==2:
                deposit_amount(Total_Accounts,acc_no)
            elif ch==3:
                Update_Aadhar_no(Total_Accounts,acc_no)
            elif ch==4:
                Update_Mobile_no(Total_Accounts,acc_no)
            else:
                print("Incorrect Choice")
        else:
            print("User Name And Password Not Correct")
    except Exception as e:
        print("ValueError",e)  

'''Function For Withdraw Amount ''' 
def WithDraw(Total_Accounts,acc_no):
    print("*"*30,"WithDraw","*"*30)
    try:
        withdraw=int(input("Enter your Amount Which You Want To Withdraw--> "))
        if withdraw>500 and withdraw<Total_Accounts[acc_no][0][2]:
            Total_Accounts[acc_no][0][2]-=withdraw
            print("Remaining Balance Is---->",Total_Accounts[acc_no][0][2])
        else:
            print(f"Withdraw  Amount must be greater than 500 and less than {Total_Accounts[acc_no][0][2]}")
    except Exception as e:
        print("ValueError",e)
'''Function For Deposit Amount ''' 
def deposit_amount(Total_Accounts,acc_no):
    print("*"*30,"Deposit","*"*30)
    try:
        Deposit=int(input("Enter your Amount Which you Want to Deposit"))
        if Deposit>1000:
            Total_Accounts[acc_no][0][2]+=Deposit
            print("After Deposit Balance is",Total_Accounts[acc_no][0][2])
        else:
            print("Deposit Amount must be greater than 1000 ")
    except Exception as e:
        print("ValueError",e)
'''Function For Update Aadhar number ''' 
def Update_Aadhar_no(Total_Accounts,acc_no):
    print("*"*30,"Update Aadhar Number","*"*30)
    try:
        Aadhar_no=int(input("Enter New Aadhar number"))
        if len(str(Aadhar_no))==12:
            Total_Accounts[acc_no][0][1]=Aadhar_no
        else:
            print("Aadhar_no must be 12 Digits")
    except Exception as e:
        print("ValueError",e)
'''Function For Update Mobile Number ''' 
def Update_Mobile_no(Total_Accounts,acc_no):
    print("*"*30,"Update Mobile Number","*"*30)
    try:
        Mobile_no=int(input("Enter new mobile number"))
        l=len(str(Mobile_no))
        if l==10:
            Total_Accounts[acc_no][0][0]=Mobile_no
        else:
            print("Please Enter 10 Digit Mobile Number")
    except Exception as e:
        print("ValueError",e)
'''Fuction Which Provide Loan Facility from Bank'''
def Loan():
    @dec
    def Decorator_For_Loan():
        print("#"," "*50,"Loan Facility"," "*51,"#",sep="")
    Decorator_For_Loan()
    try:
        sector=int(input("Enter your sector --->1. Government Sector     2. Private Sector     3.Student Sector--->"))
        if sector==1:
            Government_Sector()
        elif sector==2:
            Private_Sector()
        elif sector==3:
            print("You Are Not Eligible for Loan")
        else:
            print("Incorrect Choice")
    except ValueError as e:
        print("ValueError",e)
'''Function For loan From Government Sector'''
def Government_Sector():
    print("*"*30,"Loan For Government Sector","*"*30)
    req_doc=Required_Documents()
    if req_doc:
        print("*"*30,"You Are Eligible for Loan","*"*30)
        Approval_Government_loan()
    else:
        print("*"*30,"You Are Not Eligible for Loan","*"*30)
'''Function For loan From private Sector'''
def Private_Sector():
    print("*"*30,"Loan For private Sector","*"*30)
    req_doc=Required_Documents()
    if req_doc:
        print("*"*30,"You Are Eligible for Loan","*"*30)
        Approval_Private_loan()
    else:
        print("*"*30,"You Are Not Eligible for Loan","*"*30)
'''Function to Check required Documents'''
def Required_Documents():
    proof_of_age=input("If you Have Birth Certificate Enter yes else no--->")
    Address_proof=input("If you Have PASSBOOK Enter yes else no----------->")
    proof_of_identification=input("If you Have Driving Licence Enter yes else no-->")
    if Address_proof.casefold()=="yes" and proof_of_identification.casefold()=="yes" and proof_of_age.casefold()=="yes":
        return True
    else:
        return False
'''Function for Approval Government Loan'''
def Approval_Government_loan():
    try:
        Loan_Amount=int(input("Enter your Loan Amount---->"))
        Salary=int(input("Enter your Salary per Month---->"))
        Annual_Salary=Salary*12
        if Annual_Salary>600000:
            print("Loan Approved and You Have Provided of Loan of 70% of your Salary")
        elif Annual_Salary>100000 and Annual_Salary<=600000:
            print("Loan Approved and You Have Provided of Loan of 45% of your Salary")
        else:
            print("Loan Approved and You Have Provided of Loan of 15% of your Salary")
    except Exception as e:
        print("ValueError",e)
'''Function for Approval private Loan'''
def Approval_Private_loan():
    try:
        Loan_Amount=int(input("Enter your Loan Amount---->"))
        Salary=int(input("Enter your Salary per Month---->"))
        Annual_Salary=Salary*12
        if Annual_Salary>600000:
            print("Loan Approved and You Have Provided of Loan of 50% of your Salary")
        elif Annual_Salary>100000 and Annual_Salary<=600000:
            print("Loan Approved and You Have Provided of Loan of 35% of your Salary")
        else:
            print("Loan Approved and You Have Provided of Loan of 10% of your Salary")
    except Exception as e:
        print("ValueError",e)
'''Function For View Account Details'''
def View_Account(Total_Accounts):
    @dec
    def View_details_Decorator():
         print("#"," "*50,"View Details"," "*52,"#",sep="")
    View_details_Decorator()
    try:
        acc_no=int(input("Enter your Account Number"))
        if acc_no in Total_Accounts.keys():
            print(f"Mobile Number is {Total_Accounts[acc_no][0][0]} \nAadhar Number is {Total_Accounts[acc_no][0][1]} \nAccount Balance is {Total_Accounts[acc_no][0][2]}")
        else:
            print("Incorrect Account Number")
    except Exception as e:
        print("ValueError",e)

Manager_details={1:("SBI",123456)}           #Manager_details is a dictionary which Hold The id as key and User name , Password as Value and we use this Dictionary in Manager_Authentication function and Create_Account function
'''Function For Manager Authentication,In Which Manager can See the Total Accounts In Bank'''
    
def Manager_Authentication(Total_Accounts):
    @dec
    def Manager_Authentication_Decorator():
         print("#"," "*46,"Manager Authentication"," "*46,"#",sep="")
    Manager_Authentication_Decorator()
    try:
        i_d=int(input("Enter your ID---------->"))
        user_name=input("Enter Your UserName---->")
        pass_word=int(getpass("Enter your PassWord"))
        if user_name==Manager_details[i_d][0] and pass_word==Manager_details[i_d][1]:
            print("*"*30,"Total Accounts Details In Bank","*"*30)
            for var in Total_Accounts.keys():
                print(Total_Accounts[var])
        else:
            print("Incorrect User Name And Password")
    except ValueError as e:
        print("ValueError",e)
    except KeyError as e:
        print("KeyError",e)
def processing():
    print("Please Wait",end="")
    for i in range(6):
        sleep(.5)
        print("-",end="",flush=True)
#Function For Decorating 
def dec(fun):
    def inner():
        for i in range(1,8):
            if i==1 or i==7:
                print("$"*116)
            if i==4:
                fun()
            if i!=1 and i!=7 and i!=4:
                print("#"," "*114,"#",sep="")
    return inner
@dec                          
def Decorator_For_Login_page():
    print("#"," "*42,"Welcome To State Bank Of India"," "*42,"#",sep="")
Decorator_For_Login_page()
processing()
fp=open("hello_Accounts.json")
Total_Accounts=json.load(fp)

while True:             
    try:
        print()
        choice=int(input("Enter your choice----> 1. Create Account    2. Banking    3. Loan     4. View Account Details       5. Manager Authentication----->"))
        processing()
        print()
        if choice==1:
            Create_Account()

        elif choice==2:
            Banking(Total_Accounts)

        elif choice==3:
            Loan()

        elif choice==4:
            View_Account(Total_Accounts)

        elif choice==5:
            Manager_Authentication(Total_Accounts) 
        else:
            print("Please Enter A Valid Choice")
        press_character=input("If you Want to Continue Please press y else press Anykey : ")
        if press_character.casefold()=='y':
            os.system("cls")
        else:
            @dec
            def Decorator_For_Thank_you():
                print("#"," "*52,"Thank You"," "*53,"#",sep="")
            Decorator_For_Thank_you()
            fp = open("hello_Accounts.json","w")
            json.dump(Total_Accounts,fp)
            fp.close()
            break
            
    except ValueError as e:
        print("ValueError---->",e,sep="")
        
        

