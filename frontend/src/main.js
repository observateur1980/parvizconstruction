import Vue from 'vue';
import App from './App.vue';
import VueRecaptcha from 'vue-recaptcha-v3';
import axios from 'axios';

Vue.config.productionTip = false;

const siteKey = process.env.VUE_APP_RECAPTCHA_SITE_KEY;
if (!siteKey) {
  console.error('VUE_APP_RECAPTCHA_SITE_KEY environment variable is not set.');
}

Vue.use(VueRecaptcha, { siteKey });

Vue.prototype.$http = axios;

new Vue({
  render: h => h(App),
}).$mount('#app');
