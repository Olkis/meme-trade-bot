import json
import os
from .data_sources import get_liquidity

def load_callers_whitelist():
    """Загружает белый список коллеров."""
    whitelist_path = os.path.join("configs", "callers_whitelist.json")
    if os.path.exists(whitelist_path):
        with open(whitelist_path, "r") as f:
            return json.load(f).get("whitelisted_callers", [])
    return []

async def check_contract(token_address: str):
    """Проверяет контракт (заглушка)."""
    # TODO: Подключить Solscan API
    return True  # Тестовый результат

async def check_liquidity(token_address: str, min_liquidity: int = 2000):
    """Проверяет ликвидность."""
    liquidity = await get_liquidity(token_address)
    return liquidity >= min_liquidity