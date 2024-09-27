/** @odoo-module **/

import { Dialog } from "@web/core/dialog/dialog";
import { reactive } from "@odoo/owl";
// import { AwesomeDashboard } from "./dashboard";

export class ContentDialog extends Dialog {

    applyChanges() {
        let parentElement = document.getElementById("itemsListView");
        let inputItemsList = parentElement.querySelectorAll("input");
        inputItemsList.forEach(input => {
            localStorage.setItem(input.id,input.checked);
            this.props.items.forEach(item => {
                if (item.id === input.id) {
                    item.itemProps.display = input.checked;
                }
            })
        });
        this.data.close()
    }

    checkAttr(item_id) {
        return localStorage.getItem(item_id)==='true'?true:false;
    }
    

}

ContentDialog.template = "awesome_dashboard.ContentDialog";
ContentDialog.components = { Dialog };
ContentDialog.props = {
    ...Dialog.props,
    close : Function,
    items : {
        type : Array,
        optional : false
    }
};
delete ContentDialog.props.slots;