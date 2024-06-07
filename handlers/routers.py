from aiogram import Router
from .main import router as main_router
from .cartKazahstan import router as cart_router
from .depozite import router as depozite_router
from .open_account import router as open_account_router

router = Router()


router.include_router(main_router)
router.include_router(cart_router)
router.include_router(depozite_router)
router.include_router(open_account_router)