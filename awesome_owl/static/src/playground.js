/** @odoo-module **/

import { Component, useState, markup } from "@odoo/owl";
import { Counter } from "./counter/counter";
import { Card } from "./card/card";
import { TodoList } from "./todo/todolist";

export class Playground extends Component {
    static template = "awesome_owl.playground";
    static components = { Counter, Card, TodoList }
    value1 = markup("<p class='bg-success'>Displaying html using markup</p>")

    setup() {

        this.state = useState({sum : 0});
    }
    

    incrementSum() {

        this.state.sum ++;
    }
}
