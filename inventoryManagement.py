from models.product import Product

class Inventory:
    def __init__(self, productJson, quantity) -> None:
        self.product = Product(productJson)
        self.quantity = quantity
        
        
    def __str__(self) -> str:
        return "product: "+ str(self.product)+", quantity:"+ str(self.quantity)
        

class InventoryManagement:
    def __init__(self) -> None:
        self.db = []
        self.MAX_SHIPMENT_MASS_IN_GM = 1800
    
    def addItem(self, productJson):
        inventory = Inventory(productJson, 0)
        self.db.append(inventory)
        
    def addItems(self, productList):
        for productJson in productList:
            self.addItem(productJson)
    
    def getAll(self):
        return self.db
    
    def findItem(self, productId):
        for inventory in self.db:
            if inventory.product.product_id == productId:
                return inventory
            
            
    def stockInventory(self, productList):
        for productQuantityJson in productList:
            inventory = self.findItem(productQuantityJson["product_id"])
            inventory.quantity += productQuantityJson["quantity"]
            
    def processOrder(self, order):
        currMass = 0
        for orderItem in order["requested"]:
            inventory = self.findItem(orderItem["product_id"])
            currMass += inventory.product.mass_g
            if orderItem["quantity"] > inventory.quantity or currMass > self.MAX_SHIPMENT_MASS_IN_GM:
                return [None, order]
                
        for orderItem in order["requested"]:
            inventory = self.findItem(orderItem["product_id"])
            inventory.quantity -= orderItem["quantity"]
            
        return [{
            "order_id": order["order_id"],
            "shipped": order["requested"]
        }, None]
    
    
            
            
                
            
            
    
            
    