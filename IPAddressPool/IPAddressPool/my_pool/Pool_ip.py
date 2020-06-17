from db.DBInterface import DBInterface

from ip.IpVerify import testBaidu

# tyc_ip = DBInterface(col="tyc_ip", input_verify=test_tyc, forVerify=testBaidu, describe="天眼查")

pools = [
    # DBInterface(col="qcc_m_ip", input_verify=test_qccM, forVerify=testBaidu, describe='企查查m端'),
    DBInterface(col="ip_poolCeshi", input_verify=testBaidu, forVerify=testBaidu, describe='百度'),
    # DBInterface(col="wusong_ip", input_verify=wusong, forVerify=testBaidu, describe='无讼'),
    # DBInterface(col="zhigaodian_ip", input_verify=zhigaodian, forVerify=testBaidu, describe='制高点'),
    # DBInterface(col="zhuanli_ip", input_verify=testZhuanli, forVerify=testBaidu, describe='专利'),

]
