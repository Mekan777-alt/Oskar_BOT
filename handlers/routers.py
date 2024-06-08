from aiogram import Router
from .main import router as main_router
from .cartKazahstan import router as cart_router
from .depozite import router as depozite_router
from .open_account import router as open_account_router
from .faq import router as faq_router
from .chat import router as chat_router
from .usdt import router as usdt_router
from .back_request import router as back_request_router

router = Router()


router.include_router(main_router)
router.include_router(cart_router)
router.include_router(depozite_router)
router.include_router(open_account_router)
router.include_router(faq_router)
router.include_router(chat_router)
router.include_router(usdt_router)
router.include_router(back_request_router)