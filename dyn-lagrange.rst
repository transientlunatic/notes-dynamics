Constraints
===========

The motion of a particle may be restricted in an arbitrary way via
contraints, for example, a pendulum attached to a string of length
:math:`L` has a contraint

.. math:: x^2 + y^2 = L^2

In general a contraint can be characterised as a force, in the case of
the pendulum this is tension.

A **holonomic** constraint has the form

.. math:: g(\vec{x}_1, \vec{x}_2, \dots, \vec{x}_n, t) = 0

If the constraint has time-dependence it is **rheonomous**, otherwise it
is **scleronomous**. Not every contraint is holonomic; the constraint
that a particle may not enter a sphere is an inequality, and thus
non-holonomic, for example.

Generalised Coordinates
=======================

Generalised coordinates are chosen to simplify the description of a
system, and are linearly independent. These are a set of independent
quantities :math:`\set{q_i}`, such that

.. math::

   \label{eq:11}
     \vec{x}_i = \vec{x}_i(\set{q_i}, t)

The number of degrees of freedom, :math:`f`, for a system is equal to
the product of the system’s dimensionality, :math:`D`, and its number of
particles, :math:`N`, less the number of constraints, i.e.

.. math:: f = DN - k

and this results in a system requiring :math:`f` generalised coordinates
to fully characterise it.

Virtual Work :math:`\star`
==========================

A virtual displacement of a system is a change in a system’s
configuration as a result of any arbitrary infinitessimal change of its
coordinates, :math:`\delta \vec{r}_i`.

The virtual work of a force :math:`\vec{F}_i` is
:math:`\vec{F}_i \vdot \delta
\vec{r}_i`. If the system is in equilibrium then :math:`\vec{F}_i = 0`,
so the virtual work also vanishes. For the whole system

.. math:: \sum \vec{F}_i \vdot \delta \vec{r}_i = 0

We can express a force in the form
:math:`\vec{F}_i = \vec{F}_i^{\rm (a)} +\vec{f}_i`, the sum of an
applied force and a constraint, so

.. math::

   \label{eq:12}
     \sum \vec{F}_i^{\rm (a)} \vdot \delta \vec{r}_i + \sum_i \vec{f}_i \vdot \delta \vec{r}_i =0

 If the constraint forces produce no net virtual work (excluding e.g.
sliding friction),

.. math::

   \label{eq:13}
     \sum \vec{F}_i^{\rm (a)} \vdot \delta \vec{r}_i = 0

 Which is the principle of virtual work.

Thanks to the constraints :math:`\delta \vec{r}_i` are not independent,
so a form for the general motion of the system in general coordinates is
required.

D’Alembert’s Principle
======================

Take the equation of motion,

.. math:: \vec{F}_i = \dot{\vec{p}}_i

 which can be expressed

.. math:: \vec{F}_i - \dot{\vec{p}}_i = 0

 Then

.. math::

   \begin{aligned}
     \label{eq:14}
     \sum (\vec{F}_i - \dot{\vec{p}}_i) \vdot \delta \vec{r}_i &=0 \\
   \sum_i (\vec{F}_i^{\rm (a)} - \dot{\vec{p}}_i ) \vdot \delta \vec{r}_i + \sum \vec{f}_i \vdot \delta \vec{r}_i &= 0 \\
   \sum_i (\vec{F}_i^{\rm (a)} - \dot{\vec{p}}_i ) \vdot \delta \vec{r}_i &= 0\end{aligned}

which is *D’Alembert’s Principle*. To convert this to generalised
coordinates we use a transformation

.. math::

   \label{eq:15}
     \delta \vec{r}_i = \sum_j \pdv{\vec{r}_i}{q_j} \delta q_j

 using the summation convention, and defining
:math:`\Lambda^j_i = \pdv{\vec{r}_i}{q_j}`,

.. math:: \delta \vec{r}_i = \Lambda^j_i \delta q_j

 Then the virtual work becomes

