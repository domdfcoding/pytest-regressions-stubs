# stdlib
from typing import Any, Callable, Optional

# 3rd party
import pytest

def check_regression_fixture_workflow(
		pytester: pytest.Pytester,
		source: str,
		data_getter: Callable[[], Any],
		data_modifier: Callable[[], None],
		expected_data_1: Any,
		expected_data_2: Any,
		compare_fn: Optional[Callable[[Any, Any], bool]] = ...,
		) -> None: ...
