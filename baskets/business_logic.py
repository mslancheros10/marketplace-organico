from main.models import Basket

'''
    Method returning all baskets
'''
def getBasketsFromModel():
    return Basket.objects.all()