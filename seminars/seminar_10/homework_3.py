
class DataSerializer:
    def __init__(self):
        self.data = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    def serialize(self):
        if self._data is None:
            raise ValueError("Нет информации для сериализации")

        serialize_data = f"Serialized: {self._data}"
        return serialize_data

    def deserialize(self):
        if self._data is None:
            raise ValueError("Нет информации для сериализации")

        desiralization_data = self._data.replace("Serialized: ", "")
        return desiralization_data

serializer = DataSerializer()
serializer.data = "Hello world"

serialized = serializer.serialize()
print(serialized)

deserialized = serializer.deserialize()
print(deserialized)