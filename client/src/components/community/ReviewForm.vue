<template>
  <div>
    <div>
      <h1>Movit</h1>
      <br><br><br>
      <div class="mb-3">
        <h4 for="title" class="form-label" style="text-align:left; color:white">제목</h4>
        <input 
          v-model="review.title" 
          placeholder="제목을 입력해주세요." 
          type="text" 
          class="form-control" 
          id="title" 
          style="background-color:rgb(29, 26, 26); color:white; border-color:gray"
          >
      </div>
      <br><br>
      <div class="mb-3">
        <h4 for="content" class="form-label" style="text-align:left; color:white">내용</h4>
        <textarea 
          v-model="review.content" 
          placeholder="내용을 입력해 주세요"
          class="form-control" 
          id="content" 
          rows="10"
          style="background-color:rgb(29, 26, 26); color:white; border-color:gray"
          >
          </textarea>
      </div>
      <br>
      <button @click="uploadReview" class="btn btn-warning btn-sm">저장</button>&nbsp;
      <button @click="cancle" class="btn btn-dark btn-sm">취소</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name:'ReviewForm',
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
    uploadReview () {
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/community/create/',
        data: this.review,
        headers: this.setToken(),
      })
        .then(res => {
          console.log(res)
          this.$router.push({
            path:'/community'
          })
        })
        .catch(err => {
          console.log(err)
        })
    },
    cancle () {
      this.$router.push({
        path:'/community'
      })
    }
  }
}
</script>

<style>

</style>