'use client'

import { useState } from "react"

export default function SettingsForm() {
  const [ formData, setFormData ] = useState({
    username: '',
    password: '',
    email: '',
  });
  const [ confirmPassword, setConfirmPassword ] = useState('');
  const [ passwordMatch, setPasswordMatch ] = useState(false);

  const handleChange = (e) => {
    let {name, value} = e.target;
    setFormData((prev) => ({
      ...prev,
      [name]: value
    }));

    if (name === "password") {
      setPasswordMatch(value === confirmPassword);
    }
  };

  const handleConfirmPasswordChange = (e) => {
    const { value } = e.target;
    setConfirmPassword(value);
    setPasswordMatch(value === formData.password);
  }


  return (
    <div
      className='flex flex-col justify-center w-1/2 max-w-md bg-gray-50 dark:bg-gray-900 p-10 border-2 rounded-xl'>
      <div className='mb-4 space-y-2'>
        <p className='text-xl font-bold'>Hey User, Your Account Settings</p>
      </div>
      <form className='flex flex-col space-y-4 md:space-y-6'>
        <div>
          <label className='text-md font-medium block mb-2 dark:text-white text-gray-900'>Email Address:</label>
          <input
            type='email'
            id='email'
            required
            placeholder='me@example.com'
            autoComplete='email'
            disabled
            className='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'
          />
        </div>
        <p className='text-xl font-bold'>Change Password?</p>
        <div>
          <label className='text-md font-medium block mb-2 dark:text-white text-gray-900'>New Password:</label>
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
          Save
        </button>
      </form>
    </div>
  )
}