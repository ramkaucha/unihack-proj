'use client'

import { useState, useEffect } from 'react'
import { useTheme } from 'next-themes'
import Image from 'next/image'

export default function ThemeAwareImage({ 
  lightSrc, 
  darkSrc, 
  alt, 
  width, 
  height,
  className,
  ...props 
}) {
  const { resolvedTheme } = useTheme()
  const [mounted, setMounted] = useState(false)
  
  // Only render image after component is mounted to avoid hydration issues
  useEffect(() => {
    setMounted(true)
  }, [])
  
  // Before mounting, return a placeholder to ensure layout doesn't shift
  if (!mounted) {
    return <div className={`relative ${className}`} style={{ width, height }} />
  }
  
  // Select image source based on current theme
  const src = resolvedTheme === 'dark' ? darkSrc : lightSrc
  
  return (
    <Image
      src={src}
      alt={alt}
      width={width}
      height={height}
      className={className}
      {...props}
    />
  )
}