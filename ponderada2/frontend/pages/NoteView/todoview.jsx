// pages/PostItPage.js
import { useRouter } from 'next/router';
import { useEffect, useState } from 'react';
import axios from 'axios';


export default function PostItPage() {
  const router = useRouter();
  const { id } = router.query;
  const [postIt, setPostIt] = useState({ title: '', content: '' });
  NoteView
  useEffect(() => {
    if (id) {
      fetchPostIt();
    }
  }, [id]);

  const fetchPostIt = async () => {
    try {
      const response = await axios.get(`http://localhost:8000/todo`); // Rota para obter um post-it específico
      setPostIt(response.data); // Supondo que a resposta contém title e content
    } catch (error) {
      console.error('Error fetching post-it:', error);
    }
  };

  return (
    <div className="postit-page">
      <h1>Post-it Details</h1>
      <h2>{postIt.title}</h2>
      <p>{postIt.content}</p>
    </div>
  );
}

//TESTE