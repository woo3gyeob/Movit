<template>
  <div class="container loginform m-5 p-5">
    <div class="m-5 p-5">
      <div class="m-5 p-5">
        <div class="m-5 p-5 cardstyle">
          <div class="mx-5 px-5">
            <h1>Login</h1>
            <b-form @submit="login" @reset="onReset" v-if="show">
              <b-form-group
                id="input-group-1"
                label="ID:"
                label-for="input-1"
                description="Welcome to NamJung-ne Movie"
              >
                <b-form-input
                  id="username" 
                  v-model="credentials.username"
                  type="text"
                  placeholder="Enter ID"
                  required
                ></b-form-input>
              </b-form-group>

              <b-form-group id="input-group-1" label="Password:" label-for="input-2">
                <b-form-input
                  id="password"
                  type="password"
                  v-model="credentials.password"
                  placeholder="Enter Password"
                  required
                ></b-form-input>
              </b-form-group>

              <b-button type="submit" variant="dark">로그인</b-button>
              <b-button type="reset" variant="warning">Reset</b-button>
            </b-form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<!--
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
-->

<script>
import axios from 'axios'
import Vue from 'vue'
import { BButton, BCard, BForm, BFormGroup, BFormInput } from 'bootstrap-vue'
Vue.component('b-button', BButton)
Vue.component('b-card', BCard)
Vue.component('b-form', BForm)
Vue.component('b-form-group', BFormGroup)
Vue.component('b-form-input', BFormInput)

export default {
  name: 'Login',
  data: function () {
    return {
      credentials :{
        username: '',
        password: '',
      },
      show: true
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
    },
    onReset(event) {
      event.preventDefault()
      this.credentials.username = ''
      this.credentials.password = ''
      this.show = false
      this.$nextTick(() => {
          this.show = true
      })
    },
  },
}
</script>

<style>
  .loginform {
    height: 3000;
  }
  #input-group-1 {
    text-align: left;
    color: yellow;
  }
  .cardstyle{
    background-color: black;
    border-radius: 60px;
    border-style: solid;
    border-color: gray
  }
</style>