.. math::

   \label{eq:16}
     \sum_i \vec{F}_i  \vdot \delta \vec{r}_i = \sum_{i,j} \vec{F}_i \vdot \Lambda^j_i \delta q_j = \sum_j Q_j \delta q_j

 with :math:`Q_j` the components of a virtual force,

.. math:: Q_j = \sum_i \vec{F}_i \Lambda^i_j

We also have the reversed effective force in equation ,

.. math::

   \label{eq:17}
     \sum \dot{\vec{p}}_i \vdot \delta \vec{r}_i = \sum m_i \ddot{\vec{r}}_i \vdot \delta \vec{r}_i = \sum_{i,j} m_i \ddot{\vec{r}}_i \Lambda^j_i \delta q_j

Then

.. math::

   \begin{aligned}
     \sum m_i \ddot{\vec{r}}_i \vdot \Lambda_i^j &= \sum_i \qty[ \dv{t} \qty(m_i \dot{\vec{r}} \vdot \Lambda_i^j ) - m_i \dot{\vec{r}} \vdot \dv{t} \qty( \Lambda^j_i )  ] \\ 
   &= \sum_i \qty[ \dv{t} \qty( m_i \vec{v}_i \vdot \pdv{\vec{v}_i}{\dot{q}_j} ) - m_i \vec{v}_i \pdv{\vec{v}_i}{q_j}]\end{aligned}

 Since

.. math::

   \begin{aligned}
     \dv{t} \pdv{\vec{r}_i}{q_j} &= \pdv{\vec{v}}{q_j} \\
   \pdv{\vec{v}_i}{\dot{{q}}_j} &= \pdv{\vec{r}_i}{q_j}\end{aligned}

 Then equation can be expanded to

.. math::

   \begin{aligned}
     \sum_j & \bigg\{
       \dv{t} \qty[ 
         \pdv{\dot{q}_j} \qty( \sum_i \half m_i v_i^2) 
       ]
       \\ & \quad- \pdv{q_j} \qty( \sum_i \half m_i v_i^2 )
       - Q_j
     \bigg\} \delta q_j\end{aligned}

 Then

.. math::

   \label{eq:18}
     \sum \qty{ \qty[
       \dv{t} \qty( \pdv{T}{\dot{q}_j} ) - \pdv{T}{q_j}
     ] - Q_j } \delta q_j = 0

 For :math:`T` the kinetic energy, and so,

.. math::

   \label{eq:19}
     \dv{t} \qty( \pdv{T}{\dot{q}_j} ) - \pdv{T}{q_j} = Q_j

 When the forces are produced by a potential,
:math:`\vec{F}_i = - \nabla_i
V`,

.. math:: Q_j = - \sum_i \nabla_i V \vdot \pdv{\vec{r}_i}{q_j} = - \pdv{V}{q_i}

 so we now have

.. math::

   \label{eq:20}
     \dv{t} \qty( \pdv{T}{\dot{q}_j} ) - \pdv{(T-V)}{q_i} = 0

 and defining a function :math:`L = T - V`, the *Lagrangian*, and noting
that :math:`\pdv{V}{\dot{q}_j} = 0`, we get

.. math::

   \label{eq:21}
     \dv{t} \qty( \pdv{L}{\dot{q}_j} ) - \pdv{L}{q_j} = 0

which are *Lagrange’s equations*.

Velocity-dependent Potentials :math:`\star`
===========================================

Suppose there is no potential :math:`V` to generate the generalised
forces, but they can instead be found from a function
:math:`U(q_j, \dot{q_j})` by

.. math::

   \label{eq:22}
     Q_j = - \pdv{U}{q_j} + \dv{t}\qty( \pdv{U}{\dot{q}_j} )

 The Lagrangian is now

.. math:: L = T-U

 and :math:`U` is a “generalised potential”. Such a potential is of
importance in electromagnetism.

The Electromagnetic Vector Potential
------------------------------------

Consider the force on a charge,

.. math::

   \label{eq:23}
     \vec{F} = q \qty[ \vec{E} + \vec{v} \cp \vec{B}]

 for :math:`\vec{E} = \vec{E}(x,y,z,t)` and
