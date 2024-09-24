/** @odoo-module **/

import { Component, useState } from "@odoo/owl";

export class Counter extends Component {
    static template = "awesome_owl.counter";

    static props = {
        onChange : {
            
            type: Function,
            optional: true, 
            validate: (propValue) => {
                return propValue === undefined || typeof propValue === 'function';
            }

        }
    };

    setup() {
        this.state = useState({value : 0});
    }

    increment() {
        this.state.value ++;
        
        if (typeof this.props.onChange === 'function') { 
            
            this.props.onChange();
            
        }
            
    }

}
