<template>
    <div class="com-list-jobinfo">
        <div class="row-panel" v-for="row in rows" @click="on_click(row)">
            <div class="title-bar" >
                <div class="title" v-text="row.position"></div>
                <div class="pay" v-text="row.pay"></div>
            </div>
            <table class="item-content">
                <!--<tr>-->
                    <!--<td>-->
                        <!--<img class="label-img" src="/static/images/职位.png" alt="">-->
                    <!--</td>-->
                    <!--<td>-->
                        <!--<span v-text="row.position"></span>-->
                    <!--</td>-->

                <!--</tr>-->
                <tr>
                    <td>
                        <img class="label-img" src="/static/images/企业.png" alt="">
                    </td>
                    <td>
                        <span v-text="row.com__name"></span>
                    </td>
                </tr>
                <tr>
                    <td>
                        <img class="label-img" src="/static/images/时间 .png" alt="">
                    </td>
                    <td>
                        <span v-text=" row.require_time"></span>
                    </td>
                </tr>
                <tr>
                    <td>
                        <img class="label-img" src="/static/images/地址.png" alt="">
                    </td>
                    <td>
                        <span v-text="row.address"></span>
                    </td>

                </tr>

            </table>

            <div class="update_time" v-text="mytime( row.update_time )"></div>
        </div>
    </div>
</template>

<script>
    export default {
        props:['heads','rows'],
        data(){
            moment.lang('zh-cn');
            return {
                parStore:ex.vueParStore(this)
            }
        },
        methods:{
            mytime(time){
               return moment(time).fromNow()
            },
            on_click(row){
                ex.eval(this.parStore.vc.ctx.block_click,{row:row,head:this.parStore.vc.ctx})
            }
        }
    }
</script>

<style scoped lang="scss">
.com-list-jobinfo{
    min-height: calc( var(--app-height) - 80px );
    overflow:auto;
    -webkit-overflow-scrolling: touch;
}
.row-panel{
    margin: .3rem .1rem;
    background-color: white;
    padding: .4rem .2rem;
    position: relative;
}
.update_time{
    position: absolute;
    bottom: .2rem;
    right: .3rem;
    color: grey;
    font-size: .2rem;
}
.title-bar{
    position:relative;

    .title{
        color: black;
        font-size: .3rem;
        font-weight: 500;
        margin-bottom: .2rem;
        white-space: nowrap;
        max-width: 5rem;
        overflow: hidden;
        text-overflow: ellipsis;
    }
    .pay{
        color: grey;
        color: #d68500;
        font-size: .26rem;
        position: absolute;
        right: .3rem;
        top: .1rem;
    }
}

.item-content{
    color: grey;
    font-size: .26rem;
    padding:.2rem .4rem;

    td{
        padding: .1rem;
    }
    td:first-child{
        padding-left: .6rem;
    }
}
    .label-img{
        height: .3rem;
        width: auto;
        vertical-align: middle;
    }
</style>
