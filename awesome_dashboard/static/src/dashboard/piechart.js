/** @odoo-module **/

import { Component, onWillUnmount, useEffect, useRef, onWillStart, onMounted  } from "@odoo/owl";
// import { GraphRenderer } from "@web/views/graph/graph_renderer";
import {loadJS} from "@web/core/assets";

export class PieChart extends Component {
    static template = "awesome_dashboard.PieChart";
    static props = {
        data : {
            optional : false
        },
        options : {
            optional : true
        }
    };
    static defaultprops = {
        options : {}
    }
    

    setup() {
        
        this.canvasRef = useRef("piechart");

        onWillStart( () => loadJS(['/web/static/lib/Chart/Chart.js']));
        useEffect( () => {
            if (this.piechart) {
                this.piechart.destroy();
            }
            this.piechart = new Chart(this.canvasRef.el, {
                type: 'pie',
                data: {
                    datasets: [{
                        data: Object.values(this.props.data)
                    }],
                    labels  : Object.keys(this.props.data)
                },
                options: this.props.options
            });
        },
        () => [this.props.data] 
    );
        // useEffect(() => this.renderChart());
        onWillUnmount(this.onWillUnmount);

    }

    onWillUnmount() {
        if (this.piechart) {
            this.piechart.destroy();
        }
    }
    

}

