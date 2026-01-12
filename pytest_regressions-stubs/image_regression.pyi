# stdlib
from pathlib import Path
from typing import Optional

# 3rd party
from _pytest.fixtures import FixtureRequest
from PIL import Image

class ImageRegressionFixture:
	"""
	Regression test for image objects, accounting for small differences.
	"""
	request: FixtureRequest
	datadir: Path
	original_datadir: Path
	force_regen: bool

	def __init__(self, datadir: Path, original_datadir: Path, request: FixtureRequest): ...
	def _load_image(self, filename: Path) -> Image.Image: ...
	def _compute_manhattan_distance(self, diff_image: Image.Image) -> float: ...

	def _check_images_manhattan_distance(
			self,
			obtained_file: str,
			expected_file: str,
			expect_equal: bool,
			diff_threshold: float,
			) -> None: ...

	def check(
			self,
			image_data: bytes,
			diff_threshold: float = ...,
			expect_equal: bool = ...,
			basename: Optional[str] = ...,
			) -> None: ...
