<template>
  <div>
    <b-input v-model="review.title" placeholder="제목을 입력해주세요."></b-input>
    <b-form-textarea
        v-model="review.content"
        placeholder="내용을 입력해 주세요"
        rows="3"
        max-rows="6"
    ></b-form-textarea>
    <br>
    <b-button @click="uploadReview">저장</b-button>&nbsp;
    <b-button @click="cancle">취소</b-button>
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
    uploadReview () {
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/community/create/',
        data: this.review,
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