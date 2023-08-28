// pages/api/todo.js
//import { database } from '../../../backend/app/db'; // Importe o database do seu código

export default async function handler(req, res) {
  if (req.method === 'POST') {
    const { title, content } = req.body;
    // Lógica para adicionar a tarefa ao banco de dados usando o ORM ou código SQL
    // Por exemplo: await database.execute(...) ou await Todo.create(...)
    res.status(201).json({ message: 'Todo added successfully' });
  } else {
    res.status(405).json({ message: 'Method not allowed' });
  }
}

// Compare this snippet from ponderada2/backend/app/routes/todo.routes.js: