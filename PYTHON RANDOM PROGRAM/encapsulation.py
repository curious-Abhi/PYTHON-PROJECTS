class Heart:
    def __init__(self,owner):
        self.owner=owner
        self.given=False

    def give_heart(self,receiver):
        if not self.given:
            print(f"{self.owner}'s heart is given to {receiver}.")
            self.given=True
        else:
            print("Sorry,this heart has already been given.")

ruhi_heart=Heart("Ruhi")
abhi_heart=Heart("Abhi")

ruhi_heart.give_heart('Abhi')
abhi_heart.give_heart('Ruhi')
ruhi_heart.give_heart('ani')



