from random import randint

makeover=False
print("Velkommen til magical text adventure 2000. Du er i en skov")
print("For at udforske skoven, skriv s")
print("for at gå til borgen, skriv b")
choice=input(s)
if choice=="s":
      print("Du finder en magisk stylist, som giver dig en make-over")
      makeover=True
      print("Du går nu til borgen")

print("Du ankommer på den uhyggelige borg. Der er en ond troldmand.")
print("For at charmere ham, skriv c")
print("For at kæmpe mod ham, skriv k")
choice=input(k)

if choice=="c":
      if makeover:
        print("Med din flotte make-over charmere du ham og vinder spillet!")
      else:
        print("Du var ikke flot nok til at charmere ham, så han dræbte dig.")

else:
      print("Du kæmper mod ham, du har 1/4 chance for at vinde")
      result=randint(1, 4)
      if result==1:
        print("Du besejrede ham og vandt spillet")
      else:
        print("Han besejrede dig, du er død")
