/** @odoo-module **/

import { Component, useState } from "@odoo/owl";

export class Card extends Component {
    static template = "awesome_owl.card";
    static props = {
        title : {
            type : String,
            optional : true
        },
        body : {
            type : String,
            optional : true
        },
        class : {
            optional : true
        },
        slots : {
            optional : true
        }
    };

    setup() {

        this.state = useState({value:false});

    }

    toggleState() {
        this.state.value = !this.state.value;
    }
}
