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

+----------------+------------------------------+-------------------------------+
|                | :math:`S`                    | :math:`s^{\prime}`            |
+================+==============================+===============================+
| Position       | :math:`\vec{x}`              | :math:`\vec{x}'`              |
+----------------+------------------------------+-------------------------------+
| Velocity       | :math:`\dv{\vec{x}}{t}`      | :math:`\dv{\vec{x}'}{t}`      |
+----------------+------------------------------+-------------------------------+
| Acceleration   | :math:`\dv[2]{\vec{x}}{t}`   | :math:`\dv[2]{\vec{x}'}{t}`   |
+----------------+------------------------------+-------------------------------+

But, from above,

.. math::

   %[Addition of Velocities]
    \dv{\vec{x}}{t} = 
    \begin{pmatrix}
      \dv{x}{t} \\ \dv{y}{t} \\ \dv{z}{t}
    \end{pmatrix}
   =
   \begin{pmatrix}
     \dv{x^{\prime}}{t} + v \\
    \dv{y^{\prime}}{t} \\
    \dv{z^{\prime}}{t}
   \end{pmatrix}

Thus, for velocities we interpret this to mean that the velocity of a
particle in another frame is equal to its velocity in its own frame
added to the relative velocity of its frame to the observer’s.

Acceleration, on the other hand, is the same in both frames, and is a
frame-independent quantity. The general expression of this idea this
implies that the laws of physics are the same in all inertial frames;
the principle of Galilean relativity.

Rotating Frames
===============

Consider a frame :math:`S_1` which is rotating with angular velocity,
:math:`\omega`, about its :math:`z`-axis with respect to an inertial
frame, :math:`S_0`, such that the axes coincide when :math:`t=0`. As
such there will be an angle between the sympathetic axes of
:math:`\theta = \omega t` at any given time.

Now consider a vector :math:`\vec{A}_1` in :math:`S_1` which becomes

.. math:: A_0 = {\mathsf{R}}(\omega t) \vec{A}_1

i.e. :math:`\vec{A}` as seen in :math:`S_0` rotates about the
:math:`z`-axis, corresponding to the rotation of the :math:`S_1` axes.
The explicit form of :math:`{\mathsf{R}}(\theta)` is then

.. math::

   {\mathsf{R}} = 
   \begin{bmatrix}
     \cos(\omega t) & - \sin(\omega t) & 0 \\
   \sin(\omega t)   & \cos(\omega t)   & 0 \\
   0              & 0              & 1
   \end{bmatrix}

In general :math:`A_1` may vary with :math:`t`, i.e. :math:`A_1` is not
fixed in :math:`S_1`. Its rate of change in :math:`S_1` is not simply
given by :math:`A_1`. This seems confusing at first but due to the fact
that both the vector and the coordinate axes in :math:`S_1` are changing
with time. For example, a fixed vector in :math:`S_1` has
:math:`\dot{A}_1=0` but :math:`\dot{A}_0 \neq 0`.

The rate of change of the axes introduces an additional term to
velocities in :math:`S_0`; letting

.. math::

   \begin{aligned}
   \dd{\vec{A}_0} &= \underbracket{\qty[ \dd{{\mathsf{R}}}(\omega t) ] \vec{A}_1}_{\text{From axis rotation.}} + {\mathsf{R}}(\omega t) \dd{\vec{A}_1} \\
   &= \vec{\omega} \cp \vec{A}_0 \dd{t} + {\mathsf{R}}(\omega t) \dd{A_1} \\
   &= \vec{\omega} \cp \qty[ {\mathsf{R}}(\omega t) \vec{A}_1] \dd{t} + {\mathsf{R}}(\omega t) \dd{A_1}\end{aligned}

 Since

.. math::

   \qty| \dd{{\mathsf{R}}} \vec{A}_1| = \omega \dd{t} \qty|
   \vec{A}_0(\omega t) | = \qty| \omega \cp \vec{A}_0 | \dd{t}

 Where the second part follows from the change in :math:`\vec{A}_0`
