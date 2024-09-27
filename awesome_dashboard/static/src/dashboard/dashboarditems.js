/** @odoo-module **/

import { NumberCard } from "./numbercard";
import { PieChartCard } from "./piechartcard";
import { registry } from "@web/core/registry";

const items = {
    items :
    [
                {
                    id: "New Oders",
                    description: "Number of New Orders",
                    Component: NumberCard,
                    size: 2,
                    itemProps : {},
                    props: (data, showObject) => ({
                        title: "Number of new t-shirt orders this month",
                        data: data.nb_new_orders,
                        display : showObject
                    }),
                },
                {
                    id: "Average Quantity",
                    description: "The average number of t-shirts by order",
                    Component: NumberCard,
                    size: 2,
                    itemProps : {},
                    props: (data, showObject) => ({
                        title: "Average amount of t-shirt by order this month",
                        data: data.average_quantity,
                        display : showObject
                    }),
                },
                {
                    id: "Orders by size",
                    description: "Number of orders for each size",
                    Component: PieChartCard,
                    size: 2,
                    itemProps : {},
                    props: (data,showObject) => ({
                        title: "Orders by size",
                        data: data.orders_by_size,
                        display : showObject
                    }),
                },
    ],

    start(){
        return this.items;
    }
};

registry.category('services').add('awesome_dashboard.dashboard_items',items);
// registry.category("services").add("awesome_dashboard.statistics", statisticsService);