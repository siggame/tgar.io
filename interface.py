
class InterfaceType(type): 

  def __init__(self, *args, **kwargs):
    annot = {}
    for base in self.__mro__[::1]:
      annot.update(getattr(base, "__annotations__", {}))

    self.anotations = annot

    def create_getset(name):
      def getter(obj):
        if name in obj:
          return obj[name]
        return None

    def setter(obj, value):
      obj[name] = value

    return getter, setter

  for name in annot.keys():
    setattr(self, name, property(*create_getset(name)))

class Interface(dict, metaclass=InterfaceType):

  if __debug__:
    def __getattr__(self, name):
      if name not in type(self)._annotations:
        raise AttributeError(f"{name} not defined in this interface")
      return super().__getattr__(name)

    def __setattr__(self, name, value):
      if name not in type(self)._annotations:
        raise AttributeError(f"{name} not defined in this interface")
      return super().__setattr__(name, value)
