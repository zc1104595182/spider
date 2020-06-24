str1 = r"""var CryptoJS = require("crypto-js");
function getAesString(data,key){
    var srcs = CryptoJS.enc.Utf8.parse(data);
    var _key = CryptoJS.enc.Utf8.parse(key); //十六位十六进制数作为密钥
	var _iv = CryptoJS.enc.Utf8.parse('0000000000000000');

    var encrypted =CryptoJS.AES.encrypt(srcs,_key,
    {
            iv: _iv,
			mode: CryptoJS.mode.CBC,
			padding: CryptoJS.pad.Pkcs7

        });
    return encrypted.ciphertext;    //返回的是base64格式的密文
}


function getCiphertext(data,key){ //加密
    //var data='{"userresponse":"4c4444cc4c4c4ccc470","passtime":548,"imgload":14,"aa":"5-.02@DGmHFC8)-/-(!!Ex(((((**A(((O(ytt*ss(((t(!!(B89.:9:::?7@8:d?8:?8:@8$*8","ep":{"v":"6.0.9"},"rp":"0be21bb8e8ce275699e06f51385c4460"}'
    //var key  = 'ee76737313ef1918';
    var encrypted =getAesString(data,key); //密文
    var encrypted1 =CryptoJS.enc.Utf8.parse(encrypted);
    return encrypted;
}

function getD7W(shuzu,changdu) {
        var p2r = 0;
        for ( Z7W =shuzu,H7W =changdu,d7W = [], l7W = 0; p2r * (p2r + 1) * p2r % 2 == 0 && l7W < H7W; l7W++) {
        var q7W = Z7W[l7W >>> 2] >>> 24 - l7W % 4 * 8 & 255;
        d7W["push"](q7W);
        p2r = p2r > 33997 ? p2r / 5 : p2r * 5;
  }
        return d7W
    }

function get_Aes(o6B){
    var I9z = 3;
    var j6B='';
    var K6B='';
    var c6B =o6B["length"];
    var f6B = 0;
    while(f6B < c6B && I9z * (I9z + 1) % 2 + 3){
        var B6B
        if(f6B + 2 < c6B){
            B6B = (o6B[f6B] << 16) + (o6B[f6B + 1] << 8) + o6B[f6B + 2],
            j6B += Da(N6B(B6B, 7274496)) + Da(N6B(B6B, 9483264)) + Da(N6B(B6B, 19220)) + Da(N6B(B6B, 235));
            I9z = I9z > 53617 ? I9z - 7 : I9z + 7;
            f6B += 3;
        }
        else{
            var n6B = c6B % 3;
            2 === n6B ? (B6B = (o6B[f6B] << 16) + (o6B[f6B + 1] << 8),
            j6B += Da(N6B(B6B,7274496)) + Da(N6B(B6B,9483264)) + Da(N6B(B6B,19220)),K6B = ".") : 1 === n6B && (B6B = o6B[f6B] << 16,
            j6B += Da(N6B(B6B,7274496)) + Da(N6B(B6B,9483264)),K6B ="."+".");
            I9z = I9z > 53617 ? I9z - 7 : I9z + 7;
            f6B += 3;
        }

    }

    return j6B+K6B
}


function N6B(Q6B, x6B){
var I6B = 0,
v6B =23;
while(v6B>=0){
    1==Fa(x6B,v6B)&&(I6B = (I6B << 1) +Fa(Q6B,v6B));
    v6B -= 1;

}
return I6B

}

function Fa(R0B, C0B){
return R0B >> C0B & 1;
}

function Da(r0B){
var v9z = 1;
var h0B = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789()";
return (r0B < 0 || r0B >= h0B["length"]) && v9z * (v9z + 1) % 2 + 8 ? "." : h0B["charAt"](r0B)
}
"""