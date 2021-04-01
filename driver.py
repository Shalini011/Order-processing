from inventoryManagement import InventoryManagement
from product_info import product_info, restock
class Driver:
    
    def __init__(self) -> None:
        self.inventoryManagement = InventoryManagement()
        self.shipments = []
        self.pendingShipments = []
        
    
    def initCatalog(self):
        self.inventoryManagement.addItems(product_info)
        # inventoryList = self.inventoryManagement.getAll()
        # for inventory in inventoryList:
        #     print(inventory)
        
        
    def processRestock(self):
        self.inventoryManagement.stockInventory(restock)
        # inventoryList = self.inventoryManagement.getAll()
        # for inventory in inventoryList:
        #     print(inventory)
        
    def processSingleOrder(self, order):
        shipped, pending = self.inventoryManagement.processOrder(order)
        if shipped:
            self.shipments.append(shipped)
        else:
            self.pendingShipments.append(pending)
            
    def processMultipleOrder(self, orderList):
        for order in orderList:
            self.processSingleOrder(order)
            
    def processOrder(self):
        order = {"order_id": 123, "requested": [{"product_id": 0, "quantity": 2}, {"product_id": 10, "quantity": 4}]}
        # inventoryList = self.inventoryManagement.getAll()
        # for inventory in inventoryList:
        #     print(inventory)
        # print("=============================================")
        self.processSingleOrder(order)
        # inventoryList = self.inventoryManagement.getAll()
        # for inventory in inventoryList:
        #     print(inventory)
        
        
    def shipPackage(self):
        print(self.shipments)
        # print(self.pendingShipments)
        
driver = Driver()
driver.initCatalog()
driver.processRestock()
driver.processOrder()
driver.shipPackage()