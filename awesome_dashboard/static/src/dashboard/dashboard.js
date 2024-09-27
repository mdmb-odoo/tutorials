/** @odoo-module **/

import { Layout } from "@web/search/layout";
import { Component, onWillStart, useState } from "@odoo/owl";
import { _t } from "@web/core/l10n/translation";
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";
import { DashboardItem } from "./dashboarditem";
import { PieChart } from "./piechart";
import { ContentDialog } from "./contentdialog";


export class AwesomeDashboard extends Component {
    static template = "awesome_dashboard.AwesomeDashboard";
    static components = { Layout, DashboardItem, PieChart, ContentDialog };

    setup() {
        
        this.items = useState(useService("awesome_dashboard.dashboard_items"));
        
        this.customers = useService("action");
        this.leads = useService("action");
        
        this.statisticsService = useService("awesome_dashboard.statistics");
        // this.updateFlag = useState({value:false})
        // this.stats = useState(async () => await this.statisticsService.loadstatistics());
        this.stats = useState(this.statisticsService.stats);
        // [this.stat.stats['orders_by_size']['m'],this.stat.stats['orders_by_size']['s'],this.stat.stats['orders_by_size']['xl']]
        onWillStart(async () => {
            this.stats.data = await this.statisticsService.loadstatistics();

        });
        
        
    }
    
    showCustomers() {
        this.customers.doAction("base.action_partner_customer_form");

    }

    openDialog() {
        // window.alert(this.items);
        this.env.services.dialog.add(ContentDialog, { items : this.items });
        // window.alert(this.env.services.dialog.)
    }

    showLeads() {
        this.leads.doAction({
            type: 'ir.actions.act_window',
            name: _t('Leads'),
            res_model: 'crm.lead',
            views: [[false, 'list'],[false, 'form']],
        });

    }

    getDashboardComponentValues(item, data) {

        let storedItem = localStorage.getItem(item.id);
        // window.alert(item.id + " " +storedItem)
        if (storedItem === null) {
            storedItem = true;
            localStorage.setItem(item.id,storedItem);
        } 
        item.itemProps = item.props(data,storedItem);
        return item.itemProps;
    }

    

}


// const timer = {
//     dependencies : ["notification"],
//     start( env, { notification } ) {
//         let counter = 1;

//         setInterval( () => {
//             notification.add(`Tick Tock ${counter++}`);
//         }, 5000);
//     } 

// };

registry.category("lazy_components").add("AwesomeDashboard", AwesomeDashboard);
