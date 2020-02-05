# Generated with SMOP  0.41
from libsmop import *
# rao2.m

    
@function
def Rao2(*args,**kwargs):
    varargin = Rao2.varargin
    nargin = Rao2.nargin

    clc
    pop=10
# rao2.m:4
    
    var=30
# rao2.m:5
    
    maxFes=30000
# rao2.m:6
    
    maxGen=floor(maxFes / pop)
# rao2.m:7
    
    mini=dot(- 100,ones(1,var))
# rao2.m:8
    maxi=dot(100,ones(1,var))
# rao2.m:9
    row,var=size(mini,nargout=2)
# rao2.m:10
    x=zeros(pop,var)
# rao2.m:11
    for i in arange(1,var).reshape(-1):
        x[arange(),i]=mini(i) + dot((maxi(i) - mini(i)),rand(pop,1))
# rao2.m:13
    
    f=objective(x)
# rao2.m:15
    gen=1
# rao2.m:16
    while (gen <= maxGen):

        xnew=updatepopulation(x,f)
# rao2.m:18
        xnew=trimr(mini,maxi,xnew)
# rao2.m:19
        fnew=objective(xnew)
# rao2.m:20
        for i in arange(1,pop).reshape(-1):
            if (fnew(i) < f(i)):
                x[i,arange()]=xnew(i,arange())
# rao2.m:23
                f[i]=fnew(i)
# rao2.m:24
        disp(concat(['Iteration No. = ',num2str(gen)]))
        128
        disp('%%%%%%%% Final population %%%%%%%%%')
        disp(concat([x,f]))
        fnew=[]
# rao2.m:32
        xnew=[]
# rao2.m:32
        fopt(gen),ind=min(f,nargout=2)
# rao2.m:33
        xopt[gen,arange()]=x(ind,arange())
# rao2.m:34
        gen=gen + 1
# rao2.m:35

    
    val,ind=min(fopt,nargout=2)
# rao2.m:37
    Fes=dot(pop,ind)
# rao2.m:38
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
# rao2.m:44
    for i in arange(1,r).reshape(-1):
        y=0
# rao2.m:46
        for j in arange(1,c).reshape(-1):
            y=y + (x(i,j)) ** 2
# rao2.m:48
        z[i]=y
# rao2.m:50
    
    f=z.T
# rao2.m:52
    return f
    
if __name__ == '__main__':
    pass
    
    
@function
def updatepopulation(x=None,f=None,*args,**kwargs):
    varargin = updatepopulation.varargin
    nargin = updatepopulation.nargin

    row,col=size(x,nargout=2)
# rao2.m:55
    t,tindex=min(f,nargout=2)
# rao2.m:56
    Best=x(tindex,arange())
# rao2.m:57
    w,windex=max(f,nargout=2)
# rao2.m:58
    worst=x(windex,arange())
# rao2.m:59
    xnew=zeros(row,col)
# rao2.m:60
    for i in arange(1,row).reshape(-1):
        k=randi(row)
# rao2.m:62
        while (k == i):

            k=randi(row)
# rao2.m:64

        if (f(i) < f(k)):
            for j in arange(1,col).reshape(-1):
                r=rand(1,2)
# rao2.m:68
                xnew[i,j]=x(i,j) + dot(r(1),(Best(j) - worst(j))) + dot(r(2),(abs(x(i,j)) - abs(x(k,j))))
# rao2.m:69
        else:
            for j in arange(1,col).reshape(-1):
                r=rand(1,2)
# rao2.m:73
                xnew[i,j]=x(i,j) + dot(r(1),(Best(j) - worst(j))) + dot(r(2),(abs(x(k,j)) - abs(x(i,j))))
# rao2.m:74
    
    return xnew
    
if __name__ == '__main__':
    pass
    
    
@function
def trimr(mini=None,maxi=None,x=None,*args,**kwargs):
    varargin = trimr.varargin
    nargin = trimr.nargin

    row,col=size(x,nargout=2)
# rao2.m:80
    for i in arange(1,col).reshape(-1):
        x[x(arange(),i) < mini(i),i]=mini(i)
# rao2.m:82
        x[x(arange(),i) > maxi(i),i]=maxi(i)
# rao2.m:84
    
    z=copy(x)
# rao2.m:86
    return z
    
if __name__ == '__main__':
    pass
    