import unittest
from boomerang import constant


class ConstantTestCase(unittest.TestCase):
    def setUp(self):
        self.config = constant(ENV="production")

    def test_env_is_set(self):
        self.assertEqual('production', self.config.ENV)

    def test_setting_env_raises_exception(self):
        with self.assertRaises(AttributeError):
            self.config.ENV = 'test'

    def test_can_set_property(self):
        self.config.NONEXISTANT = 'test'

        self.assertEqual('test', self.config.NONEXISTANT)

    def test_can_set_property_only_once(self):
        with self.assertRaises(AttributeError):
            self.config.NONEXISTANT = 'test'
            self.config.NONEXISTANT = 'test'

    def test_empty_constant_call(self):
        constant()

    def test_assign_properties_on_empty_constant(self):
        config = constant()
        config.ENV = 'production'
        config.NONEXISTANT = 'test'

        self.assertEqual('production', config.ENV)
        self.assertEqual('test', config.NONEXISTANT)


if __name__ == '__main__':
    unittest.main()
