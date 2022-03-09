""" Unit tests for the Async locator class """

from unittest import IsolatedAsyncioTestCase, main
from unittest.mock import patch

from context import GeckoAsyncLocator


class TestAsyncLocator(IsolatedAsyncioTestCase):
    """Test the GeckoAsyncLocator class"""

    def setUp(self) -> None:
        self.locator = GeckoAsyncLocator(None, None)

    async def asyncSetUp(self) -> None:
        pass

    async def asyncTearDown(self) -> None:
        pass

    def tearDown(self) -> None:
        del self.locator

    #####################################################

    def test_on_construct(self):
        self.assertIsNone(self.locator.spas)
        self.assertFalse(self.locator.is_running)
        self.assertEqual(self.locator.age, 0)
        self.assertFalse(self.locator.has_had_enough_time)
        self.assertEqual(self.locator.status_line, "Initialized")

    def test_discover_none(self):
        self.assertFalse(True)
