# stdlib
from typing import Any, Callable, Mapping, Optional, Sequence, Type, Union
from pathlib import Path

# 3rd party
import yaml
from _pytest.fixtures import FixtureRequest
from typing_extensions import Literal


class DataRegressionFixture:
	"""
	Implementation of `data_regression` fixture.
	"""

	request: FixtureRequest
	datadir: Path
	original_datadir: Path
	force_regen: bool

	def __init__(self, datadir: Path, original_datadir: Path, request: FixtureRequest): ...

	def check(
			self,
			data_dict: Union[Sequence, Mapping],
			basename: Optional[str] = ...,
			fullpath: Optional[str] = ...,
			) -> None: ...

	# non-PEP 8 alias used internally at ESSS
	Check = check


class RegressionYamlDumper(yaml.SafeDumper):

	def ignore_aliases(self, data) -> Literal[True]: ...

	@classmethod
	def add_custom_yaml_representer(
			cls,
			data_type: Type,
			representer_fn: Callable[[Any, Any], Any],
			): ...
