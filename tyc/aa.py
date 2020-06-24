aa_str=r"""
function s6z(a){
var N5r = 9;
var Y6z, g6z, a6z, E6z = [], D6z = 0, P6z=[], J6z = 0, l6z = a["length"] - 1;
while(J6z<l6z && N5r * (N5r + 1) % 2 + 7){
Y6z=Math["round"](a[J6z+1][0]-a[J6z][0]),
g6z=Math["round"](a[J6z+1][1]-a[J6z][1]),
a6z=Math["round"](a[J6z+1][2]-a[J6z][2]),
P6z["push"]([Y6z, g6z, a6z])
0 == Y6z && 0 == g6z && 0 == a6z || (0 == Y6z && 0 == g6z ? D6z += a6z : (E6z["push"]([Y6z, g6z, a6z + D6z]),D6z = 0));
N5r = N5r > 34958 ? N5r / 6 : N5r * 6;
J6z++
	}
	return 0 !== D6z && E6z["push"]([Y6z, g6z, D6z]),E6z;
}


function u6z(a){
var f5r = 9;
var z6z = [[1, 0], [2, 0], [1, -1], [1, 1], [0, 1], [0, -1], [3, 0], [2, -1], [2, 1]],
h6z = 0,
C6z = z6z["length"]
c = "stuvwxyz~";
while(h6z < C6z && f5r * (f5r + 1) % 2 + 7){
if ( a[0] ==z6z[h6z][0] &&a[1] == z6z[h6z][1]){
      return c[h6z];
    } 
else{
	f5r = f5r >= 62252 ? f5r - 6 : f5r + 6;
    h6z++;
}
}
	return 0;
}





function O6z(a){
var d6z = "()*,-./0123456789:?@ABCDEFGHIJKLMNOPQRSTUVWXYZ_abcdefghijklmnopqr",
    m6z = d6z["length"],
    Z6z = "",
	H6z=Math["abs"](a),
	W6z = parseInt(H6z / m6z);
	W6z >= m6z && (W6z = m6z - 1),
	W6z && (Z6z = d6z["charAt"](W6z)),
	H6z %= m6z;
	var q6z ="";
	return a < 0 && (q6z += "!"),
	Z6z && (q6z += "$"),
	q6z + Z6z + d6z["charAt"](H6z)

}



function get_aa (z3O) {
  var o5r = 6;
  var N1z,X1z = s6z(z3O),
      f1z = [],
      B1z = [],
      o1z= [],
      t1z = 0,
      j1z = X1z["length"];
  while(o5r * (o5r + 1) % 2 + 8 && t1z < j1z){
      N1z = u6z(X1z[t1z]),
      N1z ? B1z["push"](N1z) : (f1z["push"](O6z(X1z[t1z][0])), 
	  B1z["push"](O6z(X1z[t1z][1]))),
      o1z.push(O6z(X1z[t1z][2]));
	  o5r = o5r >= 17705 ? o5r / 3 : o5r * 3;
	  t1z++;
  }
	  return f1z["join"]("") +"!!" + B1z["join"]("") + "!!" + o1z["join"]("");
}





 function get_Aa(Q1z, v1z, T1z){
		 var K5r = 2;
		var j5r = 4;
		 if ((!v1z || !T1z) && j5r * (j5r + 1) * j5r % 2 == 0){
			return Q1z;
		 }
		 else{
			var i1z, x1z = 0, c1z = Q1z, y1z = v1z[0], k1z = v1z[2], L1z = v1z[4];
			while((i1z = T1z["substr"](x1z, 2)) && K5r * (K5r + 1) * K5r % 2 == 0){
			x1z += 2;
			var n1z = parseInt(i1z, 16),
			M1z = String["fromCharCode"](n1z),
			I1z = (y1z * n1z * n1z + k1z * n1z + L1z) % Q1z["length"];
			c1z = c1z["substr"](0, I1z) + M1z + c1z["substr"](I1z);
			K5r = K5r > 10375 ? K5r / 8 : K5r * 8;
			}
			return c1z
		 }
 }
 
"""