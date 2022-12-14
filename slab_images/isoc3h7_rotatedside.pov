#include "colors.inc"
#include "finish.inc"

global_settings {assumed_gamma 1 max_trace_level 6}
background {color White transmit 1.0}
camera {perspective
  right -9.28*x up 8.26*y
  direction 100.00*z
  location <0,0,100.00> look_at <0,0,0>}


light_source {<  2.00,   3.00,  40.00> color White
  area_light <0.70, 0, 0>, <0, 0.70, 0>, 3, 3
  adaptive 1 jitter}
// no fog
#declare simple = finish {phong 0.7}
#declare pale = finish {ambient 0.5 diffuse 0.85 roughness 0.001 specular 0.200 }
#declare intermediate = finish {ambient 0.3 diffuse 0.6 specular 0.1 roughness 0.04}
#declare vmd = finish {ambient 0.0 diffuse 0.65 phong 0.1 phong_size 40.0 specular 0.5 }
#declare jmol = finish {ambient 0.2 diffuse 0.6 specular 1 roughness 0.001 metallic}
#declare ase2 = finish {ambient 0.05 brilliance 3 diffuse 0.6 metallic specular 0.7 roughness 0.04 reflection 0.15}
#declare ase3 = finish {ambient 0.15 brilliance 2 diffuse 0.6 metallic specular 1.0 roughness 0.001 reflection 0.0}
#declare glass = finish {ambient 0.05 diffuse 0.3 specular 1.0 roughness 0.001}
#declare glass2 = finish {ambient 0.01 diffuse 0.3 specular 1.0 reflection 0.25 roughness 0.001}
#declare Rcell = 0.050;
#declare Rbond = 0.100;

#macro atom(LOC, R, COL, TRANS, FIN)
  sphere{LOC, R texture{pigment{color COL transmit TRANS} finish{FIN}}}
#end
#macro constrain(LOC, R, COL, TRANS FIN)
union{torus{R, Rcell rotate 45*z texture{pigment{color COL transmit TRANS} finish{FIN}}}
     torus{R, Rcell rotate -45*z texture{pigment{color COL transmit TRANS} finish{FIN}}}
     translate LOC}
#end

// no cell vertices
atom(< -1.63,  -2.78,  -8.49>, 1.16, rgb <0.82, 0.82, 0.88>, 0.0, ase3) // #0
atom(< -1.63,  -2.78,  -5.66>, 1.16, rgb <0.82, 0.82, 0.88>, 0.0, ase3) // #1
atom(< -1.63,  -2.77,  -2.83>, 1.16, rgb <0.82, 0.82, 0.88>, 0.0, ase3) // #2
atom(<  0.82,  -2.77,  -7.07>, 1.16, rgb <0.82, 0.82, 0.88>, 0.0, ase3) // #3
atom(<  0.83,  -2.73,  -4.23>, 1.16, rgb <0.82, 0.82, 0.88>, 0.0, ase3) // #4
atom(<  0.83,  -2.72,  -1.44>, 1.16, rgb <0.82, 0.82, 0.88>, 0.0, ase3) // #5
atom(<  3.27,  -2.77,  -5.66>, 1.16, rgb <0.82, 0.82, 0.88>, 0.0, ase3) // #6
atom(<  3.24,  -2.73,  -2.83>, 1.16, rgb <0.82, 0.82, 0.88>, 0.0, ase3) // #7
atom(<  3.26,  -2.77,  -0.00>, 1.16, rgb <0.82, 0.82, 0.88>, 0.0, ase3) // #8
atom(< -3.26,  -0.45,  -8.48>, 1.16, rgb <0.82, 0.82, 0.88>, 0.0, ase3) // #9
atom(< -3.26,  -0.46,  -5.66>, 1.16, rgb <0.82, 0.82, 0.88>, 0.0, ase3) // #10
atom(< -3.27,  -0.45,  -2.83>, 1.16, rgb <0.82, 0.82, 0.88>, 0.0, ase3) // #11
atom(< -0.81,  -0.45,  -7.07>, 1.16, rgb <0.82, 0.82, 0.88>, 0.0, ase3) // #12
atom(< -0.81,  -0.46,  -4.25>, 1.16, rgb <0.82, 0.82, 0.88>, 0.0, ase3) // #13
atom(< -0.81,  -0.46,  -1.41>, 1.16, rgb <0.82, 0.82, 0.88>, 0.0, ase3) // #14
atom(<  1.63,  -0.45,  -5.66>, 1.16, rgb <0.82, 0.82, 0.88>, 0.0, ase3) // #15
atom(<  1.63,  -0.15,  -2.83>, 1.16, rgb <0.82, 0.82, 0.88>, 0.0, ase3) // #16
atom(<  1.63,  -0.44,   0.00>, 1.16, rgb <0.82, 0.82, 0.88>, 0.0, ase3) // #17
atom(<  1.49,   2.58,  -3.79>, 0.65, rgb <0.56, 0.56, 0.56>, 0.0, ase3) // #18
atom(<  1.98,   1.98,  -2.48>, 0.65, rgb <0.56, 0.56, 0.56>, 0.0, ase3) // #19
atom(<  1.29,   2.59,  -1.27>, 0.65, rgb <0.56, 0.56, 0.56>, 0.0, ase3) // #20
atom(<  2.04,   2.21,  -4.66>, 0.26, rgb <1.00, 1.00, 1.00>, 0.0, ase3) // #21
atom(<  0.42,   2.40,  -3.95>, 0.26, rgb <1.00, 1.00, 1.00>, 0.0, ase3) // #22
atom(<  1.63,   3.67,  -3.75>, 0.26, rgb <1.00, 1.00, 1.00>, 0.0, ase3) // #23
atom(<  3.06,   2.10,  -2.40>, 0.26, rgb <1.00, 1.00, 1.00>, 0.0, ase3) // #24
atom(<  1.67,   2.19,  -0.33>, 0.26, rgb <1.00, 1.00, 1.00>, 0.0, ase3) // #25
atom(<  1.48,   3.67,  -1.27>, 0.26, rgb <1.00, 1.00, 1.00>, 0.0, ase3) // #26
atom(<  0.21,   2.45,  -1.30>, 0.26, rgb <1.00, 1.00, 1.00>, 0.0, ase3) // #27

// no constraints
