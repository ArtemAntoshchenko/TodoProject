-- Создаем расширения если нужны
-- CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Комментарии к таблице
COMMENT ON TABLE todos IS 'Таблица для хранения задач (todos)';

-- Комментарии к колонкам
COMMENT ON COLUMN todos.id IS 'Уникальный идентификатор задачи';
COMMENT ON COLUMN todos.title IS 'Заголовок задачи (макс 200 символов)';
COMMENT ON COLUMN todos.description IS 'Описание задачи (макс 1000 символов)';
COMMENT ON COLUMN todos.status IS 'Статус задачи: pending, in_progress, completed';
COMMENT ON COLUMN todos.created_at IS 'Дата создания задачи';
COMMENT ON COLUMN todos.updated_at IS 'Дата последнего обновления задачи';

-- Создаем индексы для быстрого поиска
CREATE INDEX IF NOT EXISTS idx_todos_status ON todos(status);
CREATE INDEX IF NOT EXISTS idx_todos_created_at ON todos(created_at);