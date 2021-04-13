# Payment Function Credit Card
def Payment():
    """This is function which will do online credit card payment
    it will take input of cardno, , expiry  , owner, and amount cvv.
    This will work as a replacement of human to ai for online payment."""

    name = input("Whats Your good Name sir/maam\n"
                 "Enter Here:- ")
    print("Ok", name, "Nice to meet you")
    cardno = int(input("Enter Your card no.:-  "))
    if cardno < 12 and cardno > 12: print("Invalid number") and int(input("Enter Your card no.:-  "))
    expirydate = str(input("Enter card expiry:- "))
    cardowner = str((input("Enter Card Owner Name:- ")))
    cvv = int(input("Enter cvv:- "))
    if cvv < 3 and cvv > 3: print("Invalid cvv") and int(input("Enter cvv:- "))
    print()
    amount = int(input("Whats the amount rupees:-"))
    print("Pls confirm your details:-")
    print("Card number - ",cardno)
    print("Expiry Date", expirydate)
    print("Card Owner - ", cardowner)
    print("CVV - ", cvv)
    print("Amount", amount)
    print()
    comform = str(input("Conform? yes or no\n"
                        "enter here:- "))
    if comform== "yes":
        print("Payment Succesfull")
    else:
        print()
        print("Ok", name, "Do Payment again:-\n")




