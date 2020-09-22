*******************
Newtonian Mechanics
*******************

.. math::
   
   \def\ddt#1{\frac{\text{d} #1}{\text{d}t}}
   \def\dd#1#2{\frac{\text{d} #1}{\text{d} #2}}
   \def\ddd#1#2#3{\frac{\text{d}^{#3} #1}{\text{d} #2^{#3}}}

In the simplest form of classical mechanics we can consider point particles which have a :physics:ref:`Mass`, but no physical extent.
Instantaneously such particles are described by two quantities; their :physics:ref:`Position`, and their :physics:ref:`Mass`.

.. physics:quantity:: Mass
   :dimensions: M
   :symbol: m

   Mass is a quantity which measures an object's resistance to acceleration.

.. physics:quantity:: Position
   :dimensions: L
   :symbol: :math:\vec{x}

   The location of an object is the coordinate of an object in a specified coordinate system.


The position of a particle can change over time.
In Newtonian mechanics time is assumed to be *absolute*, and the geometry of space is therefore *Euclidean*. 
The time derivatives of the position are also named quantities.

.. physics:quantity:: Velocity
   :dimensions: L, T^{-1}

   The rate of change of position with respect to time.

   .. math:: \vec{v} = \ddt{\vec{x}}

   ..
      :x: Position
      :t: Time
      :v: Velocity

.. physics:quantity:: Acceleration
   :dimensions: L, T^{-2}

   The rate of change of velocity with respect to time.

   .. math:: \vec{a} = \ddd{\vec{x}}{t}{2}


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
