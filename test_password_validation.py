import pytest
from .password_validation import validate

def test_short():
    passwd = '1234'
    validation = validate(passwd)
    assert 'The password is not accepted' in validation

def test_only_digit():
	passwd = '12345678'
	validation = validate(passwd)
	assert 'The password is not accepted' in validation

def test_only_letters():
	passwd = 'jhdfgjdhghd'
	validation = validate(passwd)
	assert 'The password is not accepted' in validation

def test_correct_passwd():
	passwd = 'password123'
	validation = validate(passwd)
	assert 'The password is accepted' in validation

