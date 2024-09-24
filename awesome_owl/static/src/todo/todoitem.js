/** @odoo-module **/

import { Component, useState, markup } from "@odoo/owl";
import { Card } from "../card/card";

export class TodoItem extends Component {
    static template = "awesome_owl.todoitem";
    static components = { Card }
    
    static props = {
        item_id : {
            type : Number,
            optional : false
        },
        description : {
            type : String,
            optional : false
        },
        isCompleted : {
            type : Boolean,
            optional : false
        },
        onChange : {
            
            type: Function,
            optional: true, 
            validate: (propValue) => {
                return propValue === undefined || typeof propValue === 'function';
            }

        },
        removeTodo : {
            type: Function,
            optional: true, 
            validate: (propValue) => {
                return propValue === undefined || typeof propValue === 'function';
            }

        }
    };

    toggleState() {

        this.props.isCompleted = !this.props.isCompleted;

        if (typeof this.props.onChange === 'function') { 
            
            this.props.onChange(this.props.item_id);
            
        }
    }

    removeTodo() {

        this.props.removeTodo(this.props.item_id);

    }


    
}