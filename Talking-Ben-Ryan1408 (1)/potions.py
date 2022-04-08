#talking ben's potions

Blue = {"Pink":"*A whirlwind appears*", "Cyan":"*A thunderstorm appears*", "Green":"*A large plant grows*","Yellow":"*Lava spews out of the flask*"}
Pink = {"Cyan":"*Ben breathes fire*","Green":"*Explosion*","Yellow":"*Ben Breathes Smoke*","Blue":"*Whirlwind*"}
Cyan = {"Green":"*Some water splashes*","Yellow":"*Smoke*","Blue":"*A thunderstorm appears*","Pink":"*A fire appears and burns Ben's pubes off*"}
Green = {"Yellow":"*A flame appears*","Blue":"*A large plant grows*","Pink":"*Explosion*","Cyan":"*Water splashes*"}
Yellow = {"Blue":"Lava","Pink":"*Ben Breathes smoke*","Cyan":"*The flask explodes, covering ben in a thick cloud of black smoke*", "Green":"*A flame appears*"}

def firstPick():
  pick = int(input("\n\nPick your first colour:\n\n[1] - Blue\n[2] - Pink\n[3] - Cyan\n[4] - Green\n[5] - Yellow\n\n"))
  return pick



def secondPick():
  pick = int(input("\n\nPick your second colour:\n\n[1] - Blue\n[2] - Pink\n[3] - Cyan\n[4] - Green\n[5] - Yellow\n\n"))
  return pick

def TheMotionOfThePotion():
  try:
    select = firstPick()
    
    if select == 1:
      pickOne = Blue
    elif select == 2:
      pickOne = Pink
    elif select == 3:
      pickOne = Cyan
    elif select == 4:
      pickOne = Green
    elif select == 5:
      pickOne = Yellow
  
    if select > 0 and select <= 5:
      secondSelect = secondPick()
  
      if select != secondSelect:
        if secondSelect == 1:
          return pickOne["Blue"]
        elif secondSelect == 2:
          return pickOne["Pink"]
        elif secondSelect == 3:
          return pickOne["Cyan"]
        elif secondSelect == 4:
          return pickOne["Green"]
        elif secondSelect == 5:
          return pickOne["Yellow"]
        else:
          return "Invalid selection!"
      else:
        return "You can't use the same colour twice!"
  
    else:
      return "Invalid selection!"
  except:
    return "Invalid selection!"