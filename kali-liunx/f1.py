from plyer import notification

# تكوين الإشعار
titl = 'عنوان الإشعار'
message = 'محتوى الإشعار'
# عرض الإشعار
notification.notify(
    title=titl,
    message=message,
    app_name='اسم التطبيق (اختياري)'
)
