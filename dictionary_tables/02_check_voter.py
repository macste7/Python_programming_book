voted = {}
def check_voter(name):
  if voted.get(name):
    print "Pogoni� go!"
  else:
    voted[name] = True
    print "Niech zag�osuje!"

check_voter("tomasz")
check_voter("micha�")
check_voter("micha�")
