// components/AddPostIt.js
import { useState } from 'react';
import { useRouter } from 'next/router';
import Cookies from 'js-cookie';
import axios from 'axios';

export default function AddPostIt() {
  const [title, setTitle] = useState('');
  const [content, setContent] = useState('');
  const router = useRouter();

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      await axios.post('http://localhost:8000/todo', { title: title, content: content }, {
        headers: {
            Authorization: `Bearer ${Cookies.get('jwt_token')}`
        }
      });
      alert('Post-it added successfully!');
      router.push("/NoteView")
    } catch (error) {
      console.error('Error adding post-it:', error);
    }
  };

  return (
    <div className="add-postit">
      <h2>Add New Post-it</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Title"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
        />
        <textarea
          placeholder="Content"
          value={content}
          onChange={(e) => setContent(e.target.value)}
        />
        <button type="submit">Add Post-it</button>
      </form>
    </div>
  );
}

//TESTE