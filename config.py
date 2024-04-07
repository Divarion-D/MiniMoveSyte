KODIK_TOKEN = "447d179e875efe44217f20d1ee2146be"
APP_SECRET_KEY = "some_super_ultra_unbelievable_key"
DEBUG = True  # Debug от Flask
SAVE_DATA = (
    False  # Для сохранения результатов парсинга (картинки, названия, ссылки на видео)
)
USE_SAVED_DATA = False  # Для использования уже сохранённых результатов
SAVED_DATA_FILE = "cache.json"  # Файл с сохранёнными данными (если SAVE_DATA == False и USE_SAVED_DATA == False, файл не обязателен)
SAVING_PERIOD = (
    10  # (В минутах) Как часто будет перезаписываться файл с сохранёнными данными
)
# Сохранение будет производиться только при условии что пользователь воспользовался сайтом
CACHE_LIFE_TIME = 1  # (В днях) Как часто будет обновляться информация в базе

ALLOW_WATCH_TOGETER = True  # Функция совместного просмотра
REMOVE_TIME = 5  # (В минутах) Через какое время не используемая комната для совместного просмотра будет удалена
# Рекомендуется включить кеширование если, впротивном случае для каждого пользователя видео будет искаться отдельно

# "/" в начале обязательно
IMAGE_NOT_FOUND = "/resources/no-image.png"  # Картинка для замены ненайденной
IMAGE_AGE_RESTRICTED = "/resources/age-restricted.png"  # Картинка для обозначения контента с ограничениями по возрасту

# Путь к иконке
FAVICON_PATH = "resources/favicon.ico"

# Адрес для доступа
HOST = "0.0.0.0"  # Такой адрес позволяет получить доступ как через 127.0.0.1, так и через локальный адрес компьютера (позволяет получить доступ к серверу с других устройств в сети)

# Порт для доступа
PORT = 5000