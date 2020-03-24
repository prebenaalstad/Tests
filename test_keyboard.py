import pytest
from keyboard import Keyboard

def test_creation():
    keyboard = Keyboard("NO")
    assert keyboard.num_keys() == 105
    assert keyboard.has_key("æ")

def test_keypress():
    keyboard = Keyboard("NO")
    keyboard.press_key("n")
    assert len(keyboard.pressed_keys) == 1
    assert keyboard.last_pressed() == "n"
    assert keyboard.currently_pressed() == ["n"]
    keyboard.release_key("n")
    assert keyboard.currently_pressed() == []
    assert len(keyboard.pressed_keys) == 0

def test_keylog():
    keyboard = Keyboard("NO")
    keyboard.press_key("p")
    keyboard.release_key("p")
    keyboard.press_key("o")
    keyboard.release_key("o")
    keyboard.press_key("l")
    assert keyboard.key_log == ["p","o"]
    keyboard.release_key("l")
    assert keyboard.key_log == ["p","o","l"]

def test_keyrelease():
    keyboard = Keyboard("NO")
    with pytest.raises(RuntimeError):
        keyboard.release_key("t")