being perpendicular to :math:`\vec{A}_0` for the infinitessimal interval
:math:`\dd{t}`. The quantity :math:`\vec{\omega} \cp \vec{A}_0` points
in the direction of :math:`\dd{R} \vec{A}_1`, so given that the rotation
is about the same axis as the finite rotation
:math:`{\mathsf{R}}(\omega t)`,

.. math::

   \omega \times \qty( {\mathsf{R}} \vec{A}_1) = {\mathsf{R}} \qty[ \vec{\omega}
   \cp \vec{A}_1]

 This implies that the order of rotations is irrelevant, so

.. math::

   \begin{aligned}
     \dd{{\mathsf{R}}} \vec{A}_1 &= {\mathsf{R}}(\omega t) \qty[ \vec{\omega} \cp \vec{A}_1] \dd{t} \nonumber \\
   \implies \dd{\vec{A}_0} &= {\mathsf{R}}(\omega t) \qty[ \dd{\vec{A}_1} + \vec{\omega} \cp \vec{A}_1] \dd{t} \nonumber \\
   \label{eq:2}
   \dot{\vec{A}}_0 &= {\mathsf{R}}( \omega t ) \qty[ \dot{\vec{A}}_1 + \vec{\omega} \cp \vec{A}_1 ]\end{aligned}

The Coriolis and Centrifugal Forces
===================================

Let a particle have positions :math:`\vec{x}_0` and :math:`\vec{x}_1` in
the frames :math:`S_0` and :math:`S_1` respectively, with :math:`S_1`
rotating relative to :math:`S_0` according to the transformation
:math:`{\mathsf{R}}(\omega t)`, so

.. math::

   \begin{aligned}
     \vec{x}_0 &= {\mathsf{R}}(\omega t) \vec{x}_1 \\
   &= {\mathsf{R}}(\omega t) \qty[ \dot{\vec{x}}_1 + \vec{\omega} \cp \vec{x}_1 ] &\omit\hfill \text{ (by eq. \eqref{eq:2})} \\
   \implies \vec{v}_0 &= {\mathsf{R}}(\omega t) \qty[ \vec{v}_1 + \vec{\omega} \cp \vec{x}_1 ]\end{aligned}

 Letting :math:`\vec{A}_0 = \vec{v}_0`, and
:math:`\vec{A}_1 = \vec{v}_1 + \vec{\omega} \cp \vec{x}_1`, then

.. math::

   \begin{aligned}
     \dot{\vec{v}}_0 &= {\mathsf{R}}(\omega t) \qty[ \dot{\vec{v}}_1 + \vec{\omega} \cp \dot{\vec{x}} + \vec{\omega} \cp \qty( \vec{v}_1 + \vec{\omega} \cp \vec{x}_1 ) ] \\ 
   &= {\mathsf{R}}(\omega t) \qty[ \dot{\vec{v}}_1 + 2 \vec{\omega} \cp \vec{v}_1 + \vec{\omega} \cp ( \vec{\omega} \cp \vec{x}_1 )]\end{aligned}

 Since :math:`\vec{a}_i = \dot{\vec{v}}_i` is the acceleration observed
in the frame :math:`S_i`, then

.. math::

   \vec{a}_1 = {\mathsf{R}}(-\omega t) \vec{a}_0 - 2 \vec{\omega} \cp
   \vec{v}_1 - \vec{\omega} \cp ( \vec{\omega} \cp \vec{x}_1 )

 So the acceleration is not the same in each frame, and since in the
individual frames Newton’s laws are valid, we see two additional forces,

.. math::

   \begin{aligned}
     \label{eq:3}
     \vec{f}~{cor} &= - 2 m \vec{\omega} \cp \vec{v}_1 \\
   \vec{f}~{cen} &= - m \vec{\omega} \cp \qty( \vec{\omega} \cp \vec{x}_1 )\end{aligned}

Respectively the Coriolis and Centrifugal forces.

Motion at the Earth’s Surface
=============================

