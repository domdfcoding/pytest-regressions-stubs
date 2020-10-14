# stdlib
from typing import Any, List, Mapping, Optional

# 3rd party
import numpy

# this package
from pytest_regressions.dataframe_regression import DataFrameRegressionFixture


class NumericRegressionFixture(DataFrameRegressionFixture):
	"""
	Numeric Data Regression fixture implementation used on num_regression fixture.
	"""

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
