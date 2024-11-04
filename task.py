class Task:
    def __init__(self, name):
        self.name = name
        self.components = {}

    def __str__(self):
        s = self.name + " using "

        for component in self.components:
            s += str(self.components[component]) + " " + component + ", "

        return s[:-2]

    def addComponent(self, number, componentName):
        self.components[componentName] = number

    def getName(self):
        return self.name

    def getComponents(self):
        return self.components
