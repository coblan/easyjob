<template>
    <div class="com-apply-detail">
        <div class="item" v-for="row in rows" @click="on_click(row)">
            <table>
                <tr>
                    <td>公司:</td>
                    <td>  <span v-text="row.company"></span></td>
                </tr>
                <tr>
                    <td>职位:</td>
                    <td> <span v-text="row._job_label"></span></td>
                </tr>
            </table>

            <van-tag :type="mytype(row)">
                <span v-text="row._status_label"></span>
            </van-tag>
            <span class="apply-time" v-text="mytime( row.createtime )"></span>

            <van-icon class="next-arrow ab-v-center" style="right: .1rem" name="arrow" />

        </div>

        <div v-if="rows.length==0" class="ab-center" >
            <span>暂时没有申请记录</span>
        </div>

    </div>
</template>
<script>
    export default {
        props:['heads','rows'],
        mounted(){
            this.parStore = ex.vueParStore(this)
        },
        methods:{
            on_click(row){
                ex.eval(this.parStore.vc.ctx.block_click,{row:row})
            },
            mytime(time){
                return moment(time).fromNow()
            },
            mytype(row){
                var data_map = {
//                    0:'',
                    1:'success',
                    2:'warning',
                    3:'primary'
                }
                return data_map[row.status]
            },

        }

    }
</script>
<style scoped lang="scss">
    .com-apply-detail{
        width: 100vw;
        height: calc(100vh - 50px );
    }
    .item{
        position: relative;
        padding: .3rem;
        background-color: white;
        margin: 1px 0;
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding-right: .6rem;
    }


.apply-time{
    position: absolute;
    right: .6rem;
    font-size: .26rem;
    color: grey;
    bottom: .3rem;

}
    td{
        padding: .2rem;
    }
</style>