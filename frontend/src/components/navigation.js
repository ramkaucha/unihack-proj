"use client";

import { useEffect, useState } from "react";
import Link from "next/link";
import { motion } from "framer-motion";
import { ArrowRight } from "lucide-react";
import { ModeToggle } from "./NodeToggle";
import { Button } from "./ui/button";
import { useRouter } from "next/navigation";

export default function Navigation() {
  const [scrolled, setScrolled] = useState(false);
  const router = useRouter();

  useEffect(() => {
    const handleScroll = () => {
      if (window.scrollY > 10) {
        setScrolled(true);
      } else {
        setScrolled(false);
      }
    };

    window.addEventListener("scroll", handleScroll);

    // Cleanup
    return () => {
      window.removeEventListener("scroll", handleScroll);
    };
  }, []);

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
            <Link href="/" className="font-bold text-xl dark:text-white text-black mt-3">
              <img src="/logo.png" alt="logo" className="h-10"/>
            </Link>
          </div>
          <nav className="flex space-x-6 items-center mt-3">
            <Button onClick={() => router.push('/login')} variant="outline" className="text-gray-900 dark:text-gray-300 transition-colors flex flex-row items-center space-x-2 border-1 rounded-md py-2 px-3" >
              <span>Sign In!</span>
              <ArrowRight className="w-4 h-4" />
            </Button>
            <ModeToggle/>
          </nav>
        </div>
      </div>
    </motion.header>
  );
}