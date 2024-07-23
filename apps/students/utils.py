from django.utils.crypto import get_random_string


def generate_code(count: int, range_str: str):
    code = get_random_string(count, range_str)
    return code


def triple_latter(obj: str) -> str:
    return "".join([i[0] for i in obj.title().split()])


def post_generate_unique_username(sender, instance, created, *args, **kwargs):
    if created:
        instance.student.generate_unique_user()
        instance.save()

