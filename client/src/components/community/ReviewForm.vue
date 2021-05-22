<template>
  <div>
    <b-input v-model="context.title" placeholder="제목을 입력해주세요."></b-input>
    <b-form-textarea
        v-model="context.content"
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
      context : {
        title:'',
        content:'',
        // username이랑 created_at 가져오는 방법 찾기
        username:'dfsf',
        created_at: '2020-12-23',
      }
    }
  },
  methods:{
    uploadReview () {
      this.$router.push({
        path:'/community'
      })
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/community/create/',
        data: this.context,
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