'use client'
import notifyService from "@/components/notifyServices";
import { useState } from "react"
import { ToastContainer } from "react-toastify";
import { AUTH_ENDPOINTS } from "@/lib/apiEndpoints";
import { setToken } from "@/lib/auth";

export default function RegisterForm() {
  const [ formData, setFormData ] = useState({
    username: "",
    password: "",
    email: "",
    name: "",
  });
  const [ confirmPassword, setConfirmPassword ] = useState("");
  const [ passwordMatch, setPasswordMatch ] = useState(true);

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const jsonPayload = {
        user_name: formData.username,
        email: formData.email,
        password: formData.password
      };

      const response = await fetch(`${AUTH_ENDPOINTS.REGISTER}`, {
        method: 'POST',
        headers: {
          'Content-type': 'application/json',
          'Accept': 'application/json'
        },
        body: JSON.stringify(jsonPayload),
        credentials: 'omit',
      });


      if (!response.ok) {
        console.log(response);
        notifyService.showError('Error while Registering. Try Again!');
        return;
      }

      const data = await response.json();
      console.log('Register successful');

      setToken();
      window.location.href = '/posts';
    } catch (error) {
      notifyService.showError(error.message || 'An unexpected error occurred');
    }
  }

  const handleChange = (e) => {
    let { name, value } = e.target;
    setFormData((prev) => ({
      ...prev,
      [name]: value,
    }));

    if (name === "password") {
      setPasswordMatch(value === confirmPassword);
    }
  };

  const handleConfirmPasswordChange = (e) => {
    const { value } = e.target;
    setConfirmPassword(value);
    setPasswordMatch(value === formData.password);
  };

  return (
    <div
      className='flex flex-col justify-center align-center w-3/4 bg-gray-50 dark:bg-gray-900 p-10 border-2 rounded-xl'>
      <div className='mb-4 space-y-2'>
        <p className='text-xl font-bold'>Join Us!</p>
        <p className='text-md font-semibold'>Create an Account</p>
      </div>
      <form className='flex flex-col space-y-4 md:space-y-6' onSubmit={handleSubmit}>
        <div>
          <label className='text-md font-medium block mb-2 dark:text-white text-gray-900'>Full Name:</label>
          <input
            type='text'
            name='name'
            id='name'
            required
            placeholder='John Doe'
            autoComplete='name'
            value={formData.name}
            onChange={handleChange}
            className='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'
          />
        </div>
        <div>
          <label className='text-md font-medium block mb-2 dark:text-white text-gray-900'>Email Address:</label>
          <input
            type='email'
            name='email'
            id='email'
            required
            placeholder='me@example.com'
            autoComplete='email'
            value={formData.email}
            onChange={handleChange}
            className='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'
          />
        </div>
        <div>
          <label className='text-md font-medium block mb-2 dark:text-white text-gray-900'>Username:</label>
          <input
            type='text'
            name='username'
            id='username'
            required
            placeholder='johndoe123'
            autoComplete='username'
            value={formData.username}
            onChange={handleChange}
            className='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'
          />
        </div>
        <div>
          <label className='text-md font-medium block mb-2 dark:text-white text-gray-900'>Password:</label>
          <input
            type='password'
            name='password'
            id='password'
            required
            autoComplete='new-password'
            placeholder='***********'
            value={formData.password}
            onChange={handleChange}
            className='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'
          />
        </div>
        <div>
          <label className='text-md font-medium block mb-2 dark:text-white text-gray-900'>Confirm Password:</label>
          <input
            type='password'
            id='confirm-password'
            required
            placeholder='***********'
            value={confirmPassword}
            onChange={handleConfirmPasswordChange}
            className='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'
          />
          {!passwordMatch && confirmPassword && (
            <p className="text-red-500 mt-1 text-sm">Passwords do not match</p>
          )}
        </div>
        <button
          type='submit'
          className='w-full border-1 text-white bg-blue-950 hover:bg-blue-400 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'
        >
          Sign Up
        </button>
      </form>
      <p className="text-sm font-light text-gray-900 dark:text-gray-400 mt-5">
        Already have an account?{" "}
        <a href="/login" className="font-medium text-blue-600 hover:underline dark:text-primary-500">
          Sign In here</a>
      </p>
      <ToastContainer />
    </div>
  )
}