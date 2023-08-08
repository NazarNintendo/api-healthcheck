import asyncio
from typing import List

import requests
from requests import RequestException

from data import API, APIState


async def create_job(state: APIState, api: API) -> None:
    """
    Create a job for each API.
    :param state: The state of the APIs.
    :param api: The API to ping.
    :return: None
    """
    while True:
        await asyncio.sleep(api.freq)
        ping(state, api)


def ping(state: APIState, api: API) -> None:
    """
    Ping the API and notify if the state has changed.
    :param state: The state of the APIs.
    :param api: The API to ping.
    :return: None
    """
    try:
        resp = requests.get(api.url, verify=False)
        ok = resp.json().get("ok")
        if not ok:
            raise RequestException
    except RequestException:
        now_state = False
    else:
        now_state = True

    if state.get(api.id) == now_state:
        return

    state.set(api.id, now_state)
    notify(now_state, api.integration, api.args)


def notify(ok: bool, integration: str, args: List[str]) -> None:
    """
    Notify the user if the state has changed.
    Use the integration specified in the config file.
    :param ok: The current state of the API.
    :param integration: The integration to use.
    :param args: The arguments for the integration.
    :return: None
    """
    if integration == "telegram":
        notify_telegram(ok, args)


# --------------------------- INTEGRATIONS ---------------------------


def notify_telegram(ok: bool, args: List[str]) -> None:
    """
    Notify the user via Telegram.
    :param ok: The current state of the API.
    :param args: The arguments for the integration.
    :return: None
    """
    ok_text = "✅ API is up and running again!"
    not_ok_text = "❌ API is down!"
    requests.get(
        args[0],
        params={"chat_id": args[1], "text": ok_text if ok else not_ok_text},
    )


def notify_slack(ok: bool, args: List[str]) -> None:
    ...
