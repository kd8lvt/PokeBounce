import json

def newBattlerData(allChars,target):
        vs = {}
        for char in allChars:
            if (char.name != target): vs.setdefault(char.name,{"wins":0,"winsMatchSize":[0,0,0,0,0,0,0,0,0,0,0,0],"losses":0,"lossesMatchSize":[0,0,0,0,0,0,0,0,0,0,0,0],"matches":0,"matchesMatchSize":[0,0,0,0,0,0,0,0,0,0,0,0]})
        return {"matches":0,"matchesMatchSize":[0,0,0,0,0,0,0,0,0,0,0,0],"wins":0,"winsMatchSize":[0,0,0,0,0,0,0,0,0,0,0,0],"lossesMatchSize":[0,0,0,0,0,0,0,0,0,0,0,0],"vs":vs}

def read():
    with open("data.json","r") as file:
        return json.load(file)
    
def init(allChars):
    data = None
    try:
        open("data.json","r").close()
    except:
        data={}
        for battler in allChars:
            if battler.name not in data.keys():
                data.setdefault(battler.name,newBattlerData(allChars,battler.name))

        with open("data.json","w") as file:
            json.dump(data,file)


def write(allChars,participants,winner):
    init(allChars)
    data = read()
    for battler in participants:
        matchSize = len(participants)
        if battler.name not in data.keys():
            data.setdefault(battler.name,newBattlerData(allChars,battler.name))

        bData = data[battler.name]
        won = battler.name == winner

        bData["matches"]+=1
        bData["matchesMatchSize"][matchSize]+=1
        if won: 
            bData["wins"]+=1
            bData["winsMatchSize"][matchSize]+=1

        for other in participants:
            if other.name == battler.name: continue
            bData["vs"][other.name]["matches"]+=1
            bData["vs"][other.name]["matchesMatchSize"][matchSize]+=1
            if won:
                bData["vs"][other.name]["wins"]+=1
                bData["vs"][other.name]["winsMatchSize"][matchSize]+=1
            elif winner == other.name:
                bData["vs"][other.name]["losses"]+=1
                bData["vs"][other.name]["lossesMatchSize"][matchSize]+=1
        data[battler.name] = bData
        
    with open("data.json","w") as file:
        json.dump(data,file,indent=2)