<style lang="less" scoped>
    @import "../../common/css/index";

    .container {
        padding-bottom: 100px;
        .least-full-screen();

        #go-order-img {
            .wl(33px, 27px);
        }

        .pay-order {
            width: 129px;
            height: 46px;
            border: 1px solid rgba(255, 255, 255, 1);
            border-radius: 20px;
            .fontc(46px);
            .sc(24px, white);
            background: @mainColor;
        }

        .banner {
            height: 180px;
            margin-bottom: 10px;

            img {
                width: 100%;
                height: 100%;
            }
        }

        .nav-wrap {
            .nav-list-parent {
                background: white;
                overflow-x: scroll;
                white-space: nowrap;

                .nav-item {
                    height: 80px;
                    display: inline-block;
                    padding: 0 50px;
                    .fontc(80px);

                    &.active {
                        color: @mainColor;
                        border-bottom: 3px solid @mainColor;
                    }
                }
            }
            .nav-list-children {
                height: 80px;
                overflow-x: scroll;
                .fj(flex-start);
                align-items: center;
                flex-wrap: nowrap;

                .pillow-item {
                    /*line-height: 80px;*/
                    /*display: inline-block;*/
                    margin-right: 50px;
                    border: 1px solid rgba(110, 171, 184, 1);
                    padding: 4px 23px;
                    border-radius: 30px;
                    white-space: nowrap;

                    &.active {
                        color: white;
                        background: @mainColor;
                    }

                    &:first-of-type {
                        margin-left: 42px;
                    }
                    &:last-of-type {
                        margin-right: 42px;
                    }
                }

                .pillow-item-tail {
                    flex: 42px;
                    .wl(42px, 10px);
                }

            }
        }

        .goods-list {
            padding: 0 10px;
            background: white;

            .goods-item {
                padding: 35px 2px 32px 16px;
                border-bottom: 1px solid #DBDBDB;
                .fj();

                &:last-child {
                    border-bottom: 0;
                }

                .goods-img {
                    margin-right: 40px;
                    .wl(100px, 100px);

                    img {
                        .wl(100%, 100%);
                    }
                }

                .goods-description {
                    flex: 1;
                    .fj();
                    flex-direction: column;
                    .goods-description-header {
                        .fz(28px);

                    }
                    .goods-description-content {
                        .fj();

                        .goods-description-price {

                            .current-price {
                                margin-right: 20px;
                                color: #FC0000;

                            }
                            .original-price {
                                color: black;
                                text-decoration: line-through;

                            }
                        }

                    }
                }
            }
        }
    }
</style>

<template>
    <div class="container">
        <header-top :title="'云仓'">
            <section slot="left">
                <router-link tag="img" to="/mallOrder" id="go-order-img" src="/static/images/myOrder.png"
                             alt=""></router-link>
            </section>
            <section slot="right">
                <button class="pay-order" @click="gotoPayOrder">结算</button>
            </section>
        </header-top>

        <section class="banner">
            <img src="/static/images/testbg.jpg" alt="">
        </section>

        <section class="nav-wrap">
            <ul class="nav-list-parent">
                <li v-for="item in parentCategory" :class="{'nav-item': true, 'active': item.PAid == paSelected}"
                    @click="switchPACategory(item)">
                    {{item.PAname}}
                </li>
            </ul>

            <ul class="nav-list-children">
                <li v-for="item in secondCategory" :class="{'pillow-item': true, 'active': item.PAid == secondSelected}"
                    @click="chooseSECategory(item)">{{item.PAname}}
                </li>
                <!--<li class="pillow-item-tail"></li>-->
            </ul>
        </section>

        <ul class="goods-list">
            <li class="goods-item" v-for="item in productListWithCart">
                <section class="goods-img">
                    <img :src="item.PRpic" alt="">
                </section>
                <section class="goods-description">
                    <header class="goods-description-header">
                        {{item.PRname}}
                    </header>
                    <section class="goods-description-content">
                        <p class="goods-description-price">
                            <span class="current-price">￥{{item.PRoldprice}}</span>
                            <span class="original-price">￥{{item.PRprice}}</span>
                        </p>

                        <buy-cart :shopNum.sync="item.PRnum" @add.passive="addCart(item)"
                                  @minus.passive="reduceCart(item)"></buy-cart>
                    </section>
                </section>
            </li>
        </ul>

        <section class="load-more-wrap">
            <load-more :type="loadingType"></load-more>
        </section>

        <footer-guide></footer-guide>
    </div>
