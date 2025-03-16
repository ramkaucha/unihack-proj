export default function SectionThree() {
  const [isMembersExpanded, setIsMembersExpanded] = useState(false);

  const members = [
    {
      username: "JohnDoe",
      role: "Project Manager",
      description: "Oversees project progress.",
    },
    {
      username: "JaneSmith",
      role: "Developer",
      description: "Writes code for the project.",
    },
    {
      username: "AliceJohnson",
      role: "Designer",
      description: "Creates the visual designs.",
    },
  ];

  const toggleMembersSection = () => {
    setIsMembersExpanded(!isMembersExpanded);
  };

  return (
      <section className="mb-6">
        <button
          onClick={toggleMembersSection}
          className="text-blue-500 font-semibold hover:underline"
        >
          {isMembersExpanded ? "Hide Members" : "Show Members"}
        </button>

        {isMembersExpanded && (
          <div className="mt-4 space-y-4">
            {members.map((member, index) => (
              <div key={index} className="p-4 border rounded-lg shadow-md">
                <h3 className="font-semibold text-xl">{member.username}</h3>
                <p className="text-gray-600">Role: {member.role}</p>
                <p className="text-gray-500">{member.description}</p>
              </div>
            ))}
          </div>
        )}
      </section>
  
  );
}
