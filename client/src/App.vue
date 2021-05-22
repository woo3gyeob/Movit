<template>
  <div id="app">
    <div id="nav">
      <router-link :to="{name:'Home'}">Home</router-link> |
      <router-link :to="{name:'RecommendMovie'}">추천 영화</router-link> |
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
      @login="isLogin=true"
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
    }
  },
  methods: {
    getMovies: function () {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/movies/',
        // url: 'https://api.themoviedb.org/3/movie/top_rated?api_key=ba63b1ddcacdc9265f089a977d88f6e0&language=ko-KR',
      })
        .then(res => {
          this.movies = res.data.results
          console
        })
        .catch(err => { 
          console.log(err)
        })
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
  }
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
