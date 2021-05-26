<template>
  <div class="padding background-img4">
    <h1>Movit 리뷰 수정</h1>
    <br><br>
    <div class="mb-3 row">
      <label for="title" class="form-label" style="text-align:left">제목</label>
      <input 
        v-model="review.title" 
        placeholder="제목을 입력해주세요." 
        type="text" 
        class="form-control"
        style="background-color:rgb(29, 26, 26); color:white; border-color:gray"
        id="title" >
    </div>
    <div class="mb-3 row">
      <label for="content" class="form-label" style="text-align:left">내용</label>
      <textarea 
        v-model="review.content" 
        placeholder="내용을 입력해 주세요"
        style="background-color:rgb(29, 26, 26); color:white; border-color:gray"
        class="form-control" id="content" rows="10"></textarea>
    </div>
    <button @click="updateReviewDetail" class="btn btn-dark btn-sm">저장</button>&nbsp;
    <button @click="cancle" class="btn btn-warning btn-sm">취소</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name:'ReviewUpdate',
  data (){
    return{
      review : {
        title:'',
        content:'',
      }
    }
  },
  methods:{
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`,
      }
      return config
    },
    updateReviewDetail: function () {
      axios({
        method:'put',
        url: `http://127.0.0.1:8000/community/update/${this.$route.params.reviewId}/`,
        data: this.review,
        headers: this.setToken(),
      })
        .then(() =>{
          this.$router.push({name:'Community'})
        })
        .catch((err) => {
          alert(err)
        })
    },
    cancle () {
      this.$router.push({
        path:'/community'
      })
    }
  },
  created () {
    axios({
      method:'get',
      url: `http://127.0.0.1:8000/community/update/${this.$route.params.reviewId}/`,
      headers: this.setToken(),
    })
      .then((res) =>{
        this.review.content = res.data.content
        this.review.title = res.data.title
      })
      .catch((err) => {
        console.log(err)
      })
  }
}
</script>

<style>
  .background-img4 { 
    background: linear-gradient(rgba(0,0,0,0.7),rgba(0,0,0,0.7)),url('data/harry.jpg');
    background-size:cover;
    height:100vh;
    /* background-color: black; */
    background-repeat: no-repeat;
  }
</style>