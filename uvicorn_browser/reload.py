from pathlib import Path
from socket import socket
from time import sleep
from typing import Callable, List, Optional

from uvicorn.config import Config
from uvicorn.supervisors.basereload import BaseReload
from uvicorn.supervisors.watchgodreload import CustomWatcher, logger

from uvicorn_browser.driver import RefreshableDriver


class BrowserReload(BaseReload):
    def __init__(
        self,
        config: Config,
        target: Callable[[Optional[List[socket]]], None],
        sockets: List[socket],
        url: str,
    ) -> None:
        super().__init__(config, target, sockets)
        self.reloader_name = "browser"
        self.watchers = []
        reload_dirs = []
        for directory in config.reload_dirs:
            if Path.cwd() not in directory.parents:
                reload_dirs.append(directory)
        if Path.cwd() not in reload_dirs:
            reload_dirs.append(Path.cwd())
        for w in reload_dirs:
            self.watchers.append(CustomWatcher(w.resolve(), self.config))
        self.driver = RefreshableDriver(url=url, flavour="chrome")

    def startup(self) -> None:
        super().startup()
        sleep(1)
        self.driver.load()

    def should_restart(self) -> bool:
        for watcher in self.watchers:
            change = watcher.check()
            if change != set():
                message = "BrowserReload detected file change in '%s'. Reloading..."
                logger.warning(message, [c[1] for c in change])
                self.driver.reload()
                return True

        return False

    def shutdown(self) -> None:
        # TODO: Needs to tier down the browser resources w/ self.driver.close/quit()
        super().shutdown()
