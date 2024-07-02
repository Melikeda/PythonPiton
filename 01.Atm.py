melikeAccount = {
    'name' : 'Melike Kulahci' ,
    'accountNumber' : '12786' ,
    'balance' : 4000 ,
    'additionalAccount' : 2000
    }


def withdrawMoney(account, amount):
    print(f"Hello {account['name']}")

    if (account['balance'] >= amount):
        print("You can get your money")

    else:
        total = account["balance"] + account["additionalAccount"]  
        
        if(total >= amount):
            additionalaccountuse =input("Should I use an additional account?  (y/n) ")

            if additionalaccountuse == 'y':
                print("You can get your money")

            else:
                print(f"{account['accountNumber']} in your account no {account["balance"]} does not exist") 

        else:
            print("Sorry, insufficient funds")           
            
        

withdrawMoney(melikeAccount,5000)
