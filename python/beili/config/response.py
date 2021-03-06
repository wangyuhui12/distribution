# *- coding:utf8 *-
# from common.base_error import BaseError

"""
class PARAMS_MISS(BaseError):
    status = 405
    status_code = 405001
    message = '参数缺失'

class PARAMS_ERROR(BaseError):
    status = 405
    status_code = 405001
    message = '参数错误'

class PARAMS_REDUNDANCE(BaseError):
    status= 405
    status_code= 405003
    message= "参数冗余"


class TOKEN_ERROR(BaseError):
    status = 405
    status_code = 405001
    message = "未登录"


class MethodNotAllowed(BaseError):
    status = 405
    status_code = 405002
    message = "方法不支持"


class AUTHORITY_ERROR(BaseError):
    status = 405
    status_code = 405001
    message = "无权限"


class SYSTEM_ERROR(BaseError):
    status_code = 200
    message = '系统错误'
    status = 404

class NOT_FOUND(BaseError):
    status_code = 200
    message = '对象不存在'
    status = 404

class APIS_WRONG(BaseError):
    status = 405
    status_code = 405002
    message = "接口未注册"


class TIME_ERROR(BaseError):
    status = 405
    status_code = 405003
    message = "敬请期待"


class NETWORK_ERROR(BaseError):
    status = 405
    status_code = 405004
    message = '网络异常'
"""
PARAMS_MISS = {
    "status": 405,
    "status_code": 405001,
    "message": "参数缺失"
}
NO_PHONENUM_OR_PASSWORD = {
    "status": 405,
    "status_code": 405001,
    "message": "请输入账户名或密码"
}
PARAMS_ERROR = {
    "status": 405,
    "status_code": 405002,
    "message": "参数错误"
}
TOKEN_ERROR = {
    "status": 405,
    "status_code": 405003,
    "message": "token错误"
}
SYSTEM_ERROR = {
    "status": 404,
    "status_code": 404001,
    "message": "系统错误"
}
AUTHORITY_ERROR = {
    "status": 405,
    "status_code": 405004,
    "message": "没有权限"
}
NOT_FOUND_PHONENUM = {
    "status": 405,
    "status_code": 405005,
    "message": "没有找到该号码信息"
}
PHONE_OR_PASSWORD_WRONG = {
    "status": 405,
    "status_code": 405006,
    "message": "手机或密码错误"
}
NOT_FOUND_IMAGE = {
    "status": 405,
    "status_code": 405007,
    "message": "图片未找到"
}
PASSWORD_WRONG = {
    "status": 405,
    "status_code": 405008,
    "message": "密码错误"
}
NOT_FOUND_USER = {
    "status": 405,
    "status_code": 405009,
    "message": "未找到该用户"
}
NO_ADDRESS = {
    "status": 405,
    "status_code": 405010,
    "message": "未找到地址"
}
INFORCODE_WRONG = {
    "status": 405,
    "status_code": 405011,
    "message": "验证码错误"
}
NOT_FOUND_ADDRESS = {
    "status": 405,
    "status_code": 405012,
    "message": "未找到收货地址"
}
BAD_ADDRESS = {
    "status": 405,
    "status_code": 405013,
    "message": "无效的地址代号"
}
NO_THIS_CATEGORY = {
    "status": 405,
    "status_code": 405014,
    "message": "没有此分类"
}
UPDATE_ADDRESS_FAIL = {
    "status": 405,
    "status_code": 405015,
    "message": "更新地址失败"
}
CHANGE_ADDRESS_FAIL = {
    "status": 405,
    "status_code": 405016,
    "message": "切换地址失败"
}
STOCK_NOT_ENOUGH = {
    "status": 405,
    "status_code": 405017,
    "message": "商品库存不足"
}
NO_ENOUGH_MOUNT = {
    "status": 405,
    "status_code": 405018,
    "message": "账户余额不足"
}
NO_BAIL = {
    "status": 405,
    "status_code": 405019,
    "message": "未缴纳保证金"
}
PRlogisticsfee_WRONG = {
    "status": 405,
    "status_code": 405020,
    "message": "运费金额核对出错"
}
TOTAL_PRICE_WRONG = {
    "status": 405,
    "status_code": 405021,
    "message": "商品总价核对出错"
}
NOT_FOUND_FILE = {
    "status": 405,
    "status_code": 405022,
    "message": "图片未找到"
}