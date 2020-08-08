In the Lagrangian formalism the equations of motion are given by

.. math::

   \tag{\ref{eq:21}}
     \dv{t}\qty(\pdv{L}{\dot{q}_i}) - \pdv{L}{q_i} = 0

 These are second-order differential equations, and so :math:`2n`
initial values are required for a full solution, with an
:math:`n`-dimensional configuration space. The Hamiltonian approach is
to recast the equations of motion as first-order equations, with a
configuration space of :math:`2n` independent variables, describing the
position of a point is spacetime, and the conjugate momenta. Now
:math:`(p, q)` are the canonical variables.

The Legendre Transform
======================

In order to switch from the parameters of the Lagrangian formalism,
:math:`(q, \dot{q}, t)` to those of the Hamiltonian, :math:`(q, p, t)`
we introduce a transformation.

Consider a function of the form

.. math::

   \dd{f} = u \dd{x} + v \dd{y}, \qquad u= \pdv{f}{x}, \quad
   v=\pdv{f}{y}

We want to change from using :math:`x` and :math:`y` in the description
to using :math:`u` and :math:`y`, so let

.. math:: g = f - ux

 which has a differential,

.. math:: \dd{g} = \dd{f} - u \dd{x} - x \dd{u} = v \dd{y} - x \dd{u}

 Thus :math:`x` and :math:`v` are now functions of :math:`u` and
:math:`y`:

.. math:: x = - \pdv{g}{u}, \qquad v = \pdv{g}{y}

[Legendre transforms in thermodynamics] Consider the first law of
thermodynamics,

.. math:: \dd{U}= \dd{Q} - \dd{W}

For a gas undergoing a reversible process this can be re-expressed as

.. math:: \dd{U} = T \dd{S} - P \dd{V}

 For the entropy, :math:`S`, and volume :math:`V`. The temperature and
the pressure are given

.. math:: T = \pdv{U}{S} \qquad P = - \pdv{U}{V}

 To find the enthalpy, :math:`H(S,P)` we use a Legendre transform,

.. math:: H = U + PV

 which gives

.. math:: \dd{H} = T \dd{S} + V \dd{P}

 where

.. math:: T = \pdv{H}{S}\ \qquad V = \pdv{H}{P}

The Hamiltonian
===============

The Hamiltonian function is generated from the Lagrangian using a
Legendre transform, starting with the differential of :math:`L`,

.. math::

   \label{eq:83}
     \dd{L} = \pdv{L}{q_i} \dd{q_i} + \pdv{L}{\dot{q}_i} \dd{\dot{q}_i} + \pdv{L}{t} \dd{t}

 Recalling that :math:`p_i = \pdv*{L}{q_i}`, then

.. math::

   \label{eq:84}
     \dd{L} = \dot{p}_i \dd{q}_i + p_i \dd{\dot{q}}_i + \pdv{L}{t} \dd{t}

 and we can transform to the Hamiltonian using

.. math::

   \label{eq:85}
     H(q, p, t) = \dot{q}_i p_i - L(q, \dot{q}, t)

with differential

.. math::

   \label{eq:86}
     \dd{H}= \dot{q}_i \dd{p_i} - \dot{p}_i \dd{q}_i - \pdv{L}{t}

 and so

.. math::

   \label{eq:88}
     \dd{H} - \pdv{H}{q_i} \dd{q_i} + \pdv{H}{p_i} + \pdv{H}{t} \dd{t}

Thus we have :math:`2n +1` relations,

.. math::

   \begin{aligned}
   \label{eq:89}
       \dot{q}_i    & = \pdv{H}{p_i} \\
   \label{eq:90}
       - \dot{p}_i  & = \pdv{H}{q_i} \\
   \label{eq:91}
       - \pdv{L}{t} & = \pdv{H}{t}
     \end{aligned}

with equations ([eq:89] – [eq:90]) the *canonical equations of
Hamilton*, which are the :math:`2n` first-order equations which replace
the :math:`n` second-order Lagrange equations.

If the forces involved in the Lagrangian are the result of a
conservative potential, and if the equations with generalised
coordinates don’t depend explicitly on time then the Hamiltonian is
equal to the total energy.

From the definition of :math:`H` in equation ([eq:85]), and in the
manner of equation ([eq:94]),

.. math::

   \label{eq:98}
     H = \dot{q}_i p_i - [L_0(q_i, t) + L_1(q_i, t)\dot{q}_k + L_2(q_i, t) \dot{q}_k \dot{q}_m]

 If the equations defining the generalised coordinates do not explicitly
depend on time, :math:`L_2 \dot{q}_k \dot{q}_m = T`, and if the forces
can be derived from a conservative potential, :math:`L_0 = -V`, and thus

.. math::

   \label{eq:99}
     H = T + V = E

Constructing the Hamiltonian
============================

The procedure for constructing the Hamiltonian is

#. Construct :math:`L` in a given set of :math:`q_i`,

#. Define the :math:`p_i`

#. Form the Hamiltonian using equation ([eq:85])

#. Invert the conjugate momenta to gain the :math:`\dot{q}_i`\ s

#. These are used to eliminate all :math:`\dot{q}_i` from :math:`H`
