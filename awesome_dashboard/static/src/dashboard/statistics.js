/** @odoo-module **/

import { registry } from "@web/core/registry";
import { memoize } from "@web/core/utils/functions";
import { reactive } from "@odoo/owl";



// export const statisticsService = reactive({
//     dependencies : ['rpc'],

//     start(env, {rpc}) {

//         const loadstatistics = memoize(async function() { return rpc('/awesome_dashboard/statistics'); });
//         setInterval( async () => {
//             const loadstatistics = memoize(async function() { return rpc('/awesome_dashboard/statistics'); });
//             // window.alert(JSON.stringify(memoize(await loadstatistics())));
//             // window.alert(memoize(await loadstatistics()));
//             // window.alert((JSON.stringify(await loadstatistics())));
//             return { loadstatistics };
            
//             }, 5000);
//         return { loadstatistics };
    
//     },

    
// }, () => window.alert("Hey there"));

export const statisticsService = {
    dependencies : ['rpc'],

    start(env, {rpc}) {

        const loadstatistics = memoize(async function() { return rpc('/awesome_dashboard/statistics'); });
        let stats = reactive({});
        setInterval( async () => {
            stats.data = await rpc('/awesome_dashboard/statistics');
            }, 100000);
        return { loadstatistics, stats };
    
    },

    
};

registry.category("services").add("awesome_dashboard.statistics", statisticsService);