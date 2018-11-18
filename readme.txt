|ProjectName
|-app/ 程序包
|  |-__init__.py
|  |-models.py  // 数据库模型
|  |-emails.py  // 邮件处理程序
|  |-main/  // 程序模块，根据业务区分，不同的模块可以各自拥有自己的单独目录
|  |  |-__init__.py
|  |  |-views.py
|  |  |-errors.py
|  |  |-forms.py
|  |-templates/  // Jinja2的html模板
|  |-static/  // css、js、图片等静态文件
|-migrations/  // 数据库迁移文件夹
|-venv/  // 虚拟环境
|-tests/  // 单元测试程序，可以包含多个文件
|  |-__init__.py
|  |-test*.py  // 单元测试文件
|-manage.py  // 启动程序
|-config.py  // 全局配置文件
|readme.txt
