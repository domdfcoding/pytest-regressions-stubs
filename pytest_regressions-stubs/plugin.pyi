# stdlib
from pathlib import Path

# 3rd party
import pytest
from _pytest.config.argparsing import Parser
from _pytest.fixtures import FixtureRequest

# this package
from .data_regression import DataRegressionFixture
from .dataframe_regression import DataFrameRegressionFixture
from .file_regression import FileRegressionFixture
from .num_regression import NumericRegressionFixture
from .image_regression import ImageRegressionFixture

def pytest_addoption(parser: Parser) -> None: ...

@pytest.fixture
def data_regression(datadir: Path, original_datadir: Path, request: FixtureRequest) -> DataRegressionFixture: ...

@pytest.fixture
def file_regression(datadir: Path, original_datadir: Path, request: FixtureRequest) -> FileRegressionFixture: ...

@pytest.fixture
def num_regression(datadir: Path, original_datadir: Path, request: FixtureRequest) -> NumericRegressionFixture: ...

@pytest.fixture
def image_regression(datadir: Path, original_datadir: Path, request: FixtureRequest) -> ImageRegressionFixture: ...

@pytest.fixture
def dataframe_regression(datadir: Path, original_datadir: Path, request: FixtureRequest) -> DataFrameRegressionFixture: ...
