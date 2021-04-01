class Product:
    mass_g = 0
    product_name = ""
    product_id = -1
    
    def __init__(self, productJson) -> None:
        self.mass_g = productJson['mass_g']
        self.product_name = productJson['product_name']
        self.product_id = productJson['product_id']
        
    def __str__(self) -> str:
        return "mass_g: " +str(self.mass_g) +", product_name: "+str(self.product_name)+", product_id: "+str(self.product_id)
        
        
    