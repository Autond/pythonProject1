

#Multilevel inheritance
class GF:

    def bangla(self):
        print("GF's bangla")


class father(GF):
        pass



class daughter(father):
        pass


D = daughter()
D.bangla()