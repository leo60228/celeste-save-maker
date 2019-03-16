def check_number(num, default = 0, min = None, max = None):
    try:
        int(num)
    except ValueError:
        print("Invalid input, defaulting to " + str(default))
        return True
    if min != None:
        if int(num) < min:
            print("Invalid input, defaulting to " + str(default))
            return True
    if max != None:
        if int(num) > max:
            print("Invalid input, defaulting to " + str(default))
            return True
    return False

areas = ["Prologue", "Forsaken City", "Old Site", "Celestial Resort", "Golden Ridge", "Mirror Temple", "Reflection", "Summit", "Epilogue", "Core"]

print("CELESTE SAVE MAKER v0.1\nMade by Pikzel (@pikzelgames)\nIf you have any questions regarding this tool, message Pikzel#6979 on Discord\n\nNote: Make sure to close Celeste before using this tool.\n")

while True:
    operating_system_number = int(input("Which operating system are you using? (1: Windows, 2: macOS): "))
    if operating_system_number in [1, 2]:
        if operating_system_number == 1:
            operating_system = "Windows"
        elif operating_system_number == 2:
            operating_system = "macOS"
        break

save_location = input("Where is your saves folder located? (leave blank for default): ")
if save_location == "":
    if operating_system == "Windows":
        save_location = "C:\\Program Files\\Steam\\steamapps\\common\\Celeste\\Saves\\"
    elif operating_system == "macOS":
        print("As this is an alpha build, we don't have the default path for macOS yet, but please PM Pikzel#6979 on Discord if you can tell us what it is :)")
if save_location[-1] != "\\":
    save_location += "\\"

save_number = input("Which save do you want to write to? (starting from 0) (any progress currently stored in this slot will be lost): ")

save_path = save_location + save_number + ".celeste"
save_file = open(save_path, 'w')

print("For all the following questions, except otherwise noted, leaving a blank answer will set the value to a predetermined default")
name = input("What is the name of the profile?: ")
if name == "":
    name = "Madeline"

#TIME CODE HERE

cheat_mode = input("Has cheat mode been used (0 or 1)? ")
if cheat_mode == "0":
    cheat_mode = "false"
elif cheat_mode == "1":
    cheat_mode = "true"
else:
    if cheat_mode != "":
        print("Invalid input, defaulting to false")
    cheat_mode = "false"

assist_mode = input("Has assist mode been used (0 or 1)? ")
if assist_mode == "0":
    assist_mode = "false"
elif assist_mode == "1":
    assist_mode = "true"
else:
    if assist_mode != "":
        print("Invalid input, defaulting to false")
    assist_mode = "false"

theo_sister = input("What's the name of Theo's sister (default = Alex)? ")
if theo_sister == "":
    theo_sister = "Alex"

unlocked_areas = input("How many areas have been unlocked (9 = All A-Sides, 0 = Only Prologue)? ")
if unlocked_areas == "":
    unlocked_areas = "0"
if check_number(unlocked_areas, 0, 0, 9):
    unlocked_areas = "0"

total_deaths = input("How many deaths are recorded? ")
if total_deaths == "":
    total_deaths = "0"
try:
    int(total_deaths)
except ValueError:
    print("Invalid input, defaulting to 0")
    total_deaths = 0

total_strawberries = input("How many red strawberries have been collected (max 175)? ")
if total_strawberries == "":
    total_strawberries = "0"
if check_number(total_strawberries, 0, 0, 175):
    total_strawberries = "0"

total_goldens = input("How many golden strawberries have been collected (max 25)? ")
if total_goldens == "":
    total_goldens = "0"
if check_number(total_goldens, 0, 0, 25):
    total_goldens = "0"

total_jumps = input("How many jumps have been inputted (not including wall jumps)? ")
if total_jumps == "":
    total_jumps = "0"
if check_number(total_jumps, 0, 0):
    total_jumps = "0"

total_wall_jumps = input("How many wall jumps have been inputted? ")
if total_wall_jumps == "":
    total_wall_jumps = "0"
if check_number(total_wall_jumps, 0, 0):
    total_wall_jumps = "0"

total_dashes = input("How many dashes have been inputted? ")
if total_dashes == "":
    total_dashes = "0"
if check_number(total_dashes, 0, 0):
    total_dashes = "0"

