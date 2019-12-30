import home_brand  from './home_brand.vue'
import  jobinfo_item from './jobinfo_item.vue'
Vue.component('com-top-home-brand',home_brand)

Vue.component('com-list-jobinfo-item',function(resolve,reject){
    var p1 = ex.load_js(js_config.js_lib.moment)
    var p2 = ex.load_js('http://cdn.staticfile.org/moment.js/2.24.0/moment-with-locales.min.js')
    Promise.all([p1,p2]).then(()=>{
        resolve(jobinfo_item)
    })
} )