pro pick_a_flare

readcol,'/Users/james/research/flaremorph/gj1243_master_lc.dat',t,f,e

; pick the flare
x = where(t ge 549.725 and t le 549.97)

; zero it
f2 = (f[x] - median(f)) - 0.65d4

c1 = where(t[x] lt 549.75)
c2 = where(t[x] gt 549.96)
c = [c1,c2]

fit = poly_fit(t[x[c]], f[x[c]], 1)

f2 = f[x] - poly(t[x], fit)

; dump the flare to text file
forprint, t[x], f2-min(f2), textout='davenport_flare1.txt', f='(D,D)', /nocomm



x2 = where(t ge 1130.1 and t le 1132.1)
forprint, t[x2], f[x2], /nocomm, textout='davenport_lcsample.txt',f='(D,D)'

stop
end
