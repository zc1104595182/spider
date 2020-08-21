var express = require('express')
var bodyParser = require("body-parser")
var api = express()
var sdk = require("./jiasule.js")
api.use(bodyParser.urlencoded({
    parameterLimit: 50000,
    limit: '50mb',
    extended: false
}));
api.post('/jiasule',function (req, res) {
    var content = req.body.content
    // console.log(content)
    // console.log(typeof content)
    var result = sdk.jiasule(content)
    res.send(result)

})
var servser = api.listen(6666,function () {

})
