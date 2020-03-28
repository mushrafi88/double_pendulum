    # Setting ----------------------------------------
    reset
    set border linecolor rgbcolor "white"
    set key textcolor rgbcolor "white"
    set title "Double Pendulum Simulation without small angle approximation" textcolor rgbcolor "white"
    set obj 1 rectangle behind from screen 0,0 to screen 1,1
    set obj 1 fillstyle solid 1.0 fillcolor rgbcolor "black"
    set nokey
    set term gif animate delay 4 size 854,480
    set output 'double_pendulum.gif'

    set xr[-20:20]
    set yr[-20:20]
    set xl 'x'
    set yl 'y'
     
    set size ratio -1
    set grid
     
    m1  = 1.0              
    m2  = 1.0
    l1  = 10.0             
    l2  = 10.0
    g  = 9.81              
    dt   = 0.01            
    M  = m2 / (m1+m2) 
    l=l1/l2    
    dx  = dt/5
    R  = 1                   
    r  = 0.1                             
     
     

    alpha1(ang_1, ang_2)=(1/l)*M*cos(ang_1-ang_2)
    alpha2(ang_1, ang_2)=l*cos(ang_1-ang_2)
    f1(ang_1, ang_2, w1, w2)=(-1/l)*M*(w2**2)*sin(ang_1-ang_2)-(g/l1)*sin(ang_1)
    f2(ang_1, ang_2, w1, w2)=l*(w1**2)*sin(ang_1-ang_2)-(g/l2)*sin(ang_2)

    g1(ang_1, ang_2, w1, w2) = w1      
    g2(ang_1, ang_2, w1, w2) = w2   
    g3(ang_1, ang_2, w1, w2) = (f1(ang_1, ang_2, w1, w2)-alpha1(ang_1, ang_2)*f2(ang_1, ang_2, w1, w2))/(1-alpha1(ang_1, ang_2)*alpha2(ang_1, ang_2))
    g4(ang_1, ang_2, w1, w2) = (f2(ang_1, ang_2, w1, w2)-f1(ang_1, ang_2, w1, w2)*alpha2(ang_1, ang_2))/(1-alpha1(ang_1, ang_2)*alpha2(ang_1, ang_2))
     
     

    x1 = pi/2          
    x2 = pi/2     
    x3 = 0.0        
    x4 = 0.0            
    t  = 0.0              
     
   
    do for [i = 1:100000] {
        t = t + dt
        k11 = g1(x1, x2, x3, x4)
        k12 = g2(x1, x2, x3, x4)
        k13 = g3(x1, x2, x3, x4)
        k14 = g4(x1, x2, x3, x4)
        k21 = g1(x1+dt/2*k11, x2+dt/2*k12, x3+dt/2*k13, x4+dt/2*k14 )
        k22 = g2(x1+dt/2*k11, x2+dt/2*k12, x3+dt/2*k13, x4+dt/2*k14 )
        k23 = g3(x1+dt/2*k11, x2+dt/2*k12, x3+dt/2*k13, x4+dt/2*k14 )
        k24 = g4(x1+dt/2*k11, x2+dt/2*k12, x3+dt/2*k13, x4+dt/2*k14 )
        k31 = g1(x1+dt/2*k21, x2+dt/2*k22, x3+dt/2*k23, x4+dt/2*k24 )
        k32 = g2(x1+dt/2*k21, x2+dt/2*k22, x3+dt/2*k23, x4+dt/2*k24 )
        k33 = g3(x1+dt/2*k21, x2+dt/2*k22, x3+dt/2*k23, x4+dt/2*k24 )
        k34 = g4(x1+dt/2*k21, x2+dt/2*k22, x3+dt/2*k23, x4+dt/2*k24 )
        k41 = g1(x1+dt*k31,  x2+dt*k32,  x3+dt*k33,  x4+dt*k34 )
        k42 = g2(x1+dt*k31,  x2+dt*k32,  x3+dt*k33,  x4+dt*k34 )
        k43 = g3(x1+dt*k31,  x2+dt*k32,  x3+dt*k33,  x4+dt*k34 )
        k44 = g4(x1+dt*k31,  x2+dt*k32,  x3+dt*k33,  x4+dt*k34 )
     
        x1 = x1 + dx * (k11 + 2*k21 + 2*k31 + k41)
        x2 = x2 + dx * (k12 + 2*k22 + 2*k32 + k42)
        x3 = x3 + dx * (k13 + 2*k23 + 2*k33 + k43)
        x4 = x4 + dx * (k14 + 2*k24 + 2*k34 + k44)
        
        # linker
        set arrow 1 nohead lw 1 from 0, 0 to l1*sin(x1), -l1*cos(x1) linecolor rgbcolor "white"
        set arrow 2 nohead lw 1 from l1*sin(x1), -l1*cos(x1) to l1*sin(x1)+l2*sin(x2), -(l1*cos(x1)+l2*cos(x2)) linecolor rgbcolor "white"
        


        # bobs
        set object 2*i+2 circle at l1*sin(x1), -l1*cos(x1) fc rgb "blue" size R fs solid front
        set object 2*i+3 circle at l1*sin(x1)+l2*sin(x2), -(l1*cos(x1)+l2*cos(x2)) fc rgb "red" size R fs solid front
     
     
        if (i%20==0){
            plot 1/0    
        }
     
        set object 2*i+2 size r/10
        set object 2*i+3 size r/10
        
    }
     
    set out