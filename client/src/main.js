import Vue from 'vue'
import App from './App.vue'
import router from './router'
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import { NavbarPlugin } from 'bootstrap-vue'
import { BButton } from 'bootstrap-vue'
import Carousel3d from 'vue-carousel-3d';
Vue.use(Carousel3d);

Vue.component('b-button', BButton)
Vue.use(NavbarPlugin)

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
Vue.use(BootstrapVue)
Vue.component('b-button','b-sidebar')
