import teamdata
import time


def TSarrangement():

    print("------------------------------------")
    print("|          |  {}  |           |".format(teamdata.Player1[0]))
    print("|          |___________|           |")
    print("|       {}    {}        |".format(teamdata.Player3[0], teamdata.Player4[0]))
    print("| {}                  {}  |".format(teamdata.Player2[0], teamdata.Player5[0]))
    print("|                                  |")
    print("|        {}       {}         |".format(teamdata.Player6[0], teamdata.Player7[0]))
    print("|__________________________________|")
    print("|                                  |")
    print("|  {}       {}      {}  |".format(teamdata.Player9[0], teamdata.Player10[0], teamdata.Player8[0]))
    print("|                                  |")
    print("|                                  |")
    print("|           ____________           |")
    print("|          |  {}   |          |".format(teamdata.Player11[0]))
    print("|          |            |          |")
    print("------------------------------------")

def GSarrangement():

    print("------------------------------------")
    print("|          |  {}  |           |".format(teamdata.Player12[0]))
    print("|          |___________|           |")
    print("|        {}     {}        |".format(teamdata.Player14[0], teamdata.Player15[0]))
    print("| {}                  {}  |".format(teamdata.Player13[0], teamdata.Player16[0]))
    print("|                                  |")
    print("|          {}       {}         |".format(teamdata.Player17[0], teamdata.Player18[0]))
    print("|__________________________________|")
    print("|                                  |")
    print("|  {}   {}   {}  |".format(teamdata.Player20[0], teamdata.Player21[0], teamdata.Player19[0]))
    print("|                                  |")
    print("|                                  |")
    print("|           ____________           |")
    print("|          |   {}   |          |".format(teamdata.Player22[0]))
    print("|          |            |          |")
    print("------------------------------------")

def FBarrangement():

    print("------------------------------------")
    print("|          |  {}    |           |".format(teamdata.Player23[0]))
    print("|          |___________|           |")
    print("|        {}     {}          |".format(teamdata.Player25[0], teamdata.Player26[0]))
    print("| {}                  {}  |".format(teamdata.Player24[0], teamdata.Player27[0]))
    print("|                                  |")
    print("|        {}      {}         |".format(teamdata.Player28[0], teamdata.Player29[0]))
    print("|__________________________________|")
    print("|                                  |")
    print("|  {}      {}     {}  |".format(teamdata.Player31[0], teamdata.Player32[0], teamdata.Player30[0]))
    print("|                                  |")
    print("|                                  |")
    print("|           ____________           |")
    print("|          |   {}   |          |".format(teamdata.Player33[0]))
    print("|          |            |          |")
    print("------------------------------------")

def BJKarrangement():
    print("------------------------------------")
    print("|          |  {}   |           |".format(teamdata.Player34[0]))
    print("|          |___________|           |")
    print("|         {}        {}         |".format(teamdata.Player36[0], teamdata.Player37[0]))
    print("| {}                    {}  |".format(teamdata.Player35[0], teamdata.Player38[0]))
    print("|                                  |")
    print("|        {}       {}         |".format(teamdata.Player39[0], teamdata.Player40[0]))
    print("|__________________________________|")
    print("|                                  |")
    print("|  {}       {}      {}  |".format(teamdata.Player42[0], teamdata.Player43[0], teamdata.Player41[0]))
    print("|                                  |")
    print("|                                  |")
    print("|           ____________           |")
    print("|          |   {}    |          |".format(teamdata.Player44[0]))
    print("|          |            |          |")
    print("------------------------------------")

def TSedit(change1, change2):
    count = 0
    count = teamdata.Tsarrangmentchange[change1]
    teamdata.Tsarrangmentchange[change1] = teamdata.Tsarrangmentchange[change2]
    teamdata.Tsarrangmentchange[change2] = count
    print("New team arrangment is coming...\n")
    time.sleep(3)

    i = 0
    while (i < 11):
        print(str(i) + "." + teamdata.Tsarrangmentchange[i])
        i += 1


def GSedit(change3, change4):
    count = 0
    count = teamdata.Gsarrangmentchange[change3]
    teamdata.Gsarrangmentchange[change3] = teamdata.Gsarrangmentchange[change4]
    teamdata.Gsarrangmentchange[change4] = count
    print("New team arrangment is coming...\n")
    time.sleep(3)

    i = 0
    while (i < 11):
        print(str(i) + "." + teamdata.Gsarrangmentchange[i])
        i += 1


def FBedit(change5, change6):
    count = 0
    count = teamdata.Fbarrangmentchange[change5]
    teamdata.Fbarrangmentchange[change5] = teamdata.Fbarrangmentchange[change6]
    teamdata.Fbarrangmentchange[change6] = count
    print("New team arrangment is coming...\n")
    time.sleep(3)

    i = 0
    while (i < 11):
        print(str(i) + "." + teamdata.Fbarrangmentchange[i])
        i += 1


def BJKedit(change7, change8):
    count = 0
    count = teamdata.Bjkarrangmentchange[change7]
    teamdata.Bjkarrangmentchange[change7] = teamdata.Bjkarrangmentchange[change8]
    teamdata.Bjkarrangmentchange[change8] = count
    print("New team arrangment is coming...\n")
    time.sleep(3)

    i = 0
    while (i < 11):
        print(str(i) + "." + teamdata.Bjkarrangmentchange[i])
        i += 1

def TSlist():
    i = 0
    while (i < 11):
        print(str(i) + "." + teamdata.TSname[i])
        i += 1

def GSlist():
    i = 0
    while (i < 11):
        print(str(i) + "." + teamdata.GSname[i])
        i += 1

def FBlist():
    i = 0
    while (i < 11):
        print(str(i) + "." + teamdata.FBname[i])
        i += 1

def BJKlist():
    i = 0
    while (i < 11):
        print(str(i) + "." + teamdata.BJKname[i])
        i += 1
