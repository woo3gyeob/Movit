<template>
  <div id="app">
    
      <div>
        <b-button v-b-toggle.sidebar-right>Toggle Sidebar</b-button>
        <b-sidebar id="sidebar-right" title="Sidebar" right shadow>

          <div id="nav">
            <router-link :to="{name:'Home'}">Home</router-link> |
            <router-link :to="{ name:'Community'}">커뮤니티</router-link> |
            <span v-if="isLogin">
              <router-link :to="{ name: 'Profile'}">마이페이지</router-link> |
              <router-link @click.native="logout" to="#">로그아웃</router-link>
            </span>
            <span v-else>
              <router-link :to="{ name: 'Signup' }">Signup</router-link> |
              <router-link :to="{ name: 'Login' }">Login</router-link> 
            </span>
          </div>
        </b-sidebar>
      </div>
    <router-view 
      @login="login"
    />
  </div>
</template>

<script>
import Vue from 'vue'
import { BButton, BSidebar } from 'bootstrap-vue'
Vue.component('b-button', BButton)
Vue.component('b-sidebar', BSidebar)

export default {
  name: 'App',
  data: function () {
    return {
      isLogin: false,
      currentUser:'',
    }
  },
  methods: {
    login: function (username) {
      this.isLogin = !this.isLogin
      this.currentUser = username
    },
    logout: function () {
      this.isLogin = false
      localStorage.removeItem('jwt')
      this.$router.push({name:"Home"})
    }
  },
  created () {
    const token = localStorage.getItem('jwt')
    if (token) {
      this.isLogin= true
    }
  },

}

</script>


<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
