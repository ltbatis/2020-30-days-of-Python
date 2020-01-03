tup = ()
tup = ("abc","abc")
print(tup)

tup = (
    ("another","another"),
    ("more","more")
)
print(tup)
print("1st tuple in tup: {}".format(tup[0]))
print("1st element in 1st tuple of tup: {}".format(tup[0][0]))

tup += ("yetAnother",123)
print(tup)
tup += (("yetAnother",123),)
print(tup)