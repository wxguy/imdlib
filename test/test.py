import imdlib as imd
import os


def test_read():
    cwd = os.path.dirname(os.path.abspath(__file__))
    #/home/travis/build/iamsaswata/cct_nn
    a = imd.open_data((2018, 2018), 'rain','yearwise', cwd)
    assert a.data.shape == (365,135,1290)


#a.shape
#b = a.get_xarray()
# plt.show(b.mean('time').plot())