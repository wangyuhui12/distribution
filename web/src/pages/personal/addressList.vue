<style lang="less" scoped>
    @import "../../common/css/index";

    .container {
        .least-full-screen();

        .address-list {
            background: white;
            margin-top: 14px;
            padding: 0 43px 0 26px;

            .address-item {
                padding: 39px 0 23px;
                border-bottom: 1px solid #cccccc;

                &:last-of-type {
                    border-bottom: none;
                }

                .address-item-detail {
                    .fj(flex-start);
                    align-items: center;
                    margin-bottom: 26px;

                    .radio-img {
                        .wl(30px, 30px);
                        margin-right: 30px;
                    }

                    .detail-right {
                        flex: 1;
                        .fj();
                        flex-direction: column;
                        color: #666666;

                        .row-one {
                            margin-bottom: 30px;
                            .fj();
                        }

                        .row-two {

                        }
                    }

                }

                .action-block {
                    color: #999999;
                    .fj(flex-end);

                    .action-item {
                        margin-right: 40px;

                        &:last-of-type {
                            margin-right: 0;

                        }
                    }
                }
            }

        }
    }
</style>

<template>
    <div class="container">
        <header-top :show-back="true">
            <section slot="right">
                <router-link to="/addressEdit" tag="img" src="/static/images/add.png"
                             class="my-add-img"></router-link>
            </section>
        </header-top>

        <ul class="address-list">
            <li class="address-item" v-for="item in addressList">
                <section class="address-item-detail" @click="chooseDeliveryAddress(item)">
                    <img :src="item.isdefault ? '/static/images/radio_check.png': '/static/images/radio_uncheck.png'"
                         class="radio-img">

                    <section class="detail-right" >
                        <p class="row-one">
                            <span class="personal-name">{{item.username}}</span>
                            <span class="phone">{{item.userphonenum}}</span>
                        </p>

                        <p class="row-two" >
                            {{item.provincename}}-{{item.cityname}}-{{item.areaname}} {{item.details}}
                        </p>
                    </section>
                </section>
                <section class="action-block">
                    <span class="action-item" @click.stop="gotoEditAddress(item)">编辑</span>
                    <span v-if="!item.isdefault" class="action-item" @click.stop="doDeleteAddress(item)">删除</span>
                </section>

            </li>
        </ul>
    </div>
</template>

<script>
    import {getUserAddress,changeDefaultAddress} from "src/api/api"

    export default {
        name: "addressList",

        data() {
            return {
                isChoose: false,
                addressList: []
            }
        },

        components: {},

        computed: {

        },

        methods: {
            gotoEditAddress(address){
                this.$router.push({
                    path: '/addressEdit',
                    query: {
                        address
                    }
                })
            },
            doDeleteAddress(address){

            },
            //  下单页选择收货地址
            chooseDeliveryAddress(address){
                let defaultAddress  = this.addressList.find(item => item.isdefault);

                if(defaultAddress){
                    changeDefaultAddress(defaultAddress.uaid, address.uaid).then(
                        ({message}) => {
                            this.$toast(message);
                            this.$router.back();
                        }
                    )
                }
            }
        },

        async created() {
            let {data: adrList} = await getUserAddress(0, 1, '');
            this.addressList = adrList;

            if(this.$route.query.isChoose){
                this.isChoose = true;
            }
        },
    }
</script>

