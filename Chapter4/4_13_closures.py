def knights2(saying):
    def inner2():
        return "We are the knights who say: '%s'" %saying
    return inner2

a = knights2('Duck')
b = knights2('Hasenpfeffer')

print(a())
print(b())