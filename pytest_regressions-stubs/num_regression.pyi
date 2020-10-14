# stdlib
from pathlib import Path
from typing import Any, Dict, List, Mapping, Optional

# 3rd party
import numpy
import pandas
from _pytest.fixtures import FixtureRequest


class NumericRegressionFixture:
	"""
	Numeric Data Regression fixture implementation used on num_regression fixture.
	"""

	DISPLAY_PRECISION: int = 17  # Decimal places
	DISPLAY_WIDTH: int = 1000  # Max. Chars on outputs
	DISPLAY_MAX_COLUMNS: int = 1000  # Max. Number of columns (see #3)

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
			data_dict: Mapping[str, numpy.ndarray],
			basename: Optional[str] = None,
			fullpath: Optional[str] = None,
			tolerances: Optional[Mapping[str, Any]] = None,
			default_tolerance: Optional[Mapping[str, float]] = None,
			data_index: List[int] = None,
			fill_different_shape_with_nan: bool = True,
			) -> None: ...
