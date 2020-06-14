<template>
    <div class="com-apply-list-company">
        <div class="block" v-for="row in rows" :key="row.pk" @click="on_click(row)">

                <table>
                    <tr>
                        <td>
                            <span>申请者:</span>
                        </td>
                        <td>
                            <span v-text="row._worker_label"></span>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <span>职位:</span>
                        </td>
                        <td>
                            <span v-text="row._job_label"></span>
                        </td>
                    </tr>
                </table>

            <van-tag :type="mytype(row)">
                <span v-text="status_label(row)"></span>
            </van-tag>
            <span  class="creattime" v-text="mytime( row.createtime )"></span>

            <van-icon class="next-arrow" name="arrow" />
        </div>
    </div>
</template>
<script>
    export default {
        props:['heads','rows'],
        data(){
          return {
              parStore:ex.vueParStore(this),
              status_head :ex.findone(this.heads,{name:'status'})
          }
        },
        methods:{
            on_click(row){
                ex.eval(this.parStore.vc.ctx.block_click,{row:row,head:this.parStore.vc.ctx})
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
            status_label(row){
                return ex.findone(this.status_head.options,{value:row.status}).label
            },
            mytime(time){
                return moment(time).fromNow()
            },
        }

    }
</script>
<style scoped lang="scss">
.block{
    padding:  .5rem .3rem;
    background-color: white;
    margin: .1rem 0;
    display: flex;
    justify-content: space-between;
    align-items:center;
    padding-right: .7rem;
}
    .creattime{
        position: absolute;
        bottom: .1rem;
        right: .7rem;
        color: #a69e9e;
        font-size: .25rem;
    }
    td{
        padding: .1rem;
    }
    .next-arrow{
        position: absolute;
        right: .1rem;
        top:50%;
        transform: translateY(-50%);
    }
</style>