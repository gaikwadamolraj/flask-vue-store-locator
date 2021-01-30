import Vue from 'vue'
import App from './App.vue'
import { BootstrapVue, IconsPlugin, TablePlugin } from 'bootstrap-vue'


Vue.config.productionTip = false

new Vue({
  render: h => h(App),
}).$mount('#app')

Vue.use(BootstrapVue);
Vue.use(IconsPlugin)

Vue.use(TablePlugin)