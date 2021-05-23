<template>
  <div>
    <div class="shadow">
      <ul v-for="favoriteMovie in myFavoriteMovies" :key="favoriteMovie.id" class="shadow">
        <h4>{{ favoriteMovie.title }}</h4>
        <div>{{ favoriteMovie.content }}</div>
      </ul>
      <div v-if="!myFavoriteMovies.length">"좋아요한 영화가 없습니다."</div>
    </div>
  </div>
</template>

<script>

export default {
  name:'MyMovieList',
  props: {
    myFavoriteMovies:{
      type: Array
    }  
  },
  methods:{
  },
  created () {
  }

}
</script>

<style scoped>
  /* ul {
    list-style-type: none;
    padding-left: 0px;
    width:75vh;
    margin-top: 0px;
    text-align: left;
  }
  li {
    display: flex;
    min-height: 50px;
    height: 100px;
    line-height: 50px;
    margin: 0.5rem 0;
    padding: 0 0.9rem;
    background: white;
    border-radius: 5px;
  } */
  input:focus {
    outline: none;
  }
</style>