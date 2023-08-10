\begin{center}
\begin{tikzpicture}
  \definecolor{textcolor1}{HTML}{0E2A35}
  \definecolor{arrowcolor1}{HTML}{0E2A35}
  \definecolor{backgroundcircle1}{HTML}{FFFFF0}
  \definecolor{innercircle1}{HTML}{0E2A35}
  \filldraw[fill=backgroundcircle1, draw=backgroundcircle1] (0,0) circle (1.21cm);
  \filldraw[fill=innercircle1, draw=innercircle1] (0,0) circle (0.77cm);
  \path
    [decorate,decoration={
      text along path,
      text={ PLAN DO CHECK ACT \ },
      text color={textcolor1},
      text align={fit to path stretching spaces},
      reverse path}
    ]
    (0,0) circle (0.9cm);
  \path
    [decorate,decoration={
      markings,
      mark=at position 0.3cm with {\arrow[arrowcolor1,line width=0.40mm]{triangle 90 reversed}},
      mark=at position 1.8cm with {\arrow[arrowcolor1,line width=0.40mm]{triangle 90 reversed}},
      mark=at position 3.8cm with {\arrow[arrowcolor1,line width=0.40mm]{triangle 90 reversed}},
      mark=at position 4.9cm with {\arrow[arrowcolor1,line width=0.40mm]{triangle 90 reversed}}
      }
    ]
    (0,0) circle (0.99cm);
\end{tikzpicture}
\end{center}
