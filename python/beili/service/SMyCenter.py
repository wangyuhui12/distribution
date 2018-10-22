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
        return self.session.query(IdentifyingCode).filter_by(ICphonenum=phonenum).order_by( \
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
    def get_province(self):
        return self.session.query(Province.id, Province.name, Province.provinceid).all()

    @close_session
    def get_city_by_provincenum(self, provinceid):
        return self.session.query(City.name, City.provinceid, City.id, City.cityid).filter_by(provinceid=provinceid).all()

    @close_session
    def get_area_by_citynum(self, cityid):
        return self.session.query(Area.id, Area.cityid, Area.name, Area.areaid).filter_by(cityid=cityid).all()

    @close_session
    def get_default_address_by_usid(self, usid):
        """获取默认地址"""
        return self.session.query(UserAddress.UAid, UserAddress.USid) \
            .filter_by(USid=usid, UAdefault=True, UAstatus=False).first()

    @close_session
    def add_address(self, uaid, usid, usname, usphonenum, usdetails, areaid, uadefault):
        """添加地址地址"""
        address = UserAddress()
        address.UAid = uaid
        address.USid = usid
        address.UAname = usname
        address.UAphonenum = usphonenum
        address.UAdetails = usdetails
        address.areaid = areaid
        address.UAdefault = uadefault
        self.session.add(address)

    @close_session
    def get_address(self, usid):
        return self.session.query(UserAddress.UAdefault, UserAddress.UAid\
                                  , UserAddress.UAname, UserAddress.UAcreatetime, UserAddress.UAphonenum\
                                  , UserAddress.UAdetails).filter(UserAddress.USid == usid).first()


    @close_session
    def get_addressinfo_by_areaid(self, areaid):
        return self.session.query(Area.name, City.name, Province.name).filter(Area.cityid == City.cityid\
                                  , City.provinceid == Province.provinceid).filter(Area.areaid == areaid).all()