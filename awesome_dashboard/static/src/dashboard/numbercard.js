/** @odoo-module **/

import { Component } from "@odoo/owl";
import { Card } from "../../../../awesome_owl/static/src/card/card";

export class NumberCard extends Component {
    static template = "awesome_dashboard.NumberCard";
    static components = { Card };
    static props = {
        title: String,
        data: Number,
        display: {opitonal:true}
    };
    static defaultprops = {
        display : true
    }


    

}
