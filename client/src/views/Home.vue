<template>
  <div class="home">
    <div class="d-flex flex-row">
      <MovieCard v-for="movie in movies" :key="movie.id" :movie="movie"/>
    </div>
 </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios'
import MovieCard from '@/components/MovieCard'

export default {
  name: 'Home',
  components:{
    MovieCard,
  },
  data () {
    return {
      movies: [],
    }
  },
  methods: {
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`,
      }
      return config
    },
    getMovies: function () {
      axios({
        method:'get',
        url: 'http://127.0.0.1:8000/movies/',
        headers: this.setToken(),
      })
        .then(res => {
          this.movies = res.data
        })
        .catch(err => { 
          console.log(err)
        })
    },
  },
  created() {
    this.getMovies()
  }

}
</script>

<style>

</style>
