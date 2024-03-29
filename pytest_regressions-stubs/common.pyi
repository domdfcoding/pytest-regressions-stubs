# stdlib
from pathlib import Path
from typing import Callable, List, Optional

# 3rd party
import pytest

def import_error_message(libname: str) -> str: ...

def check_text_files(
		obtained_fn: Path,
		expected_fn: Path,
		fix_callback: Callable[[List[str]], List[str]] = ...,
		encoding: Optional[str] = ...,
		) -> None: ...

def perform_regression_check(
		datadir: Path,
		original_datadir: Path,
		request: pytest.FixtureRequest,
		check_fn: Callable[[Path, Path], None],
		dump_fn: Callable[[Path], None],
		extension: str,
		basename: Optional[str] = ...,
		fullpath: Optional[str] = ...,
		force_regen: bool = ...,
		with_test_class_names: bool = ...,
		obtained_filename: Optional[str] = ...,
		dump_aux_fn: Callable[[Path], List[Path]] = ...,
		) -> None: ...
