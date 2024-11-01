## Описание:
<p>Web-игра "Покер на костях": онлайн игра на 2 человека с поддержкой параллельной игры в различных лобби на сайте, доступ к лобби осуществляется посредством кода, который выдается один раз при создании владельцу. 
<a href="https://en.wikipedia.org/wiki/Hobbit#Lifestyle" title="Hobbit lifestyles">Правила игры тут</a>
</p>

## Требования:
<ul>
    <li><strong>Функциональные:</strong>
        <ul>
            <li>Авторизация отсутствует</li>
            <li>Интерфейс создания лобби на 2х пользователей</li>
            <li>Подключение к уже существующещму лобби происходит посредством кода, который выдается владельцу при создании</li>
            <li>Обучение на предоставленном пользователем тексте произведения</li>
            <li>Формирование краткого пересказа указанного участка текста</li>
            <li>Создание индивидуальных рекомендаций для пользователя</li>
        </ul>
    </li>
    <li><strong>Нефункциональные:</strong>
        <ul>
            <li>Время отклика веб-платформы должно быть менее 2 секунд для всех основных операций.</li>
            <li>Платформа должна выдерживать до 2^16 пользователей единовременно</li>
            <li>Соответствие требований WCAG (Web Content Accessibility Guidelines).</li>
        </ul>
    </li>
</ul>

## Ограничения:
<ul>
    <li><strong>Технологические:</strong>
        <ul>
            <li>Использование определенных технологий, которые могут быть обусловлены навыками команды разработки.</li>
        </ul>
    </li>
</ul>

## Планировка разработки:
<ul>
    <li><strong>Часть 1:</strong>
        <ol>
            <li>Разработка базового GUI для web-приложения</li>
            <li>Разработка игрового процесса для 1й сессии из 2х игроков</li>
            <li>Тестирование игрового процесса</li>
            <li>Разработка распараллеливания игрового процесса на несколько сессий (несколько игровых лобби)</li>
            <li>Релиз первой рабочей версии</li>
        </ol>
    </li>
    <li><strong>Часть 2:</strong>
        <ol>
            <li>Не успели за первую часть: релиз и логика</li>
            <li>Логика написана (какая-то)</li>
            <li>Есть GUI (какой-то)</li>
            <li>Добавили лицензию</li>
            <li>Добавили релизную версию</li>
            <li>Не успели совсем: многопользовательский режим (больше одного лобби)</li>
        </ol>
    </li>
</ul>

## Установка и запуск:
    poetry install
    poetry run python -m uvicorn backend.main:app --reload

    url - /homepage
