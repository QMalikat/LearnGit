from random import randint

print("Din kæreste og dig vågnede af brandalarmen. Jeres hus brænder og du kan kun nå at redde en ting")
print("Din elskede gamle hund, skriv h")
print("Din kæreste, skriv k")
choice=input(k)
if choice == (h)
        print("Du redder din hund, men din kæreste besvimer af røgforgiftning og dør i brænden")
if choice=="k":
      print("Din kæreste trøster dig, fordi din hund ikke klarede den med ud af det brændende hus")

print("Brænde begyndte fordi du glemte at slukke for komfuret inden du gik i seng. Du bliver forhørt af politiet")
print("For at fortælle sandheden, skriv s")
print("For at undgå sandheden, skriv l")
choice=input(s)

if choice=="s":
      if kæreste:
        print("Med din flotte kærestes hjælp kommer du igennem politiens forhør uden problemer")
      else:
        print("Din historie er en smule vag og politiet ønsker at anholde dig.")

else:
      print("Du lyver alt hvad du kan, for at undgå at blive anholdt. Du har 1/4 chance for at overbevise dem")
      result=randint(1, 4)
      if result==1:
        print("Det lykkes og du er ikke fundet skydig i din kærestes død")
      else:
        print("Politiet tror ikke på dig og du bliver anholdt for uagtsomt manddrab")
