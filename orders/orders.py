orders_list = [] 
 
def add_order(product_name, quantity): 
    orders_list.append({"product": product_name, "quantity": quantity}) 
 
def list_orders(): 
    return orders_list 
