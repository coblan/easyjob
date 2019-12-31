<template>
    <div class="com-brand">
       易职通
        <div class="userhead" @click="on_click">
            <van-icon name="user-circle-o" />
        </div>
    </div>
</template>

<script>
    export default {
        methods:{
            on_click(){
                live_root.open_live('live_userinfo',{title:"我的账号"})
            }
        }
    }
</script>
<style scoped lang="scss">
.com-brand{
    height: 4rem;
    font-size: .5rem;
    text-align: center;
    line-height: 3rem;
    vertical-align: middle;
    letter-spacing: .2rem;
    color: white;
    position: relative;
    /*background: rgb(108, 172, 244);*/
    /*background: -moz-linear-gradient(70deg, rgb(108, 172, 244) 25%, rgb(154, 140, 250) 91%);*/
    /*background: -webkit-linear-gradient(70deg, rgb(108, 172, 244) 25%, rgb(154, 140, 250) 91%);*/
    /*background: -o-linear-gradient(70deg, rgb(108, 172, 244) 25%, rgb(154, 140, 250) 91%);*/
    /*background: -ms-linear-gradient(70deg, rgb(108, 172, 244) 25%, rgb(154, 140, 250) 91%);*/
    /*background: linear-gradient(160deg, rgb(108, 172, 244) 25%, rgb(154, 140, 250) 91%);*/

    /*background: rgb(108, 172, 244);*/
    /*background: -moz-linear-gradient(45deg, rgb(108, 172, 244) 44%, rgb(174, 196, 250) 63%);*/
    /*background: -webkit-linear-gradient(45deg, rgb(108, 172, 244) 44%, rgb(174, 196, 250) 63%);*/
    /*background: -o-linear-gradient(45deg, rgb(108, 172, 244) 44%, rgb(174, 196, 250) 63%);*/
    /*background: -ms-linear-gradient(45deg, rgb(108, 172, 244) 44%, rgb(174, 196, 250) 63%);*/
    /*background: linear-gradient(135deg, rgb(108, 172, 244) 44%, rgb(174, 196, 250) 63%);*/

    background-image: url("/static/images/ezgif.com-webp-to-jpg.jpg");
    background-size: cover;
    background-repeat:no-repeat;
}
    .userhead{
        position: absolute;
        right: .3rem;
        top: -.8rem;
    }
</style>