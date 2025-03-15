"use client";
import React, { useState } from "react";
import { motion } from "framer-motion";

export default function ProjectPage() {
  // State for handling expandable section
  const [isMembersExpanded, setIsMembersExpanded] = useState(false);

  const [projectDescription, setProjectDescription] = useState(`
    Project Phoenix is a next-generation collaboration platform designed to empower teams working across multiple time zones. 
    By leveraging cutting-edge technologies, we aim to streamline communication, enhance workflow visibility, and reduce operational overhead. 
    Ultimately, our goal is to create a seamless remote work environment that fosters productivity, innovation, and camaraderie, enabling organizations to adapt to the rapidly changing digital landscape.
  `);

  const [projectTitle, setProjectTitle] = useState(
    "Project Phoenix: Reimagining Remote Collaboration"
  );

  const handleSupportClick = () => {
    alert("Support");
  };

  const handleSolveClick = () => {
    alert("Solve");
  };

  const [statProject, setStatProject] = useState("Design"); // Set initial status here

  // Sample data for members and comments
  const members = [
    {
      username: "JohnDoe",
      role: "Project Manager",
    },
    {
      username: "JaneSmith",
      role: "Lead Developer",
    },
    {
      username: "AliceJohnson",
      role: "UI/UX Designer",
    },
    {
      username: "Addd",
      role: "UI/UX Designer 2",
    },
  ];

  // Assign avatars using the image names from your public folder
  const comments = [
    {
      user: "JohnDoe",
      comment: "Great work! Keep it up.",
      avatar: "/frog.png",
    },
    {
      user: "JaneSmith",
      comment: "I agree, the design looks amazing.",
      avatar: "/hen.png",
    },
    {
      user: "AliceJohnson",
      comment: "Thanks, I will work on the next iteration!",
      avatar: "/tiger.png",
    },
  ];

  // Handle expanding/collapsing member section
  const toggleMembersSection = () => {
    setIsMembersExpanded(!isMembersExpanded);
  };

  return (
    <div className="min-h-screen w-full bg-gray-50 dark:bg-gray-900">
      <div className="flex justify-center items-center">
        <h1 className="  my-21 text-3xl md:text-4xl font-bold text-blue-600 dark:text-blue-500">
          {projectTitle}
        </h1>
      </div>

      <div className="full-div flex justify-center ">
        <div className="max-w-7xl  flex justify-center gap-6">
          {/* First sub-div takes 75% of the width */}
          <div className="w-full md:w-2/4">
            <section className="mb-8">
              <p className="mt-5 text-base md:text-lg text-gray-700 dark:text-gray-300 text-justify">
                {projectDescription}
              </p>
            </section>

            {/* Section 2: Buttons */}
            <section className="my-20 flex justify-center gap-12">
              <button
                onClick={handleSupportClick}
                className="px-6 py-2 text-lg bg-blue-500 text-white rounded-full hover:bg-blue-600 transition-colors flex items-center gap-2"
              >
                <span className="text-2xl">👍</span> Support
              </button>
              <button
                onClick={handleSolveClick}
                className="px-6 py-2 text-lg bg-green-500 text-white rounded-full hover:bg-green-600 transition-colors flex items-center gap-2"
              >
                <span className="text-2xl">🧠</span> Solve
              </button>
            </section>
          </div>

          {/* Second sub-div takes 25% of the width */}
        </div>
      </div>

      <div className="w-full md:w-[30%]">
        {/* Section 3: Expandable Members Section */}
        <div className="w-full md:w-[100%]">
          <div className="mb-8 md:w-[100%]">
            <div className="w-full flex align-center items-center">
              <div className="w-full">
                <span className="text-blue-600 dark:text-blue-400 font-semibold hover:underline text-2xl font-bold text-gray-800 dark:text-gray-100">
                  Members
                </span>
              </div>
            </div>

            <div className="w-full flex flex-wrap gap-6 justify-start">
              {members.map((member, index) => {
                // Assign an avatar based on index (rotate through provided images)
                const avatars = [
                  "/frog.png",
                  "/hen.png",
                  "/tiger.png",
                  "/shark.png",
                  "/hen.png",
                  "/rabbit.png",
                ];
                const avatar = avatars[index % avatars.length];

                return (
                  <div
                    key={index}
                    className="w-full md:w-[40%] p-4 flex items-center border border-gray-200 dark:border-gray-700 rounded-lg shadow-sm bg-white dark:bg-gray-800"
                  >
                    <img
                      src={avatar}
                      alt={`${member.username} Avatar`}
                      className="w-12 h-12 rounded-full object-cover"
                    />
                    <div className="ml-4">
                      <h3 className="font-semibold text-lg text-gray-800 dark:text-gray-100">
                        {member.username}
                      </h3>
                      <p className="text-xs text-gray-600 mt-1 dark:text-gray-300">
                        {member.role}
                      </p>
                    </div>
                  </div>
                );
              })}
            </div>
          </div>
        </div>

        {/* Section 4: Project Status */}
        <section className="mb-10">
          <div className="flex items-center">
            <h2 className="text-2xl font-bold text-gray-800 dark:text-gray-100 mr-6">
              Project Status:
            </h2>
            <div className="mt-4 flex flex-wrap gap-6">
              {statProject === "Design" && (
                <span className="inline-block px-6 py-3 bg-yellow-300 text-gray-800 rounded-full text-base font-semibold">
                  In Design
                </span>
              )}
              {statProject === "Development" && (
                <span className="inline-block px-6 py-3 bg-blue-300 text-gray-800 rounded-full text-base font-semibold">
                  In Development
                </span>
              )}
              {statProject === "Done" && (
                <span className="inline-block px-6 py-3 bg-green-300 text-gray-800 rounded-full text-base font-semibold">
                  Done
                </span>
              )}
            </div>
          </div>
        </section>
      </div>

      {/* Container */}
      <div className="max-w-5xl mx-auto px-4 py-8 md:py-12">
        {/* Section 1: Title and Description */}

        {/* Section 5: Comment Section */}
        <section className="mb-8">
          <h2 className="text-2xl font-bold text-gray-800 dark:text-gray-100 mb-4">
            Comments
          </h2>
          <div className="space-y-4">
            {comments.map((comment, index) => (
              <div
                key={index}
                className="p-2 border border-gray-200 dark:border-gray-700 rounded-lg shadow-sm bg-white dark:bg-gray-800"
              >
                <div className="flex items-start space-x-3">
                  <img
                    src={comment.avatar}
                    alt={`${comment.user} Avatar`}
                    className="w-12 h-12 rounded-full object-cover"
                  />
                  <div>
                    <h3 className="font-semibold text-lg text-gray-800 dark:text-gray-100">
                      {comment.user}
                    </h3>
                    <p className="text-gray-600 dark:text-gray-300">
                      {comment.comment}
                    </p>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </section>
      </div>
    </div>
  );
}
