user_response_str=r"""
function get_userresponse (L0z,o0z){
	 var g4r = 6;
	 var Y4r = 7;
	 var F4r = 3;
	 //var j0z=o0z["slice"](32),
	 var j0z=o0z.substring(o0z.length-2,o0z.length);
	 c0z = [],
	 X0z = 0;
	 while(X0z < j0z["length"] && F4r * (F4r + 1) % 2 + 6){
	 var K0z = j0z["charCodeAt"](X0z);
	 c0z[X0z] = K0z > 57 ? K0z - 87 : K0z - 48;
	 F4r = F4r >= 10020 ? F4r / 5 : F4r * 5;
	 X0z++;
	 }
	 j0z = 36 * c0z[0] + c0z[1];
	 var k0z = Math["round"](L0z) + j0z;
	 o0z = o0z["slice"](0, 32);
	 var n0z, f0z = [[], [], [], [], []], Q0z = {}, N0z = 0;
	 X0z = 0;
	 var i0z = o0z["length"]
	 while( X0z < i0z && Y4r * (Y4r + 1) * Y4r % 2 == 0){
	 n0z = o0z["charAt"](X0z),
	 Q0z[n0z] || (Q0z[n0z] = 1,
	 f0z[N0z]["push"](n0z),
	 N0z++,
	 N0z = 5 == N0z ? 0 : N0z);
     Y4r = Y4r >= 19614 ? Y4r / 7 : Y4r * 7;
	 X0z++;
	 }
	 var y0z, v0z = k0z, B0z = 4, x0z ="", I0z = [1, 2, 5, 10, 50];
	 while(v0z > 0 && g4r * (g4r + 1) * g4r % 2 == 0){
	 v0z - I0z[B0z] >= 0 ? (y0z = parseInt(Math["random"]() * f0z[B0z]["length"], 10),
	 x0z += f0z[B0z][y0z],
	 v0z -= I0z[B0z]) : (f0z["splice"](B0z, 1),
	 I0z["splice"](B0z, 1),
     B0z -= 1);
	 g4r = g4r > 32264 ? g4r / 5 : g4r * 5;
	 }
	 return x0z
}
"""