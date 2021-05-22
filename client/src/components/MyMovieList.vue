<template>
  <div>
    <div class="input-box shadow">
        <input type="text" v-focus v-model="inputMovie" v-on:keypress.enter="addFavoriteMovie" placeholder="좋아하는 영화를 입력하세요.">
       <button v-on:click="addFavoriteMovie">추가</button>

       <span class="add-container" v-on:click="addFavoriteMovie">
          <i class="add-btn fa fa-plus" aria-hidden="true"></i>
       </span>
    </div>

    <li v-for="favoriteMovie in myFavoriteMovies" :key="favoriteMovie.id" class="shadow">
      <h4>{{ favoriteMovie.title }}</h4>

    </li>
  </div>
</template>

<script>
// import axios from 'axios'

export default {
  name:'MyMovieList',
  data (){
    return {
      inputMovie:'',
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
    addFavoriteMovie () {
      // 추가 기능 영화제목 입력하면, 영화 정보 보내주는 걸로
      const newMovie = {
        title: this.inputMovie
        // id:, 아이디는 어케 처리하지
      }
      this.myFavoriteMovies.push(newMovie) 
      this.inputMovie=''  
    }
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
  .input-box {
    background: white;
    height: 50px;
    line-height: 50px;
    border-radius: 5px;
  }
  .input-box input {
    border-style: none;
    font-size: 0.9rem;
  }
  .add-container {
    float: right;
    background: linear-gradient(to right, #6478FB, #8763FB);
    display: inline-block;
    width: 3rem;
    border-radius: 0 5px 5px 0;
    cursor: pointer;
  }
  .add-btn {
    color: white;
  }
</style>