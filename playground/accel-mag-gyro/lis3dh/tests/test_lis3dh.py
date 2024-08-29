import sys, os, pytest
sys.path.append(os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + "/../"))

from lis3dh import LIS3DH

def test_constructorPasses():
    assert LIS3DH() is not None
    assert LIS3DH(sensitivity=4) is not None
    assert LIS3DH(sensitivity=8) is not None
    assert LIS3DH(sensitivity=16) is not None

def test_constructorFailsAssertionError():
    with pytest.raises(AssertionError):
        LIS3DH(sensitivity=3)

def test_constructorFailsOSError():
    with pytest.raises(OSError):
        LIS3DH(address=0x19)