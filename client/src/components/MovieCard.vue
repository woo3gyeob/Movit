<template>
  <div>
    <img 
      @click="imgClicked"   
      :src="`https://image.tmdb.org/t/p/original${movie.poster_path}`" 
      width="250px" alt="image">

    <MovieCardDetail v-if="isShowed" @close-modal="isShowed=false">
      <h3 slot="header">
        {{ movie.title }}
        <i class="fas fa-times cloesModalBtn" @click="isShowed=false"></i>
      </h3>
      <div slot="body">
        <img 
          :src="`https://image.tmdb.org/t/p/original${movie.poster_path}`" 
          width="250px" alt="image">
          개봉일 : {{ movie.release_date}}
        <div>{{ movie.overview }}</div>
      </div>
    </MovieCardDetail>
    <!-- Modal -->
  </div>
</template>

<script>
import MovieCardDetail from '@/components/MovieCardDetail'

export default {
  name: 'MovieCard',
  components:{
    MovieCardDetail
  },
  props:{
    movie:{
      type: Object,
    } 
  },
  data () {
    return {
      isShowed: false,
    }
  },
  computed:{

  },
  methods:{
    imgClicked: function () {
      this.isShowed = !this.isShowed
    }
  }
}
</script>


<style>


</style>