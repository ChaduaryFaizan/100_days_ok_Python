print(" Wellcome to Tip Calculator")
bill=float(input("What was Your Total Bill : "))
tip=float(input("How much persentage of tip you will give 10,15 or 20 : "))
persons=int(input("how much persons you'll share the bill : "))
tip_incement=float((bill *tip) /100 )
total_bill=tip_incement+bill
print( "total Bill : ",round(total_bill))
b_person=total_bill/persons
print("bill per Person : ",round(b_person,2))
input()