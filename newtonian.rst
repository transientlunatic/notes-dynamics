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
Such a reference frame is described as *inertial*, since within that reference frame the particle will appear to move in a straight line, such that

.. math:: \CMposition[x](t) = \CMposition[x](t_0) + \CMvelocity t

Newton's first law (the law of inertia) is a description of the existence of such a reference frame.



The *Galilean principle of relativity* states that in all possible inertial frames the laws of mechanics will be the same.


Inertial reference frames are not unique, and indeed there are transformations which map between reference frames.
Galilean transformations constitute *translations*, *rotations*, and *boosts* (uniform motions) between frames:

There are three spatial translations, :math:`\CMposition \to \vec{a} \CMposition` for some vector :math:`\vec{a} \in \mathbb{R}^3`,
and also one temporal translation :math:`\CMtime \to s \CMtime` for a real number :math:`c \in \mathbb{R}`.

There are three spatial rotations, :math:`\CMposition \to \mat{G} \CMposition` for an orthogonal matrix transformation :math:`\mat{G}:\mathbb{R^3} \to \mathbb{R}^3`.

The boost transformations all involve a velocity: :math:`\CMposition \to \CMposition + v \CMtime` for a uniform velocity :math:`\vec{v}`

There are a total of ten Galilean transformations, giving a ten dimensional Lie algebra.
The composition of two Galilean transformations is also a Galilean transformation, and so an eleventh transformation can be formed from the composition.

The set of all Galilean transformations under composition forms the Galilean group.


Force
=====

The aim of classical mechanics is to predict the position of a particle at some point in the future knowing its mechanical properties.

An important quantity is the *momentum* of the particle, which is defined simply as the product of its mass, :math:`\CMmass` and velocity, :math:`\CMvelocity`:

.. physics:quantity:: Momentum
   :dimensions: M, L, T^-1
   :symbol: \CMmomentum
	    
   .. math:: \CMmomentum = \CMmass \CMvelocity

Newton's second law allows the equation of motion to be determined from its momentum and the force :math:`\CMforce` on the particle.
	    
.. physics:quantity:: Force
   :dimensions: M, L, T^-2
   :symbol: \CMforce

   .. math:: \CMforce = \ddt{\CMmomentum} = \CMmass \CMacceleration
		


Energy
======

It is useful in mechanics toi be able to identify conserved quantities, and an important example of such a quantity is the energy of the system.

In Newtonian mechanics we can arrive at the notion of energy via *work*, which is the integral of a force over the distance, :math:`s` for which it is applied along a path :math:`S`, that is

.. physics:quantity:: Work
   :dimensions: M, L^2, T^-2
   :symbol: \CMenergy[W]
	    
   .. math:: \CMenergy[W] = \int_S F \cdot \dd{s}

The *kinetic energy* of a particle is the energy due to its own motion, and is defined as

.. physics:quantity:: Kinetic Energy
   :dimensions: M, L^2, T^-2
   :symbol: \CMenergy[T]

   .. math:: \CMenergy[T] = \frac{1}{2} \CMmass \CMvelocity^2

Whereas its *potential energy* is the energy which a particle has as a result of some force acting upon it (and corresponds to the kinetic energy which would be gained by the particle were the force to act upon it.

.. physics:quantity:: Potential Energy
   :dimensions: M, L^2, T^-2
   :symbol: \CMenergy[V]

The rate at which a particle's energy changes is the *power* applied to that particle.
	    
.. physics:quantity:: Power
   :dimensions: M, L^2, T^-3
   :symbol: \CMpower

   .. math:: \CMpower = \ddt{\CMenergy}
