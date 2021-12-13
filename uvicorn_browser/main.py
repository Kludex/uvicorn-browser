import logging
import os
import sys
from typing import Any

import click
from uvicorn.config import Config
from uvicorn.main import LOGGING_CONFIG
from uvicorn.main import main as uvicorn_main
from uvicorn.server import Server

from uvicorn_browser.reload import BrowserReload

if sys.version_info < (3, 8):
    from typing_extensions import Literal
else:
    from typing import Literal

url_reloader = click.option("--reload-url", default=None, help="URL to reload.")
driver = click.option(
    "--driver",
    default="chrome",
    help=(
        "Browser driver. Only used if reload-url is set."
        "Supported: 'chrome', 'firefox.'"
    ),
)

uvicorn_main = driver(url_reloader(uvicorn_main))


def decorator(func):
    def wrapper(**kwargs):
        log_config = kwargs.get("log_config")
        kwargs["log_config"] = LOGGING_CONFIG if log_config is None else log_config

        reload_dirs = kwargs.get("reload_dirs")
        kwargs["reload_dirs"] = reload_dirs if reload_dirs else None

        reload_includes = kwargs.get("reload_includes")
        kwargs["reload_includes"] = reload_includes if reload_includes else None

        reload_excludes = kwargs.get("reload_excludes")
        kwargs["reload_excludes"] = reload_excludes if reload_excludes else None

        reload_url = kwargs.pop("reload_url")
        driver = kwargs.pop("driver")
        if reload_url:
            kwargs["reload"] = True
            run(**kwargs, reload_url=reload_url, driver=driver)
        else:
            func(**kwargs)

    return wrapper


uvicorn_main.callback = decorator(uvicorn_main.callback)
main = uvicorn_main


def run(reload_url: str, driver: Literal["chrome", "firefox"], **kwargs: Any) -> None:
    app_dir = kwargs.pop("app_dir", None)
    if app_dir is not None:
        sys.path.insert(0, app_dir)

    config = Config(**kwargs)
    server = Server(config=config)

    if (config.reload or config.workers > 1) and not isinstance(kwargs.get("app"), str):
        logger = logging.getLogger("uvicorn.error")
        logger.warning(
            "You must pass the application as an import string to enable 'reload' or "
            "'workers'."
        )
        sys.exit(1)

    sock = config.bind_socket()
    BrowserReload(reload_url, driver, config, target=server.run, sockets=[sock]).run()

    if config.uds:
        os.remove(config.uds)
