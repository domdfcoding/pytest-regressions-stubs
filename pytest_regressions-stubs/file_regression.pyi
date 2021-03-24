# stdlib
from pathlib import Path
from typing import Any, AnyStr, Callable, Optional

# 3rd party
from _pytest.fixtures import FixtureRequest

class FileRegressionFixture:
	"""
	Implementation of ``file_regression`` fixture.
	"""
	request: FixtureRequest
	datadir: Path
	original_datadir: Path
	force_regen: bool

	def __init__(self, datadir: Path, original_datadir: Path, request: FixtureRequest): ...

	def check(
			self,
			contents: AnyStr,
			encoding: Optional[str] = ...,
			extension: str = ...,
			newline: Optional[str] = ...,
			basename: Optional[str] = ...,
			fullpath: Optional[str] = ...,
			binary: bool = ...,
			obtained_filename: Optional[str] = ...,
			check_fn: Optional[Callable[[Any, Any], Any]] = ...,
			) -> None: ...

	# non-PEP 8 alias used internally at ESSS
	Check = check
