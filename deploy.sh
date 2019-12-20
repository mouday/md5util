# 打包部署
rm -rf dist build *.egg-info \
&& python setup.py install \
&& python setup.py sdist bdist_wheel \
&& twine check dist/* \
&& twine upload dist/* \
&& rm -rf dist build *.egg-info

# 安装升级
pip uninstall md5util -y \
&& pip install -U md5util -i https://pypi.org/simple
