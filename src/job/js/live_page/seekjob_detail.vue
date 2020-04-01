<template>
    <div class="com-seekjob-detail">
        <com-uis-nav-bar  :title="ctx.row._worker_label" :back="true" :ops="ctx.ops"></com-uis-nav-bar>
        <div class="content">
            <div class="title-panel">
                <div class="head-panel">
                    <div class="head">
                        <img  :src="ctx.row.worker__head || '/static/images/头像.png'" alt="">
                    </div>
                    <div class="name" v-text="ctx.row.worker__name"></div>
                </div>


                <table class="mytable">
                    <tr>
                        <td>期望薪酬:</td>
                        <td v-text="ctx.row.salary"></td>
                    </tr>
                    <tr>
                        <td>联系方式:</td>
                        <td v-text="ctx.row.worker__contact"></td>
                    </tr>
                    <tr>
                        <td>当前住址:</td>
                        <td v-text="ctx.row.worker__address"></td>
                    </tr>
                    <tr>
                        <td>上岗日期:</td>
                        <td v-text="ctx.row.jobtime"></td>
                    </tr>
                </table>


                <div class="key-words">
                    <img src="/static/images/关键字.png" alt="">
                    <span>关键字:</span>
                    <span  v-text="ctx.row.key_words"></span>
                </div>

            </div>
            <div  class="detail">
                <div class="title">证书</div>
                <div class="cert">
                    <img @click="on_click_image(item)" class="item" v-for="item in ctx.row.cert_images" :src="item" alt="">
                </div>
            </div>
            <div class="detail">
                <div class="title">详细</div>
                <pre class="mycontent" v-text="ctx.row.desp"></pre>
            </div>
            <div class="update_time">
                <span class="mylabel">更新于:</span>
                <span v-text="mytime( ctx.row.update_time )"></span>
            </div>
        </div>


    </div>

</template>
<script>
    export default {
        props:['ctx'],
        data(){

            return {

            }
        },
        methods:{
            mytime(time){
                return moment(time).fromNow()
            },
            on_click_image(url){
                cfg.open_image(url)
            }
        }
    }
</script>
<style scoped lang="scss">
    .com-seekjob-detail{
        background-color: #ffffff;
        min-height: calc( var(--app-height) - 80px );
    }
    .content{
        overflow-y: auto;
        height: calc( 100% - 80px );
    }
    .title-panel{
        background-color: white;
        padding: .2rem .2rem;
        margin: .2rem .1rem;
    }
    .mytable{
        margin-top:.3rem;
        td{
            padding: .1rem 0 .1rem .3rem;
            min-width: 1.6rem;
        }
        td:first-child{
            text-align: left;
            color: #999999;
        }
        td:last-child{
            padding-left: .3rem;
        }
    }

    .cert{
        text-align:center;
        img{
            max-width: 2rem;
            max-height: 2rem;
            display: inline-block;
            padding: .1rem;
        }
    }

    .key-words{
        margin-top:.2rem;
        padding: .3rem .1rem;
        color: #747474;
        font-size: .25rem;
        img{
            width: .3rem;
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
        .mycontent{
            font-size: .26rem;
            white-space: pre-wrap;
            word-wrap: break-word;
        }
    }

    .head-panel{
        display:flex;
        justify-content:space-around;
        .head{
            border: 1px solid #eeeeee;
            padding:.1rem;
            img{
                max-width: 2rem;
                max-height: 2rem;
            }
        }
        .name{
            width: 40vw;
            text-align: center;
            white-space: nowrap;
            line-height: 2rem;
            font-size: .4rem;
            font-weight: 500;
        }

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