import i18n
import os

# Получаем абсолютный путь к директории проекта
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Путь к папке с языковыми файлами
languages_dir = os.path.join(project_dir, 'languages')

# Настройка i18n
i18n.load_path.append(languages_dir)
i18n.set('filename_format', '{locale}.yml')
i18n.set('fallback', 'ru')
i18n.set('locale', "ru")  # Устанавливаем новую локаль

def _(key, locale=None):
    if locale:
        return i18n.t(key, locale=locale)
    return i18n.t(key)

def set_language(new_locale):
    if new_locale in ['en', 'ru']:  # Проверка, что локаль поддерживается
        i18n.set('locale', new_locale)  # Устанавливаем новую локаль
    else:
        raise ValueError(f"Unsupported locale: {new_locale}")