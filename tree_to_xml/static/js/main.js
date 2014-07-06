    $(function () {
        $('#jstree_demo_div').jstree(
                {
                    "core": {
                        'data': {
                            'url': '/main/get_all',
                            'data': function (node) {
                            }
                        },
                        // so that create works
                        "check_callback": true
                    },

                    "plugins": [ "contextmenu", "types"],
                    'types': {
                        'd': {  },
                        'f': { 'valid_children': [], 'icon': "jstree-file" }
                    },
                    'contextmenu': {
                        'items': function (node) {
                            var tmp = $.jstree.defaults.contextmenu.items();
                            delete tmp.create.action;
                            delete tmp.ccp;
                            tmp.create.label = "New";
                            tmp.create.submenu = {
                                "create_folder": {
                                    "separator_after": true,
                                    "label": "Folder",
                                    "action": function (data) {
                                        var inst = $.jstree.reference(data.reference),
                                                obj = inst.get_node(data.reference);
                                        inst.create_node(obj, { type: "d", text: "New folder" }, "last", function (new_node) {
                                            setTimeout(function () {
                                                inst.edit(new_node);
                                            }, 0);
                                        });
                                    }
                                },
                                "create_file": {
                                    "label": "File",
                                    "action": function (data) {
                                        var inst = $.jstree.reference(data.reference),
                                                obj = inst.get_node(data.reference);
                                        inst.create_node(obj, { type: "f", text: "New file" }, "last", function (new_node) {
                                            setTimeout(function () {
                                                inst.edit(new_node);
                                            }, 0);
                                        });
                                    }
                                }
                            };
                            if (this.get_type(node) === "file") {
                                delete tmp.create;
                            }
                            return tmp;
                        }
                    }


                }
        ).on('create_node.jstree', function (e, data) {
                    var data_to_send = { 'type': data.node.type, 'id': data.node.parent, 'parent_id': data.node.parent, 'name': data.node.text }
                    $.ajax({
                        type: "POST",
                        url: "/main/create",
                        data: data_to_send,
                        success: function (resp) {
                            data.instance.set_id(data.node, resp.id);
                        },
                        dataType: "json"
                    });

                }).on('rename_node.jstree', function (e, data) {

                    var data_to_send = { 'id': data.node.id, 'text': data.text }

                    $.ajax({
                        type: "POST",
                        url: "/main/update",
                        data: data_to_send,
                        success: function (resp) {
                            data.instance.set_id(data.node, resp.id);
                        },
                        dataType: "json"
                    });
                }).on('delete_node.jstree', function (e, data) {
                    var data_to_send = { 'id' : data.node.id };
                    $.ajax({
                        type: "POST",
                        url: "/main/delete",
                        data: data_to_send,
                        success: function (resp) {
                            data.instance.refresh();
                        },
                        dataType: "json"
                    });
				})
    });