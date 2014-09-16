pro pick_a_flare

readcol,'/Users/james/research/flaremorph/gj1243_master_lc.dat',t,f,e

; pick the flare
x = where(t ge 549.725 and t le 549.965)

; zero it
f2 = (f[x] - median(f)) / median(f) - 0.025

; dump the flare to text file
forprint, t[x], f2, textout='davenport_flare1.txt', f='(D,D)', /nocomm


stop
end
