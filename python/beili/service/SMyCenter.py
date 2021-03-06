# *- coding:utf8 *-
import sys
import os
import uuid
from werkzeug.security import check_password_hash
from service.SBase import SBase, close_session
from models.model import User, IdentifyingCode, Province, City, Area, UserAddress
sys.path.append(os.path.dirname(os.getcwd()))


class SMyCenter(SBase):

    @close_session
    def get_uptime_by_usphonenum(self, usphonenum):
        return self.session.query(IdentifyingCode.ICtime).filter_by(ICphonenum=usphonenum) \
            .order_by(IdentifyingCode.ICtime.desc()).first()

    @close_session
    def update_user_by_uid(self, uid, users):
        self.session.query(User).filter_by(USid=uid).update(users)

    @close_session
    def get_inforcode_by_usphonenum(self, phonenum):
        return self.session.query(IdentifyingCode.ICcode).filter_by(ICphonenum=phonenum).order_by( \
            IdentifyingCode.ICtime.desc()).first()

    @close_session
    def add_inforcode(self, usphonenum, code, time):
        new_infocode = IdentifyingCode()
        new_infocode.ICid = str(uuid.uuid1())
        new_infocode.ICphonenum = usphonenum
        new_infocode.ICcode = code
        new_infocode.ICtime = time
        self.session.add(new_infocode)
        self.session.commit()
        self.session.close()
        return True

    @close_session
    def get_user_basicinfo(self, usid):
        return self.session.query(User.USphonenum, User.USmount, User.USbail, User.USheadimg, User.USname,\
                                  User.subscribe, User.USpre).filter_by(USid=usid).first()

    @close_session
    def get_user_totalinfo(self, usid):
        return self.session.query(User.USphonenum, User.USmount, User.USbail, User.USheadimg, User.USname, \
                                  User.subscribe, User.USpre, User.unionid, User.openid,\
                                  User.accesstoken).filter_by(USid=usid).first()

    @close_session
    def get_province(self):
        return self.session.query(Province.provincename, Province.provinceid).all()

    @close_session
    def get_city_by_provincenum(self, provinceid):
        return self.session.query(City.cityname, City.provinceid, City.cityid).filter_by(provinceid=provinceid).all()

    @close_session
    def get_area_by_citynum(self, cityid):
        return self.session.query(Area.cityid, Area.areaname, Area.areaid).filter_by(cityid=cityid).all()

    @close_session
    def get_all_address(self, usid):
        return self.session.query(UserAddress.UAdefault, UserAddress.UAid, UserAddress.cityid\
                                  , UserAddress.UAname, UserAddress.UAcreatetime, UserAddress.UAphonenum\
                                  , UserAddress.UAdetails, UserAddress.areaid).filter(UserAddress.USid == usid)\
                                  .filter(UserAddress.UAstatus == 1).all()

    @close_session
    def get_default_address_by_usid(self, usid):
        """获取默认地址"""
        return self.session.query(UserAddress.UAid, UserAddress.USid) \
            .filter_by(USid=usid, UAdefault=True, UAstatus=True).first()

    @close_session
    def add_address(self, uaid, usid, usname, usphonenum, usdetails, areaid, uadefault, createtime, cityid):
        """添加地址地址"""
        address = UserAddress()
        address.UAid = uaid
        address.USid = usid
        address.UAname = usname
        address.UAphonenum = usphonenum
        address.UAdetails = usdetails
        address.areaid = areaid
        address.UAdefault = uadefault
        address.UAcreatetime = createtime
        address.cityid = cityid
        self.session.add(address)

    @close_session
    def get_default_address(self, usid):
        return self.session.query(UserAddress.UAdefault, UserAddress.UAid, UserAddress.cityid\
                                  , UserAddress.UAname, UserAddress.UAcreatetime, UserAddress.UAphonenum\
                                  , UserAddress.UAdetails, UserAddress.areaid).filter(UserAddress.USid == usid)\
                                  .filter(UserAddress.UAdefault == 1).filter(UserAddress.UAstatus == 1).first()

    @close_session
    def get_other_address(self, usid, uaid):
        return self.session.query(UserAddress.UAdefault, UserAddress.UAid, UserAddress.cityid\
                                  , UserAddress.UAname, UserAddress.UAcreatetime, UserAddress.UAphonenum \
                                  , UserAddress.UAdetails, UserAddress.areaid).filter(UserAddress.USid == usid) \
            .filter(UserAddress.UAid == uaid).filter(UserAddress.UAstatus == 1).first()

    @close_session
    def update_address(self, id, UAid, update):
        return self.session.query(UserAddress).filter_by(USid=id).filter_by(UAid=UAid).update(update)

    @close_session
    def change_default(self, usid, oldid, newid):
        old = {}
        old['UAdefault'] = False
        result1 = self.session.query(UserAddress).filter_by(USid=usid).filter_by(UAid=oldid).update(old)
        if result1:
            new = {}
            new['UAdefault'] = True
            result2 = self.session.query(UserAddress).filter_by(USid=usid).filter_by(UAid=newid).update(new)
        if result1 == result2 == 1:
            return True

    @close_session
    def delete_useraddress(self, id, uaid, address):
        return self.session.query(UserAddress).filter_by(USid=id).filter_by(UAid=uaid).update(address)

    @close_session
    def get_one_address(self):
        return self.session.query(UserAddress.UAid).filter(UserAddress.UAstatus == 1).first()

    @close_session
    def set_default(self, uaid, update_address):
        self.session.query(UserAddress).filter_by(UAid=uaid).update(update_address)

    @close_session
    def get_area_by_areaid(self, areaid):
        return self.session.query(Area.areaname, Area.areaid, Area.cityid).filter(Area.areaid == areaid).first()

    @close_session
    def get_all_areaid(self):
        return self.session.query(Area.areaid).all()

    @close_session
    def get_all_cityid(self):
        return self.session.query(City.cityid).all()

    @close_session
    def get_city_by_cityid(self, cityid):
        return self.session.query(City.cityname, City.cityid, City.cityname, City.provinceid).filter(City.cityid == cityid).first()

    @close_session
    def get_province_by_provinceid(self, provinceid):
        return self.session.query(Province.provincename, Province.provinceid).filter(Province.provinceid == provinceid).first()