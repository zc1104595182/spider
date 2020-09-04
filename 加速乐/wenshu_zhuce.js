const timetrans = (date, dayOrTime) => {
    if (!date) {
        return ''
    }
    var _date = new Date(date);//如果date为13位不需要乘1000
    var Y = _date.getFullYear() + '-';
    var M = (_date.getMonth() + 1 < 10 ? '0' + (_date.getMonth() + 1) : _date.getMonth() + 1) + '-';
    var D = (_date.getDate() < 10 ? '0' + (_date.getDate()) : _date.getDate());
    var h = (_date.getHours() < 10 ? '0' + _date.getHours() : _date.getHours()) + ':';
    var m = (_date.getMinutes() < 10 ? '0' + _date.getMinutes() : _date.getMinutes());
    var s = ':' + (_date.getSeconds() < 10 ? '0' + _date.getSeconds() : _date.getSeconds());
    if (dayOrTime === 'day') {
        return Y + M + D;
    } else if (dayOrTime === 'time') {
        return h + m + s;
    } else if (dayOrTime === 'timeHM') {
        return h + m;
    } else {
        return Y + M + D + " " + h + m + s;
    }
}
var CryptoJS = require('crypto-js');
var DES3 = {
    iv: function() {
        return timetrans(new Date(),'day').replace(/-/g,'')
    },
    encrypt: function(b, c, a) {
        if (c) {
            return (CryptoJS.TripleDES.encrypt(b, CryptoJS.enc.Utf8.parse(c), {
                iv: CryptoJS.enc.Utf8.parse(a || DES3.iv()),
                mode: CryptoJS.mode.CBC,
                padding: CryptoJS.pad.Pkcs7
            })).toString()
        }
        return ""
    },
    decrypt: function(b, c, a) {
        if (c) {
            return CryptoJS.enc.Utf8.stringify(CryptoJS.TripleDES.decrypt(b, CryptoJS.enc.Utf8.parse(c), {
                iv: CryptoJS.enc.Utf8.parse(a || DES3.iv()),
                mode: CryptoJS.mode.CBC,
                padding: CryptoJS.pad.Pkcs7
            })).toString()
        }
        return ""
    }
};
function deal_password(val) {
    return DES3.encrypt(val, "sL9p4mS2mSVTSBzWn4p16Mu7");
}
module.exports = {
    deal_password,

}