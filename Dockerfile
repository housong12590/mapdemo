FROM 192.168.0.210/library/pyweb

#RUN cd /var/www/app && git init \
#    && git remote add origin http://housong:pss123546@git.jiankanghao.net/haiwei/chaos.git \
#    && git pull origin develop

RUN cd /var/www/app
COPY . /var/www/app/

# 配置运行环境
RUN pip install -r requirements.txt
#RUN export LANG=C.UTF-8 && export FLASK_APP=pro.py && flask assets clean && flask assets build

