DM  "log;clear;output;clear;";
options nodate;

data a;

proc iml;

beta = {0.5 2 1.5 0.2};
observation=100;

start covariates(x,y,beta);
    * Generate covariates (x) and value (y) based on beta parameters;
    y = beta[1];
    do i = 1 to ncol(x);
      if (ranuni(0)>0.5) then x[i]=1;
      else x[i]=0;
      y = y + beta[i + 1] * x[i];
    end;
finish;

dataset= j(observation,4,.);
do i=1 to observation;
  x = j(1,(ncol(beta)-1),0);
  y = 0;
  call covariates(x,y,beta);
  do k = 1 to ncol(x);
    dataset[i,k] = x[k];
  end;
    dataset[i,(ncol(x) + 1)] = y;
end;

print dataset;
quit;



