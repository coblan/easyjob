<template>
    <div class="com-pop-protocal">
        <div class="content">
            <div class="inn-wrap" v-html="ctx.content"></div>
        </div>

        <div class="btn-panel">
            <van-button type="default"  size="small" @click="reject">拒绝</van-button>
            <van-button type="primary" size="small" @click="agree">同意</van-button>
        </div>

    </div>
</template>
<script>
export default {
    props:['ctx'],
    data(){
        return {
            parStore:ex.vueParStore(this)
        }
    },
    methods:{
        reject(){
            this.parStore.vc.close()
        },
        agree(){
            this.$emit('finish')
        }
    }
}
</script>

<style scoped lang="scss">
.com-pop-protocal{
    width: 90vw;
    height: 90vh;
    background-color: white;
    border: 1px solid grey;
    display: flex;
    flex-direction: column;
    padding: .5rem .2rem .1rem .2rem;
    line-height: .45rem;
}
.content{
    position: relative;
    flex-grow: 10;
    .inn-wrap{
        position:absolute;
        top:0;
        bottom: 0;
        left: 0;
        right: 0;
        overflow: auto;
    }
}
.btn-panel{
    flex-grow: 0;
    text-align: right;
    height: .8rem;
    padding:.1rem .3rem;
}
</style>