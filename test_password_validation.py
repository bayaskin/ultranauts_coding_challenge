import pytest
from .password_validation import validate

def test_short_regular():
    passwd = '1234'
    role = 'regular'
    validation = validate(passwd, role)
    assert 'The password is not accepted' in validation

def test_only_digit_regular():
	passwd = '12345678'
	role = 'regular'
	validation = validate(passwd, role)
	assert 'The password is not accepted' in validation

def test_only_letters_regular():
	passwd = 'jhdfgjdhghd'
	role = 'regular'
	validation = validate(passwd, role)
	assert 'The password is not accepted' in validation

def test_correct_passwd_regular():
	passwd = 'password123'
	role = 'regular'
	validation = validate(passwd, role)
	assert 'The password is accepted' in validation


def test_short_admin():
    passwd = '1qwertypas!'
    role = 'admin'
    validation = validate(passwd, role)
    assert 'The password is not accepted' in validation

def test_only_digit_admin():
	passwd = '12345678'
	role = 'admin'
	validation = validate(passwd, role)
	assert 'The password is not accepted' in validation

def test_only_letters_admin():
	passwd = 'jhdfgjdhghd'
	role = 'admin'
	validation = validate(passwd, role)
	assert 'The password is not accepted' in validation

def test_correct_passwd_admin():
	passwd = '!qwerty@password123#'
	role = 'admin'
	validation = validate(passwd, role)
	assert 'The password is accepted' in validation

	
