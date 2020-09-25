******************
Oscillatory motion
******************

The Double Pendulum
===================

Consider a double pendulum, consisting of two bobs, one hung below the
other. Each has length :math:`a`, and bobs of mass :math:`m`, so the
potential energy is

.. math::

   \label{eq:36}
     V = -mga \cos(\theta) - mga \qty( \cos(\theta) + \cos(\phi) )

 and the kinetic energy is

.. math::

   \label{eq:36}
     T = \half m a^2 \dot{\theta}^2 + \half ma^2 (\dot{\theta} + \dot{\phi})^2

 Then,

.. math::

   \begin{aligned}
     L & = \half ma^2 \dot{\theta}^2 + \half ma^2 (\dot{\theta}^2 + \dot{\phi}^2 + 2 \dot{\theta} \dot{\phi}) \\
       &                          \qquad  + mga (2 \cos(\theta) + \cos(\phi) ) \\
   &\approx \half m a^2 \dot{\theta}^2 + \half m a^2 (\dot{\theta}^2 + \dot{\phi}^2 + 2 \dot{\theta} \dot{\phi}) \\
   & \qquad - mga \qty(\theta^2 + \half \phi^2 )\end{aligned}

 The equations of motion from the Lagrange equations are

.. math::

   \begin{aligned}
       \label{eq:36}
   2 \ddot{\theta} + \ddot{\phi} + \frac{2g}{a} \theta & =0 \\
   \ddot{\theta} + \ddot{\phi} + \frac{g}{a} \phi &= 0
     \end{aligned}

Each of these equations has a form comparable to that of a harmonic
oscillator, :math:`\ddot{x} + \omega^2 x = 0`; attempting a trial
solution

.. math::

   \begin{bmatrix}
     \theta \\ \phi
   \end{bmatrix}
   =
   \begin{bmatrix}
     c_{\theta} e^{i \omega t} \\ c_{\phi} e^{i \omega t}
   \end{bmatrix}

 For :math:`c_{\theta}`, :math:`c_{\phi}` complex constants, then

.. math:: \ddot{\theta} = - \omega^2 \theta, \qquad \ddot{\phi} = - \omega^2 \phi

 So

.. math::

   \begin{aligned}
   \label{eq:39}
       \qty( - 2 \omega^2 + \frac{2g}{a} ) c_{\theta} - \omega^2 c_{\phi} &= 0 \\
   \label{eq:38}
   - \omega^2 c_{\theta} + \qty( -\omega^2 + \frac{g}{a} ) c_{\phi} &= 0
     \end{aligned}

Which can be expressed in matrix notation

.. math::

   \label{eq:37}
     \begin{bmatrix}
       2 \frac{g}{a} - 2 \omega^2 & - \omega^2 \\ - \omega^2 & \frac{g}{a} - \omega^2
     \end{bmatrix}
     \begin{bmatrix}
       c_{\theta} \\ c_{\phi}
     \end{bmatrix} = 0

This implies that the determinant of the matrix must be zero, so

.. math::

   \label{eq:40}
       \begin{vmatrix}
       2 \frac{g}{a} - 2 \omega^2 & - \omega^2 \\ - \omega^2 & \frac{g}{a} - \omega^2
     \end{vmatrix} = 2 \qty( \frac{g}{a} - \omega^2 )^2 - \omega^4 = 0

 This has two solutions,

.. math::

   \label{eq:41}
     \omega^2 = \frac{g}{a} ( 2 \pm \sqrt{2})

 which are the normal frequencies for the system, and the coordinates
:math:`c_i` are the normal modes. To find these we substitute the normal
frequencies into equation ,

.. math::

   \label{eq:42}
     \frac{g}{a}
     \begin{bmatrix}
       2-4-2 \sqrt{2} & -2-\sqrt{2} \\ -2 -\sqrt{2} & 1-2-\sqrt{2}
     \end{bmatrix}
     \begin{bmatrix}
       c_{\theta} \\ c_{\phi} 
     \end{bmatrix} = 0

 These turn out to give two copies of the same equation relating the
coefficients, so clearly only the relative relation of them is fixed,

.. math::

   \label{eq:43}
     \frac{c_{\theta}}{c_{\phi}} = - \frac{2 + \sqrt{2}}{2(1+\sqrt{2})} = - \frac{(2+\sqrt{2})(1-\sqrt{2})}{2(1+\sqrt{2})(1-\sqrt{2})} = -\frac{1}{\sqrt{2}}

 Thus

