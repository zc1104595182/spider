
function getJSL(x,y) {
    f=function(x,y){var a=0,b=0,c=0;x=x.split("");y=y||99;while((a=x.shift())&&(b=a.charCodeAt(0)-77.5))c=(Math.abs(b)<13?(b+48.5):parseInt(a,36))+y*c;return c}
    // console.log("aaaa")
    window = {}
    var z = f(y.match(/\w/g).sort(function(x, y) {
        return f(x) - f(y)
    }).pop());
    var data = "";
    var initZ = z;
    while (data.indexOf("document.cookie='__jsl") == -1 && z++-initZ < 20) {
        data = y.replace(/\b\w+\b/g, function(y) {
            return x[f(y, z) - 1] || ("_" + y)
        });
    };
    return eval(data.slice(data.indexOf("'__jsl_clearance"), data.indexOf("+';Expires")).replace(/document(.*?)toLowerCase\(\)/g, function(y) {
        return '"www.gsxt.gov.cn/"'
    }));
}

const jiasu = (query) => {
    canshu1 = query["callback"]
    canshu2= query["callback2"]
    clearance = getJSL(canshu1,canshu2)
    // console.log(clearance)
    return clearance
};
module.exports={jiasu}
