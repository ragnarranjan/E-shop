from django import template 


register = template.Library()


@register.filter('is_in_cart')
def is_in_cart(product,cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return True
    return False


@register.filter('cart_quantity')
def cart_quantity(product,cart):
    keys = cart.keys()
    print("nn")
    for id in keys:
        print(id)
        if int(id) == product.id:
            print(id)
            return cart.get(id)
    return 0

