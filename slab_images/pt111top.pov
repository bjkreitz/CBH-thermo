#include "colors.inc"
#include "finish.inc"

global_settings {assumed_gamma 1 max_trace_level 6}
background {color White transmit 1.0}
camera {perspective
  right -11.34*x up 5.68*y
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
atom(< -4.24,  -1.55,  -2.18>, 1.16, rgb <230.00, 230.00, 230.00>, 0.0, ase3) // #0
atom(< -1.41,  -1.55,  -2.18>, 1.16, rgb <230.00, 230.00, 230.00>, 0.0, ase3) // #1
atom(<  1.41,  -1.55,  -2.18>, 1.16, rgb <230.00, 230.00, 230.00>, 0.0, ase3) // #2
atom(< -2.83,  -0.91,  -4.55>, 1.16, rgb <230.00, 230.00, 230.00>, 0.0, ase3) // #3
atom(<  0.00,  -0.91,  -4.55>, 1.16, rgb <230.00, 230.00, 230.00>, 0.0, ase3) // #4
atom(<  2.83,  -0.91,  -4.55>, 1.16, rgb <230.00, 230.00, 230.00>, 0.0, ase3) // #5

// no constraints
