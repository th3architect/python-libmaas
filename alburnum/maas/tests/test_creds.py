# Copyright 2012-2015 Canonical Ltd. Copyright 2015 Alburnum Ltd.
# This software is licensed under the GNU Affero General Public
# License version 3 (see the file LICENSE).

"""Tests for handling of MAAS API credentials."""

__all__ = []

from alburnum.maas.creds import Credentials
from alburnum.maas.testing import TestCase
from testtools.matchers import IsInstance


class TestCredentials(TestCase):
    """Tests for `alburnum.maas.creds.Credentials`."""

    def test_str_form_is_colon_separated_triple(self):
        creds = Credentials("foo", "bar", "baz")
        self.assertEqual(':'.join(creds), str(creds))

    def test_parse_reads_a_colon_separated_triple(self):
        creds = Credentials.parse("foo:bar:baz")
        self.assertEqual(("foo", "bar", "baz"), creds)
        self.assertThat(creds, IsInstance(Credentials))
        self.assertEqual("foo", creds.consumer_key)
        self.assertEqual("bar", creds.token_key)
        self.assertEqual("baz", creds.token_secret)

    def test_parse_rejects_too_few_parts(self):
        self.assertRaises(ValueError, Credentials.parse, "foo:bar")

    def test_parse_rejects_too_many_parts(self):
        self.assertRaises(ValueError, Credentials.parse, "foo:bar:baz:wibble")
