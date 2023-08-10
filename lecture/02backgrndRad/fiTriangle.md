
\begin{center}
  \begin{tikzpicture}[xscale=1.7,show background rectangle]
  \tikzstyle{background rectangle}=[rounded corners,fill=bkgroundcolor]

    \node[chenattr]      (a00) at (2.5,6.0)    {psych};
    \node[chenattr]      (a01) at (0.0,0)    {graphics};
    \node[chenattr]      (a02) at (5.0,0)    {coding};

    \draw[relat] (a00) -- (a01);
    \draw[relat] (a00) -- (a02);
    \draw[relat] (a01) -- (a02);

    \node[chentinyattr]  (a03) at (2.5,2.0)  {ui\\ designer};
    \node[chentinyattr]  (a04) at (2.5,3.2)  {ux\\ designer};
    \node[chentinyattr]  (a05) at (2.5,4.3)  {ux\\ researcher};
    \node[chentinyattr]  (a06) at (1.2,0.7)  {visual\\ designer};
    \node[chentinyattr]  (a07) at (3.7,0.7)  {ux\\ engineer};
  \end{tikzpicture}
\end{center}

