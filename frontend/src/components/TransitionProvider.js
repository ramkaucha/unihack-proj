"use client";

import { AnimatePresence } from "framer-motion";
import { usePathname } from "next/navigation";

export default function TransitionProvider({ children }) {
  const pathname = usePathname();

  return (
    <AnimatePresence mode="wait">
      {/* Using a key based on the pathname ensures the animation triggers on route changes */}
      <div key={pathname}>
        {children}
      </div>
    </AnimatePresence>
  );
}