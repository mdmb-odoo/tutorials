/** @odoo-module **/

import { Component, useState, onMounted } from "@odoo/owl";
import { TodoItem } from "./todoitem";
import { useAutofocus } from "../utils";

export class TodoList extends Component {
    static template = "awesome_owl.todolist";
    static components = { TodoItem };
    setup() {

        this.toDoInputRef = useAutofocus("toDoListInput");
        
        this.todos = useState([]);
        this.state = useState({count : 0});

    }

    toggleState(elemId) {
        const index = this.todos.findIndex((elem) => elem.item_id === elemId);
        if (index >= 0) {
            this.todos[index].isCompleted = !this.todos[index].isCompleted;
        }
    }

    removeTodo(elemId) {
        const index = this.todos.findIndex((elem) => elem.item_id === elemId);
        if (index >= 0) {
            // remove the element at index from list
            this.todos.splice(index, 1);
        }
    }

    addTask(ev) {

        if (ev.keyCode===13) {
            if (this.toDoInputRef.el.value !== '') {
                this.todos.push(
                    {
                        item_id : ++ this.state.count,
                        description : this.toDoInputRef.el.value,
                        isCompleted : false
                    }
                )
                this.toDoInputRef.el.value = '';
            }
        }
    }
    
}