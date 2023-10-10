package repository;

import entity.TodoList;

public interface TodoListRepository {

    TodoList getAll();

    void AddTodo(TodoList todo);

    void removeTodo(Integer id);

}
