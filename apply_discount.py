def apply_discount(product, discount):
    price = int(product['цена'] * (1.0 - discount))
    assert 0 <= price <= product['цена']
    return print(price)

def delete_product(prod_id, user):
    assert user.is_admin(),

shoes = {'name': 'shoes', 'цена': 1490}
apply_discount(shoes, 2.0)
