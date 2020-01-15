import Vue from 'vue';
import axios from 'axios';
import App from './App.vue';
import router from './router';
import vuetify from './plugins/vuetify';

Vue.config.productionTip = false;
Vue.prototype.$http = axios.create({
  baseUrl: 'http://localhost:5000/',
});

new Vue({
  router,
  vuetify,
  render: h => h(App),
}).$mount('#app');
