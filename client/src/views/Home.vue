<template>
  <div class="home">
    <div class="d-flex flex-row">
      <MovieCard v-for="movie in movies" :key="movie.id" :moviePoster="movie" :currentUserId="currentUserId"/>
    </div>
    <div class="d-flex flex-row">
      <MovieCard v-for="recomMovie in recommendedMovies" :key="recomMovie.id" :moviePoster="recomMovie" :currentUserId="currentUserId"/>
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
  props:{
    currentUserId: {
      type: Number,
    }
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
    getMoviePoster: function () {
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
    getRecommendedMoviePoster: function () {
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
    this.getMoviePoster()
    this.getRecommendedMoviePoster()
  }

}
</script>

<style>

</style>
