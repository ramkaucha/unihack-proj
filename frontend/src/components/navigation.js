"use client";

import { useEffect, useState } from "react";
import Link from "next/link";
import { motion } from "framer-motion";

import { ArrowRight, User } from "lucide-react";
import { ModeToggle } from "./NodeToggle";
import { Button } from "./ui/button";
import { useRouter } from "next/navigation";
import ThemeAwareImage from "./ThemeAwareImage";
import { isAuthenticated, removeToken } from "@/lib/auth";
import { DropdownMenu, DropdownMenuContent, DropdownMenuItem, DropdownMenuTrigger } from "@radix-ui/react-dropdown-menu";


export default function Navigation() {
  const [scrolled, setScrolled] = useState(false);
  const [ authenticated, setAuthenticated ] = useState(false);
  const router = useRouter();

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
              <DropdownMenu>
                <DropdownMenuTrigger asChild>
                  <button className="h-10 w-10 rounded-full bg-blue-600 text-white flex items-center justify-center hover:bg-blue-700 border-2 border-white dark:border-gray-700 focus:outline-none">
                    <User className="mr-2 h-4 w-4" />
                    <span>Profile</span>
                  </button>
                </DropdownMenuTrigger>
                <DropdownMenuContent align="end" className="w-56">
                  <DropdownMenuItem className="cursor-pointer" onClick={() => router.push('/settings')}>
                      <Settings className="mr-2 h-4 w-4" />
                      <span>Settings</span>
                    </DropdownMenuItem>
                    <DropdownMenuSeparator />
                    <DropdownMenuItem className="cursor-pointer text-red-500 focus:text-red-500" onClick={logout}>
                      <LogOut className="mr-2 h-4 w-4" />
                      <span>Logout</span>
                    </DropdownMenuItem>
                  </DropdownMenuContent>
              </DropdownMenu>
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
    </motion.header>
  );
}