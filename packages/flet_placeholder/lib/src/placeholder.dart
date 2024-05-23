import 'dart:convert';
import 'dart:io';

import 'package:collection/collection.dart';
import 'package:flet/flet.dart';
import 'package:flutter/material.dart';

class PlaceholderWidget extends StatelessWidget {
  final Color color;
  const PlaceholderWidget({
    required this.color,
  });

  @override
  Widget build(BuildContext context) {
    return Container(
      height: 100.0,
      width: 100.0,
      child: Placeholder(color: this.color),
    );
  }
}

class PlaceholderControl extends StatefulWidget {
  final Control? parent;
  final Control control;
  final FletControlBackend backend;

  const PlaceholderControl(
      {super.key,
      required this.parent,
      required this.control,
      required this.backend});

  @override
  State<PlaceholderControl> createState() => _PlaceholderControlState();
}

class _PlaceholderControlState extends State<PlaceholderControl>
    with FletStoreMixin {
  late PlaceholderWidget phwidget;

  @override
  void initState() {
    phwidget = PlaceholderWidget(
      color:
          widget.control.attrColor("color", null, Colors.cyan) ?? Colors.cyan,
    );
    super.initState();
  }

  @override
  void dispose() {
    super.dispose();
  }

  void _onError(String? message) {
    debugPrint("Placeholder onError: $message");
    widget.backend
        .triggerControlEvent(widget.control.id, "error", message ?? "");
  }

  @override
  Widget build(BuildContext context) {
    debugPrint("Placeholder build: ${widget.control.id}");

    () async {
      // debug
      var tempFile4 = await File('/tmp/foo4.txt').create();
      await tempFile4
          .writeAsString("Widget control id = ${widget.control.id}\n ");

      widget.backend.subscribeMethods(widget.control.id,
          (methodName, args) async {
        // debug
        var tempFile1 = await File('/tmp/foo2.txt').create();
        await tempFile1.writeAsString("Method name passed = $methodName\n ");

        switch (methodName) {
          case "change_color":
            debugPrint("Placeholder.jump($hashCode)");
            var intcolor = int.tryParse(args["color"] ?? "") ?? 0;
            var color = intcolor == 0 ? Colors.red : Color(intcolor);
            // debug
            var tempFile = await File('/tmp/foo1.txt').create();
            await tempFile.writeAsString("Color passed in: $color\n ");
            // next set our color in the widget.
            setState(() {
              phwidget = PlaceholderWidget(color: color);
            });

            break;
        }
        return null;
      });
      // debug
      var tempFile2 = await File('/tmp/foo3.txt').create();
      await tempFile2.writeAsString("Well at least the async was called\n ");
    }();

    return constrainedControl(context, phwidget, widget.parent, widget.control);
  }
}
