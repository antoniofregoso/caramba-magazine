/* License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl). */

odoo.define('theme_magazine.theme_customize', function(require) {
    "use strict";
    var ThemeCustomizeDialog = require('website.theme');
    var ctx = require('web_editor.context');
    var core = require('web.core');
    var ajax = require('web.ajax');
    var Dialog = require('web.Dialog');
    var qweb = core.qweb;
    var _t = core._t;

    ajax.loadJS('/web/static/lib/ace/ace.odoo-custom.js').done(function() {
        ajax.loadJS('/web/static/lib/ace/mode-less.js');
        ajax.loadJS('/web/static/lib/ace/theme-monokai.js');
    });

    ThemeCustomizeDialog.include({
        theme: null,
        website: null,
        xmlDependencies: ['/theme_magazine/static/src/xml/theme_customize.xml'],
        events: {
            'click .btn-apply': 'apply',
            'click .btn-close': 'close'
        },
        willStart: function() {
            var self = this;
            var website_id = ctx.get().website_id;
            var get_theme = $.Deferred();
            this._rpc({
                model: 'website',
                method: 'search_read',
                domain: [['id', '=', website_id]]
            }).then(function(website) {
                self.website = website[0];
                self._rpc({
                    model: 'theme.magazine',
                    method: 'search_read',
                    domain: [['id', '=', website[0].theme_flexible_id[0]]]
                }).then(function(theme) {
                    self.theme = theme[0];
                    get_theme.resolve();
                });
            });
            return $.when(this._super.apply(this, arguments), get_theme);
        },
        start: function() {
            var res = this._super.apply(this, arguments);

            this.setupCssEditor();

            this.set(this.theme);
            this.$('a[href="#tab-layout"]').click();
            return res;
        },
        setupCssEditor: function() {
            this.cssEditor = window.ace.edit(this.$('[name="css"]')[0]);
            this.cssEditor.setTheme('ace/theme/monokai');
            this.cssEditor.session.setMode('ace/mode/less');
        },
        set: function(theme) {
            for(var name in theme) {
                var input = this.$('input[name="' + name + '"], select[name="' + name + '"]');
                var type = input.attr('type') || 'select';
                switch(type) {
                    case 'select':
                        input.val(theme[name]);
                        break;

                    case 'checkbox':
                        input.prop('checked', theme[name]);
                        break;

                    default:
                        if(theme[name] === false) {
                            theme[name] = '';
                        }
                        if(input.parent().hasClass('colorpicker-component')) {
                            if(theme[name]) {
                                input.parent().colorpicker({'color': theme[name]});
                            } else {
                                input.parent().colorpicker();
                            }
                        } else {
                            input.val(theme[name]);
                        }
                        break;
                }
            }
            this.cssEditor.setValue(theme.css || '');
        },
        get: function() {
            var values = {};
            this.$('input, select').each(function() {
                var type = $(this).attr('type') || 'select';
                switch(type) {
                    case 'checkbox':
                        values[$(this).attr('name')] = $(this).prop('checked');
                        break;

                    default:
                        values[$(this).attr('name')] = $(this).val();
                        break;
                }
            });
            values.css = this.cssEditor.getValue();
            return values;
        },
        apply: function(e) {
            var $btn = $(e.target);
            $btn.attr('disabled', true);
            $btn.html($('<i class="fa fa-cog fa-spin" />'));
            return this._rpc({
                model: 'theme.magazine',
                method: 'write',
                args: [[this.theme.id], this.get()]
            }).then(function() {
                var href = '/website/theme_customize_reload'+
                    '?href='+encodeURIComponent(window.location.href)+
                    '&enable='+encodeURIComponent([
                        'theme_magazine.assets_frontend_menu',
                        'theme_magazine.assets_frontend_colors',
                        'theme_magazine.assets_frontend_fonts',
                        'theme_magazine.assets_frontend_layout',
                        'theme_magazine.layout'
                    ])+
                    '&disable=';
                window.location.href = href;
            });
        },
       
           
        }
    });


});