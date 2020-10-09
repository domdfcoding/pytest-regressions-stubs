# stdlib
from typing import Any, Callable, Type


def add_custom_yaml_representer(data_type: Type, representer_fn: Callable[[Any, Any], Any]):
	"""
	:param callable representer_fn: Function that receives object of `data_type` type as
		argument and must return a YAML-convertible representation.
	"""
