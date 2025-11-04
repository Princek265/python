class A:
    def printabc(self):
        print("abc")
class B:
    def printbcd(self):
        print("bcd")
class C(A,B):
    def printxyz(self):
        print("xyz")
object=C
object.printabc
object.printbcd
object.printxyz