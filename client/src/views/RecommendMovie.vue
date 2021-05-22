<template>
  <div>
    추천영화
  </div>
</template>

<script>
export default {
  name: 'RecommendMovie',
  components: {
  },
  data() {
    return {
      recommendMovies:[],
    }
  },
  methods:{
    // getRecommendMovies: function () {
    //   axios({
    //     method: 'get',
    //     url: 'https://api.themoviedb.org/3/movie/top_rated?api_key=ba63b1ddcacdc9265f089a977d88f6e0&language=ko-KR',
    //   })
    //     .then(res => {
    //       this.recommendMovies = res
    //     })
    //     .catch(err => {
    //       console.log(err)
    //     })
    // },
  }
}
</script>

<style>

</style>