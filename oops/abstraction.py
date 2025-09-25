from abc import ABC,abstractmethod

class featurePlan(ABC):
    @abstractmethod
    def login(self):
        pass

    @abstractmethod
    def logout(self):
        pass

    def checkout(self):
        pass

class implement(featurePlan):
    def login(self):
        print("login implementation successful")
    
    def logout(self):
        print("logout implementation successful")
    
    def checkout(self):
       print("checkout")
    
i = implement()

i.login()
i.logout()
i.checkout()