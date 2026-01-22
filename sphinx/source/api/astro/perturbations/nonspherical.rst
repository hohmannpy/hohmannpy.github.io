astro.NonSphericalEarth
===================================

.. warning::

   This class has a singularity at geodetic colatitudes :math:`\phi` of :math:`0, \pi` due to needing to divide by
   :math:`\sin\phi` to compute the colatitudinal acceleration in curvilinear planet-centered inertial coordinates.

.. currentmodule:: hohmannpy.astro.perturbations
.. autoclass:: NonSphericalEarth
   :members:
