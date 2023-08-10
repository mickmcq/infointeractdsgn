
\begin{center}
\begin{tikzpicture}
  \filldraw[fill=green!20!white, draw=white] (0,0) circle (1.41cm);
  \filldraw[fill=white, draw=white] (0,0) circle (0.97cm);
  \path
    [decorate,decoration={
      text along path,
      text={ DESIGN PROTOTYPE EVALUATE \ },
      text color={green!50!black},
      text align={fit to path stretching spaces},
      reverse path}
    ]
    (0,0) circle (1.1cm);
  \path
    [decorate,decoration={
      markings,
      mark=at position 0.6cm with {\arrow[green!50!black,line width=0.40mm]{triangle 90 reversed}},
      mark=at position 3.1cm with {\arrow[green!50!black,line width=0.40mm]{triangle 90 reversed}},
      mark=at position 6.0cm with {\arrow[green!50!black,line width=0.40mm]{triangle 90 reversed}}
      }
    ]
    (0,0) circle (1.19cm);
\end{tikzpicture}
\end{center}
