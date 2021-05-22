<template>
  <div id="app">
    <!-- <template>
      <div>
        <b-button v-b-toggle.sidebar-1>Toggle Sidebar</b-button>
        <b-sidebar id="sidebar-1" title="Sidebar" shadow>
          <div class="px-3 py-2">
            <p>
              Cras mattis consectetur purus sit amet fermentum. Cras justo odio, dapibus ac facilisis
              in, egestas eget quam. Morbi leo risus, porta ac consectetur ac, vestibulum at eros.
            </p>
            <b-img src="https://picsum.photos/500/500/?image=54" fluid thumbnail></b-img>
          </div>
        </b-sidebar>
      </div>
    </template> -->
    <div id="nav">
      <router-link :to="{name:'Home'}">Home</router-link> |
      <router-link :to="{ name:'Community'}">커뮤니티</router-link> |
    <span v-if="isLogin">
      <router-link :to="{ name: 'Mypage'}">마이페이지</router-link> |
      <router-link @click.native="logout" to="#">로그아웃</router-link>
    </span>
    <span v-else>
      <router-link :to="{ name: 'Signup' }">Signup</router-link> |
      <router-link :to="{ name: 'Login' }">Login</router-link> 
    </span>
    </div>
    <router-view 
      :movies="movies"
      @login="login"
    />
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'App',
  data: function () {
    return {
      movies: [],
      isLogin: false,
      currentUser:'',
    }
  },
  methods: {
    getMovies: function () {
      axios({
        method:'get',
        url: 'http://127.0.0.1:8000/movies/',
      })
        .then(res => {
          this.movies = res.data
        })
        .catch(err => { 
          console.log(err)
        })
    },
    login: function (username) {
      this.isLogin = !this.isLogin
      this.currentUser = username
      console.log(this.currentUser)
    },
    logout: function () {
      this.isLogin = false
      // localStorage.removeItem('jwt')
      this.$router.push({name:"Home"})
    }
  },
  created () {
    this.getMovies()

    // const token = localStorage.getItem('jwt')
    // if (token) {
    //   this.isLogin= true
    // }
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
