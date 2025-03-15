
export default function RegisterForm() {
  return (
    <div
      className='flex flex-col justify-center align-center w-3/4 bg-gray-50 dark:bg-gray-900 p-10  border-2 rounded-xl'>
      <div className='mb-4 space-y-2'>
        <p className='text-xl font-bold'>Join Us!</p>
        <p className='text-md font-semibold'>Create an Account</p>
      </div>
      <form className='flex flex-col space-y-4 md:space-y-6'>
        <div>
          <label className='text-md font-medium block mb-2 dark:text-white text-gray-900'>Email Address:</label>
          <input
            id='name'
            required
            placeholder='John Doe'
            autoComplete='name'
            className='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'
          />
        </div>
        <div>
          <label className='text-md font-medium block mb-2 dark:text-white text-gray-900'>Email Address:</label>
          <input
            type='email'
            id='email'
            required
            placeholder='me@example.com'
            autoComplete='email'
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
            className='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'
          />
        </div>
        <div>
          <label className='text-md font-medium block mb-2 dark:text-white text-gray-900'>Password:</label>
          <input
            type='password'
            id='confirm-password'
            required
            placeholder='***********'
            className='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'
          />
        </div>
        <button
          type='submit'
          className='w-full border-1 text-white bg-primary-600 hover:bg-primary-700 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800'
        >
          Sign Up
        </button>
      </form>
      <p className="text-sm font-light text-gray-500 dark:text-gray-400 mt-5">
        Already have an account?{" "}
        <a href="/login" className="font-medium text-blue-600 hover:underline dark:text-primary-500">
          Sign In here</a>
      </p>
    </div>
  )
}