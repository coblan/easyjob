/*
暂时没用
*/
<template>
    <div class="com-apply-detail">
        <com-uis-nav-bar  :title="jobinfo._job_label" :back="true" ></com-uis-nav-bar>
        <div class="after-nav-content">
            <div>
                <div style="display: flex;justify-content: space-between;align-items:flex-start;padding: .2rem .4rem">
                    <table>
                        <tr>
                            <td>
                                姓名:
                            </td>
                            <td>
                                <span v-text="worker.name"></span>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                电话:
                            </td>
                            <td>
                                <span v-text="worker.contact"></span>
                            </td>
                        </tr>
                        <tr>
                            <td>当前住址:</td>
                            <td>
                                <span v-text="worker.address"></span>
                            </td>
                        </tr>

                    </table>
                    <img class="head" :src="worker.head" alt="">
                </div>


            </div>


        </div>

    </div>
</template>

<script>
    export default {
        props:['ctx'],
        data(){
            return {
                jobinfo:this.ctx.jobinfo,
                worker:{}
            }
        },
        mounted(){
            ex.director_call('get_worker_info',{worker:this.ctx.worker}).then(resp=>{
                ex.vueAssign(this.worker,resp)
            })
        },
        methods:{
            mytime(time){
                return moment(time).fromNow()
            },
            on_click_image(url){
                cfg.open_image(url)
            },
            apply_work(){
                cfg.show_load()
                ex.director_call('job.apply_work',{pk:this.row.pk}).then(()=>{
                    cfg.hide_load()
                cfg.toast('申请成功')
            })
            }
        }
    }
</script>
<style scoped lang="scss">
.com-apply-detail{
    height: 100vh;
    width: 100vw;
    background-color: white;
}
    .head{
        width: 3rem;
        height: auto;
    }
td{
    padding: .2rem;
}
</style>