from fabric.api import local

def build():
    local('uglifyjs markedown.js --mangle --compress > markedown.min.js')
