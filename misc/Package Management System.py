# (use pip3 instead of pip in python3.5 and above in cmd, pympler setuptools are examples of our packages)
# to search package:
# pip search pympler

# to install package:
# pip install pympler

# to see installed packages:
# pip list

# to delete package:
# pip uninstall package

# to check package outdated or not:
# pip list -o

# to update/upgrade package:
# pip install -U setuptools

# install packages from a file
# cat r_text.txt
# pip install -r r_test.txt

# To update all packages at once   :
# pip freeze --local | grep -v '^\-e' | cut -d = -f 1 | xargs -n1 pip install -U
