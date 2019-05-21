# Очистка файлов messages и wtmp
# Для работы сценария требудтся права root.

cd /var/log
cat /dev/null > messages
cat /dev/null > wtmp
echo "Лог-файлы очищены."