.. math::

   \label{eq:44}
       \begin{bmatrix}
       c_{\theta} \\ c_{\phi} 
     \end{bmatrix} \propto
     \begin{bmatrix}
       -1 \\ \sqrt{2}
     \end{bmatrix}

 and using the negative solution

.. math::

   \label{eq:45}
       \begin{bmatrix}
       c_{\theta} \\ c_{\phi} 
     \end{bmatrix} \propto
     \begin{bmatrix}
       1 \\ \sqrt{2}
     \end{bmatrix}

 Giving a general solution

.. math::

   \label{eq:45}
     \begin{bmatrix} \theta \\ \phi \end{bmatrix}
   = \alpha_1 \begin{bmatrix}  -1 \\ \sqrt{2}  \end{bmatrix} e^{i \omega_1 t} + \alpha_2 \begin{bmatrix}  1 \\ \sqrt{2}  \end{bmatrix} e^{i \omega_2 t}

 This can be rewritten in matrix form too,

.. math::

   \label{eq:46}
       \begin{bmatrix} \theta \\ \phi \end{bmatrix} = 
       \begin{bmatrix} - 1 & 1 \\ \sqrt{2} & \sqrt{2} \end{bmatrix}
       \begin{bmatrix} \alpha_1 e^{i \omega_1 t} \\ \alpha_2 e^{i \omega_2 t}    \end{bmatrix}

 This can be inverted, giving

.. math::

   \label{eq:47}
       \begin{bmatrix} \alpha_1 e^{i \omega_1 t} \\ \alpha_2 e^{i \omega_2 t}    \end{bmatrix} =
       \begin{bmatrix} - \half & \half \sqrt{2} \\ \half & \half \sqrt{2} \end{bmatrix}
       \begin{bmatrix} \theta \\ \phi \end{bmatrix} =
       \begin{bmatrix} \xi_1 \\ \xi_2 \end{bmatrix}

 For :math:`\xi_i` the *normal coordinates* of the system, these cause
the Lagrange equations to completely decouple.

General Theory of Small Oscillations
====================================

Consider a system with time-independent constraints; this is in
equilibrium if

.. math:: \pdv{V}{q_i} = 0

 Furthermore, a stable equilibrium has

.. math:: \pdv[2]{V}{q_i}{q_j} > 0 \quad \forall i, j

Denoting the equilibrium value of each coordinate :math:`q^{*}_i`, we
can introduce a small perturbation, :math:`\eta_i`, such that

.. math::

   \label{eq:48}
     q_i = q^{*}_i + \eta_i

 Assuming small displacements we can use Taylor’s theorem to expand the
potential about :math:`q_i = q_i^{*}`:

.. math::

   \label{eq:49}
     V = V^{*} + \sum \eta_i \pdv{V}{q_i} + \sum_{i,j} \half \qty( \pdv[2]{V}{q_i}{q_j} ) \eta_i \eta_j

 to the second-order. The potential thus has the form of the second
derivative term,

.. math::

   \label{eq:50}
     V = \sum_{i,j} \half V_{,ij} \eta_i \eta_j

 Using the comma notation for derivatives. The matrix :math:`\mat{V}`
has components :math:`V_{,ij}`, and the set of displacements
:math:`\eta_i` forms a vector :math:`\vec{\eta}`, so

.. math::

   \label{eq:51}
     V = \half \trans{\eta} \mat{V} \eta

 Since :math:`\mat{V}` doesn’t depend upon the coordinates, just the
equilibrium values, it is constant. The kinetic energy has the form

.. math::

   \label{eq:52}
     T = \sum_{i,j} \half m_{ij} \dot{q}_i \dot{q}_j

 Expanding about the equilibrium we find

.. math:: \dot{q}_i = \dot{\eta}_i

 and

.. math:: m_{ij}(q_1, \dots, q_n) = m_{ij}(q_1^{*}, \dots, q_n^{{*}}) + \cdots

 Then

.. math::

   \label{eq:53}
     T = \sum_{i,j} \half T_{ij} \dot{\eta}_i \dot{\eta}_j

 having defined :math:`T_{ij} = m_{ij}(q^*_1, \dots, q^{*}_n)`, which is
