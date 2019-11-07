class OnlyOne(object):
    class __OnlyOne:
        def __init__(self, arg):
            self.val = arg
        def __str__(self):
            return repr(self) + self.val
    instance = None
    def __init__(self, arg):
        if not OnlyOne.instance:
            OnlyOne.instance = OnlyOne.__OnlyOne(arg)
        else:
            OnlyOne.instance.val = arg
    def __getattr__(self, name):
        return getattr(self.instance, name)
    def __setattr__(self, name, value):
        return super().__setattr__(self.instance, value)

x = OnlyOne("sausage")
print(x)
y = OnlyOne("eggs")
print(y)
z = OnlyOne("Spam")
print("___________________")
print(x is y is z)
print(z)
print(x)
print(y)

print('x')
print('y')
print('z')