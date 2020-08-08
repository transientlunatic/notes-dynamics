Inertial Reference Frames
=========================

An inertial frame is a coordinate system which is moving with a constant
velocity. The existence of inertial frames amounts to Newton’s first
law.

Consider a frame :math:`S(x,y,z)` and another frame
:math:`S^\prime(x^{\prime},
y^{\prime}, z^\prime)` with velocity :math:`v` with respect to :math:`S`
along the :math:`+x`-direction. The two frames are related by the
equations

.. math::

   \begin{aligned}
     x^{\prime} &= x - vt \\
     y^{\prime} &= y \\
     z^\prime &= z \\
     t^{\prime} &= t\end{aligned}

 These are an example of a Galilean transformation. We could also have
used rotations.

Now, consider a particle with mass :math:`m`. Observers in :math:`S` and
:math:`S^{\prime}` see

+----------------+------------------------------+-------------------------------------+
|                | :math:`S`                    | :math:`s^{\prime}`                  |
+----------------+------------------------------+-------------------------------------+
| Position       | :math:`\vec{x}`              | :math:`\vec{x^{\prime}}`            |
+----------------+------------------------------+-------------------------------------+
| Velocity       | :math:`\dv{\vec{x}}{t}`      | :math:`\dv{\vec{x^{\prime}}}{t}`    |
+----------------+------------------------------+-------------------------------------+
| Acceleration   | :math:`\dv[2]{\vec{x}}{t}`   | :math:`\dv[2]{\vec{x^\prime}}{t}`   |
+----------------+------------------------------+-------------------------------------+

But, from above,

[Addition of Velocities] =

| 

=

| 

Rotating Frames
===============

Consider a frame :math:`S_1` which is rotating with angular velocity,
:math:`\omega`, about its :math:`z`-axis with respect to an inertial
frame, :math:`S_0`, such that the axes coincide when :math:`t=0`. As
such there will be an angle between the sympathetic axes of
:math:`\theta = \omega t` at any given time.

Now consider a vector :math:`\vec{A}_1` in :math:`S_1` which becomes

.. math:: A_0 = \mat{R}(\omega t) \vec{A}_1

i.e. :math:`\vec{A}` as seen in :math:`S_0` rotates about the
:math:`z`-axis, corresponding to the rotation of the :math:`S_1` axes.

In general :math:`A_1` may vary with :math:`t`, i.e. :math:`A_1` is not
fixed in :math:`S_1`. Its rate of change in :math:`S_1` is not simply
given by :math:`A_1`. This seems confusing at first but due to the fact
that both the vector and the coordinate axes in :math:`S_1` are changing
with time. For example, a fixed vector in :math:`S_1` has
:math:`\dot{A}_1=0` but :math:`\dot{A}_0 \neq 0`.
