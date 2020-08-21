def two_fer(name = "you"):
    return("One for " + name + ", one for me.")


# TEST
def test_this():
    print(two_fer("trish"))
    print(two_fer())
# test_this()