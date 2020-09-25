*************************************
Rigid bodies and systems of particles
*************************************

Consider a set of particles which each has a mass :math:`m_i`, and
position vector :math:`\vec{r}_i`, then each particle can experience two
forces:

-  :math:`\vec{f}~{int}` — internal forces which act between particles
   in a system,

-  :math:`\vec{f}~{ext}` — external forces which act on the system from
   outside, e.g. a magnetic flux.

The overall motion of a system is disjoint from its internal motions,
thanks to Newton’s third law, since :math:`F_{ij} = - F_{ji}`, where
:math:`F_{ab}` is the force exerted on particle :math:`a` by particle
:math:`b`, and the force :math:`F_{ij} \propto (\vec{r}_i - \vec{r}_j)`,
i.e. acts upon the shortest path between the particles.

The Centre of Mass
==================

The total mass of a system of particles is

.. math::

   \label{eq:5}
     M = \sum_{i=1}^N m_i

 from which the total momentum can be found as

.. math::

   \label{eq:6}
     \vec{P} = \sum_{i=1}^N \vec{p}_i = \sum_{i=1}^N \dot{\vec{r}}_i m_i

 which, defining the centre of mass,

.. math:: \vec{R} = \frac{\sum_i m_i \vec{r}_i}{\sum_i m_i}

 leads to

.. math::

   \label{eq:7}
     \vec{P} = M \dv{t} \vec{R}

 The force on the :math:`i`\ th particle is then

.. math::

   \label{eq:8}
     F_i = F_i^{\rm (ext)} + \sum_{j \neq i} \vec{F}_{ji} = \dv{t}\vec{P}

 so

.. math:: \dv{t}\vec{P} = \sum_i \qty[ \vec{F}_i^{(\rm ext)} + \sum_{j \neq i} \vec{F}_{ji}]

 We have

.. math::

   \begin{aligned}
    \sum_i \sum_{j \neq i} \vec{F}_{ji} &= \sum_i \sum_{j < i} \vec{F}_{ji} + \sum_i \sum_{j > i} \vec{F}_{ji} \\ &= \sum_i \sum_{j<i} (\vec{F}_{ji} + F_{ij}) = 0\end{aligned}

 Let :math:`\vec{F}^{(\rm ext)} = \sum_i \vec{F}_i^{\rm (ext)}`, then

.. math::

   \label{eq:9}
     F^{\rm (ext)} = \dv{t} P = M \dv[2]{t} \vec{R}

 Thus, the overall motion of a system relies only on the external force
acting upon it.

Angular Momentum
================

We have

.. math:: m_i \dv[2]{t} r_i = \vec{F}_i^{\rm (ext)} + \sum_{j \neq i} \vec{F}_{ji}

 and the total angular momentum of a system as

.. math::

   \label{eq:10}
     \vec{L} = \sum^N_{i=1} \vec{r}_i \cp \vec{p}_i = \sum_{i=1}^N m_i \vec{r}_i \cp \dot{\vec{r}}_i

 Then

.. math::

   \begin{aligned}
     \dot{\vec{L}}          & = \dv{t} \sum_{i=1}^N m_i \vec{r}_i \cp \dot{\vec{r}} \nonumber                                                        \\
                            & = \sum_{i=1}^N m_i \dv{t} (\vec{r}_i \cp \dot{\vec{r}} )\nonumber                                                      \\
                            & = \sum_{i=1}^N m_i \vec{r}_i \cp \ddot{\vec{r}}_i \nonumber                                                            \\
                            & = \sum_{i=1}^N \vec{r}_i \cp \vec{F}_i^{\rm (ext)} + \sum_{i=1}^N \sum_{j \neq i} \vec{r}_i \cp \vec{F}_{ji} \nonumber \\
                            & = \vec{G}^{\rm (ext)} + \sum_{i=1}^N \sum_{j>i} (\vec{r} \cp \vec{F}_{ji} + \vec{r}_j \cp \vec{F}_{ij} ) \nonumber     \\
                            & = \vec{G}^{\rm (ext)} + \sum_{i=1}^N \sum_{j>i} (\vec{r}_i - \vec{r}_j) \cp \vec{F}_{ji} \nonumber                      \\
   \therefore \dot{\vec{L}} & = \vec{G}^{\rm (ext)}\end{aligned}

 Thus angular momentum is conserved unless there is an applied torque.

Separation of Kinetic Energy
============================

Let the position of a particle be described relative to the centre of
mass, i.e.

.. math:: \vec{r}_i = \vec{R} + \vec{r}'_i

 Then

.. math::

   \begin{aligned}
     \sum_{i=1}^N m_i \vec{r}'_i &= \sum^N_{i=1} m_i \vec{r}_i - \sum_{i=1}^N m_i R \\
   &= M \qty[ \frac{\sum m_i \vec{r}_i}{\sum m_i } - \vec{R}] = 0\end{aligned}

 the kinetic energy :math:`T` is then

.. math::

   \begin{aligned}
     T &= \half \sum m_i \dv{\vec{r}_i}{t}^2 \nonumber\\
   &= \half \sum_{i=1}^N m_i \qty[ \dot{R}^2 + 2 \dot{\vec{r}}'_i \vdot \dot{\vec{R}} + (\dot{\vec{r}}'_i)^2 ] \nonumber\\
   &= \half \sum m_i \dot{\vec{R}}^2 + \half \sum m_i \dot{\vec{r}'_i}^2 + \sum m_i \dot{\vec{r}_i'} \nonumber\\
   &= \half \sum m_i \dot{\vec{R}}^2 + \half \sum m_i (\dot{\vec{r}}'_i)^2\end{aligned}

 Thus the kinetic energy is the sum of the internal energies and the
kinetic energy of a single particle with the mass of the whole system.

Separation of Angular Momentum
==============================

The total angular momentum of a system is

.. math::

   \begin{aligned}
     \vec{L} &= \sum \vec{r}_i \cp \vec{p}_i \nonumber \\ &= \sum m \vec{r}_i \cp \dot{\vec{r}}_i \nonumber\\
   &= \sum m_i (\vec{R} + \vec{r}_i') \cp (\dot{\vec{R}} + \dot{\vec{r'}}_i ) \nonumber\\
   &= M \vec{R} \cp \dot{\vec{R}} + \qty[ \sum m_i \vec{r}' ] \cp \dot{\vec{R}} \nonumber\\ & \quad+ \vec{R} \cp \qty[ \sum m_i \dot{\vec{r}}'_i ] + \sum m_i \vec{r}'_i \cp \dot{\vec{r}}'_i \nonumber\\
   &= M \vec{R} \cp \dot{\vec{R}} + \vec{L}~{int}\end{aligned}

 Where :math:`\vec{L}~{int} = \sum m_i \vec{r}'_i \cp \dot{\vec{r}}'_i`,
so

.. math::

   \begin{aligned}
     \dot{\vec{L}} &= \sum r_i \cp \vec{F}_i^{\rm (ext)} \nonumber\\
    &= \underbracket{\vec{R} \cp \sum \vec{F}_i^{\rm (ext)}}_{\text{torque on system}} + \sum \underbracket{\vec{r}'_i \cp \vec{F}_i^{\rm (ext)}}_{\text{torque on each particle}}\end{aligned}


