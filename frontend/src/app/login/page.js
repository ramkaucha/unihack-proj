"use client";

import LoginForm from './components/LoginForm';
import MovingCard from './components/MovingCard'
import AuthLayout from "../../components/AuthLayout";
import { motion } from "framer-motion";

export default function LoginPage() {
  return (
    <AuthLayout>
      <MovingCard />
      <LoginForm />
    </AuthLayout>
  );
}