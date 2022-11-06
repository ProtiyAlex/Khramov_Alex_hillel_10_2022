def dec_type_str():
    def reverse_string(func):
        def wrapper(*args, **kwargs):
            if isinstance(func(*args, **kwargs), str):
                return func(*args, **kwargs)

        return wrapper

    @reverse_string
    def get_university_name() -> str:
        return "Western Institute of Technology and Higher Education"

    @reverse_string
    def get_university_founding_year() -> int:
        return 1957

    print(get_university_name(), get_university_founding_year(), sep="\n")


def dec_mask():
    def mask_data(target_key: str, replace_with: str = "*"):
        def decorator(func):
            def wrapper(*args, **kwargs):
                kwargs[target_key] = replace_with
                return func(*args, **kwargs)

            return wrapper

        return decorator

    @mask_data(target_key="name")
    def get_user(name: str, age: int):
        return {"name": name, "age": age}

    print(get_user(name="Alice", age=30), get_user(name="Bob", age=25), sep="\n")


def main():
    dec_type_str()
    dec_mask()




if __name__ == "__main__":
    main()