a constant matrix, so we have

.. math::

   \label{eq:54}
     T = \half \trans{\dot{\eta}} \mat{T} \dot{\eta}

 and

.. math::

   \label{eq:55}
     L = T-V = \sum_{i,j} \half \qty[ T_{ij} \dot{\eta}_i \dot{\eta}_j - V_{ij} \eta_i \eta_j] = \half \trans{\dot{\eta}} \mat{T} \dot{\eta} - \half \trans{\eta} \mat{V} \eta

 The Lagrange equations have the form

.. math:: \dv{t} \pdv{L}{\dot{\eta}_k} = \pdv{L}{\eta_k}

 Taking this in bits,

.. math:: \pdv{L}{\dot{\eta}_k} = \half \sum_{i,j} T_{ij} \qty[ \pdv{\dot{\eta}_i}{\dot{\eta}_k} + \dot{\eta}_i \pdv{\dot{\eta}_j}{\dot{\eta}_k}]

 The generalised coordinates are independent, so

.. math:: \pdv{\dot{\eta}_i}{\dot{\eta}_k} = \delta_{ik}

 Thus

.. math::

   \label{eq:56}
     \pdv{L}{\dot{\eta}_k} = \half \sum_{i,j} T_{ij} \qty[ \delta_{ik} \dot{\eta}_j + \dot{\eta}_i \delta_{jk}] = \sum_j T_{kj} \dot{\eta}_j

Similarly,

.. math::

   \label{eq:57}
     \pdv{L}{\eta_k} = - \sum_j V_{,kj} \eta_j

This gives the Lagrange equations in the form

.. math::

   \label{eq:58}
     \sum_j (T_{ij} \ddot{\theta}_j + V_{,ij} \eta_j) = 0 \equiv \mat{T} \ddot{\vec{\eta}} + \mat{V} \vec{\eta}_j = \vec{0}

 As in the double pendulum case, we can find solutions of the form

.. math:: \eta = \vec{c} e^{i \omega t}

 Then :math:`\ddot{\eta} = - \omega^2 \eta`, and so

.. math::

   \label{eq:59}
     \qty( \mat{V} - \omega^2 \mat{T} ) \eta = \vec{0}

 To satisfy the equation we need

.. math::

   \label{eq:60}
     \abs{\mat{V}-\omega^2 \mat{T}} = 0

 which is a characteristic equation, and this can be approached as an
eigenvalue equation, and once the normal frequencies are found we
substitute them back in turn, and find the vectors :math:`\vec{c}` by
solving

.. math:: \mat{V} \vec{c} = \omega^2 \mat{T} \vec{c}

 for each :math:`\omega^2`. THis is akin to finding the eigenvectors of
a matrix, and the vectors specify the *normal modes* of the oscillation.

In general, from the fact that :math:`\mat{V}` and :math:`\mat{T}` are
symmetric, and that :math:`\omega^2` has real solutions, that
:math:`\vec{c}` can be chosen to be orthonormal. The general solution
takes the form

.. math::

   \label{eq:80}
     \begin{pmatrix}
       \eta_1 \\ \vdots \\ \eta_n
     \end{pmatrix}
    = \sum_j \alpha_j \vec{c}^{(j)} \exp( i \omega_j t) = \sum_j \alpha_j 
    \begin{pmatrix}
      c_1^{(j)} \\ \vdots c_n^{(j)}
    \end{pmatrix}
   \exp(i \omega_j t)

 which can be expressed more compactly, using Einstein notation,

.. math::

   \label{eq:81}
    \eta_i = c_i^j \alpha_j \exp(i \omega_j t)

 for :math:`c_i^j = c_i^{(j)}`. We can then define normal coordinates,

.. math:: \xi_j = \alpha_j \exp(i \omega_j t)

 which correspond to the oscillation of the system at a single
frequency, and can be found by inverting equation ([eq:80]), so

.. math::

   \label{eq:82}
     \xi_j = (c_i^j)^{-1} \eta_i

 The Lagrangian then completely decouples into the sum of independent
harmonic oscillators,

.. math::

   \label{eq:87}
     L = \sum_j C_j \qty[ \dot{\xi}_j^2 - \omega^2_j \xi_j^2]

 for :math:`C_j` a normalisation constant.
