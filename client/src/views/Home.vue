<template>
  <div class="home">
    <div class="d-flex flex-row">
      <MovieCard v-for="movie in movies" :key="movie.id" :movie="movie"/>
    </div>
    <div class="d-flex flex-row">
      <MovieCard v-for="recomMovie in recommendedMovies" :key="recomMovie.id" :movie="recomMovie"/>
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
      recommendedMovies: [],
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
    getRecommendedMovies: function () {
      axios({
        method:'get',
        url: 'http://127.0.0.1:8000/movies/recommend/',
        headers: this.setToken(),
      })
        .then(res => {
          this.recommendedMovies = res.data
        })
        .catch(err => { 
          console.log(err)
        })
    },
  },
  created() {
    this.getMovies()
    this.getRecommendedMovies()
  }

}
</script>

<style>

</style>
