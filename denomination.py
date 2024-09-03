amount=int(input("please enter the amount that you want to withdraw"))
note500=amount//500
note100=(amount%500)//100
note10=((amount%500)%100)//10
print("the number of notes of 500 are",note500)
print("the number of notes of 100 are",note100)
print("the number of notes of 10 are",note10)