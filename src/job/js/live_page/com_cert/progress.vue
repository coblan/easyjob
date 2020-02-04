<template>
    <div class="com-live-com-cert-progress">
        <com-uis-nav-bar :title="ctx.title" :back="can_back" ></com-uis-nav-bar>
        <div class="content">

            <div v-if="active==0" class="mytitle">
                请尽快编辑资料后提起审核申请!
            </div>
            <div v-if="active==1" class="mytitle">
                申请已经提交，请耐心等待!
            </div>
            <div v-if="active==2" class="mytitle">
                审核通过，资料不能修改!
            </div>

            <van-steps
                    :active="active"
                    active-icon="success"
                    active-color="#38f"
            >
                <van-step>资料编辑</van-step>
                <van-step>资料审核</van-step>
                <van-step>审核通过</van-step>
            </van-steps>

            <div class="mybtn">
                <van-button v-if="active==0" @click="submit_info()" type="primary" size="large">提交申请</van-button>
            </div>

        </div>
    </div>
</template>
<script>
    export default {
        props:['ctx'],
        basename:'live-com-cert-progress',
        data(){
          return {
              active:-1,
          }
        },
        mounted(){
            ex.eval(this.ctx.init_express,{vc:this})
        },
        computed:{
            can_back(){
                return this.$root.stack.length >1
            }
        },
        methods:{
            submit_info(){
                ex.eval(this.ctx.submit_info_express,{vc:this})
            }
        }
    }
</script>
<style scoped lang="scss">
.com-live-com-cert-progress{
    background-color: #fafafa;
}
    .content{
        padding-top: .5rem ;
        margin: 0 .3rem;
    }
    .mytitle{
        color: grey;
        text-align: center;
        margin: .5rem .2rem;
    }
    .mybtn{
        padding-top: 1.6rem;
    }
</style>