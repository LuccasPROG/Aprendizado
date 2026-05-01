class MinhaString(str):
    def upper(self):
        print('CHAMOu UPPER')
        return super().upper()



string = MinhaString('luiz')
print(string.upper())