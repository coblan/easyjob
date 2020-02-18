<template>
    <div class="com-top-kefu">
       <table>
           <tr>
               <td>客服电话:</td>
               <td v-text="ctx.phone"></td>
           </tr>
           <tr>
               <td>客服时间:</td>
               <td v-text="ctx.worktime"></td>
           </tr>
       </table>
    </div>
</template>
<script>
    export default {
        props:['ctx']
    }
</script>
<style scoped lang="scss">
.com-top-kefu{
    position: relative;
    height: calc( var(--app-height) - 80px );
}
    table{
        position: absolute;
        top:50%;
        left: 50%;
        transform: translate(-50%,-50%);
    }
    td{
        padding: .2rem .1rem .1rem .3rem;
        color: #747474;
        white-space: nowrap;
    }
</style>