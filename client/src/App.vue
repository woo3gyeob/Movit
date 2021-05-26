<template>
  <div id="app">
      <b-button v-b-toggle.sidebar-right variant=""><i class="fas fa-bars "></i></b-button>
      <b-sidebar id="sidebar-right" bg-variant="dark" text-variant="warning" title="Movit" right shadow>
        <h4 class="pt-4 username">{{ username }} 님, 환영합니다!</h4>
        <div id="nav">
          <div v-if="isLogin">
            <a href=""></a>
            <div class="h2 p-3">
              <router-link class="router-link" :to="{name:'Home'}" >Movies</router-link>
            </div>
            <div class="h2 p-3">
              <router-link class="router-link" :to="{ name:'Community'}">Community</router-link>
            </div>
            <div class="h2 p-3">
              <router-link class="router-link" :to="{ name: 'Profile'}">Profile</router-link>
            </div>
            <div class="h2 p-3">
              <router-link class="router-link" @click.native="logout" to="#">Logout</router-link>
            </div>
          </div>
          <div v-else>
            <div class="h2 p-3">
              <router-link class="router-link" :to="{ name: 'Signup' }">Signup</router-link>
            </div>
            <div class="h2 p-3">
              <router-link class="router-link"   :to="{ name: 'Login' }">Login</router-link> 
            </div>
          </div>
        </div>
      </b-sidebar>
    <div class="padding">
      <router-view 
        @login="login"
        :currentUserId="currentUserId"
        :username="username"
      />
    </div>
  </div>
</template>

<script>
import jwt_decode from "jwt-decode"
import Vue from 'vue'
import { BButton, BSidebar } from 'bootstrap-vue'
Vue.component('b-button', BButton)
Vue.component('b-sidebar', BSidebar)

export default {
  name: 'App',
  data: function () {
    return {
      isLogin: false,
      currentUserId:'',
      username:'',
    }
  },
  methods: {
    getUser() {
      const token = localStorage.getItem('jwt')
      const decoded = jwt_decode(token)
      this.currentUserId = Number(decoded.user_id)
      this.username = decoded.username
    },
    login: function () {
      this.isLogin = !this.isLogin
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
      this.isLogin = true
    }
    else {
      this.$router.push({name:'Login'})
    }
    this.getUser()
  },

}

</script>


<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;

}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #fdd835;
}

#nav a.router-link-exact-active {
  color: white;
}
.btn {
  color: #fdd835;
  font-size:3vh;
}
.padding {
  padding:5%;
}
a { 
  text-decoration: none; 
}
.router-link {
  text-decoration: none; 
}
.username {
  color:#fdd835;
}
</style>
