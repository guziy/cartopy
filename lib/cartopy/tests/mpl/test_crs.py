# (C) British Crown Copyright 2013 - 2020, Met Office
#
# This file is part of cartopy.
#
# cartopy is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# cartopy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with cartopy.  If not, see <https://www.gnu.org/licenses/>.

from __future__ import (absolute_import, division, print_function)

import matplotlib.pyplot as plt
from matplotlib.testing.decorators import cleanup
import pytest

import cartopy.crs as ccrs
from cartopy.tests.mpl import ImageTesting


@pytest.mark.natural_earth
@ImageTesting(['lambert_conformal_south'])
def test_lambert_south():
    # Reference image: https://www.icsm.gov.au/mapping/map_projections.html
    crs = ccrs.LambertConformal(central_longitude=140, cutoff=65,
                                standard_parallels=(-30, -60))
    ax = plt.axes(projection=crs)
    ax.coastlines()
    ax.gridlines()


@pytest.mark.natural_earth
@ImageTesting(['mercator_squashed'])
def test_mercator_squashed():
    globe = ccrs.Globe(semimajor_axis=10000, semiminor_axis=9000,
                       ellipse=None)
    crs = ccrs.Mercator(globe=globe, min_latitude=-40, max_latitude=40)
    ax = plt.axes(projection=crs)
    ax.coastlines()
    ax.gridlines()


@pytest.mark.natural_earth
@cleanup
def test_repr_html():
    pc = ccrs.PlateCarree()
    html = pc._repr_html_()

    assert html is not None
    assert '<svg ' in html
    assert '<pre>&lt;cartopy.crs.PlateCarree object at ' in html
