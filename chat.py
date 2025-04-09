questions = [
    {
        "question": "What is the capital of France?",
        "answer": "Paris"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "answer": "Jupiter"
    },
    {
        "question": "Who wrote Romeo and Juliet?",
        "answer": "William Shakespeare"
    },
    {
        "question":"Hi",
        "answer":"Hello,How can i help you"
    },
    {
        "question":"What is your Name?",
        "answer":"My Name is Chitti"
    },
    {
        "question":"Tell me a joke.",
        "answer":"Why did Saint Peter install a new gate at the Pearly Gates? Because it was a heavenly idea!"
    },
    
    
     {
        "question":"Im not feeling well.",
        "answer":"what happened suddenly"
    },
    
     {
        "question":"No one likes me",
        "answer":"But i like u, wont u consider me as ur dear friend"
    },
    
     {
        "question":"remind me to medicine",
        "answer":"Sure!! can I know the exact time!"
    },
    
     {
        "question":"can u play 90's song for me",
        "answer":"Here u go,hope u like it"
    },
    
     {
        "question":"Tell me Mahabharatha story",
        "answer":"From which part you want to here"
    },
    
    # Add more questions and answers here
]

def search_and_provide_info(query):
    for question in questions:
        if query.lower() == question["question"].lower():
            return question["answer"]
    return "No relevant information found."


          

def main():
    while True:
        query = input("Enter your search query (or 'quit' to exit): ")
        if query.lower() == 'quit':
            print("Exiting...")
            break
        result = search_and_provide_info(query)
        print(result)

if __name__ == "__main__":
    main()
