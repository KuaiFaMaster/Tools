__author__ = 'ly'
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, re

def multi_replace(text, adict):
    rx = re.compile('|'.join(map(re.escape, adict)))
    def xlat(match):
        return adict[match.group(0)]
    return rx.sub(xlat, text)

def batrename(curdir, pairs):
    for fn in os.listdir(curdir):
        newfn = multi_replace(fn, pairs)
        if newfn != fn:
            print("Renames %s to %s in %s." % (fn, newfn, curdir))
            os.rename(os.path.join(curdir, fn), os.path.join(curdir, newfn))
        file = os.path.join(curdir, newfn)

        if os.path.isdir(file):
            batrename(file, pairs)
            continue

        text = open(file).read()
        newtext = multi_replace(text, pairs)
        if newtext != text:
            print("Renames %s." % (file,))
            open(file, 'w').write(newtext)
def copy_files(source_dir, target_dir):
    if not os.path.exists(source_dir) and not os.path.exists(target_dir):
        print('copy files from %s to %s fail:file not found' % (source_dir, target_dir))
        return
    for file in os.listdir(source_dir):
        source_file = os.path.join(source_dir, file)
        target_file = os.path.join(target_dir,file)
        if os.path.isfile(source_file):
            if not os.path.exists(target_dir):
                os.makedirs(target_dir)
            if not os.path.exists(target_file) or (os.path.exists(target_file) and (os.path.getsize(target_file) != os.path.getsize(source_file))):
                open(target_file,'wb').write(open(source_file,'rb').read())
        if os.path.isdir(source_file):
            copy_files(source_file,target_file)

if __name__=="__main__":
    sourcedir = os.path.abspath('F:\MyGit\kuaifa')
    targetdir = os.path.abspath('F:\MyGit\kuaifaTest')
    copy_files(sourcedir,targetdir)
    newsdkname = raw_input("please input new sdkName: ")
    newdomainname = raw_input("pelase input new domain name: ")
    oldsdkname = 'kuaifa'
    for i in range(4):
         if oldsdkname and newsdkname:
            if i == 1:
                oldsdkname = oldsdkname.upper()
                newsdkname = newsdkname.upper()
            elif i == 2:
                oldsdkname = oldsdkname.capitalize()
                newsdkname = newsdkname.capitalize()
            elif i == 3:
                oldsdkname = 'KuaiFa'
                newsdkname = newsdkname.capitalize()
            print  i
            print  'oldname = '+oldsdkname +',newname = '+newsdkname + ',path='+os.path.abspath(targetdir)
            batrename(os.path.abspath(targetdir), {oldsdkname:newsdkname})
    olddomainname = 'test.g.haojieru.com'
    for i in range(2):
        if i == 1:
            olddomainname = 'g.haojieru.com'
        print  i
        print  'olddomainname = '+olddomainname +',newdomainname = '+newdomainname
        batrename(os.path.abspath(targetdir), {olddomainname:newdomainname})
