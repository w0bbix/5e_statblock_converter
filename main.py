import os


def main():
    file = input("Enter a file or directory")
    if file.endswith(".xml"):
        convert(file)
    else:
        directory = os.listdir(file)
        for item in directory:
            if item.endswith(".xml"):
                convert(file + "/" + item)


def damageTypeList(resists):
    return ""


def score2mod(score):
    return "0"


def sizeadjust(abbr):
    return "Normal"


def speedlist(speeds):
    return ""


def saveslist(saves):
    return "saves"


def actionlist(actions):
    return ""


def traitlist(traits):
    return ""


def convert(path):
    xmlfile = open(path).read().splitlines()
    newfilename = path.split("/")
    newfilename = newfilename[-1]
    newfilename = newfilename[:-4]
    newfilename += ".txt"
    newfile = open(newfilename)
    xmlfile = xmlfile[3:]
    xmlfile = xmlfile[:-2]
    name = ""
    size = ""
    creaturetype = ""
    alignment = ""
    ac = ""
    maxHP = ""
    speeds = []
    STR = ""
    DEX = ""
    CON = ""
    INT = ""
    WIS = ""
    CHA = ""
    PassivePerception = ""
    saves = []
    skills = []
    languages = ""
    cr = ""
    xp = ""
    vulns = ""
    resists = ""
    immunes = ""
    conditionimmunes = ""
    senses = ""
    traits = []
    actions = []

    inblock = 0  # inblock 0 = not in a block, 1 = trait block, 2 = action block
    blockname = ""
    blocktext = ""
    lineinfo = ""
    for line in xmlfile:
        if line.endswith("</name>"):
            lineinfo = line.split("<")
            if inblock == 0:
                name = lineinfo[-1]
            else:
                blockname = lineinfo
            continue
        if line.endswith("</size>"):
            lineinfo = line.split("<")
            size = sizeadjust(lineinfo[-1])
            continue
        if line.endswith("</type>"):
            lineinfo = line.split("<")
            continue
        if line.endswith("</alignment>"):
            lineinfo = line.split("<")
            alignment = lineinfo[-1]
            continue
        if line.endswith("</ac>"):
            lineinfo = line.split("<")
            ac = lineinfo[-1]
            continue
        if line.endswith("</hp>"):
            lineinfo = line.split("<")
            maxHP = lineinfo[-1]
            continue
        if line.endswith("</speed>"):
            lineinfo = line.split("<")
            speeds += [lineinfo[-1]]
            continue
        if line.endswith("</str>"):
            lineinfo = line.split("<")
            STR = lineinfo[-1]
            continue
        if line.endswith("</dex>"):
            lineinfo = line.split("<")
            DEX = lineinfo[-1]
            continue
        if line.endswith("</con>"):
            lineinfo = line.split("<")
            CON = lineinfo[-1]
            continue
        if line.endswith("</int>"):
            lineinfo = line.split("<")
            INT = lineinfo[-1]
            continue
        if line.endswith("</wis>"):
            lineinfo = line.split("<")
            WIS = lineinfo[-1]
            continue
        if line.endswith("</cha>"):
            lineinfo = line.split("<")
            CHA = lineinfo[-1]
            continue
        if line.endswith("</save>"):
            lineinfo = line.split("<")
            saves += [lineinfo[-1]]
            continue
        if line.endswith("</passive>"):
            lineinfo = line.split("<")
            PassivePerception = lineinfo[-1]
            continue
        if line.endswith("</languages>"):
            lineinfo = line.split("<")
            languages = lineinfo[-1]
            continue
        if line.endswith("</cr>"):
            lineinfo = line.split("<")
            cr = lineinfo[-1]
            continue
        if line.endswith("</resist>"):
            lineinfo = line.split("<")
            resists = lineinfo[-1]
            continue
        if line.endswith("</immune>"):
            lineinfo = line.split("<")
            immunes = lineinfo[-1]
            continue
        if line.endswith("</vulnerable>"):
            lineinfo = line.split("<")
            vulns = lineinfo[-1]
            continue
        if line.endswith("</immune>"):
            lineinfo = line.split("<")
            immunes = lineinfo[-1]
            continue
        if line.endswith("</conditionImmune>"):
            lineinfo = line.split("<")
            conditionimmunes = lineinfo[-1]
            continue
        if line.endswith("</senses>"):
            lineinfo = line.split("<")
            senses = lineinfo[-1]
            continue
        if line.endswith("<trait>"):
            inblock = 1
            continue
        if line.endswith("</text>"):
            lineinfo = line.split("<")
            blocktext = lineinfo[-1]
            continue
        if line.endswith("</trait>"):
            traits += [(blockname, blocktext)]
            inblock = 0
            continue
        if line.endswith("<action>"):
            inblock = 2
            continue
        if line.endswith("</action>"):
            actions += [(blockname, blocktext)]
            inblock = 0
            continue
        input("Error, unrecognized line " + line)
    creatureblock = name + "\n" + size + " " + creaturetype + ", " + alignment + "\n" + ac + "\n" + "Hit Points " + \
                    maxHP + "\n" + speedlist(speeds) + "STR\nDEX\nCON\nINT\nWIS\nCHA\n" + \
                    score2mod(STR) + score2mod(DEX) + score2mod(CON) + score2mod(INT) + score2mod(WIS) + score2mod(
        CHA) + \
                    "\nSaving Throws" + saveslist(saves) + "\n" + "Damage Resistances " + damageTypeList(
        resists) + "\n" + \
                    "Damage Immunities " + damageTypeList(immunes) + "Damage Vulnerabilities " + damageTypeList(vulns) + \
                    "Condition Immunities " + damageTypeList(conditionimmunes) + "\n" + "Senses " + senses + \
                    ", Passive Perception " + PassivePerception + "\n" + "Languages " + languages + "\n" + "Challenge " + \
                    cr + " (" + xp + " XP)" + "\n" + traitlist(traits) + "\n" + actionlist(actions)
    newfile.write(creatureblock)
    newfile.close()