completed_areas = []
cassettes_collected = ["false", "false", "false", "false", "false", "false", "false", "false", "false", "false"]
hearts_collected = ["false", "false", "false", "false", "false", "false", "false", "false", "false", "false"]
for i in range(int(unlocked_areas) + 1):
    sublist = ["false", "false", "false"]
    if i != int(unlocked_areas):
        sublist[0] = "true"
    else:
        if i == 9:
            answer = input("Have you completed Core-A (0 or 1)? ")
            if answer == "0":
                sublist[0] = "false"
                cassettes_collected[9] = "false"
                hearts_collected[9] = "false"
            if answer == "1":
                sublist[0] = "true"
                hearts_collected[9] = "true"
                cassettes_collected[9] = "true"
            else:
                if answer != "":
                    print("Invalid input, defaulting to false")
                sublist[0] = "false"
                hearts_collected[9] = "false"
                cassettes_collected[9] = "false"

    if i not in [0, 8]:
        if i != 9:
            answer = input("Have you collected the crystal heart for " + areas[i] + " (0 or 1)? ")
            if answer == "0":
                hearts_collected[i] = "false"
            elif answer == "1":
                hearts_collected[i] = "true"
            else:
                if answer != "":
                    print("Invalid input, defaulting to false")
                hearts_collected[i] = "false"

            answer = input("Have you got the B-Side tape for " + areas[i] + " (0 or 1)? ")
            if answer == "0":
                cassettes_collected[i] = "false"
            elif answer == "1":
                cassettes_collected[i] = "true"
            else:
                if answer != "":
                    print("Invalid input, defaulting to false")
                cassettes_collected[i] = "false"

        if cassettes_collected[i] == "true":
            answer = input("Have you completed " + areas[i] + "-B (0 or 1)? ")
            if answer == "0":
                sublist[1] = "false"
            elif answer == "1":
                sublist[1] = "true"
            else:
                if answer != "":
                    print("Invalid input, defaulting to false")
                sublist[1] = "false"

        if sublist[1] == "true":
            answer = input("Have you completed " + areas[i] + "-C (0 or 1)? ")
            if answer == "0":
                sublist[2] = "false"
            elif answer == "1":
                sublist[2] = "true"
            else:
                if answer != "":
                    print("Invalid input, defaulting to false")
                sublist[2] = "false"
    completed_areas.append(sublist)

print("Processing...")

