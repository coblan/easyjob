<template>
    <div class="com-top-filedownload">
        <span class="title" v-text="ctx.title"></span>
        <div class="file-item" v-for="fl in ctx.files">
            <a :href="fl.url" v-text="fl.label"></a>
        </div>
    </div>
</template>
<script>
    export default {
        props:['ctx'],
        data(){
            return {

            }
        }
    }
</script>
<style scoped lang="scss">
    .com-top-filedownload{
        margin: .3rem 0;
        padding-top: .2rem;
    }
.title{
    padding:.2rem;
    color: grey;
}
.file-item{
    padding: .3rem;
    background-color: white;
    margin: .3rem .1rem;
    border: 1px solid #f5f5f5;
}
</style>