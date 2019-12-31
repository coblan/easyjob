<template>
    <div class="com-live-userinfo">
        <com-uis-nav-bar  :title="ctx.title" :back="true" :ops="ctx.ops"></com-uis-nav-bar>
        <div class="content">
            <van-button type="primary" size="large" @click="quit()">退出登录</van-button>
        </div>

    </div>
</template>
<script>
    export default{
        props:['ctx'],
        methods:{
            quit(){
                cfg.show_load()
                location = '/accounts/logout'
            }
        }
    }
</script>

<style scoped lang="scss">
    .com-live-userinfo{
        background-color: #f7f7f7;
        height: var(--app-height);
    }
.content{
    width: 90%;
    margin: auto;
    margin-top: 1rem;
}
</style>