:math:`\vec{B} = \vec{B}(x,y,z,t)` being continuous functions of time
and position. These can be derived from a scalar potential and a vector
potential, respectively :math:`\phi(t,x,y,z)` and
:math:`\vec{A}(t,x,y,z)`:

.. math::

   \begin{aligned}
   \vec{E} & = - \nabla \phi - \pdv{\vec{A}}{t} \\ 
   \vec{B} & = \nabla \cp \vec{A}  \end{aligned}

The force can then be derived from the potential :math:`U`,

.. math::

   \label{eq:24}
     U = q \phi - q \vec{A} \vdot \vec{v}

 and the Lagrangian is then

.. math::

   \label{eq:25}
     L = \half m v^2 - q \phi + q \vec{A} \vdot \vec{v}

 This can then be used to derive equation .

Dissipation :math:`\star`
=========================

If not all of the forces in a system can be derived from a potential
then

.. math::

   \label{eq:26}
     \dv{t} \qty( \pdv{L}{\dot{q}_j} ) - \pdv{L}{q_j} = Q_j

 This happens in the case of friction, where there is a force

.. math:: F_{{\rm f}x} = - k_x v_x

 Such a force can be considered by the dissipation function,

.. math::

   \label{eq:27}
     \mathcal{F} = \half \sum_i \qty( k_x v_{ix}^2 + k_y v_{iy}^2 + k_z v_{iz}^2 )

 where

.. math:: \vec{F}_{{\rm f}x} = - \pdv{\mathcal{F}}{v_x} \implies \vec{F}~{f} = - \nabla_v \mathcal{F}

 The Lagrange equations then become

.. math::

   \label{eq:28}
     \dv{t} \pdv{L}{\dot{q}_j} - \pdv{L}{q_j} + \pdv{\mathcal{F}}{\dot{q}_j} = 0

Hamilton’s Principle
====================

It is possible to derive the Lagrange equations for a system from an
integrated perspective of the motion, using Hamilton’s Principle (the
principle of least action):

    The motion of a system from a time :math:`t_1` to :math:`t_2` is
    such that the line integral

    .. math:: I = \int_{t_1}^{t_2} L \dd{t}

    for :math:`L = T - V` has a stationary value for the actual path of
    the motion.

We define the action as the integral from Hamilton’s Principle,

.. math::

   \label{eq:29}
     S( \set{q_i}, \set{\dot{q}_i} ) = \int_{t_0}^{t_1} \dd{t} L(\set{q_i}, \set{\dot{q}_i}, t)

To derive the Lagrange equations introduce a small perturbation to
:math:`q_i`,

.. math:: q_i(t) \to q_i(t) + \delta q_i(t)

The trajectory has fixed end-points, so
:math:`\delta q_i(t_0) = \delta q_i(t_1) = 0`, so

.. math:: \dot{q}_i \to q_i + \delta \dot{q}_i, \quad \delta \dot{q}_i = \dv{t} \delta q_i

This perturbs the action,

.. math:: S \to S + \var{S} = \int_{t_0}^{t_1} \dd{t} L(q_i+\var{q_i}, \dot{q}_i + \var{\dot{q}_i}, t)

 Using Taylor’s theorem,

.. math::

   \label{eq:30}
     S + \var{S} = \int_{t_0}^{t_1} \dd{t} \qty[ L + \sum_i \qty( \pdv{L}{q_i} \var{q_i} + \pdv{L}{\dot{q}_i} \var{\dot{q}_i} ) ] + \cdots

 Then

.. math::

   \begin{aligned}
     \label{eq:31}
     \var{S} &= \sum_i\int_{t_0}^{t_1} \dd{t} \qty[  \pdv{L}{q_i} \var{q_i} + \pdv{L}{\dot{q}_i} \var{\dot{q}_i}  ] \\
   &= \sum_i \qty{ \underbracket{\eval{ \pdv{L}{\dot{q}_i} \var{q_i} }_{t_0}^{t_1}}_{=0} + \underbracket{\int_{t_0}^{t_1} \dd{t} \qty[\pdv{L}{q_i} - \dv{t} \pdv{L}{\dot{q}_i} ] \delta q_i  }_{\text{Must be zero to extremise  action}} } \\
   \therefore \dv{t} \pdv{L}{\dot{q}_i}&= \pdv{L}{q_i}\end{aligned}

