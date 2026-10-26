"""PLACEHOLDER de verificación de despliegue.

Este archivo NO contiene la estrategia LCE. Solo comprueba que Railway
encuentra el paquete `lce_bot`, instala numpy/requests y arranca con el
Procfile. Sustitúyelo por tu lce_bot/main.py real (y el resto de módulos).
"""
import os
import time

import numpy as np  # noqa: F401  (comprueba que requirements.txt se instaló)
import requests


def telegram(msg: str) -> None:
    token, chat = os.getenv("TELEGRAM_BOT_TOKEN"), os.getenv("TELEGRAM_CHAT_ID")
    if not token or not chat:
        print("Telegram no configurado (faltan TELEGRAM_BOT_TOKEN / TELEGRAM_CHAT_ID)")
        return
    r = requests.post(f"https://api.telegram.org/bot{token}/sendMessage",
                      data={"chat_id": chat, "text": msg}, timeout=15)
    print("Telegram:", r.status_code)


def main() -> None:
    print("lce_bot placeholder arrancado. TRADE_MODE =", os.getenv("TRADE_MODE", "signals"))
    telegram("✅ Despliegue OK: lce_bot placeholder en marcha (aún sin estrategia).")
    while True:
        time.sleep(300)


if __name__ == "__main__":
    main()
