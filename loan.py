#input variables
def customer_eligibility():
  salary = float(input("Enter your salary amount:"))  
  loan_amount= float(input("Enter loan amount:"))
#check if the customer is eligible for loan 
  if salary>= 30000 and loan_amount<= salary *10:
      print("Eligible for loan!")
      months = int(input("months:"))

#calculate      
      loan_interest = loan_amount *0.10
      monthly_payment = loan_interest / months
      
      print(f"Your loan interest with 10%: {loan_interest:.2f}")
      print(f"Your monthly payment is:{monthly_payment:.2f}")
#if the customer is not eligible for loan
  else:
      if salary < 30000:
         print("Not eligible for loan")
      if loan_amount > salary*10 :
         print("Requested loan is too high!")

customer_eligibility()