// pages/NotesPage.js
import { useState } from 'react';
import Note from '../Note';
import Head from 'next/head';
import basestyle from'../../styles/Home.module.css';
import styles from '../../styles/notes.module.css';

export default function NotesPage() {
  const [newNote, setNewNote] = useState('');
  const [notes, setNotes] = useState([]);

  const addNote = () => {
    if (newNote.trim() !== '') {
      setNotes([...notes, newNote]);
      setNewNote('');
    }
  };

  return (
    <div className="notes-container">
      <Head>
        <title>Notes</title>
      </Head>

      <h1>My Notes</h1>
      <div className="notes-list">
        {notes.map((note, index) => (
          <Note key={index} text={note} />
        ))}
      </div>
      <div className="note-input">
        <input
          type="text"
          placeholder="Enter a new note..."
          value={newNote}
          onChange={(e) => setNewNote(e.target.value)}
        />
        <button onClick={addNote}>Add Note</button>
      </div>
    </div>
  );
}

//TESTE