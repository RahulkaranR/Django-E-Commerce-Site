from decimal import Decimal
from store.models import product


class Basket():
    '''
    a base basket class, providing some default behaviors that can be 
    inherited or overrided, as necessary.
    '''

    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('skey')
        if 'skey' not in request.session:
            basket = self.session['skey'] = {}
        self.basket = basket

    def add(self, Product, qty):
        
        product_id = str(Product.id)

        if product_id not in self.basket:
            self.basket[product_id] = {"price":str(Product.price), "qty":int(qty)}
        self.save()

    
    def __iter__(self):
        product_ids = self.basket.keys()
        products = product.Product.filter(id__in=product_ids)
        basket = self.basket.copy()

        for Product in products:
            basket[str(Product.id)]['Product'] = Product
        print(basket)
        for item in basket.values():
            item["price"] = Decimal(item['price'])
            item["total_price"] = item['price'] * item['qty']
            yield item

    def __len__(self):
        return sum(i[1]['qty'] for i in self.basket.items())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['qty'] for item in self.basket.values())

    def delete(self, Product):
        product_id = str(Product)
        if product_id in self.basket:
            del self.basket[product_id]
            print(self.basket)
        self.save()


    def update(self, productid, productqty):
        productid = str(productid)
        if productid in self.basket:
            self.basket[productid]['qty'] = productqty

        self.save()


            

    def save(self):
        self.session.modified = True



        