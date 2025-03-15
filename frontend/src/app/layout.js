'use client'

import { Geist, Geist_Mono, Poppins } from "next/font/google";
import "./globals.css";
import TransitionProvider from "../components/TransitionProvider";
import Navigation from '../components/navigation'
import { ThemeProvider } from "../components/theme-provider";
import { usePathname } from 'next/navigation';

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const poppins = Poppins({
  subsets: ["latin"],
  weight: ["100", "200", "300", "400", "500", "600", "700", "800", "900"],
  variable: "--font-poppins",
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

export default function RootLayout({ children }) {
  const pathname = usePathname();

  // Check if current path is homepage
  const isNonScrollable = pathname === '/' || pathname === '/login' || pathname === '/register';

  // Apply no-scroll class only to homepage
  const bodyClass = `${poppins.variable} ${geistSans.variable} ${geistMono.variable} antialiased w-full ${isNonScrollable ? 'overflow-hidden h-screen' : ''}`;

  return (
    <html lang="en" suppressHydrationWarning>
      <body className={bodyClass}>
        <ThemeProvider
          attribute="class"
          defaultTheme="system"
          enableSystem
          disableTransitionOnChange
        >
          <Navigation />
          <TransitionProvider>
            <main className='pt-16'>
              {children}
            </main>
          </TransitionProvider>
        </ThemeProvider>
      </body>
    </html>
  );
}