The variational approach to finding the Lagrangian allows easy extension
to systems which are not normally the domain of dynamics, for example
the descriptions of electrical circuits.

Canonical Momentum
==================

Recall the Lagrangian for a particle moving in one dimension,

.. math:: L = \half m \dot{x}^2 - V(x)

 from which

.. math:: \pdv{L}{x} = m \dot{x}

 which is the particle’s momentum. Given a general Lagrangian the
quantity

.. math::

   \label{eq:32}
     p_i = \pdv{L}{\dot{q}_i}

 is the generalised momentum, or the canonically conjugate momentum to
:math:`q_i`.

Symmetries and Conservation
===========================

If the Lagrangian of a system doesn’t explicity contain a coordinate
:math:`q_i`, (but may contain :math:`\dot{q}_j`) it is called cyclic, so

.. math::

   \label{eq:33}
     \pdv{L}{q_i} = 0 \implies \dv{t}\pdv{L}{\dot{q}_i} = \dot{p}_i = 0

 Therefore, the momentum conjugate to a cyclic coordinate is conserved.

The Energy Function
===================

Consider the time derivative of :math:`L`,

.. math::

   \begin{aligned}
     \label{eq:34}
     \dv{L}{t} &= \sum_i \pdv{L}{q_i} \dv{q_i}{t} + \sum_i \pdv{L}{\dot{q}_i} \dv{\dot{q}_i}{t} + \pdv{L}{t} \\
   &= \sum_j \dv{t} \qty(\pdv{L}{\dot{q}_j}) \dot{q}_j + \sum_j \pdv{L}{\dot{q}_j} \dv{\dot{q}_j}{t} +\pdv{L}{t}\end{aligned}

 Thus

.. math::

   \begin{aligned}
   \dv{t} \qty( \sum_j \dot{q}_j \pdv{L}{\dot{q}_j} - L ) + \pdv{L}{t} &= 0 \\
   \dv{H}{t} &= - \pdv{L}{t}\end{aligned}

 For

.. math::

   \label{eq:35}
     h = \sum_i \dot{q}_i \pdv{L}{\dot{q}_i} - L

 defined as the “Energy function”, which is physically, if not
mathematically, identical to the Hamiltonian. Thus

.. math::

   \label{eq:92}
     \dv{h}{t} = - \pdv{L}{t}

 If the Lagrangian is not explicitly a function of time then :math:`h`
is conserved. This is one of the first integrals of the motion, and is
*Jacobi’s integral*.

Under some circumstances :math:`h` is the total energy of a system;
recall that the total kinetic energy of a system can be expressed

.. math::

   \label{eq:93}
     T = T_0 + T_1 + T_2

 with :math:`T_0` a function of only the generalised coordinates,
:math:`T_1(q,
\dot{q})` is linear in the generalised velocities, and :math:`T_2(q,
\dot{q})` is quadratic in :math:`\dot{q}`. For a wide range of systems
we can similarly decompose the Lagrangian,

.. math::

   \label{eq:94}
     L = L_0 + L_1 + L_2

 If a function :math:`f` is homogeneous and of degree :math:`n` in the
variables :math:`x_i`, then :math:`
  \sum_i x_i \pdv*{f}{x_i} = nf
` applied to the function :math:`h`,

.. math::

   \label{eq:96}
     h = 2 L_2 + L_1 - L = L_2 - L_0

 If the transformations to generalised coordinates are time independent
:math:`T = T_2`, and then if the potential doesn’t depend on generalised
velocity, :math:`L_0 = -V`, so

.. math::

   \label{eq:97}
     h = T + V = E


