# stdlib
from functools import partial

# 3rd party
from typing import Any, Callable, Mapping, Optional, Type

import yaml
from _pytest.fixtures import FixtureRequest

from pytest_regressions.common import Path, check_text_files, perform_regression_check


class DataRegressionFixture:
	"""
	Implementation of `data_regression` fixture.
	"""

	request: FixtureRequest
	datadir: Path
	original_datadir: Path
	force_regen: bool

	def __init__(self, datadir: Path, original_datadir: Path, request: FixtureRequest): ...
	def check(self, data_dict: Mapping, basename: Optional[str] = None, fullpath: Optional[str] = None) -> None: ...

	# non-PEP 8 alias used internally at ESSS
	Check = check


class RegressionYamlDumper(yaml.SafeDumper):

	def ignore_aliases(self, data):
		return True

	@classmethod
	def add_custom_yaml_representer(cls, data_type: Type, representer_fn: Callable[[Any, Any], Any]):
		"""
		:param callable representer_fn: Function that receives ``(dumper, data)`` type as
			argument and must must return a YAML-convertible representation.
		"""
