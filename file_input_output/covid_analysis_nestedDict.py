f=open("covid_19_india.csv","r")
dict={}
for lines in f:
    data=lines.rstrip("\n").split(",")
    state=data[3].rstrip("***")
    if(state=="Telengana"):
        state="Telangana"
    cured=int(data[6])
    death=int(data[7])
    confirmed_case=int(data[8])
    if state not in dict:
        dict[state]={"state":state,"cured":cured,"death":death,"confirmed":confirmed_case}
    else:
        dict[state] = {"state": state, "cured": cured, "death": death, "confirmed": confirmed_case}
print(dict)
def result(**kwargs):
    state=kwargs["state"]
    if state in dict:
        if "prop" in kwargs:
            prop=kwargs["prop"]
            print("details ",dict[state][prop])
        else:
            pass
    else:
        pass
result(state="Mizoram",prop="death")