class UsersRepository:
    users = {
        "john_doe": {
            "username": "john_doe",
            "full_name": "John Doe",
            "hashed_password": "$2a$12$RiolBpEbQqFEgeH1AcdlLOhpiw8UhGqsezFeKbqJYhPvV48F5MZt.",  # secret123
            "salary": 100_000,
            "next_raise_date": "2025-12-12"
        },
    }

    @staticmethod
    def get_user(username: str) -> dict:
        return UsersRepository.users.get(username)
