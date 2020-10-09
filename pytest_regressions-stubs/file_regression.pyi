# this package
from pathlib import Path
from typing import Any, AnyStr, Callable, Optional

from _pytest.fixtures import FixtureRequest


class FileRegressionFixture:
	"""
	Implementation of `file_regression` fixture.
	"""

	request: FixtureRequest
	datadir: Path
	original_datadir: Path
	force_regen: bool

	def __init__(self, datadir: Path, original_datadir: Path, request: FixtureRequest): ...

	def check(
			self,
			contents: AnyStr,
			encoding: Optional[str] = None,
			extension: str = ".txt",
			newline: Optional[str] = None,
			basename: Optional[str] = None,
			fullpath: Optional[str] = None,
			binary: bool = False,
			obtained_filename: Optional[str] = None,
			check_fn: Optional[Callable[[Any, Any], Any]] = None,
			) -> None:
		"""
		:param check_fn: a function with signature ``(obtained_filename, expected_filename)`` that should raise
			AssertionError if both files differ.
			If not given, use internal function which compares text using :py:mod:`difflib`.
		"""

	# non-PEP 8 alias used internally at ESSS
	Check = check
