import pytest

from src.processing import filter_by_state


def test_filter_by_state(filter_state_ex):
    assert filter_by_state(filter_state_ex, state="EXECUTED") == filter_state_ex
