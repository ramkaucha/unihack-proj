"use client";

import RegisterForm from './components/RegisterForm';
import MovingCard from "./components/MovingCard";
import AuthLayout from "../../components/AuthLayout";
import { motion } from "framer-motion";

export default function RegisterPage() {
  return (
    <AuthLayout>
      <RegisterForm />
      <MovingCard />
    </AuthLayout>
  );
}