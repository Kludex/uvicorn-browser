<h1 align="center">
    <strong>uvicorn-browser</strong>
</h1>
<p align="center">
    <a href="https://github.com/Kludex/uvicorn-browser" target="_blank">
        <img src="https://img.shields.io/github/last-commit/Kludex/uvicorn-browser" alt="Latest Commit">
    </a>
        <img src="https://img.shields.io/github/workflow/status/Kludex/uvicorn-browser/Test">
        <img src="https://img.shields.io/codecov/c/github/Kludex/uvicorn-browser">
    <br />
    <a href="https://pypi.org/project/uvicorn-browser" target="_blank">
        <img src="https://img.shields.io/pypi/v/uvicorn-browser" alt="Package version">
    </a>
    <img src="https://img.shields.io/pypi/pyversions/uvicorn-browser">
    <img src="https://img.shields.io/github/license/Kludex/uvicorn-browser">
</p>

<p align="center">
  <img src="https://user-images.githubusercontent.com/7353520/145871783-f0a08a45-4baf-4f8a-bd48-c3747c4f1e37.gif" alt="uvicorn-browser" />
</p>

This project is inspired by [autoreload](https://github.com/ChillFish8/autoreload/tree/master).

## Installation

```bash
pip install uvicorn-browser
```

## Usage

Run `uvicorn-browser --help` to see all options. Those are the [same as `uvicorn`](https://www.uvicorn.org/deployment/#running-from-the-command-line), plus those:

```bash
  --reload-url TEXT               URL to reload.
  --driver TEXT                   Browser driver. Only used if reload-url is
                                  set. Supported: 'chrome', 'firefox.'
```

## License

This project is licensed under the terms of the MIT license.