The coordinate system on the Earth’s surface is defined using two
coordinates, latitude, :math:`\lambda`, and longitude, :math:`\beta`. We
also have a rotation vector, :math:`\vec{\Omega}`. A point close to the
surface is specified by three coordinates: altitude, latitude, and
longitude, and its velocity has the vector

.. math:: \vec{v} = \qty( v~{long}, v~{lat}, v~{alt})

 an object near the Earth’s surface will experience a Coriolis force,

.. math:: \vec{f}~{cor} = - 2m \vec{\Omega} \cp \vec{v}

 and we have

.. math:: \vec{\Omega} = \qty( 0, \Omega \cos(\lambda), \Omega \sin(\lambda) )

 Thus

.. math::

   \begin{aligned}
   \vec{f}~{cor} &= -2m  \qty( 0, \Omega \cos(\lambda), \Omega \sin(\lambda) ) \cp \qty( v~{long}, v~{lat}, v~{alt}) \nonumber\\
   &= - 2 m \Omega \begin{pmatrix} v~{alt} \cos(\lambda) - v~{lat} \sin(\lambda)\\ v~{long} \sin(\lambda) \\ - v~{long} \cos(\lambda)
   \end{pmatrix} \nonumber \\
   & \text{ if } v~{alt} = 0 \nonumber \\
   &= -2m \Omega
   \begin{pmatrix}
     - v~{lat} \sin(\lambda) \\ v~{long} \sin(\lambda) \\ 0 
   \end{pmatrix} \nonumber \\
   &= - 2m \qty(0 , 0 , \Omega \sin(\lambda) ) \cp \qty( v~{long}, v~{lat}, 0) \nonumber \\
   \therefore \vec{f}~{cor} &= - 2 m \vec{\Omega}~{alt} \cp \vec{v}\end{aligned}

The Foucalt Pendulum
====================

The plane of a pendulum’s motion will rotate over time in a rotating
reference frame. Let :math:`S_1` be the rotating reference frame of the
Earth, and :math:`S_2` be a frame rotating with angular velocity
:math:`\omega_2
\propto \Omega~{alt}`. The accelerations in the two frames satisfy

.. math::

   \label{eq:1}
     \vec{a}_1 = {\mathsf{R}} \qty[ \vec{a}_2 + 2 \vec{\omega}_2 \cp \vec{v}_2 + \vec{\omega}_2 \cp ( \vec{\omega}_2 \cp \vec{x}_2 )]

 where :math:`\vec{x}_i`, :math:`\vec{v}_i`, and :math:`\vec{a}_i` are
respectively the position, velocity, and accleration in the
:math:`i`\ th frame. Assuming both :math:`\vec{\Omega}` and
:math:`\vec{\omega}_2` are small, then the centrifugal term can be
neglected, and

.. math:: \vec{a}_1 = {\mathsf{R}} \qty[ \vec{a}_2 + 2 \vec{\omega}_2 \cp \vec{v}_2 ]

 we know

.. math:: \vec{a}_1 = \vec{g} - 2 \vec{\Omega}~{alt} \cp \vec{v}_2

 For :math:`\vec{g}` the acceleration due to gravity, so, given that the
pendulum undergoes horizontal motion, and we can neglect its vertical
motion, ignoring quadratic terms,

.. math:: \vec{v}_1 \approx {\mathsf{R}} \vec{v}_2

 and so

.. math::

   \vec{g} - 2 {\mathsf{R}} \qty[ \vec{\Omega}~{alt} \cp \vec{v}_2 ] =
   {\mathsf{R}} \qty[ \vec{a}_2 + 2 \vec{\omega}_2 \cp \vec{v}_2 ]

 thus, multiplying both sides by :math:`{\mathsf{R}}^{-1}`,

.. math::

   \label{eq:4}
     \vec{a}_2 = {\mathsf{R}}^{-1} \vec{g}

 and so the acceleration of the bob is simply the acceleration due to
gravity transformed into a different frame, and in :math:`S_2` it
appears as if only gravity acts, so this represents a frame which is
rotating to counteract the rotation of the pendulum’s plane, thus
demonstrating that the plane is rotating.
