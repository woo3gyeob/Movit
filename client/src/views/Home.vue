<template>
  <div class="home">
    <div class="d-flex flex-row">
      <MovieCard v-for="movie in movies" :key="movie.id" :movie="movie"/>
    </div>
 </div>
</template>

<script>
// @ is an alias to /src
import MovieCard from '@/components/MovieCard'

export default {
  name: 'Home',
  props: {
    movies: {
      type: Array,
    }
  },
  components:{
    MovieCard,
  },

}
</script>

<style>

</style>
