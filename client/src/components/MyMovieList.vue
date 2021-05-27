<template>
  <div class="background-img">
  <div class="container">
    <br><br>
    <h2 class="mx-5 px-5" style="text-align:left">내가 좋아한 영화들</h2>
      <div>
        <div class="row mx-5"><hr><br>
          <div class="col-2" v-for="favoriteMovie in myFavoriteMovies" :key="favoriteMovie.id">
            <div class="card" style="border-color:black">
              <img class="img-fluid imggroup3" :src="`https://image.tmdb.org/t/p/original${favoriteMovie.poster_path}`" alt="poster" style="cursor: pointer;">
            </div>
          </div>
        </div>
      </div>
      <div v-if="!myFavoriteMovies.length">"좋아요한 영화가 없습니다."</div>
  </div>`
  </div>
</template>


<script>

export default {
  name:'MyMovieList',
  components: { 

  },
  props: {
    myFavoriteMovies:{
      type: Array
    }  
  },
  data() {
    return {
      slides:7
    }
  },
  created () {
  }

}
</script>

<style scoped>
  input:focus {
    outline: none;
  }
  h2 {
    text-align: left;
    color: white;
  }
  a {
    text-decoration: none;
    color: white;
  }
  .background-img { 
    background: linear-gradient(rgba(0,0,0,0.7),rgba(0,0,0,0.6)),url('../data/marvel.jpg');
    background-color: black;
    height:100vh;
    background-repeat: no-repeat;
  }
  .imggroup3:hover {
    border-color: white;
    border-style: solid;
    transition-duration:0.1s;
  }
  .imggroup3 {
    box-shadow: 0 4px 8px 0 rgba(255, 255, 255, 0.4), 0 6px 20px 0 rgba(255, 255, 255, 0.2);
  }
</style>