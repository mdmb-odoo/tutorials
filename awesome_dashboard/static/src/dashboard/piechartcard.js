/** @odoo-module **/

import { Component } from "@odoo/owl";
import { Card } from "../../../../awesome_owl/static/src/card/card";
import { PieChart } from "./piechart";

export class PieChartCard extends Component {
    static template = "awesome_dashboard.PieChartCard";
    static components = { Card, PieChart };
    static props = {
        title: String,
        data: Object, 
        display: {opitonal:true}
    };

    static defaultprops = {
        display: true
    };


    

}
