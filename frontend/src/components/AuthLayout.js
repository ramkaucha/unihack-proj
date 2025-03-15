// components/AuthLayout.jsx
"use client";

import { motion } from "framer-motion";
import { usePathname } from "next/navigation";

export default function AuthLayout({ children }) {
  // Get the current path to determine which page we're on
  const pathname = usePathname();
  const isLoginPage = pathname === "/login";

  // Split the children into left and right components
  const [Left, Right] = children;

  return (
    <div className="flex flex-row min-h-screen items-center justify-center w-full overflow-hidden">
      {/* Left side */}
      <motion.div
        className="flex justify-center items-center w-1/2"
        initial={{ x: "50%", opacity: 0 }} // Start from middle (moving outward)
        animate={{ x: 0, opacity: 1 }}      // Animate to normal position
        transition={{
          type: "tween",
          ease: "easeInOut",
          duration: 1
        }}
        exit={{
          x: "50%",
          opacity: 0,
          transition: {
            type: "tween",
            ease: "easeInOut",
            duration: 2.5
          }
        }}
      >
        {Left}
      </motion.div>

      {/* Right side */}
      <motion.div
        className="w-1/2 flex justify-center items-center"
        initial={{ x: "-50%", opacity: 0 }}  // Start from middle (moving outward)
        animate={{ x: 0, opacity: 1 }}      // Animate to normal position
        transition={{
          type: "tween",
          ease: "easeInOut",
          duration: 1
        }}
        exit={{
          x: "-50%",
          opacity: 0,
          transition: {
            type: "tween",
            ease: "easeInOut",
            duration: 2.5
          }
        }}
      >
        {Right}
      </motion.div>
    </div>
  );
}