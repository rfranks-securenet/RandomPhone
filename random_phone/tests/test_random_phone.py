import pytest
import random

from random_phone import RandomUkPhone

class TestsRandomPhone:
    @classmethod
    def setup_class(cls):
        cls.rpuk = RandomUkPhone()
    
    def test_random_uk_landline(self):
        phone = self.rpuk.random_landline()
        assert phone[0] == "0"
    
    def test_random_uk_mobile(self):
        phone = self.rpuk.random_mobile()
        assert phone[0:2] == "07"
    
    def test_random_uk_freephone(self):
        phone = self.rpuk.random_freephone()
        assert phone[0:2] == "08"

    def test_random_uk_premium(self):
        phone = self.rpuk.random_premium()
        assert phone[0:2] == "09"
    
    def test_random_uk_ukwide(self):
        phone = self.rpuk.random_ukwide()
        assert phone[0:2] == "03"

        
    
    def test_random_uk_landline_international(self):
        phone = self.rpuk.random_landline(international=True)
        assert phone[0:3] == "+44"
    
    def test_random_uk_mobile_international(self):
        phone = self.rpuk.random_mobile(international=True)
        assert phone[0:4] == "+447"
    
    def test_random_uk_freephone_international(self):
        phone = self.rpuk.random_freephone(international=True)
        assert phone[0:4] == "+448"

    def test_random_uk_premium_international(self):
        phone = self.rpuk.random_premium(international=True)
        assert phone[0:4] == "+449"
    
    def test_random_uk_ukwide_international(self):
        phone = self.rpuk.random_ukwide(international=True)
        assert phone[0:4] == "+443"