const randomArr = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'];
const randomArrLen = randomArr.length;
 const happy=()=> {
    var guid = "";
    for (let i = 1; i <= 32; i++) {
        let n = Math.floor(Math.random() * 16.0).toString(16);
        guid += n;
    }
    return guid;
};
 const random= (size)=> {
    let str = "";
    for (var i = 0; i < size; i++) {
        str += randomArr[Math.round(Math.random() * (randomArrLen - 1))];
    }
    return str;
}
module.exports={happy,random}
