*******************
Newtonian Mechanics
*******************

.. include:: macros.rst


Reference frames
================

In order to describe the mechanical behaviour of a system it is necessary to define a *reference frame* in which the behaviour, and the laws which govern it, are defined.

.. sidebar:: Reference frames

   You'll also come across reference frames being called "coordinate systems" and "local frames" in other contexts.
   The reason for this will become more obvious in discussions of :ref:`special-relativity`.

In different reference frames the laws describing the system may look different.
A reference frame is a vector space 

Mechanical quantities
=====================
   
In the simplest form of classical mechanics we can consider point particles which have a :physics:ref:`Mass`, but no  physical extent, or where their physical extent is negligable compared to the scale of motion.

The position, :math:`\CMposition{}` of a particle is a vector from the origin of the reference frame to the particle.

.. physics:quantity:: Position
   :dimensions: L
   :symbol: \CMposition

   The location of an object is the radius vector of an object in a specified frame of reference.


Instantaneously such particles are described by two quantities; their :physics:ref:`Position`, and their :physics:ref:`Mass`.

.. physics:quantity:: Mass
   :dimensions: M
   :symbol: \CMmass

   Mass is a quantity which measures an object's resistance to acceleration.

The position of a particle can change over time.
In Newtonian mechanics time is assumed to be *absolute*, and the geometry of space is therefore *Euclidean*. 
The time derivatives of the position are also named quantities.

.. physics:quantity:: Velocity
   :dimensions: L, T^{-1}
   :symbol: \PHvelocity

   The rate of change of position with respect to time.

   .. math:: \vec{v} = \CMvelocity

Specifying the mass, position and the velocity of a system completely defines its mechanical state, which is an important consideration in other formulations of mechanics.

	  
.. physics:quantity:: Acceleration
   :dimensions: L, T^{-2}
   :symbol: \PHacceleration

   The rate of change of velocity with respect to time.

   .. math:: \vec{a} = \CMacceleration{}


Galilean relativity and inertial frames
=======================================

In the absence of acceleration it is always possible to choose a frame of reference for a particle which is "co-moving" with the particle.
Such a reference frame is described as *inertial*, since within that reference frame the particle does not appear to move.
Newton's first law (the law of inertia) is a description of the existence of such a reference frame.

The *Galilean principle of relativity* states that in all possible inertial frames the laws of mechanics will be the same.

Given a particle which has position :math:`\vec{x}` in one reference frame :math:`K`, it will have a position

.. math:: \vec{x}' = x + Vt

in a frame :math:`K'` which is moving with a velocity :math:`V` relative to :math:`K` at a time :math:`t`.
Importantly, in Galilean relativity it is assumed that the time will be **the same** in both frames.
This assumption is relaxed in Einstein's Special Relativity.


Now, consider a particle with mass :math:`m`. Observers in :math:`R` and
:math:`R^{\prime}` see

+----------------+------------------------------+---------------------------------+
|                | :math:`R`                    | :math:`R^{\prime}`              |
+================+==============================+=================================+
| Position       | :math:`\CMposition[x]`       | :math:`\CMposition[x']`         |
+----------------+------------------------------+---------------------------------+
| Velocity       | :math:`\ddf{\vec{x}}{t}`     | :math:`\ddf{\vec{x}'}{t}`       |
+----------------+------------------------------+---------------------------------+
| Acceleration   | :math:`\dddf{\vec{x}}{t}{2}` | :math:`\dddf{\vec{x}'}{t}{2}`   |
+----------------+------------------------------+---------------------------------+

We can see from this that the acceleration term is the same in both frames, as we'd expect from the assertion that the laws of physics look the same in all inertial frames.

Force
=====

.. physics:quantity:: Momentum
   :dimensions: M, L, T^-1

.. physics:quantity:: Force
   :dimensions: M, L, T^-2


Energy
======

.. physics:quantity:: Energy
   :dimensions: M, L^2, T^-2

.. physics:quantity:: Power
   :dimensions: M, L^2, T^-3
