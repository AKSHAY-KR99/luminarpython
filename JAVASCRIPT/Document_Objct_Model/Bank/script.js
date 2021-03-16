class Bank{

    accountDetails(){
        let userdata={
            1000:{accno:1000,password:"userone",balance:5000},
            1001:{accno:1001,password:"usertwo",balance:5000},
            1002:{accno:1002,password:"userthree",balance:5000}
        }
        return userdata
    }

    static authenticate(acno,password){
        var dataset=Bank.accountDetails()


    }

    static login(){
        var accno=document.querySelector("#accno")
        var password=document.querySelector("#password")
        let user=Bank.authenticate(accno,password)
        if(user==-1){
            alert("Invalid Account Number")
        }
        else if(user==0){
            alert("Invalid password")
        }
        else if(user==1){
            alert("Log in success")
        }
    }

    withdrawal(){

    }

    deposit(){

    }
}