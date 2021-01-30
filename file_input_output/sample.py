confirmed_data={}
for lines in f:
    slno,date,time,state,cnfmi,cnfmf,cured,deaths,confirmed=lines.rstrip("\n").split(",")
    if state not in confirmed_data:
        confirmed_data[state]={"slno":slno,"date":date,"time":time,"state":state,"cnfmi":cnfmi,"cnfmf":cnfmf,
                               "cured":cured,"deaths":deaths,"confirmed":confirmed}
    else:
        pass


def result(**kwargs):
    state=kwargs["state"]
    if state in confirmed_data:
        print(confirmed_data[state])
        if "prop" in kwargs:
            prop=kwargs["prop"]
            print(confirmed_data[state][prop]

result(state="Kerala",prop="confirmed")