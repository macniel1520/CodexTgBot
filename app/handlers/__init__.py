from aiogram import Router

from . import photo, start

router = Router()
router.include_router(start.router)
router.include_router(photo.router)