# WRITING TO THE SAVE FILE
save_file.write(f"""<?xml version="1.0"?>
<SaveData xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
  <Version>1.2.6.1</Version>
  <Name>{name}</Name>
  <Time>000000000</Time>
  <LastSave>0001-01-01T00:00:00</LastSave>
  <CheatMode>{cheat_mode}</CheatMode>
  <AssistMode>{assist_mode}</AssistMode>
  <Assists>
    <GameSpeed>10</GameSpeed>
    <Invincible>false</Invincible>
    <DashMode>Normal</DashMode>
    <InfiniteStamina>false</InfiniteStamina>
    <MirrorMode>false</MirrorMode>
    <ThreeSixtyDashing>false</ThreeSixtyDashing>
    <InvisibleMotion>false</InvisibleMotion>
    <NoGrabbing>false</NoGrabbing>
    <LowFriction>false</LowFriction>
    <SuperDashing>false</SuperDashing>
    <Hiccups>false</Hiccups>
    <PlayAsBadeline>false</PlayAsBadeline>
  </Assists>
  <TheoSisterName>{theo_sister}</TheoSisterName>
  <UnlockedAreas>{unlocked_areas}</UnlockedAreas>
  <TotalDeaths>{total_deaths}</TotalDeaths>
  <TotalStrawberries>{total_strawberries}</TotalStrawberries>
  <TotalGoldenStrawberries>{total_goldens}</TotalGoldenStrawberries>
  <TotalJumps>{total_jumps}</TotalJumps>
  <TotalWallJumps>{total_wall_jumps}</TotalWallJumps>
  <TotalDashes>{total_dashes}</TotalDashes>
  <Flags />
  <Poem />
  <LastArea ID="0" Mode="Normal" SID="Celeste/0-Intro" />
  <Areas>
    <AreaStats ID="0" Cassette="{cassettes_collected[0]}" SID="Celeste/0-Intro">
      <Modes>
        <AreaModeStats TotalStrawberries="0" Completed="{completed_areas[0][0]}" SingleRunCompleted="false" FullClear="false" Deaths="0" TimePlayed="00000000" BestTime="0" BestFullClearTime="0" BestDashes="0" BestDeaths="0" HeartGem="{hearts_collected[0]}">
          <Strawberries />
          <Checkpoints />
        </AreaModeStats>
        <AreaModeStats TotalStrawberries="0" Completed="{completed_areas[0][1]}" SingleRunCompleted="false" FullClear="false" Deaths="0" TimePlayed="00000000" BestTime="0" BestFullClearTime="0" BestDashes="0" BestDeaths="0" HeartGem="{completed_areas[0][1]}">
          <Strawberries />
          <Checkpoints />
        </AreaModeStats>
        <AreaModeStats TotalStrawberries="0" Completed="{completed_areas[0][2]}" SingleRunCompleted="false" FullClear="false" Deaths="0" TimePlayed="00000000" BestTime="0" BestFullClearTime="0" BestDashes="0" BestDeaths="0" HeartGem="{completed_areas[0][2]}">
          <Strawberries />
          <Checkpoints />
        </AreaModeStats>
      </Modes>
    </AreaStats>
    <AreaStats ID="1" Cassette="{cassettes_collected[1]}" SID="Celeste/1-ForsakenCity">
      <Modes>
        <AreaModeStats TotalStrawberries="0" Completed="{completed_areas[1][0]}" SingleRunCompleted="false" FullClear="false" Deaths="0" TimePlayed="00000000" BestTime="0" BestFullClearTime="0" BestDashes="0" BestDeaths="0" HeartGem="{hearts_collected[1]}">
          <Strawberries />
          <Checkpoints />
        </AreaModeStats>
        <AreaModeStats TotalStrawberries="0" Completed="{completed_areas[1][1]}" SingleRunCompleted="false" FullClear="false" Deaths="0" TimePlayed="00000000" BestTime="0" BestFullClearTime="0" BestDashes="0" BestDeaths="0" HeartGem="{completed_areas[1][1]}">
          <Strawberries />
          <Checkpoints />
        </AreaModeStats>
        <AreaModeStats TotalStrawberries="0" Completed="{completed_areas[1][2]}" SingleRunCompleted="false" FullClear="false" Deaths="0" TimePlayed="00000000" BestTime="0" BestFullClearTime="0" BestDashes="0" BestDeaths="0" HeartGem="{completed_areas[1][2]}">
          <Strawberries />
          <Checkpoints />
        </AreaModeStats>
      </Modes>
    </AreaStats>
    <AreaStats ID="2" Cassette="{cassettes_collected[2]}" SID="Celeste/2-OldSite">
      <Modes>
        <AreaModeStats TotalStrawberries="0" Completed="{completed_areas[2][0]}" SingleRunCompleted="false" FullClear="false" Deaths="0" TimePlayed="00000000" BestTime="0" BestFullClearTime="0" BestDashes="0" BestDeaths="0" HeartGem="{hearts_collected[2]}">
          <Strawberries />
          <Checkpoints />
        </AreaModeStats>
        <AreaModeStats TotalStrawberries="0" Completed="{completed_areas[2][1]}" SingleRunCompleted="false" FullClear="false" Deaths="0" TimePlayed="00000000" BestTime="0" BestFullClearTime="0" BestDashes="0" BestDeaths="0" HeartGem="{completed_areas[2][1]}">
          <Strawberries />
          <Checkpoints />
        </AreaModeStats>
        <AreaModeStats TotalStrawberries="0" Completed="{completed_areas[2][2]}" SingleRunCompleted="false" FullClear="false" Deaths="0" TimePlayed="00000000" BestTime="0" BestFullClearTime="0" BestDashes="0" BestDeaths="0" HeartGem="{completed_areas[2][2]}">
          <Strawberries />
          <Checkpoints />
        </AreaModeStats>
      </Modes>
    </AreaStats>
    <AreaStats ID="3" Cassette="{cassettes_collected[3]}" SID="Celeste/3-CelestialResort">
      <Modes>
        <AreaModeStats TotalStrawberries="0" Completed="{completed_areas[3][0]}" SingleRunCompleted="false" FullClear="false" Deaths="0" TimePlayed="00000000" BestTime="0" BestFullClearTime="0" BestDashes="0" BestDeaths="0" HeartGem="{hearts_collected[3]}">
          <Strawberries />
          <Checkpoints />
        </AreaModeStats>
        <AreaModeStats TotalStrawberries="0" Completed="{completed_areas[3][1]}" SingleRunCompleted="false" FullClear="false" Deaths="0" TimePlayed="00000000" BestTime="0" BestFullClearTime="0" BestDashes="0" BestDeaths="0" HeartGem="{completed_areas[3][1]}">
          <Strawberries />
          <Checkpoints />
        </AreaModeStats>
        <AreaModeStats TotalStrawberries="0" Completed="{completed_areas[3][2]}" SingleRunCompleted="false" FullClear="false" Deaths="0" TimePlayed="00000000" BestTime="0" BestFullClearTime="0" BestDashes="0" BestDeaths="0" HeartGem="{completed_areas[3][2]}">
          <Strawberries />
          <Checkpoints />
        </AreaModeStats>
      </Modes>
    </AreaStats>
    <AreaStats ID="4" Cassette="{cassettes_collected[4]}" SID="Celeste/4-GoldenRidge">
      <Modes>
        <AreaModeStats TotalStrawberries="0" Completed="{completed_areas[4][0]}" SingleRunCompleted="false" FullClear="false" Deaths="0" TimePlayed="00000000" BestTime="0" BestFullClearTime="0" BestDashes="0" BestDeaths="0" HeartGem="{hearts_collected[4]}">
          <Strawberries />
          <Checkpoints />
        </AreaModeStats>
        <AreaModeStats TotalStrawberries="0" Completed="{completed_areas[4][1]}" SingleRunCompleted="false" FullClear="false" Deaths="0" TimePlayed="00000000" BestTime="0" BestFullClearTime="0" BestDashes="0" BestDeaths="0" HeartGem="{completed_areas[4][1]}">
          <Strawberries />
          <Checkpoints />
        </AreaModeStats>
        <AreaModeStats TotalStrawberries="0" Completed="{completed_areas[4][2]}" SingleRunCompleted="false" FullClear="false" Deaths="0" TimePlayed="00000000" BestTime="0" BestFullClearTime="0" BestDashes="0" BestDeaths="0" HeartGem="{completed_areas[4][2]}">
          <Strawberries />
          <Checkpoints />
        </AreaModeStats>
      </Modes>
    </AreaStats>
    <AreaStats ID="5" Cassette="{cassettes_collected[5]}" SID="Celeste/5-MirrorTemple">
      <Modes>
        <AreaModeStats TotalStrawberries="0" Completed="{completed_areas[5][0]}" SingleRunCompleted="false" FullClear="false" Deaths="0" TimePlayed="00000000" BestTime="0" BestFullClearTime="0" BestDashes="0" BestDeaths="0" HeartGem="{hearts_collected[5]}">
          <Strawberries />
          <Checkpoints />
        </AreaModeStats>
        <AreaModeStats TotalStrawberries="0" Completed="{completed_areas[5][1]}" SingleRunCompleted="false" FullClear="false" Deaths="0" TimePlayed="00000000" BestTime="0" BestFullClearTime="0" BestDashes="0" BestDeaths="0" HeartGem="{completed_areas[5][1]}">
          <Strawberries />
          <Checkpoints />
        </AreaModeStats>
        <AreaModeStats TotalStrawberries="0" Completed="{completed_areas[5][2]}" SingleRunCompleted="false" FullClear="false" Deaths="0" TimePlayed="00000000" BestTime="0" BestFullClearTime="0" BestDashes="0" BestDeaths="0" HeartGem="{completed_areas[5][2]}">
          <Strawberries />
          <Checkpoints />
        </AreaModeStats>
      </Modes>
    </AreaStats>
    <AreaStats ID="6" Cassette="{cassettes_collected[6]}" SID="Celeste/6-Reflection">
      <Modes>
        <AreaModeStats TotalStrawberries="0" Completed="{completed_areas[6][0]}" SingleRunCompleted="false" FullClear="false" Deaths="0" TimePlayed="00000000" BestTime="0" BestFullClearTime="0" BestDashes="0" BestDeaths="0" HeartGem="{hearts_collected[6]}">
          <Strawberries />
          <Checkpoints />
        </AreaModeStats>
        <AreaModeStats TotalStrawberries="0" Completed="{completed_areas[6][1]}" SingleRunCompleted="false" FullClear="false" Deaths="0" TimePlayed="00000000" BestTime="0" BestFullClearTime="0" BestDashes="0" BestDeaths="0" HeartGem="{completed_areas[6][1]}">
          <Strawberries />
          <Checkpoints />
        </AreaModeStats>
        <AreaModeStats TotalStrawberries="0" Completed="{completed_areas[6][2]}" SingleRunCompleted="false" FullClear="false" Deaths="0" TimePlayed="00000000" BestTime="0" BestFullClearTime="0" BestDashes="0" BestDeaths="0" HeartGem="{completed_areas[6][2]}">
          <Strawberries />
          <Checkpoints />
        </AreaModeStats>
      </Modes>
    </AreaStats>
    <AreaStats ID="7" Cassette="{cassettes_collected[7]}" SID="Celeste/7-Summit">
      <Modes>
        <AreaModeStats TotalStrawberries="0" Completed="{completed_areas[7][0]}" SingleRunCompleted="false" FullClear="false" Deaths="0" TimePlayed="00000000" BestTime="0" BestFullClearTime="0" BestDashes="0" BestDeaths="0" HeartGem="{hearts_collected[7]}">
          <Strawberries />
          <Checkpoints />
        </AreaModeStats>
        <AreaModeStats TotalStrawberries="0" Completed="{completed_areas[7][1]}" SingleRunCompleted="false" FullClear="false" Deaths="0" TimePlayed="00000000" BestTime="0" BestFullClearTime="0" BestDashes="0" BestDeaths="0" HeartGem="{completed_areas[7][1]}">
          <Strawberries />
          <Checkpoints />
        </AreaModeStats>
        <AreaModeStats TotalStrawberries="0" Completed="{completed_areas[7][2]}" SingleRunCompleted="false" FullClear="false" Deaths="0" TimePlayed="00000000" BestTime="0" BestFullClearTime="0" BestDashes="0" BestDeaths="0" HeartGem="{completed_areas[7][2]}">
          <Strawberries />
          <Checkpoints />
        </AreaModeStats>
      </Modes>
    </AreaStats>
    <AreaStats ID="8" Cassette="{cassettes_collected[8]}" SID="Celeste/8-Epilogue">
      <Modes>
        <AreaModeStats TotalStrawberries="0" Completed="{completed_areas[8][0]}" SingleRunCompleted="false" FullClear="false" Deaths="0" TimePlayed="00000000" BestTime="0" BestFullClearTime="0" BestDashes="0" BestDeaths="0" HeartGem="{hearts_collected[8]}">
          <Strawberries />
          <Checkpoints />
        </AreaModeStats>
        <AreaModeStats TotalStrawberries="0" Completed="{completed_areas[8][1]}" SingleRunCompleted="false" FullClear="false" Deaths="0" TimePlayed="00000000" BestTime="0" BestFullClearTime="0" BestDashes="0" BestDeaths="0" HeartGem="{completed_areas[8][1]}">
          <Strawberries />
          <Checkpoints />
        </AreaModeStats>
        <AreaModeStats TotalStrawberries="0" Completed="{completed_areas[8][2]}" SingleRunCompleted="false" FullClear="false" Deaths="0" TimePlayed="00000000" BestTime="0" BestFullClearTime="0" BestDashes="0" BestDeaths="0" HeartGem="{completed_areas[8][2]}">
          <Strawberries />
          <Checkpoints />
        </AreaModeStats>
      </Modes>
    </AreaStats>
    <AreaStats ID="9" Cassette="{cassettes_collected[9]}" SID="Celeste/9-Core">
      <Modes>
        <AreaModeStats TotalStrawberries="0" Completed="{completed_areas[9][0]}" SingleRunCompleted="false" FullClear="false" Deaths="0" TimePlayed="00000000" BestTime="0" BestFullClearTime="0" BestDashes="0" BestDeaths="0" HeartGem="{hearts_collected[9]}">
          <Strawberries />
          <Checkpoints />
        </AreaModeStats>
        <AreaModeStats TotalStrawberries="0" Completed="{completed_areas[9][1]}" SingleRunCompleted="false" FullClear="false" Deaths="0" TimePlayed="00000000" BestTime="0" BestFullClearTime="0" BestDashes="0" BestDeaths="0" HeartGem="{completed_areas[9][1]}">
          <Strawberries />
          <Checkpoints />
        </AreaModeStats>
        <AreaModeStats TotalStrawberries="0" Completed="{completed_areas[9][2]}" SingleRunCompleted="false" FullClear="false" Deaths="0" TimePlayed="00000000" BestTime="0" BestFullClearTime="0" BestDashes="0" BestDeaths="0" HeartGem="{completed_areas[9][2]}">
          <Strawberries />
          <Checkpoints />
        </AreaModeStats>
      </Modes>
    </AreaStats>
  </Areas>
  <LastArea_Safe ID="0" Mode="Normal" SID="Celeste/0-Intro" />
</SaveData>
""")

print("Save file made. Now you can open Celeste and everything should be working! (if it's not please message me on Discord :D)")
