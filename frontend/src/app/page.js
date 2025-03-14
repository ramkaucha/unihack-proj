'use client'

import { useState, useEffect } from 'react';

export default function Home() {
  const [ message, setMessage ] = useState('Loading...');
  useEffect(() => {
    const apiUrl = process.env.NEXT_PUBLIC_API_URL;

  
    fetch(`${apiUrl}/`).then(response => {
      if (!response.ok) {
        console.error("Network response error");
      }

      return response.json();
    }).then(data => {
        setMessage(data.message);
      }).catch(error => {
        console.error(error);
      });
  }, []);

  return (
    <div className="flex justify-center items-center min-h-screen">
      <h1 className="text-4xl font-bold text-center">{message}</h1>
    </div>
  )
}
