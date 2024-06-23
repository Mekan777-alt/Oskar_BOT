from django.contrib import admin
from .models import GoToChat, KazahstanCart, USDT, OpenAccount, Deposited


@admin.register(KazahstanCart)
class KazahstanCardAdmin(admin.ModelAdmin):
    pass


@admin.register(USDT)
class USDTAdmin(admin.ModelAdmin):
    pass


@admin.register(OpenAccount)
class OpenAccountAdmin(admin.ModelAdmin):
    pass


@admin.register(Deposited)
class DepositedAdmin(admin.ModelAdmin):
    pass


@admin.register(GoToChat)
class GoToChatAdmin(admin.ModelAdmin):
    pass
