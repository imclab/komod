for i in range(1, 61):

    print r'\begin{center}'
    print r'\parbox{0.40\linewidth}{\includegraphics[width=4.5cm, angle=0]{2007cc_'+str(i).zfill(3)+'.eps}\\'
    print r' \centering  }'
    print r'\hspace{0.1\linewidth}'
    print r'\parbox{0.40\linewidth}{\includegraphics[width=4.5cm, angle=0]{2007_noocean_cc_'+str(i).zfill(3)+'.eps}\\'
    print r'\centering }'

    print r'\end{center}'




