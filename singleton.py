class Singleton(object):
    _INSTANCE = None

    def __new__(cls, *args, **kwargs):
        if not cls._INSTANCE:
            cls._INSTANCE = super(Singleton, cls).__new__(cls)
            # cls._INSTANCE.args = args
            # cls._INSTANCE.kwargs = kwargs
        return cls._INSTANCE

    def __init__(self, *args, **kwargs):
        pass


if __name__ == '__main__':
    class SingleSpam(Singleton):
        def __init__(self, s):
            self.s = s

        def __str__(self):
            return self.s


    s1 = SingleSpam('spam')
    print (id(s1), s1)
    s2 = SingleSpam('spa')
    print (id(s2), s2)
    print (id(s1), s1)