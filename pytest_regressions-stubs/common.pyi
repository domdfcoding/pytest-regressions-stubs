# stdlib
from pathlib import Path
from typing import Callable, List, Optional

# 3rd party
from _pytest.fixtures import SubRequest


def import_error_message(libname: str) -> str:
	return f"'{libname}' library is an optional dependency and must be installed explicitly when the fixture 'check' is used"


def check_text_files(
		obtained_fn: Path,
		expected_fn: Path,
		fix_callback: Callable[[List[str]], List[str]] = lambda x: x,
		encoding: Optional[str] = None,
		) -> None: ...

def perform_regression_check(
		datadir: Path,
		original_datadir: Path,
		request: SubRequest,
		check_fn: Callable[[Path, Path], None],
		dump_fn: Callable[[Path], None],
		extension: str,
		basename: Optional[str] = None,
		fullpath: Optional[str] = None,
		force_regen: bool = False,
		obtained_filename: str = None,
		dump_aux_fn: Callable[[Path], List[Path]] = lambda filename: [],
		) -> None: ...
