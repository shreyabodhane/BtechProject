# Generated with SMOP  0.41
from libsmop import *
# rao1.m

    
@function
def Rao1(*args,**kwargs):
    varargin = Rao1.varargin
    nargin = Rao1.nargin

    clc
    clear('all')
    pop=10
# rao1.m:4
    
    var=30
# rao1.m:5
    
    maxFes=30000
# rao1.m:6
    
    maxGen=floor(maxFes / pop)
# rao1.m:7
    
    mini=dot(- 100,ones(1,var))
# rao1.m:8
    maxi=dot(100,ones(1,var))
# rao1.m:9
    row,var=size(mini,nargout=2)
# rao1.m:10
    x=zeros(pop,var)
# rao1.m:11
    for i in arange(1,var).reshape(-1):
        x[arange(),i]=mini(i) + dot((maxi(i) - mini(i)),rand(pop,1))
# rao1.m:13
    
    f=objective(x)
# rao1.m:15
    gen=1
# rao1.m:16
    while (gen <= maxGen):

        xnew=updatepopulation(x,f)
# rao1.m:18
        xnew=trimr(mini,maxi,xnew)
# rao1.m:19
        fnew=objective(xnew)
# rao1.m:20
        for i in range(1,pop).reshape(-1):
            if (fnew(i) < f(i)):
                x[i,arange()]=xnew(i,arange())
# rao1.m:23
                f[i]=fnew(i)
# rao1.m:24
        disp(concat(['Iteration No. = ',num2str(gen)]))
        disp('%%%%%%%% Final population %%%%%%%%%')
        disp(concat([x,f]))
        fnew=[]
# rao1.m:30
        xnew=[]
# rao1.m:30
        fopt(gen),ind=min(f,nargout=2)
# rao1.m:31
        xopt[gen,arange()]=x(ind,arange())
# rao1.m:32
        gen=gen + 1
# rao1.m:33

    
    val,ind=min(fopt,nargout=2)
# rao1.m:35
    Fes=dot(pop,ind)
# rao1.m:36
    disp(concat(['Optimum value = ',num2str(val,10)]))
    return
    
if __name__ == '__main__':
    pass
    
    ##The objective function is given below.
    
@function
def objective(x=None,*args,**kwargs):
    varargin = objective.varargin
    nargin = objective.nargin

    r,c=size(x,nargout=2)
# rao1.m:41
    for i in arange(1,r).reshape(-1):
        y=0
# rao1.m:43
        for j in arange(1,c).reshape(-1):
            y=y + (x(i,j)) ** 2
# rao1.m:45
        z[i]=y
# rao1.m:47
    
    f=z.T
# rao1.m:49
    return f
    
if __name__ == '__main__':
    pass
    
    
@function
def updatepopulation(x=None,f=None,*args,**kwargs):
    varargin = updatepopulation.varargin
    nargin = updatepopulation.nargin

    row,col=size(x,nargout=2)
# rao1.m:53
    t,tindex=min(f,nargout=2)
# rao1.m:54
    Best=x(tindex,arange())
# rao1.m:55
    w,windex=max(f,nargout=2)
# rao1.m:56
    worst=x(windex,arange())
# rao1.m:57
    xnew=zeros(row,col)
# rao1.m:58
    for i in arange(1,row).reshape(-1):
        for j in arange(1,col).reshape(-1):
            xnew[i,j]=(x(i,j)) + dot(rand,(Best(j) - worst(j)))
# rao1.m:61
    
    return xnew
    
if __name__ == '__main__':
    pass
    
    
@function
def trimr(mini=None,maxi=None,x=None,*args,**kwargs):
    varargin = trimr.varargin
    nargin = trimr.nargin

    row,col=size(x,nargout=2)
# rao1.m:66
    for i in arange(1,col).reshape(-1):
        x[x(arange(),i) < mini(i),i]=mini(i)
# rao1.m:68
        x[x(arange(),i) > maxi(i),i]=maxi(i)
# rao1.m:69
    
    z=copy(x)
# rao1.m:71
    return z
    
if __name__ == '__main__':
    pass
    
