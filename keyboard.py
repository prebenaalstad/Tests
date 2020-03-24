#  -*- coding: utf-8 -*-
class Keyboard:
    def __init__(self, language):
        self.language = language
        self.alphabet = ["æ"] # Insert get keyboard function here.
        self.pressed_keys = []
        self.key_log = []
    def press_key(self, key):
        self.pressed_keys.append(key)
    def num_keys(self):
        if self.language == 'NO':
            return 105
    def has_key(self, key):
        if key in self.alphabet:
            return True
    def last_pressed(self):
        return self.pressed_keys[-1]
    def currently_pressed(self):
        return self.pressed_keys
    def release_key(self, key):
        self.key_log.append(key)
        try:
            self.pressed_keys.remove(key)
        except ValueError:
            raise RuntimeError
