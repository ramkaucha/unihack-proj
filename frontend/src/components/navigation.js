"use client";

import { useEffect, useState } from "react";
import Link from "next/link";
import { motion } from "framer-motion";

import { ArrowRight, User, Settings, LogOut } from "lucide-react";
import { ModeToggle } from "./NodeToggle";
import { Button } from "./ui/button";
import { useRouter } from "next/navigation";
import { isAuthenticated, removeToken } from "@/lib/auth";
import { DropdownMenu, DropdownMenuContent, DropdownMenuItem, DropdownMenuTrigger } from "@radix-ui/react-dropdown-menu";
import ProjectModal from "./ProjectModal";


export default function Navigation() {
  const [scrolled, setScrolled] = useState(false);
  const [ authenticated, setAuthenticated ] = useState(false);
  const router = useRouter();
  const [ isModalOpen, setIsModalOpen ] = useState(false);

  const handlePostSubmit = (data) => {
    console.log(data);
  }

  useEffect(() => {
    setAuthenticated(isAuthenticated());

    const handleScroll = () => {
      if (window.scrollY > 10) {
        setScrolled(true);
      } else {
        setScrolled(false);
      }
    };

    window.addEventListener("scroll", handleScroll);

    return () => {
      window.removeEventListener("scroll", handleScroll);
    };
  }, []);

  const logout = () => {
    removeToken();
    router.push('/');
    location.reload();
  }

  return (
    <motion.header
      className={`fixed w-full top-0 z-50 transition-all duration-300 ${
        scrolled ? "bg-white/80 dark:bg-gray-800/80 backdrop-blur-sm shadow-md" : "bg-transparent"
      }`}
      initial={{ y: -100 }}
      animate={{ y: 0 }}
      transition={{ duration: 0.5 }}
    >
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-4 mb-4">
        <div className="flex justify-between items-center">
          <div className="flex items-center justify-center">
            <Link href="/" className="font-bold text-3xl dark:text-white text-black mt-3">
              Solve.
              {/* <ThemeAwareImage lightSrc="/logo-light.png" darkSrc="/logo.png" alt="Logo" height={80} width={100} /> */}
            </Link>
          </div>
          <nav className="flex space-x-6 items-center mt-3">
            {authenticated ? (
              <div className="flex flex-row space-x-6">
                <Button variant="primary" onClick={() => setIsModalOpen(true)}  className="pointer-cursor text-gray-900 dark:text-gray-300 transition-colors flex bg-green-500 items-center space-x-2 border-1 rounded-md py-2 px-3">Create Post</Button>
                <DropdownMenu>
                  <DropdownMenuTrigger asChild>
                    <Button variant="primary" className="p-0 overflow-hidden h-10 w-10 rounded-full">
                      <img
                        src="/cat.png"
                        alt="User Profile"
                        className="h-full w-full object-cover"
                      />
                    </Button>
                  </DropdownMenuTrigger>
                  <DropdownMenuContent align="end">
                    <DropdownMenuItem>
                      Profile
                    </DropdownMenuItem>
                    <DropdownMenuItem>
                      Settings
                    </DropdownMenuItem>
                    <DropdownMenuItem onClick={logout}>
                      Logout
                    </DropdownMenuItem>
                  </DropdownMenuContent>
                </DropdownMenu>
              </div>
            ) : (
              <Button onClick={() => router.push('/login')} variant="outline" className="text-gray-900 dark:text-gray-300 transition-colors flex flex-row items-center space-x-2 border-1 rounded-md py-2 px-3" >
                <span>Sign In!</span>
                <ArrowRight className="w-4 h-4" />
              </Button>
            )}
            <ModeToggle/>
          </nav>
        </div>
      </div>
      <ProjectModal
        isOpen={isModalOpen}
        onClose={() => setIsModalOpen(false)}
        onSubmit={handlePostSubmit}
      />
    </motion.header>
  );
}