// pages/login.js
import { useState } from 'react';
import Head from 'next/head';
import styles from '../styles/Home.module.css';
import axios from 'axios';
import Cookies from 'js-cookie';

export default function AuthPage() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [isSignup, setIsSignup] = useState(false); // State para alternar entre login e signup

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      let response;
      if (isSignup) {
        response = await axios.post('http://34.206.160.255/users/signup', { email, password });
      } else {
        response = await axios.post('http://34.206.160.255/users/login', { email, password });
      }

      const token = response.data["acess token"]; // Supondo que o token é retornado na resposta
      console.log(isSignup ? 'Signup successful. Token:' : 'Login successful. Token:', token);

      // Armazene o token em um cookie com uma validade (em segundos)
      Cookies.set('jwt_token', token, { expires: 7 }); // Expira em 7 dias

    // Redirecione o usuário para a página Streamlit
    window.location.href = '/Streamlit'; // Substitua pela URL desejada

  } catch (error) {
    console.error(isSignup ? 'Signup error:' : 'Login error:', error);
    // Lidar com erros de login aqui, por exemplo, exibir uma mensagem de erro ao usuário.
  }
};
  return (
    <div className={styles.body}>
      <Head>
        <title className={styles.title}>{isSignup ? 'Signup' : 'Login'}</title>
      </Head>

      <div className={styles.logincard}>
        <h1 className={styles.title}>{isSignup ? 'Signup' : 'Login'}</h1>
        <form onSubmit={handleSubmit}>
          <div className="input-group">
            <label className = {styles.label}>Email:</label>
            <input className = {styles.input} type="email" value={email} onChange={(e) => setEmail(e.target.value)} />
          </div>
          <div className="input-group">
            <label className={styles.label}>Password:</label>
            <input className={styles.input} type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
          </div>
          <br/>
          <button className = {styles.button} type="submit">{isSignup ? 'Signup' : 'Login'}</button>
        </form>
        <p>
          {isSignup
            ? 'Already have an account?'
            : 'Don\'t have an account yet?'}
          <span
            className="auth-switch"
            onClick={() => setIsSignup(!isSignup)}
          >
            {isSignup ? 'Login' : 'Signup'}
          </span>
        </p>
      </div>
    </div>
  );
}

//TESTE