Four-potential for a field
==========================

In electromagnetism the action has two components; the action for the
free particle, and then a term describing the interaction of the
particle with the field. In electromagnetism this interaction is
determined by a single parameter, the charge, :math:`e`, of the
particle.

The action for a charge in an electromagnetic field has the form

.. math::

   \label{eq:75}
     S = \int_a^b \qty( -mc \dd{s} + \frac{e}{c} A_i \dd{x}^i )

 The three spatial components of the four-vector, :math:`A^i` form the
vector potential, :math:`\vec{A}`, while the time-component,
:math:`A^0 = \phi` is the scalar potential. Introducing the velocity,
:math:`\vec{v} =
\dv*{\vec{r}}{t}`, and integrating over :math:`t`,

.. math::

   \label{eq:76}
     S = \int_{t_1}^{t_2} \qty( - mc^2 \sqrt{1 - \frac{v^2}{c^2}} + \frac{e}{c} \vec{A} \vdot \vec{v} - e \phi ) \dd{t}

 and we can then determine the Lagrangian,

.. math::

   \label{eq:77}
     L = - mc^2 \sqrt{1 - \frac{v^2}{c^2}} 
         + \frac{e}{c} \vec{A} \vdot \vec{v} 
         - e \phi

 The derivative of the Lagrangian, :math:`\pdv{L}{\vec{v}}` is the
generalised momentum of the particle, so

.. math::

   \label{eq:78}
     \vec{P} = \frac{m \vec{v}}{\sqrt{1 - \frac{v^2}{c^2}}} + \frac{e}{c} \vec{A} = \vec{p} + \frac{e}{c} \vec{A}

 and the Hamiltonian is then

.. math::

   \label{eq:79}
     H = \vec{v} \vdot \pdv{L}{\vec{v}} - L = \frac{mc^2}{\sqrt{1 - \frac{v^2}{c^2}}} + e \phi


