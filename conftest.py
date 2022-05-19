import os

def pytest_addoption(parser):
    parser.addoption(
        "--chromedriver",
        default=f"{os.path.abspath(os.curdir)}/chromedriver",
        action="store",
        help=(
            """Parameter for deliver chromedriver into selenium"""
        ),
    )