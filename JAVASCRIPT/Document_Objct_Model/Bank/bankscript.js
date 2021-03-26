console.log(localStorage.getItem("acnt"));
class Bank{
    static accountDetails(){
        let userData={
            1000:{acno:1000,password:"userone",balance:5000},
            1001:{acno:1001,password:"usertwo",balance:5000},
            1002:{acno:1002,password:"userthree",balance:5000}
        }
        return userData;
        localStorage.setItem("data",JSON.stringify(userData))
    }


    static authenticate(acno,password){
        var dataSet=Bank.accountDetails()
        if(acno in dataSet){
            if(password==dataSet[acno]["password"]){
                
                // succesful auth
                return 1
            }
            else{
                return 0
            }
        }
        else{
            return -1
        }
    }
    static setStorage(acnt,pswd){
        let obj={
            acnt:acnt,
            pswd:pswd
        }
        localStorage.setItem("data",JSON.stringify(obj))
    }

    static login(){
        var accno=document.querySelector("#acno").value
        var password=document.querySelector("#pwd").value
        let user=Bank.authenticate(accno,password)
        if(user==0){
            alert("Invalid password")
        }
        else if(user==1){

            alert("Log in succesful")
            Bank.setStorage(accno,password)
            window.location.href="detail.html"
        }
        else if(user==-1){
            alert("invaid Account number")
        }
    }

    static withdrawal(){
        let detail=Bank.accountDetails()
        var accno=document.querySelector("#acno").value
        var password=document.querySelector("#pwd").value
        let amount=document.querySelector("#amount").value
        let user=Bank.authenticate(accno,password)
        if(user==0){
            alert("Invalid password")
        }
        else if(user==1){
            if(amount>detail[accno]["balance"]){
                alert("Insufficient balance. Cant Debit. Current balance is "+detail[accno]["balance"])
            }
            else{
                let bal=detail[accno]["balance"]-amount
                alert("Amount of "+amount+" succesfully debited and current balance is "+bal)
            }
        }
        else if(user==-1){
            alert("invaid Account number")
        }

    }

   static deposit(){

        let detail=Bank.accountDetails()
        var accno=document.querySelector("#acno").value
        var password=document.querySelector("#pwd").value
        let amount=document.querySelector("#amount").value
        let user=Bank.authenticate(accno,password)
        if(user==0){
            alert("Invalid password")
        }
        else if(user==1){
            let bal=detail[accno]["balance"]+amount
            alert("amount of "+amount+" is succesfully deposited and current balance is "+bal)
        }
        else if(user==-1){
            alert("invaid Account number")
        }
    }
}