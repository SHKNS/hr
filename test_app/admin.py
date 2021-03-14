from django.contrib import admin

# Register your models here.
from test_app.models import UnionBoard 
admin.site.register(UnionBoard)

from test_app.models import AuctionBoard 
admin.site.register(AuctionBoard)