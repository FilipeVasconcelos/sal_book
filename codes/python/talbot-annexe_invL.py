def talbot(t,f,M=20):
<<<<<<< HEAD
    """
    Algorithme fixe de Talbot :
    Equation (18) abate2004.pdf
    """
=======
>>>>>>> 6d1391af3fd63e3ed9f90ea106cd31d84803ac19
    r=2.0*M/(5.0*t)
    sumk=0.5*f(r)*np.exp(r*t)
    step=np.pi/M
    for k in range(1,M):
        tk=k*step
        cotk=1.0/np.tan(tk)
        stk=r*tk*(cotk+1j)
        sigtk=tk+(tk*cotk-1)*cotk
        sumk+=f(stk)*(1+1j*sigtk)*np.exp(t*stk)
    return (sumk*r/M).real
