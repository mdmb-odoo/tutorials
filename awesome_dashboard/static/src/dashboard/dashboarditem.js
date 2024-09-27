/** @odoo-module **/

import { Component } from "@odoo/owl";
import { Card } from "../../../../awesome_owl/static/src/card/card";

export class DashboardItem extends Component {
    static template = "awesome_dashboard.AwesomeDashboardItem";
    static components = { Card };
    static props = {
        size : {
            type : Number,
            optional : true
        },
        slots: { 
            type: Object, 
            optional: true 
        },
        toggle : {
            type : Boolean,
            optional : true
        },
    }

    static defaultProps = {
        size: 1,
        toggle : false
    };


    

}

