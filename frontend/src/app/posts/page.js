'use client'

const examplePosts = [
  {
    "image": "https://plus.unsplash.com/premium_photo-1689568126014-06fea9d5d341?fm=jpg&q=60&w=3000&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8cHJvZmlsZXxlbnwwfHwwfHx8MA%3D%3D",
    "title": "Weather App with Mood Recommendations",
    "description": "Looking for help building an app that suggests activities based on local weather."
  },
  {
    "image": "https://plus.unsplash.com/premium_photo-1689568126014-06fea9d5d341?fm=jpg&q=60&w=3000&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8cHJvZmlsZXxlbnwwfHwwfHx8MA%3D%3D",
    "title": "Plant Care Tracking System",
    "description": "Need developers for a mobile app that reminds users when to water their plants."
  },
  {
    "image": "https://plus.unsplash.com/premium_photo-1689568126014-06fea9d5d341?fm=jpg&q=60&w=3000&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8cHJvZmlsZXxlbnwwfHwwfHx8MA%3D%3D",
    "title": "Budget Management Tool for Students",
    "description": "Seeking collaboration on a financial app designed specifically for college students."
  },
  {
    "image": "https://plus.unsplash.com/premium_photo-1689568126014-06fea9d5d341?fm=jpg&q=60&w=3000&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8cHJvZmlsZXxlbnwwfHwwfHx8MA%3D%3D",
    "title": "Local Farmers Market Finder",
    "description": "Anyone interested in creating a map-based app for finding farmers markets nearby?"
  },
  {
    "image": "https://plus.unsplash.com/premium_photo-1689568126014-06fea9d5d341?fm=jpg&q=60&w=3000&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8cHJvZmlsZXxlbnwwfHwwfHx8MA%3D%3D",
    "title": "Language Exchange Platform",
    "description": "Looking for partners to build a platform connecting language learners worldwide."
  },
  {
    "image": "https://plus.unsplash.com/premium_photo-1689568126014-06fea9d5d341?fm=jpg&q=60&w=3000&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8cHJvZmlsZXxlbnwwfHwwfHx8MA%3D%3D",
    "title": "Volunteer Opportunity Aggregator",
    "description": "Need help creating a website that collects volunteer opportunities from multiple sources."
  },
  {
    "image": "https://plus.unsplash.com/premium_photo-1689568126014-06fea9d5d341?fm=jpg&q=60&w=3000&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8cHJvZmlsZXxlbnwwfHwwfHx8MA%3D%3D",
    "title": "Sustainable Recipe Finder",
    "description": "Seeking developers for an app that suggests recipes based on seasonal ingredients."
  },
  {
    "image": "https://plus.unsplash.com/premium_photo-1689568126014-06fea9d5d341?fm=jpg&q=60&w=3000&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8cHJvZmlsZXxlbnwwfHwwfHx8MA%3D%3D",
    "title": "Freelancer Project Management Tool",
    "description": "Looking for collaborators on a specialized tool for managing freelance projects."
  },
  {
    "image": "https://plus.unsplash.com/premium_photo-1689568126014-06fea9d5d341?fm=jpg&q=60&w=3000&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8cHJvZmlsZXxlbnwwfHwwfHx8MA%3D%3D",
    "title": "Community Book Exchange Platform",
    "description": "Need help building an app where neighbors can share and borrow books."
  },
  {
    "image": "https://plus.unsplash.com/premium_photo-1689568126014-06fea9d5d341?fm=jpg&q=60&w=3000&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8cHJvZmlsZXxlbnwwfHwwfHx8MA%3D%3D",
    "title": "Meditation Timer with Progress Tracking",
    "description": "Seeking partners to develop a meditation app with visual progress metrics."
  }
];

const randomDevs = [
  {
    'name': 'Sarah Chen',
    'rating': 4.8,
    'specialty': 'React',
    'yearsExperience': 7,
    'hourlyRate': 85
  },
  {
    'name': 'Michael Rodriguez',
    'rating': 4.9,
    'specialty': 'Full Stack',
    'yearsExperience': 9,
    'hourlyRate': 95
  },
  {
    'name': 'Aisha Patel',
    'rating': 4.7,
    'specialty': 'UI/UX',
    'yearsExperience': 6,
    'hourlyRate': 80
  },
  {
    'name': 'David Kim',
    'rating': 4.5,
    'specialty': 'Node.js',
    'yearsExperience': 5,
    'hourlyRate': 75
  },
  {
    'name': 'Emma Johnson',
    'rating': 5.0,
    'specialty': 'Mobile Development',
    'yearsExperience': 8,
    'hourlyRate': 90
  },
  {
    'name': 'Jamal Washington',
    'rating': 4.6,
    'specialty': 'DevOps',
    'yearsExperience': 7,
    'hourlyRate': 85
  },
  {
    'name': 'Olivia Martinez',
    'rating': 4.9,
    'specialty': 'Python',
    'yearsExperience': 6,
    'hourlyRate': 80
  },
  {
    'name': 'Liam Nguyen',
    'rating': 4.7,
    'specialty': 'Data Science',
    'yearsExperience': 8,
    'hourlyRate': 95
  },
  {
    'name': 'Sophie Williams',
    'rating': 4.8,
    'specialty': 'Cloud Architecture',
    'yearsExperience': 9,
    'hourlyRate': 100
  },
  {
    'name': 'Raj Patel',
    'rating': 4.6,
    'specialty': 'Blockchain',
    'yearsExperience': 5,
    'hourlyRate': 90
  }
];

import { useState, useEffect } from 'react';

import { Heart, Users } from 'lucide-react';

export default function Posts() {
  const [ message, setMessage ] = useState('Loading...');
  const [ posts, setPosts ] = useState(examplePosts);

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
    <div className="flex flex-col md:flex-row gap-6 p-6 min-h-screen">
      <div className='w-full md:w-3/4 space-y-4'>
        {posts.map((post) => (
          <div 
            key={post.title} 
            className='flex flex-col md:flex-row border-1 rounded-lg shadow-md p-4 hover:shadow-lg transition-shadow duration-300 cursor-pointer'
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
            <div className='flex justify-center flex-col items-center'>
              <div className='flex flex-row justify-center items-center space-x-2'>
                <span>1</span>
                <Heart className='w-4 h-4'/>
              </div>
              <div className='flex flex-row justify-center items-center space-x-2'>
                <span>10</span>
                <Users className='w-4 h-4' />
              </div>
            </div>
          </div>
        ))}
      </div>
      {/* Sidebar */}
      <div className='w-full md:w-1/4'>
        <div className='rounded-lg shadow-md p-4 sticky top-6'>
          <h1 className='font-bold text-xl text-gray-800 dark:text-gray-100 mb-4 border-b border-gray-200 pb-2'>Top Developers</h1>
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
        <div className='w-full md:w-1/4'>
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
    </div>
  );
}
