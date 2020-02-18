<template>
    <div class="com-top-seekjob-item">
        <div class="row-panel" v-for="row in rows" @click="on_click(row)">
            <div class="head">
                <img :src="row.worker__head || '/static/images/头像.png'" alt="">
            </div>
            <div>
                <div v-text="row.worker__name"></div>
                <div class="salary" v-text="row.salary"><span>期望薪酬</span> </div>
                <div class="key_words" v-text="row.key_words"></div>
            </div>
            <div class="update_time" v-text="mytime( row.update_time )"></div>
        </div>
    </div>
</template>
<script>
    export default {
        props:['heads','rows'],
        data(){

          return {
              parStore:ex.vueParStore(this)
          }
        },
        methods:{
            mytime(time){
                return moment(time).fromNow()
            },
            on_click(row){
                ex.eval(this.parStore.vc.ctx.block_click,{row:row})
            }
        }
    }
</script>
<style scoped lang="scss">
.com-top-seekjob-item{
    min-height: calc( var(--app-height) - 80px );
    overflow:auto;
    -webkit-overflow-scrolling: touch;
}
.row-panel{
    margin: .3rem .1rem;
    background-color: white;
    padding: .4rem .2rem;
    position: relative;

    display: flex;
}
.head{
    margin-right:.5rem;

    img{
        max-width: 1rem;
        max-height: 1.2rem;
    }
}

.salary{
    position: absolute;
    right: .3rem;
    top:.3rem;
    color: #d68500;;
}
.key_words{
    margin-top:.3rem;
    color: grey;
    font-size: .25rem;
}
.update_time{
    position: absolute;
    bottom: .2rem;
    right: .3rem;
    color: grey;
    font-size: .2rem;
}
</style>