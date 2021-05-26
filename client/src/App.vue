<template>
  <div id="app">
      <span class="h1 btn"><b-button v-b-toggle.sidebar-right class="h1 btn-warning">Movit <i class="fas fa-bars ps-2"></i></b-button></span>
      <b-sidebar id="sidebar-right" bg-variant="dark" text-variant="warning" title="Movit" right shadow>
        <div v-if="username">
          <h4 class="pt-4 username">{{ username }} 님, 환영합니다!</h4>
        </div>
        <div id="nav">
          <div v-if="isLogin">
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
    <div class="">
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
      hover: false,
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
      this.getUser()
    },
    logout: function () {
      this.isLogin = false
      localStorage.removeItem('jwt')
      this.$router.push({name:"Home"})
      this.username=''
    }
  },
  created () {
    const token = localStorage.getItem('jwt')
    if (token) {
      this.isLogin = true
      this.getUser()
    }
    else {
      this.$router.push({name:'Login'})
    }
  },

}

</script>


<style>
#app {
  position: sticky;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
}

#nav {
  padding: 30px;
}

#nav a {
  color: white;
  transition:color 0.25s;
}
#nav a:hover{
  color:#FFCA2C;
  /* background:linear-gradient(to right, #f6d365 0%, #fda085  40%, #f6d365 100%); */
  background: -webkit-linear-gradient( #EFB633,  #e7e41a);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  font-weight: bold;
}

#nav a.router-link-exact-active {
  color: #FFCA2C;
  font-weight: bold;
}
.btn {
  color: #fdd835;
  font-size:3vh;
}
/* .padding {
  padding: 5% 15%;
} */
.router-link {
  text-decoration: none; 
}
.username {
  color: white;
}

</style>
