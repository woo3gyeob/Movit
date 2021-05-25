<template>
  <div>
    <h1>Login</h1>
    <div>
      <label for="username">사용자 이름:</label>
      <input type="text" id="username" v-model="credentials.username">
    </div>
    <div>
      <label for="password">비밀번호:</label>
      <input type="password" id="password" v-model="credentials.password">
    </div>
    <button @click="login">로그인</button>
    <button @click="$router.push({name:'Signup'})">회원가입</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Login',
  data: function () {
    return {
      credentials :{
        username: '',
        password: '',
      },
    }
  },
  methods: {
    login: function () {
      axios({
        method:'post',
        url: 'http://127.0.0.1:8000/accounts/login/',
        data: this.credentials,
      })
        .then((res) => {
          localStorage.setItem('jwt', res.data.token)
          this.$emit('login', this.credentials.username)
          this.$router.push({name: 'Home'})
        })
        .catch(err => {
          alert(JSON.stringify(err.response.data))
          console.log(err)
        })
    }
  },
}
</script>
