#!/usr/bin/python
#

import unittest
import spotify

TEST_APP_KEY = [
	0x01, 0xFB, 0x02, 0x78, 0xBF, 0x19, 0xFA, 0x8A, 0xCE, 0x1E, 0x03, 0xCE, 0xF0, 0xA1, 0x04, 0x9B,
	0xD4, 0x2D, 0x1A, 0xC1, 0x08, 0x2E, 0xA7, 0x65, 0x57, 0xF5, 0xAA, 0x91, 0x12, 0x0D, 0x62, 0x82,
	0x4A, 0x20, 0x85, 0x13, 0x67, 0x22, 0x24, 0x90, 0x48, 0xB5, 0x30, 0xEF, 0x59, 0x07, 0x03, 0xC9,
	0xD9, 0x54, 0xDB, 0xEF, 0x65, 0xA1, 0xFB, 0xA6, 0x84, 0xDA, 0x52, 0x7A, 0x37, 0x3F, 0x9C, 0x2E,
	0xA1, 0x16, 0x55, 0x74, 0x69, 0x14, 0xF1, 0x94, 0x80, 0x71, 0xAA, 0xD8, 0x65, 0x69, 0x65, 0x99,
	0x2E, 0x34, 0x55, 0xA1, 0x11, 0x3E, 0xEB, 0xEF, 0x9D, 0xEA, 0x39, 0x0C, 0xBB, 0x72, 0x0A, 0xE8,
	0xA7, 0xD1, 0x7F, 0x4C, 0x21, 0xD1, 0xDC, 0x25, 0xF3, 0x64, 0x2F, 0xAF, 0xDA, 0x06, 0xC3, 0xF4,
	0x5B, 0x48, 0x5E, 0xDA, 0xC1, 0x4B, 0xAF, 0x39, 0x31, 0xD2, 0x1C, 0x10, 0x5B, 0x33, 0xA6, 0x7D,
	0xB7, 0x8E, 0x0E, 0x73, 0x2A, 0x05, 0xA3, 0x70, 0x50, 0xEC, 0x91, 0xB4, 0xBB, 0x7C, 0xC5, 0x69,
	0x6A, 0xB1, 0xCF, 0x39, 0xAD, 0x16, 0xB2, 0x55, 0x99, 0x8E, 0x5B, 0xED, 0x74, 0x86, 0xBD, 0x90,
	0xBA, 0xC3, 0xCD, 0x22, 0xF3, 0x85, 0xC3, 0xA9, 0x2A, 0xAF, 0x36, 0x46, 0xBA, 0x4D, 0x42, 0x64,
	0x05, 0xEB, 0x37, 0xE7, 0xCF, 0x4E, 0x34, 0x8C, 0x4D, 0x71, 0x23, 0x3B, 0x77, 0x09, 0xC7, 0x31,
	0x2B, 0xBA, 0x26, 0x77, 0x01, 0xBC, 0x89, 0xF1, 0xDA, 0xC3, 0xB1, 0xD6, 0x8F, 0xFC, 0x31, 0xE8,
	0xCC, 0xF5, 0x48, 0x43, 0x5E, 0xAC, 0x52, 0xF6, 0x2D, 0x4A, 0x3B, 0x34, 0x2A, 0xA1, 0xD7, 0x75,
	0x8C, 0xE7, 0x15, 0x02, 0xD2, 0x4B, 0x07, 0x0F, 0x6F, 0xC0, 0x00, 0xE9, 0x11, 0x62, 0x81, 0x0C,
	0x6B, 0xB6, 0xAC, 0x14, 0xE4, 0x69, 0x5C, 0x18, 0x23, 0x35, 0xF1, 0x79, 0xD8, 0x2C, 0xED, 0xF3,
	0x36, 0xAD, 0xBF, 0x4C, 0x88, 0x16, 0xC8, 0xAA, 0x68, 0xFC, 0xC9, 0x2E, 0x95, 0x7D, 0x23, 0xE9,
	0xA1, 0x2A, 0xAC, 0x23, 0x19, 0x25, 0x9D, 0xAE, 0xFF, 0x9F, 0x49, 0x0E, 0x4E, 0xF3, 0x35, 0x58,
	0x2A, 0x7A, 0x49, 0xF3, 0x45, 0x30, 0x48, 0xD3, 0x0B, 0x73, 0x41, 0x0F, 0x8C, 0x74, 0x1B, 0xD3,
	0xCC, 0xBB, 0x4C, 0x1B, 0xDE, 0xD3, 0x05, 0x7C, 0x8C, 0x01, 0x0A, 0x19, 0x4E, 0xB0, 0x34, 0x73,
	0x2C,
]

class Generic(unittest.TestCase):

    def test_get_key(self):
        assert spotify.get_app_key() == TEST_APP_KEY

    def test_error_message(self):
        assert spotify.error_message(0) == 'No error'

if __name__ == '__main__':
    unittest.main()
