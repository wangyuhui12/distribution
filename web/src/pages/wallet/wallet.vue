<style lang="less" scoped>
    @import "../../common/css/index";

    .container {

        .go-withdraw-cash {
            width: 129px;
            height: 36px;
            border: 1px solid rgba(255, 255, 255, 1);
            border-radius: 20px;
            .fontc(36px);
            .sc(24px, white);
            background: @mainColor;
        }

        .bank-balance {
            background: white;
            padding: 48px 20px 16px;
            .bs(10px,3px, 6px);

            .bank-balance-hd {
                padding: 0 20px 26px;

                .row-one {
                    margin-bottom: 41px;
                    .fj();
                    align-items: center;

                    .margin-money{
                        .margin-money-num{
                            color: @moneyColor;
                        }
                    }
                }

                .num {
                    .sc(80px, @moneyColor);
                    font-weight: bold;
                }
            }

            .bank-balance-charge {
                padding: 20px 5px 20px 20px;
                border-top: 1px solid @grayBorderColor;
                border-bottom: 1px solid @grayBorderColor;
                .fj();
                align-items: center;

                .left {

                }
                .right {
                    .wl(15px, 26px);
                }
            }

            .bank-balance-ft{
                .fj(flex-end);
                padding-top: 22px;

                .go-balance-record{
                    .sc(21px, @mainColor);
                    .wl(120px,40px);
                    .fontc(28px);
                    background: white;
                    .bd(@mainColor, 30px);
                }
            }
        }

        .balance-record-list {
            .balance-record-item {
                .bgw();
                .bs(10px,3px, 6px);
                padding: 0 20px;

                .record-hd{
                    padding: 22px 6px 16px;
                    border-bottom: 1px solid @grayBorderColor;
                    .fj();

                    .type{
                        .fz(28px);
                    }

                    .date{
                        .sc(18px, @lightFontColor);
                    }
                }

                .record-bd{
                    padding: 19px 6px 41px;
                    color: @lightFontColor;

                    .price{
                        margin-bottom: 15px;
                    }
                    .order-no{}

                }

                &:last-of-type{
                    margin-bottom: 144px;
                }
            }
        }
    }
</style>

<template>
    <div class="container">
        <header-top :title="$route.meta.title" :showBack="true">
            <section slot="right">
                <router-link tag="button" to="/withdrawCash" class="go-withdraw-cash">提现</router-link>
            </section>
        </header-top>

        <section class="bank-balance">
            <header class="bank-balance-hd">
                <p class="row-one">
                    <span>
                        账户余额（元）
                    </span>
                    <router-link to="/marginMoney" tag="section"  class="margin-money">
                        <span class="">保证金</span>
                        <span class="margin-money-num">￥0.00</span>
                    </router-link>
                </p>
                <p class="num">￥200.00</p>
            </header>

            <router-link to="/balanceCharge" tag="section" class="bank-balance-charge">
                <span>余额充值</span>
                <img src="/static/images/arrow.png" class="right" alt="">
            </router-link>

            <footer class="bank-balance-ft" >
                <router-link to="/balanceRecord" tag="button" class="go-balance-record" >收支记录</router-link>
            </footer>
        </section>

        <ul class="balance-record-list">
            <li class="balance-record-item" v-for="item in 3">
                <header class="record-hd">
                    <span class="type">
                        类型：订单支出
                    </span>
                    <span class="date">
                        2017-08-19 15：15：23
                    </span>
                </header>

                <section class="record-bd">
                    <p class="price">金额：0.00</p>
                    <p>订单号：154857468451253456123132135</p>
                </section>
            </li>
        </ul>

        <load-more></load-more>
    </div>
</template>

<script>
    export default {
        name: "wallet",

        data() {
            return {}
        },

        components: {},

        methods: {},
    }
</script>

