'use client'
import { useState, useEffect } from 'react';
import TypeWriter from '@/components/TypeWrite';
import { Button } from '@/components/ui/button';
import { Image } from 'next/image';
import Pattern from '@/components/RandomPattern';
import { useRouter } from 'next/navigation';

export default function Home() {
  const router = useRouter();
  useEffect(() => {
    const apiUrl = process.env.NEXT_PUBLIC_API_URL;
    fetch(`${apiUrl}/`).then(response => {
      if (!response.ok) {
        console.error("Network response error");
      }

      return response.json();
    }).then(data => {
        console.log('nothing');
      }).catch(error => {
        console.error(error);
      });
  }, []);

  return (
      <div className="relative flex flex-col min-h-screen overflow-hidden">
        {/* Top content section with centered items */}
        <div className="flex flex-col gap-6 p-6 items-center z-10 mt-16">
          <div>
            <TypeWriter
              text={["Real, Problems.", "Real Experience.", "Real Growth."]}
              speed={80}
              delay={200}
              loop={true}
              className='text-8xl font-bold text-center'
            />
          </div>
          <div>
            <p className='text-xl font-light text-center max-w-2xl'>
              Connect with developers eager to solve your unique challenges
              while building their portfolio with meaningful projects.
            </p>
          </div>
          <Button variant='secondary' className='text-md bg-orange-500 mt-2' onClick={() => router.push('/posts')}>
            Go to Our Posts
          </Button>
        </div>
        <div className="absolute bottom-0 left-0 w-full flex justify-center">
        <Pattern />
        </div>
      </div>
    );
}
