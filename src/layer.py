from abc import ABC, abstractmethod

class Layer(ABC):
    @abstractmethod
    def __init__(self, layer_type):
        print("Creating Layer: ", layer_type)
