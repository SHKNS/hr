from django.contrib import admin

# Register your models here.
from test_app.models import UnionBoard, OverseeBoard
admin.site.register(UnionBoard)
admin.site.register(OverseeBoard)


from test_app.models import FmBoard, PpBoard,CoolBoard, RuliBoard
admin.site.register(FmBoard)
admin.site.register(PpBoard)
admin.site.register(CoolBoard)
admin.site.register(RuliBoard)

from test_app.models import AuctionBoard, CoupangBoard, ElevenBoard, GmarketBoard
admin.site.register(AuctionBoard)
admin.site.register(CoupangBoard)
admin.site.register(ElevenBoard)
admin.site.register(GmarketBoard)
