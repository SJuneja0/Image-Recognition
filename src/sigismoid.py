from layer import Layer

class Sigismoid(Layer):
    def __init__(self, layer_type):
        print("Creating Layer: ", layer_type)

sigismoid = Sigismoid("Sigismoid")