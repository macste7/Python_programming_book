def greet2(name):
    print "Jak si� masz, " + name + "?"

def bye():
    print "Ok, cze��!"

def greet(name):
    print "Cze��, " + name + "!"
    greet2(name)
    print "Przygotowanie do po�egnania..."
    bye()

greet("adit")
