/** @odoo-module **/
import { useRef, useEffect } from "@odoo/owl";

// value1 = markup("<p class='bg-success'>Hey you how are you??!!</p>")
export function useAutofocus(name) {
    let ref = useRef(name);
    useEffect(
        (el) => el && el.focus(),
        () => [ref.el]
    );
    return ref
}
