<template>
  <div>
    <div class="shadow">
      <li v-for="favoriteMovie in myFavoriteMovies" :key="favoriteMovie.id" class="shadow">
        <h4>{{ favoriteMovie.title }}</h4>
      </li>
    </div>
  </div>
</template>

<script>
// import axios from 'axios'

export default {
  name:'MyMovieList',
  data (){
    return {
      myFavoriteMovies: [
        {
          id:123,
          title: '영화제목',
          overview:'줄거리',
        },
        {
          id:4556,
          title: '영화제목2',
          overview:'줄거리',

        }
      ],
    }
  },
  methods:{
    getFavoriteMovies () {
      // axios({
      //   method:'get',
      //   url:'',
      // })
      //   .then(res => {
      //     console.log()
      //     this.myFavoriteMovies = res
      //   })
      //   .catch(err => {
      //     console.log(err)
      //   })
    },
  },
  created () {
    // this.getFavoriteMovies()
  }

}
</script>

<style scoped>
  ul {
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
  }
  input:focus {
    outline: none;
  }
</style>