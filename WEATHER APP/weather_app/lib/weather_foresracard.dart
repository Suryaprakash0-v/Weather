import 'package:flutter/material.dart';

class CardWidget extends StatelessWidget {
  final String time;
  final IconData icon;
  final String value;
  const CardWidget({
    super.key,
    required this.time,
    required this.icon,
    required this.value,
  });

  @override
  Widget build(BuildContext context) {
    return Card(
      elevation: 6,
      child: Container(
        width: 100,
        padding: const EdgeInsets.all(8.0),
        decoration: BoxDecoration(borderRadius: BorderRadius.circular(12)),
        child: Column(
          children: [
            Text(
              (time),
              style: TextStyle(fontSize: 10, fontWeight: FontWeight.bold),
            ),
            const SizedBox(height: 5),
            Icon(icon, size: 30),
            const SizedBox(height: 5),
            Text((value), style: TextStyle(fontSize: 10)),
          ],
        ),
      ),
    );
  }
}
