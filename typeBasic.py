>>> "%10s" % "hi"
'         hi'

>>> "%-10sjane" % 'hi'
'ji        jane'

>>> "%0.4f" % 3.42134234
'3.4213'

>>> "%10.4f" % 3.42134234
'   3.4213'

>>> "I eat {0} apples".format(3)
'I eat 3 apples'

>>> "I eat {0} apples".format("five")
'I eat five apples'

>>> number = 3
>>> "i eat {0} apples". format(number)
'I eat 3 apples'

