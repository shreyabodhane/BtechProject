# Generated with SMOP  0.41
from libsmop import *
# rao3.m

    
@function
def Rao3(*args,**kwargs):
    varargin = Rao3.varargin
    nargin = Rao3.nargin

    clc
    clear('all')
    pop=10
# rao3.m:4
    
    var=30
# rao3.m:5
    
    maxFes=30000
# rao3.m:6
    
    maxGen=floor(maxFes / pop)
# rao3.m:7
    
    mini=dot(- 100,ones(1,var))
# rao3.m:8
    maxi=dot(100,ones(1,var))
# rao3.m:9
    row,var=size(mini,nargout=2)
# rao3.m:10
    x=zeros(pop,var)
# rao3.m:11
    for i in arange(1,var).reshape(-1):
        x[arange(),i]=mini(i) + dot((maxi(i) - mini(i)),rand(pop,1))
# rao3.m:13
    
    f=objective(x)
# rao3.m:15
    gen=1
# rao3.m:16
    while (gen <= maxGen):

        xnew=updatepopulation(x,f)
# rao3.m:18
        xnew=trimr(mini,maxi,xnew)
# rao3.m:19
        fnew=objective(xnew)
# rao3.m:20
        for i in arange(1,pop).reshape(-1):
            if (fnew(i) < f(i)):
                x[i,arange()]=xnew(i,arange())
# rao3.m:23
                f[i]=fnew(i)
# rao3.m:24
        disp(concat(['Iteration No. = ',num2str(gen)]))
        disp('%%%%%%%% Final population %%%%%%%%%')
        disp(concat([x,f]))
        fnew=[]
# rao3.m:30
        xnew=[]
# rao3.m:30
        fopt(gen),ind=min(f,nargout=2)
# rao3.m:31
        xopt[gen,arange()]=x(ind,arange())
# rao3.m:32
        gen=gen + 1
# rao3.m:33

    
    val,ind=min(fopt,nargout=2)
# rao3.m:35
    Fes=dot(pop,ind)
# rao3.m:36
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
# rao3.m:41
    for i in arange(1,r).reshape(-1):
        y=0
# rao3.m:43
        for j in arange(1,c).reshape(-1):
            y=y + (x(i,j)) ** 2
# rao3.m:45
        z[i]=y
# rao3.m:47
    
    f=z.T
# rao3.m:49
    return f
    
if __name__ == '__main__':
    pass
    
    
@function
def updatepopulation(x=None,f=None,*args,**kwargs):
    varargin = updatepopulation.varargin
    nargin = updatepopulation.nargin

    row,col=size(x,nargout=2)
# rao3.m:52
    t,tindex=min(f,nargout=2)
# rao3.m:53
    Best=x(tindex,arange())
# rao3.m:54
    w,windex=max(f,nargout=2)
# rao3.m:55
    worst=x(windex,arange())
# rao3.m:56
    xnew=zeros(row,col)
# rao3.m:57
    for i in arange(1,row).reshape(-1):
        k=randi(row)
# rao3.m:59
        while (k == i):

            k=randi(row)
# rao3.m:61

        if (f(i) < f(k)):
            for j in arange(1,col).reshape(-1):
                r=rand(1,2)
# rao3.m:65
                xnew[i,j]=x(i,j) + dot(r(1),(Best(j) - abs(worst(j)))) + dot(r(2),(abs(x(i,j)) - x(k,j)))
# rao3.m:66
        else:
            for j in arange(1,col).reshape(-1):
                r=rand(1,2)
# rao3.m:70
                xnew[i,j]=x(i,j) + dot(r(1),(Best(j) - abs(worst(j)))) + dot(r(2),(abs(x(k,j)) - x(i,j)))
# rao3.m:71
    
    return xnew
    
if __name__ == '__main__':
    pass
    
    
@function
def trimr(mini=None,maxi=None,x=None,*args,**kwargs):
    varargin = trimr.varargin
    nargin = trimr.nargin

    row,col=size(x,nargout=2)
# rao3.m:77
    for i in arange(1,col).reshape(-1):
        x[x(arange(),i) < mini(i),i]=mini(i)
# rao3.m:79
        x[x(arange(),i) > maxi(i),i]=maxi(i)
# rao3.m:80
    
    z=copy(x)
# rao3.m:82
    return z
    
if __name__ == '__main__':
    pass
    