'use client'
// cat, duck, frog, gorilla, hen, penguin, rabbit, shark, tiger, tutle
const examplePosts = [
  {
    "image": "/cat.png",
    "title": "Project Phoenix: Reimagining Remote Collaboration",
    "description": "Project Phoenix is a next-generation collaboration platform designed to empower teams working across multiple time zones. By leveraging cutting-edge technologies, we aim to streamline communication, enhance workflow visibility, and reduce operational overhead.",
    "likes": "2",
    "members": "5"
  },
  {
    "image": "/duck.png",
    "title": "Plant Care Tracking System",
    "description": "Need developers for a mobile app that reminds users when to water their plants.",
    "likes": "1",
    "members": "0"
  },
  {
    "image": "/frog.png",
    "title": "Budget Management Tool for Students",
    "description": "Seeking collaboration on a financial app designed specifically for college students.",
    "likes": "10",
    "members": "10"
  },
  {
    "image": "/gorilla.png",
    "title": "Local Farmers Market Finder",
    "description": "Anyone interested in creating a map-based app for finding farmers markets nearby?",
    "likes": "12",
    "members": "1"
  },
  {
    "image": "/hen.png",
    "title": "Language Exchange Platform",
    "description": "Looking for partners to build a platform connecting language learners worldwide.",
    "likes": "223",
    "members": "20"
  },
  {
    "image": "/penguin.png",
    "title": "Volunteer Opportunity Aggregator",
    "description": "Need help creating a website that collects volunteer opportunities from multiple sources.",
    "likes": "23",
    "members": "5"
  },
  {
    "image": "/rabbit.png",
    "title": "Sustainable Recipe Finder",
    "description": "Seeking developers for an app that suggests recipes based on seasonal ingredients.",
    "likes": "0",
    "members": "0"
  },
  {
    "image": "/shark.png",
    "title": "Freelancer Project Management Tool",
    "description": "Looking for collaborators on a specialized tool for managing freelance projects.",
    "likes": "55",
    "members": "3"
  },
  {
    "image": "/tiger.png",
    "title": "Community Book Exchange Platform",
    "description": "Need help building an app where neighbors can share and borrow books.",
    "likes": "10",
    "members": "5"
  },
  {
    "image": "/turtle.png",
    "title": "Meditation Timer with Progress Tracking",
    "description": "Seeking partners to develop a meditation app with visual progress metrics.",
    "likes": "29",
    "members": "8"
  }
];

const randomDevs = [
  {
    "name": "Sarah Chen",
    "rating": 5,
    "specialty": "React",
    "yearsExperience": 7,
    "hourlyRate": 85,
    "image": "/cat.png"
  },
  {
    "name": "Michael Rodriguez",
    "rating": 5,
    "specialty": "Full Stack",
    "yearsExperience": 9,
    "hourlyRate": 95,
    "image": "/turtle.png"
  },
  {
    "name": "Aisha Patel",
    "rating": 9,
    "specialty": "UI/UX",
    "yearsExperience": 6,
    "hourlyRate": 80,
    "image": "/tiger.png"
  },
  {
    "name": "David Kim",
    "rating": 9,
    "specialty": "Node.js",
    "yearsExperience": 5,
    "hourlyRate": 75,
    "image": "/turtle.png"
  },
  {
    "name": "Emma Johnson",
    "rating": 8,
    "specialty": "Mobile Development",
    "yearsExperience": 8,
    "hourlyRate": 90,
    "image": "/shark.png"
  },
  {
    "name": "Jamal Washington",
    "rating": 7,
    "specialty": "DevOps",
    "yearsExperience": 7,
    "hourlyRate": 85,
    "image": "/duck.png"
  },
  {
    "name": "Olivia Martinez",
    "rating": 8,
    "specialty": "Python",
    "yearsExperience": 6,
    "hourlyRate": 80,
    "image": "/hen.png"
  },
  {
    "name": "Liam Nguyen",
    "rating": 9,
    "specialty": "Data Science",
    "yearsExperience": 8,
    "hourlyRate": 95,
    "image": "/cat.png"
  },
  {
    "name": "Sophie Williams",
    "rating": 9,
    "specialty": "Cloud Architecture",
    "yearsExperience": 9,
    "hourlyRate": 10,
    "image": "/cat.png"
  },
  {
    "name": "Raj Patel",
    "rating": 9,
    "specialty": "Blockchain",
    "yearsExperience": 5,
    "hourlyRate": 90,
    "image": "/cat.png"
  }
];