</template>

<script>
    import {Toast} from "mint-ui"
    import footerGuide from "src/components/footer/footerGuide"
    import buyCart from "src/components/common/buyCart"
    import {getProductCategory, getProductList} from "src/api/api"
    import LoadMore from "src/components/common/loadMore"
    import common from "src/common/js/common"
    import {mapMutations, mapState,mapGetters} from "vuex"


    export default {
        name: "mall",

        data() {
            return {
                parentCategory: [], //  父级类别
                paSelected: '',    // 父级类别选中的PAid

                secondCategory: [], //  二级类别
                secondSelected: '',    // 二级类别选中的PAid

                productList: [],    //  商品列表
                page: 1,
                count: 10,
                loadingType: 'normal',  // 加载组件加载状态
            }
        },

        components: {
            buyCart,
            footerGuide,
            LoadMore,
        },

        computed: {
            ...mapState({
                productListWithCart: function (state) {
                    let rst = this.productList.concat();

                    for (let i = 0; i < state.cartList.length; i++) {
                        for (let j = 0; j < this.productList.length; j++) {
                            if (state.cartList[i].PRid == this.productList[j].PRid) {
                                rst[j].PRnum = state.cartList[i].PRnum;
                            }
                        }
                    }

                    return rst;
                }
            }),
            ...mapGetters(['usefulCartList']),

        },

        methods: {
            ...mapMutations({
                addCart: 'ADD_CART',
                reduceCart: 'REDUCE_CART'
            }),
            // 滚动条监听事件
            touchMove() {
                let scrollTop = common.getScrollTop();
                let scrollHeight = common.getScrollHeight();
                let ClientHeight = common.getClientHeight();

                if (scrollTop + ClientHeight >= scrollHeight - 10 && this.loadingType == 'normal') {
                    this.setProductList();
                }
            },
            gotoPayOrder() {
                if(this.usefulCartList.length){
                    this.$router.push('/payOrder');
                }else{
                    this.$toast('请选几样商品加入购物车!');
                }
            },

            switchPACategory(categroy) {
                // 选中还是当前父级tab就结束
                if (categroy.PAid == this.paSelected) {
                    return;
                }

                this.paSelected = categroy.PAid;
                this.initSECategory();
            },

            chooseSECategory(categroy) {
                if (categroy.PAid == this.secondSelected) {

                } else {
                    this.secondSelected = categroy.PAid;
                    this.setProductList(true);
                }
            },

            // 初始分类及第一个父级分类的所有商品
            async initCategoryAndPrds() {
                let {data: paData} = await getProductCategory(1, 0);

                this.parentCategory = paData;
                this.paSelected = this.parentCategory[0].PAid;

                await this.initSECategory();
            },

            async initSECategory() {
                let {data: seData} = await  getProductCategory(2, this.paSelected);

                this.secondCategory = seData;
                this.secondSelected = this.secondCategory[0].PAid;

                await this.setProductList(true);
            },

            /**
             * 获取商品列表
             * @param replace
             */
            async setProductList(replace) {
                if (replace) {
                    this.page = 1;
                }
                this.loadingType = 'loading';
                let {data: prdList} = await getProductList(2, this.secondSelected, 1, this.page, this.count);

                if (prdList.length < this.count) {
                    this.loadingType = 'nomore';
                } else {
                    this.loadingType = 'normal';
                }

                if (replace) {
                    this.productList = prdList;
                } else {
                    this.productList = [...this.productList, ...prdList];
                }

                this.page++;
            },
        },

        destroyed() {
            window.removeEventListener('scroll', this.touchMove);
        },

        async mounted() {
            await this.initCategoryAndPrds();
            window.addEventListener('scroll', this.touchMove);
        }
    }
</script>

