astro.maneuvers
===================

.. currentmodule:: hohmannpy.astro

A set of burns which may be scheduled for satellites. Note that :class:`~hohmannpy.astro.ContinuousBurn` is a
base class template and should never be instantiated directly. Instead instantiate its children.

.. autosummary::
   :signatures: none

   ImpulsiveBurn
   ContinuousBurn
   ConstantContinuousBurn
   LookupContinuousBurn
   FunctionContinuousBurn

.. toctree::
   :maxdepth: 1
   :hidden:

   impulsive
   continuous
   const_continuous
   lookup_continuous
   function_continuous
