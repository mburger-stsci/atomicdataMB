import astropy.units as u
from atomicdataMB import atomicmass
import periodictable as pt

def test_Na():
    assert atomicmass('Na') == pt.Na.mass * u.u

def test_H2O():
    assert atomicmass('H2O') == pt.formulas.formula('H2O').mass * u.u