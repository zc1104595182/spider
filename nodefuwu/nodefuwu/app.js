var _ = require('koa-route');
var Koa = require('koa');

const {random,happy} =require('./util')
const {haha} = require("./wenshu");
const {jiasu} = require("./jiasu");
var app = new Koa();


var pets = {
    list: (ctx) => {
        var names = Object.keys(db);
        ctx.body = 'pets: ' + names.join(', ');
    },
    show: (ctx, name) => {
        var pet = db[name];
        if (!pet) return ctx.throw('cannot find that pet', 404);
        ctx.body = pet.name + ' is a ' + pet.species;
    },
    haha:(ctx)=>{
        ctx.body = haha();
    }
};





var wenshu = {
    random: (ctx, size) => {
        ctx.body = random(size)
    },
    happy: (ctx) => {
        ctx.body = happy()
    },
    haha:(ctx)=>{
        ctx.body = haha();
    },
};
app.use(_.get('/wenshu/random/:size',wenshu.random));
app.use(_.get('/wenshu/pageid',wenshu.happy));
app.use(_.get('/wenshu/ciphertext',wenshu.haha));

// app.use(_.get('/wenshu/jiasuText/:text1,text2,text3',wenshu.jiasu));

app.use(_.get('/wenshu/jiasuText', function (ctx, next) {
    const query = ctx.query
    // console.log(query)
    // jiasu(query)
    ctx.body = jiasu(query)

}));


app.use(_.get('/pets', pets.list));
app.use(_.get('/pets/:name', pets.show));
app.listen(30021);
console.log('listening on port 3000');
