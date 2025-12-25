import 'package:flutter/widgets.dart';

class AddInfo extends StatelessWidget {
  final IconData icon;
  final String label;
  final String value;
  const AddInfo({
    super.key,
    required this.icon,
    required this.label,
    required this.value,
  });

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        Icon(icon, size: 32),
        const SizedBox(height: 5),
        Text(label),
        const SizedBox(height: 5),
        Text(value),
      ],
    );
  }
}
