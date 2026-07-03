def Calculation(No1,No2):
    Add=No1+No2
    Sub=No1-No2
    Mult=No1*No2
    Div=No1/No2
    
    return Add,Sub,Mult,Div



def main():
    Value1=int(input("Enter a  first number:"))
    Value2=int(input("Enter a  second number:"))
    Ret=Calculation(Value1,Value2)

    print("Addition,Substraction,Multiplication and Division of two numbers are respectively is:",Ret)


if __name__=="__main__":
    main()