<template>
  <div>
     <div class="mb-3 row">
        <label for="title" class="form-label">제목</label>
        <input v-model="review.title" placeholder="제목을 입력해주세요." type="text" class="form-control" id="title" >
      </div>
      <div class="mb-3 row">
        <label for="content" class="form-label">내용</label>
        <textarea 
          v-model="review.content" 
          placeholder="내용을 입력해 주세요"
          class="form-control" id="content" rows="3"></textarea>
      </div>
    <button @click="updateReviewDetail">저장</button>&nbsp;
    <button @click="cancle">취소</button>
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

</style>