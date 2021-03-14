class Bank{
    bank_name="federal Bank"
    createAccount(accno,name,minbalnce){
        this.accno=accno
        this.name=name
        this.minbalnce=minbalnce
    }
    withdraw(amount){
        if(amount>this.minbalnce){
            console.log("Insufficient balance on our account");
        }
        else{
            this.minbalnce-=amount
            console.log(Bank.bank_name` your account ${this.accno} has been debited with ammount of ${amount} and current balance is ${this.minbalnce}`);
        }
    }
    deposit(depo){
        this.minbalnce+=depo
        console.log(`your account ${this.accno} has been credited with ammount of ${depo} and current balance is ${this.minbalnce}`);
    }
    balanceEnqry(){
        console.log(`your account ${this.accno} and current balance is ${this.minbalnce}`);
    }
}

// obj1=new Bank
// obj1.createAccount(101010,"Akshay",2000,"fedaral Bank")
// obj1.deposit(12599)
obj1=new Bank
obj1.createAccount(101010,"Akshay",2000)
obj1.deposit(599)