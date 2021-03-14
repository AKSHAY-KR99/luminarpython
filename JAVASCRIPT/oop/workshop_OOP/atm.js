class Bank{
    bal_enqry(){
        console.log("Balance Enquiry");
    }
    withdraw(){
        console.log("withdraw");
    }
    __deposit(){
        console.log("inside depo");
    }
}
class Atm extends Bank{

}
atm=Atm
atm.bal_enqry
atm.withdraw