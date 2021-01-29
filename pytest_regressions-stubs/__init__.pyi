# stdlib
from typing import Any, Callable, Type

def add_custom_yaml_representer(
		data_type: Type,
		representer_fn: Callable[[Any, Any], Any],
		): ...
