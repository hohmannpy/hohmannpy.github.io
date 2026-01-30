astro.perturbations
===================

.. currentmodule:: hohmannpy.astro

A set of perturbing functions that can be used to model deviations from two-body Keplerian motion. See
:class:`~hohmannpy.astro.perturbations.Perturbation` for the abstract base class template.

.. autosummary::
   :signatures: none

   Perturbation
   NonSphericalEarth
   J2
   AtmosphericDrag
   ThirdBodyGravity
   LunarGravity
   SolarGravity
   SolarRadiation

.. toctree::
   :maxdepth: 1
   :hidden:

   perturbations/base
   perturbations/nonspherical
   perturbations/j2
   perturbations/drag
   perturbations/third_body_gravity
   perturbations/lunar_gravity
   perturbations/solar_gravity
   perturbations/solar_radiation
