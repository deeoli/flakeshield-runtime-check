import pytest
import random


def test_stable_pass():
    assert True


def test_potential_flake():
    # This will fail 50% of the time in a real CI to simulate flakiness
    assert random.choice([True, False])


def test_hard_failure():
    assert False, "This is a definitive bug"

#comment