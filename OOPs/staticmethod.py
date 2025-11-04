# class Math:
#     x=10
#     @staticmethod #similar to void funtions in C dont create change to the real values
#     # doesnt have access to any thing in the class
#     def add5():
#         return x+5
# print(Math.add5())

class Math:
    @staticmethod #similar to void funtions in C dont create change to the real values
    def add5(x):
        return x+5
print(Math.add5(10))