import { useState, useEffect } from 'react';
import ProjectModal from '@/components/ProjectModal';

import { Heart, Users } from 'lucide-react';
import { useRouter } from 'next/navigation';

export default function Posts() {
  const router = useRouter();
  const [ message, setMessage ] = useState('Loading...');
  const [ posts, setPosts ] = useState(examplePosts);
  const [ topUsers, setTopUsers ] = useState(
    [ ...randomDevs ].sort((a,b) => b.rating - a.rating)
  );

  const [ isModalOpen, setIsModalOpen ] = useState(false);

  const handleSubmit = (data) => {
    console.log(data);
  }

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
    <div className="flex flex-col md:flex-row gap-6 py-6 px-34 min-h-screen">
      <div className='w-full md:w-3/4 space-y-4'>
        {posts.map((post) => (
          <div key={post.title} className='flex flex-col border-b border-t border-l-0 border-r-0 rounded-lg shadow-md p-4 hover:shadow-lg transition-shadow duration-300 cursor-pointer' onClick={() => router.push('/individualpost')}>
            <div 
              key={post.title} 
              className='flex flex-col md:flex-row'
            >
              <div className='mr-4 mb-3 md:mb-0'>
                <img
                  src={post.image}
                  alt='Profile image'
                  className='rounded-lg w-16 h-16 object-cover'
                />
              </div>
              <div className='flex-1'>
                <h1 className='font-bold text-xl text-gray-800 dark:text-gray-200 mb-2'>{post.title}</h1>
                <p className='text-md text-gray-600 dark:text-gray-300'>{post.description}</p>
              </div>
            </div>
            <div className='flex justify-left mt-3 flex-row items-center space-x-4'>
                <div className='flex flex-row justify-center items-center space-x-2'>
                  <span>{post.likes}</span>
                  <Heart className='w-4 h-4'/>
                </div>
                <div className='flex flex-row justify-center items-center space-x-2'>
                  <span>{post.members}</span>
                  <Users className='w-4 h-4' />
                </div>
              </div>
          </div>
        ))}
      </div>
      {/* Sidebar */}
      <div className='w-full md:w-1/4'>
        <div className='rounded-lg shadow-md p-4 top-6'>
          <h1 className='font-bold text-xl text-gray-800 dark:text-gray-100 mb-4 border-b border-gray-200 pb-2'>Top Developers</h1>
          <div className='space-y-2'>
            {topUsers.map((dev) => (
              <div key={dev.name} className='flex items-center space-x-3 p-2 hover:bg-gray-100 dark:hover:bg-gray-700 rounded-lg transition-colors duration-200'>
              {/* Left: Image */}
              <div className='flex-shrink-0'>
                <img
                  src={dev.image}
                  className='w-12 h-12 rounded-full object-cover'
                />
              </div>
              {/* Right: Name & Rating */}
              <div className='flex flex-col'>
                <a
                  href={`#${dev.name}`}
                  className='font-medium text-gray-800 dark:text-white hover:underline'
                >
                  {dev.name}
                </a>
                <div className='text-sm text-gray-500 dark:text-gray-400 flex items-center'>
                  <span>Rating: {dev.rating}/10</span>
                </div>
              </div>
            </div>
            ))}
          </div>
        </div>
        <div className='rounded-lg shadow-md p-4 sticky top-6'>
          <h1 className='font-bold text-xl text-gray-800 dark:text-gray-100 mb-4 border-b border-gray-200 pb-2'>Top Posts</h1>
          <div className='space-y-2'>
            {posts.map((post) => (
              <a
                key={post.title}
                href={`#${post.title}`}
                className='block p-2 hover:bg-gray-500 rounded transition-colors duration-200 text-gray-700 dark:text-white'
              >
                {post.title}
              </a>
            ))}
          </div>
        </div>
      </div>
      <ProjectModal
        isOpen={isModalOpen}
        onClose={() => setIsModalOpen(false)}
        onSubmit={handleSubmit}
      />
    </div>
  );
}
