# 一、IpAddressPoolMain.py
程序主入口，启动两个主线程持续调用
* service.IpService.testIp() 测试ip
* service.IpService.acquire() 获取ip
* service.IpService.deleteIp() 删除ip

# 二、service.IpService
* service.IpService.testIp() 测试ip
> * 启动一个线程，根据ip.IpVerify.py的测试规则测试并更新ip状态
* service.IpService.acquire() 获取ip
> * 调用ip.IpAcquire.acquireIp()请求一次代理提供商 获取ip
* service.IpService.deleteIp() 删除ip
> * 调用db.MongoDb.py删除标记过期的ip

# 三、ip
* Ip2Db.py 所有请求到的新ip在这里统一入库，可新增入库规则
* IpAcquire.py 请求并解析一次新ip，并调用Ip2Db.py入库
* IpVerify.py 提供ip的校验规则

# 四、db
* MongoDb.py 针对ip的db操作
* isValid=1表示ip有效

# 五、config
* SourceUrl.py ip提供商的url，可配置多个