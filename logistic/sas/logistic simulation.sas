DM  "log;clear;output;clear;";
options nodate;

data a;

proc iml;

beta0=0.5;
beta1=2;
beta2=1.5;
beta3=0.2;
observation=100;

start covariates(x,y);
    if (ranuni(0)>0.5) then x[1]=1; else x[1]=0;
    if (ranuni(0)>0.5) then x[2]=1; else x[2]=0;
    if (ranuni(0)>0.5) then x[3]=1; else x[3]=0;
    y=beta0+beta1*x[1]+beta2*x[2]+beta3*x[3];
finish;

dataset= j(observation,4,.);
 do i=1 to observation;
 
           x = j(1,3,0);
           y = 0;
           call covariates(x1,x2,x3,y);
           dataset=[i,1]=x1;
           dataset=[i,2]=x2;
           dataset=[i,3]=x3;
           dataset=[i,4]=y;
 end;

quit;



