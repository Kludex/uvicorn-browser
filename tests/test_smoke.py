import inspect

import uvicorn_browser


def test_smoke():
    assert inspect.ismodule(uvicorn_browser)
