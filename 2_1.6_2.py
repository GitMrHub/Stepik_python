class ExtendedStack(list):

    def sum(self):
        if len(self) >1:
            self.append(self.pop() + self.pop())
        return self

    def sub(self):
        if len(self) > 1:
            x = self.pop()
            y = self.pop()
            self.append(x - y)
        return self

    def mul(self):
        if len(self) > 1:
            x = self.pop()
            y = self.pop()
            self.append(x * y)
        return self

    def div(self):
        if len(self) > 1:
            x = self.pop()
            y = self.pop()
            self.append(x // y)
        return self
