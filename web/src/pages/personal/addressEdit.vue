<style lang="less" scoped>
    @import "../../common/css/index";

    .container {
        .least-full-screen();

        .form-wrap {
            margin-top: 19px;

        }

        .city-picker-popup {
            width: 100%;

            .city-picker-toolbar {
                .fj();
                padding: 10px 30px;

                button {
                    .bgw();
                    .sc(38px, #26b83a);

                    &.cancel-btn {
                        color: @lightFontColor;
                    }
                }
            }
        }
    }
</style>

<template>
    <div class="container">
        <header-top :title="isAdd ? '新增地址': ''" :show-back="true"></header-top>

        <section class="form-wrap">
            <mt-field label="收件人" v-model.trim="formData.USname" placeholder="请输入收件人姓名"></mt-field>
            <mt-field label="手机号" type="tel" v-model.trim="formData.USphonenum" placeholder="请输入手机号"></mt-field>
            <mt-field label="省市区" placeholder="请选择省市区" v-model="city" :readonly="true"
                      :disableClear="true" @click.native="showCityPopup">
                <img src="/static/images/arrow_down.png" style="width: 16px;height: 14px;" alt="">
            </mt-field>
            <mt-field label="详细地址" v-model.trim="formData.details" placeholder="请输入详细地址"></mt-field>
            <!--<mt-field label="邮政编码" placeholder="请输入邮政编码"></mt-field>-->
            <!--<mt-field label="设为默认地址" placeholder="" :readonly="true">-->
                <!--<mt-switch v-model="isDefault"></mt-switch>-->
            <!--</mt-field>-->

        </section>

        <section class="my-confirm-btn-wrap">
            <button class="my-confirm-btn" @click="saveAddress">保 存</button>
        </section>


        <mt-popup class="city-picker-popup" position="bottom" v-model="cityPopupVisible">
            <mt-picker :slots="slots" defaultIndex="2" valueKey="name" @change="onValuesChange" :showToolbar="true">
                <section class="city-picker-toolbar">
                    <button class="cancel-btn" @click="cityPopupVisible= false">取消</button>
                    <button @click="confirmPickArea">确认</button>
                </section>
            </mt-picker>
        </mt-popup>
    </div>
</template>

<script>
    import {getAllArea,addUserAddress,updateUserAddress} from "src/api/api"
    import {getStore, setStore} from "src/common/js/mUtils"
    import common from "src/common/js/common"
    import {ALL_AREA} from "src/common/js/const"


    export default {
        name: "addressEdit",

        data() {
            return {
                isAdd: true,    //  是否为新增地址
                isDefault: false,

                formData: {
                    USname: '',
                    USphonenum: '',
                    areaid: '',
                    details: ''
                },

                city: '',
                cityPopupVisible: false,
                allArea: [],
                slots: [
                    {
                        flex: 1,
                        values: [],
                        className: 'slot1',
                        textAlign: 'center'
                    }, {
                        divider: true,
                        content: '-',
                        className: 'slot2'
                    }, {
                        flex: 1,
                        values: [],
                        className: 'slot3',
                        textAlign: 'center'
                    }
                    , {
                        divider: true,
                        content: '-',
                        className: 'slot4'
                    }, {
                        flex: 1,
                        values: [],
                        className: 'slot5',
                        textAlign: 'center'
                    }
                ],
                pickAreaVal: []
            }
        },

        components: {},

        computed: {},

        methods: {
            onValuesChange(picker, values) {
                if (!values[0] || !this.allArea.length) {
                    return
                }
                //  数据没拿到
                let pickProvince = this.allArea.find(item => item.id == values[0].id);

                if (pickProvince) {
                    let citys = pickProvince.city.map(item => {
                        return {
                            id: item.id,
                            name: item.name,
                            area: item.area
                        }
                    })
                    picker.setSlotValues(1, citys);

                    if (values[1]) {
                        let pickCity = citys.find(item => item.id == values[1].id);

                        if (pickCity) {
                            picker.setSlotValues(2, pickCity.area)

                            this.pickAreaVal = values;
                        }
                    }
                }
            },
            confirmPickArea() {
                if (this.pickAreaVal[2] && this.pickAreaVal[2].id) {
                    this.formData.areaid = this.pickAreaVal[2].id;
                    this.city = this.pickAreaVal[0].name + ' ' + this.pickAreaVal[1].name + ' ' + this.pickAreaVal[2].name;
                    this.cityPopupVisible = false;
                }
            },
            initCityPicker(){
                this.allArea = JSON.parse(getStore(ALL_AREA));
                this.slots[0].values = this.allArea.map(item => {
                    return {
                        id: item.id,
                        name: item.name,
                    }
                });
                this.slots[2].values = this.allArea[0].city.map(item => {
                    return {
                        id: item.id,
                        name: item.name,
                    }
                });
                this.slots[4].values = this.allArea[0].city[0].area;
            },
            showCityPopup() {
                setTimeout(() => {
                    this.cityPopupVisible = true
                }, 300)
            },
            formDataCheck(){
                if(!this.formData.USname){
                    return '请输入收件人';
                }
                if(!this.formData.USphonenum){
                    return '请输入手机号';
                }
                if(!this.formData.areaid){
                    return '请选择省市县';
                }
                if(!this.formData.details){
                    return '请输入详细地址';
                }

            },
            saveAddress() {
                let checkMsg = this.formDataCheck();

                if(checkMsg){
                    this.$toast(checkMsg);
                    return;
                }else{
                    let {USname, USphonenum, areaid, details} = this.formData;

                    if(this.isAdd){
                        addUserAddress(USname,USphonenum,details,areaid).then(
                            data => {
                                this.$toast('新增地址成功');
                                this.$router.back();
                            }
                    )
                    }else{

                    }
                }
            }
        },

        created() {
            this.initCityPicker();
            let editAddress = this.$route.query.address

            if (editAddress) {
                this.isAdd = false;

                this.formData.USname = editAddress.username;
                this.formData.USphonenum = editAddress.userphonenum;
                this.city = editAddress.provincename + ' ' + editAddress.cityname + ' ' + editAddress.areaname ;
                // this.formData.areaid = editAddress.username;
                this.formData.details = editAddress.details;
            }else{
                common.changeTitle('新增地址');
            }
        },
    }
</script>

