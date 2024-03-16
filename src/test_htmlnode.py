import unittest

from htmlnode import HTMLNode

class TestHTMKNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode(
            "h1",
            "Hello World!",
            None,
            {"href": "https://www.boot.dev", "target": "_blank"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' href="https://www.boot.dev" target="_blank"',
        )


if __name__ == "__main__":
    unittest.main()