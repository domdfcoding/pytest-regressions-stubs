# stdlib
from typing import Any, List, Mapping, Optional

# 3rd party
import numpy  # type: ignore

# this package
from pytest_regressions.dataframe_regression import DataFrameRegressionFixture

class NumericRegressionFixture(DataFrameRegressionFixture):
	"""
	Numeric Data Regression fixture implementation used on num_regression fixture.
	"""

	def check(  # type: ignore[override]
			self,
			data_dict: Mapping[str, numpy.ndarray],
			basename: Optional[str] = ...,
			fullpath: Optional[str] = ...,
			tolerances: Optional[Mapping[str, Any]] = ...,
			default_tolerance: Optional[Mapping[str, float]] = ...,
			data_index: Optional[List[int]] = ...,
			fill_different_shape_with_nan: bool = ...,
			) -> None: ...
