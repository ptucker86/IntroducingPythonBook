# pg 149

def unicode_test(value):
    import unicodedata
    name = unicodedata.name(value)
    value2 = unicodedata.lookup(name)
    print('value="%s", name="%s", value2="%s"' % (value, name, value2))

unicode_test('A')
unicode_test('$')
unicode_test('\u00a2')
unicode_test('\u20ac')
unicode_test('\u2603')

place = 'caf\u00e9'
print(place)

place2 = "caf\N{LATIN SMALL LETTER E WITH ACUTE}"
print(place2)