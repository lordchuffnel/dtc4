<template>
  <div class='auth-container'>
    <label for="username">User name</label><br />
    <input placeholder="username" id="username" v-model="username" /><br />
    <label for="password">Password</label><br />
    <input
      placeholder="password"
      id="password"
      v-model="password"
      type="password"
    /><br />
    <button @click="login()" v-if="loginMode">Login</button>
    <button @click="register()" v-else>Register</button>
    <p @click="loginMode = false" v-if="loginMode">
      Don't have an account yet? Register Here
    </p>
    <p @click="loginMode = true" v-else>Already have an account. Login here.</p>
  </div>
</template>

<script>
// import axios from 'axios';
export default {
  name: 'Auth',
  data() {
    return {
      username: '',
      password: '',
      loginMode: false,
    };
  },
  created() {
    if (this.$cookies.isKey('dtc4-token')) {
      this.$router.push('/');
    }
  },
  methods: {
    login() {
      fetch('http://127.0.0.1:8000/auth/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          username: this.username,
          password: this.password,
        }),
      })
        .then((res) => res.json())
        .then((res) => {
          this.$cookies.set('dtc4-token', res.token, '30d');
          this.$router.push('/')
        })
        .catch((err) => console.log(err));
    },
    register() {
      fetch(`http://127.0.0.1:8000/api/users/`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          username: this.username,
          password: this.password,
        }),
      })
        .then(() => {
          this.login();
        })
        .catch((err) => console.log(err));
    },
  },
};
</script>

<style scoped>
.auth-container {
  width: 50%;
  margin: 50px 25%;
}
</style>