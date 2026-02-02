astro.NonSphericalEarth
===================================

.. caution::

   This class has a singularity at geodetic colatitudes :math:`\phi` of :math:`0, \pi` due to needing to divide by
   :math:`\sin\phi` to compute the colatitudinal acceleration in curvilinear Earth-centered Earth-fixed coordinates.

.. currentmodule:: hohmannpy.astro
.. autoclass:: NonSphericalEarth
   :members:
