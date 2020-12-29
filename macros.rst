.. math::
   % UTILITIES %
   \newcommand{\half}{\frac{1}{2}}%
   \renewcommand{\vec}[1]{\mathbf{#1}}%
   \newcommand{\mat}[1]{\mathbf{\mathsf{#1}}}%
   \newcommand{\vdot}[2]{{#1}\cdot{#2}}% Vector dot product
   \def\dd#1{\,\text{d}#1}%
   \def\ddt#1{\frac{\text{d} #1}{\text{d}t}}%
   \def\df#1{\frac{\text{d}}{\text{d} #1}}%
   \def\pdf#1{\frac{\partial}{\partial #1}}%
   %
   \def\ddf#1#2{\frac{\text{d} #1}{\text{d} #2}}%
   \def\pddf#1#2{\frac{\partial #1}{\partial #2}}%
   %
   \def\dddf#1#2#3{\frac{\text{d}^{#3} #1}{\text{d} #2^{#3}}}%
   \def\cp{\times}%
   % BASIC PHYSICS %
   \newcommand{\PHdistance}[1][r]{{\color{red} \vec{#1}}}%
   \newcommand{\PHvelocity}[1][v]{{\color{red} \vec{#1}}}%
   \newcommand{\PHacceleration}[1][a]{{\color{red} \vec{#1}}}%
   \newcommand{\PHmass}[1][m]{{\color{green} #1}}%
   \newcommand{\PHlength}[1][l]{{\color{red}#1}}%
   \newcommand{\PHenergy}[1][E]{{\color{blue} #1}}%
   % DISTANCE-LIKE %
   \newcommand{\CMdistance}[1][x]{\PHlength[#1]}%
   \newcommand{\CMposition}[1][x]{\vec{#1}}%
   \newcommand{\CMvelocity}[1][x]{\ddt{\CMposition[#1]}}%
   \newcommand{\CMacceleration}[1][x]{\dddf{\CMposition[#1]}{t}{2}}%
   \newcommand{\CMmomentum}[1][p]{\vec{#1}}%
   \newcommand{\CMforce}[1][F]{\vec{#1}}%
   \newcommand{\CMtime}[1][t]{#1}%
   \newcommand{\CMenergy}[1][E]{#1}%
   \newcommand{\CMpower}[1][P]{#1}%
   % MASS-LIKE %
   \newcommand{\CMmass}[1][m]{\PHmass[m]}%
   % PHYSICAL CONSTANTS %
   \newcommand{\CMg}{\PHacceleration[g]}%
