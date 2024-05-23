import 'package:flet/flet.dart';

import 'placeholder.dart';

CreateControlFactory createControl = (CreateControlArgs args) {
  switch (args.control.type) {
    case "placeholder":
      return PlaceholderControl(
          parent: args.parent,
          control: args.control,
          backend: args.backend);
    default:
      return null;
  }
};

void ensureInitialized() {
  // nothing to initialize
}
