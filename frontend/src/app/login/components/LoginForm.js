'use client'

import { useState } from "react"
import { AUTH_ENDPOINTS } from "@/lib/apiEndpoints";
import { ToastContainer } from "react-toastify";
import notifyService from "@/components/notifyServices";
import { setToken } from "@/lib/auth";

export default function LoginForm() {
  const [ formData, setFormData ] = useState({
    username: "",
    password: ""
  });

  const handleChange = (e) => {
    let { name, value } = e.target;
    setFormData((prev) => ({
      ...prev,
      [name]: value
    }));
  }

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const formPayload = new URLSearchParams({
        username: formData.username,
        password: formData.password
      });
      const response = await fetch(`${AUTH_ENDPOINTS.LOGIN}`, {
        method: 'POST',
        headers: {
          'Content-type': 'application/x-www-form-urlencoded',
          'Accept': 'application/json'
        },
        body: formPayload.toString(),
        credentials: 'omit',
      });

      if (!response.ok) {
        const errorData = await response.json().catch(() => ({}));
        notifyService.showError("Error while Submitting");
      }
      const data = await response.json();
      console.log("login successful");

      setToken(formData.username);
      window.location.href = "/posts"
    } catch (error) {
      notifyServices.showError(error);
    }
  }


  return (
    <div
      className='flex flex-col justify-center align-center w-3/4 bg-gray-50 dark:bg-gray-900 p-10  border-2 rounded-xl'>
      <div className='mb-4 space-y-2'>
        <p className='text-xl font-bold'>Welcome back!</p>
        <p className='text-md font-semibold'>Login to your account</p>
      </div>
      <form className='flex flex-col space-y-4 md:space-y-6' onSubmit={handleSubmit}>
        <div>
          <label className='text-md font-medium block mb-2 dark:text-white text-gray-900'>Email Address:</label>
          <input
            type='email'
            id='email'
            required
            placeholder='me@example.com'
            autoComplete='email'
            value={formData.username}
            onChange={handleChange}
            className='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'
          />
        </div>
        <div>
          <label className='text-md font-medium block mb-2 dark:text-white text-gray-900'>Password:</label>
          <input
            type='password'
            id='password'
            required
            autoComplete='new-password'
            placeholder='***********'
            value={formData.password}
            onChange={handleChange}
            className='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'
          />
        </div>
        <button
          type='submit'
          className='w-full border-1 text-white bg-blue-950 hover:bg-blue-400 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'
        >
          Sign In
        </button>
      </form>
      <p className="text-sm text-gray-900 dark:text-gray-400 mt-5">
        Don't have an account?{" "}
        <a href="/register" className="font-medium text-blue-600 hover:underline dark:text-primary-500">
          Sign Up here</a>
      </p>
      <ToastContainer />
    </div>
  )
}