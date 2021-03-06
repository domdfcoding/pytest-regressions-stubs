# stdlib
from pathlib import Path
from typing import Any, Dict, Mapping, Optional

# 3rd party
import pandas  # type: ignore
from _pytest.fixtures import FixtureRequest

class DataFrameRegressionFixture:
	"""
    Pandas DataFrame Regression fixture implementation used on dataframe_regression fixture.
    """
	DISPLAY_PRECISION: int = ...  # Decimal places
	DISPLAY_WIDTH: int = ...  # Max. Chars on outputs
	DISPLAY_MAX_COLUMNS: int = ...  # Max. Number of columns (see #3)
	request: FixtureRequest
	datadir: Path
	original_datadir: Path
	_force_regen: bool
	_tolerances_dict: Dict[str, Any]
	_default_tolerance: Dict[str, float]
	_pandas_display_options: Dict[str, float]

	def __init__(self, datadir: Path, original_datadir: Path, request: FixtureRequest): ...
	def _check_data_types(self, key: str, obtained_column: pandas.Series, expected_column: pandas.Series) -> None: ...
	def _check_data_shapes(self, obtained_column: pandas.Series, expected_column: pandas.Series) -> None: ...
	def _check_fn(self, obtained_filename: str, expected_filename: str) -> None: ...
	def _dump_fn(self, data_object: pandas.DataFrame, filename: str) -> None: ...

	def check(
			self,
			data_frame: pandas.DataFrame,
			basename: Optional[str] = ...,
			fullpath: Optional[str] = ...,
			tolerances: Optional[Mapping[str, Any]] = ...,
			default_tolerance: Optional[Mapping[str, float]] = ...,
			) -> None: ...
