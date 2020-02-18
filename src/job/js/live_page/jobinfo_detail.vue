<template>
    <div class="com-jobinfo-detail">
        <com-uis-nav-bar  :title="ctx.title" :back="true" :ops="ctx.ops"></com-uis-nav-bar>
       <div class="title-panel">
           <div class="title" v-text="row.position"></div>
           <div class="pay" v-text="row.pay"></div>
           <table class="item-content">
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
               <tr>
                   <td>
                       <img class="label-img" src="/static/images/联系.png" alt="">
                   </td>
                   <td>
                       <span v-text="row.com__contact"></span>
                   </td>
               </tr>

           </table>

       </div>
        <div class="detail">
            <div class="title">详细</div>
            <div v-text="row.detail"></div>
        </div>
        <div class="update_time">
            <span class="mylabel">更新于:</span>
            <span v-text="mytime( row.update_time )"></span>
        </div>
    </div>
</template>

<script>
    export default {
        props:['ctx'],
        data(){
            return {
                row:this.ctx.row
            }
        },
        methods:{
            mytime(time){
                return moment(time).fromNow()
            },
        }
    }
</script>
<style scoped lang="scss">
.com-jobinfo-detail{
    background-color: #ffffff;
    min-height: calc( var(--app-height) - 80px );

}
.title-panel{
    background-color: white;
    padding: .2rem .2rem;
    margin: .2rem .1rem;

    .title{
        font-size: .4rem;
        font-weight:500;
        text-align: center;
    }
    .pay{
        color: #eba324;
        padding: .4rem 0 .2rem .4rem;
    }
}
.item-content{
    td{
        padding: .1rem .2rem;
    }
    td:first-child{
        padding-left: .3rem;
    }
}
.detail{
    background-color: white;
    line-height: .4rem;
    font-size: .25rem;
    padding: .2rem .2rem;
    margin: .2rem .1rem;
    .title{
        font-size: .35rem;
        font-weight: 500;
        border-bottom: 1px solid #e6e6e6;
        margin-bottom: .3rem;
    }
}
.label-img{
    height: .3rem;
    width: auto;
    vertical-align: middle;
}
    .update_time{
        padding: .2rem .3rem;
        text-align: right;
        color: grey;
        font-size: .26rem;
        .mylabel{
            display: inline-block;
            margin-right: .1rem;
        }
    }

</style>