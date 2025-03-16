export default function SectionFive() {
  const comments = [
    { user: "JohnDoe", comment: "Great work! Keep it up." },
    { user: "JaneSmith", comment: "I agree, the design looks amazing." },
    {
      user: "AliceJohnson",
      comment: "Thanks, I will work on the next iteration!",
    },
  ];

  return (
      <section>
        <h2 className="text-2xl font-bold text-gray-800 mb-4">Comments</h2>
        <div className="space-y-4">
          {comments.map((comment, index) => (
            <div key={index} className="p-4 border rounded-lg shadow-md">
              <h3 className="font-semibold text-lg">{comment.user}</h3>
              <p className="text-gray-600">{comment.comment}</p>
            </div>
          ))}
        </div>
      </section>
 
  );
}
