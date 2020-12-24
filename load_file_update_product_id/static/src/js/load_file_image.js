odoo.define('load_file_update_product_id.LoadFileActionID', function (require) {
    "use strict";

    var core = require('web.core')
    var Widget = require('web.Widget');
    var AbstractAction = require('web.AbstractAction');
    var framework = require('web.framework');

    var QWeb = core.qweb;
    var _t = core._t;


    var LoadFileAction = AbstractAction.extend({
        title: 'Load File',
        contentTemplate: 'large_file_id_template',

        /**
         * @override
         * @param {Object} params
         * @param {Object} params.context
         *
         */
        init: function (parent, params) {
            this._super.apply(this, arguments);
        },


        /**
         * append the renderer and instantiate the line renderers
         *
         * @override
         */
        start: function () {
            var self = this;
            this.$el.on('click', '#continuing_id', function (event) {

                framework.blockUI();

                $('#form_large_id_file_load').ajaxSubmit({
                    url: '/large_id/file/upload_id',
                    type: 'POST',
                    resetForm: true,
                    success: function (responseText) {
                        framework.unblockUI;
                        self.do_notify(_t("Update Product Image"), responseText);
                    },
                    complete: framework.unblockUI,
                    done: framework.unblockUI,

                });
//                self.destroy();

            });

        },


    });


    core.action_registry.add('large_file_load_view', LoadFileAction);

    return {
        LoadFileAction: LoadFileAction,
    };
});
