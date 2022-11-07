class ClassToDict:

    def slotted_to_dict(self):
        return {s: getattr(self, s) for s in self.__slots__ if hasattr(self, s)}