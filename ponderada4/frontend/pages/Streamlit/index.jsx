// Página que redireciona para o Streamlit
import { useEffect, useState } from 'react';
import Cookies from 'js-cookie';

export default function RedirectStreamlit() {
  const [token, setToken] = useState('');

  useEffect(() => {
    // Recupere o token JWT do cookie
    const jwtToken = Cookies.get('jwt_token');

    if (jwtToken) {
      setToken(jwtToken);
    }
  }, []);

  return (
    <div>
      {token && (
        <iframe
          src={`http://54.163.165.25:8501/?token=${token}`} // Substitua pela URL real do servidor Streamlit
          width="100%"
          height="800px"
          title="Streamlit App"
        ></iframe>
      )}
    </div>
  );
}
