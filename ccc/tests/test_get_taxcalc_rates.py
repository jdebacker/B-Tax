import numpy as np
import pytest
from ccc import get_taxcalc_rates as tc
from ccc.parameters import Specification
from ccc.utils import TC_LAST_YEAR


def test_get_calculator_cps():
    '''
    Test the get_calculator() function
    '''
    calc1 = tc.get_calculator(True, 2019, 2019)
    assert calc1.current_year == 2019


@pytest.mark.needs_puf
@pytest.mark.parametrize('data', ['puf.csv', None],
                         ids=['data=PUF', 'data=None'])
def test_get_calculator(data):
    '''
    Test the get_calculator() function
    '''
    calc1 = tc.get_calculator(True, 2019, 2019, data=data)
    assert calc1.current_year == 2019


def test_get_calculator_exception():
    '''
    Test the get_calculator() function
    '''
    with pytest.raises(Exception):
        assert tc.get_calculator(True, TC_LAST_YEAR + 1)


def test_get_rates():
    '''
    Test of the get_rates() functions
    '''
    # has default tax rates, which should equal what is returned from TC
    p = Specification(start_year=2020, end_year=2020)
    test_dict = tc.get_rates(
        baseline=False, start_year=2020, end_year=2020, reform={},
        data='cps')
    for k, v in test_dict.items():
        print('Tax rate = ', k)
        assert(np.allclose(v, p.__dict__[k]))
