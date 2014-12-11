def constant(**kwargs):
    return ConstantClass(**kwargs)

class ConstantClass(object):
    __attributes_set = {}

    def __init__(self, **kwargs):
        for item in kwargs:
            setattr(self, item, kwargs[item])

        self.__attributes_set = {key: True for key in kwargs}

    def __setattr__(self, key, value):
        """Only allows setting one through the header or directly on the object"""

        if self.__attributes_set and key in self.__attributes_set:
            raise AttributeError('CONSTANT: %(key)s cannot be written to. It has been already set' % locals())

        if self.__attributes_set and key not in self.__attributes_set:
            self.__attributes_set[key] = value

        super(ConstantClass, self).__setattr__(key, value)