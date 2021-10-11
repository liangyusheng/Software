#!/usr/bin/python
# -*- coding: utf8 -*-

import os
import sys

# 检查操作系统
def checkOs()->bool:
    file = '/etc/issue'
    txt = ''
    with open(file, 'r') as f:
        txt = f.readline()
        f.close()
    code = 'Manjaro Linux \\r  (\\n) (\\l)\n'
    
    if txt == code:
        return True
    return False

# 追加文本
def appendTextToFirstLine(file, txt) ->None:
    oldTxt = ''
    with open(file, 'r') as f:
        f.seek(0)
        oldTxt = f.read()
        f.close()
    with open(file, 'w') as f:
        f.seek(0)
        f.write(txt)
        f.write(oldTxt)
        f.close()

# 写入普通文本
def writeTxt(file, txt):
    with open(file, 'w+') as f:
        f.write(txt)
        f.close()

class PrintInfo:
    def print_warmming(input):
        print("\033[0;35;40m%s\033[0m" %input)

    def print_errors(input):
        print("\033[0;31;40m%s\033[0m" %input)

    def print_normal(input):
        print("\033[0;36;40m%s\033[0m" %input)

    def print_pass(input):
        print("\033[0;32;40m%s\033[0m" %input)

# 设置 pacman 软件源
def setPacmanSoftwareSource() ->None:
    file = '/etc/pacman.d/mirrorlist'
    code = 'Server = https://mirrors.tuna.tsinghua.edu.cn/archlinux/$repo/os/$arch\n'
    appendTextToFirstLine(file, code)

# 安装 yay 软件
def installYayHelper() ->None:
    file = '/etc/pacman.conf'
    code = '''
[archlinuxcn]
Server = https://mirrors.tuna.tsinghua.edu.cn/archlinuxcn/$arch
'''
    with open(file, 'a+') as f:
        f.write(code)
        f.close()

    os.system('rm -f /etc/lsb-release')
    os.system('pacman -Syy')
    os.system('pacman -S archlinuxcn-keyring')
    os.system('pacman -S yay')
    os.system('pacman -S fakeroot vim')
    os.system('pacman -Rs vi nano')

# 安装必备软件
def installPrerequisiteSoftwares() ->None:
    cmd = '''
pacman -S qt5-base qt5-doc clang clazy qt5-quick3d qt5-quickcontrols2 qt5-serialport
pacman -S qt5-svg qt5-tools qt5-webengine syntax-highlighting yaml-cpp cmake gdb qbs
pacman -S qt5-examples qt5-translations llvm
pacman -S qtcreator pkgconf gdb vim cmake boost sfml gitg neofetch
pacman -S electron qv2ray v2ray qbittorrent mpv typora obs-studio
'''
    os.system(cmd)
    yaySoftwares = 'sudo -u yusheng yay -S netease-cloud-music'
    os.system(yaySoftwares)
    yaySoftwares = 'sudo -u yusheng yay -S google-chrome'
    os.system(yaySoftwares)
    yaySoftwares = 'sudo -u yusheng yay -S wing-personal'
    os.system(yaySoftwares)
    yaySoftwares = 'sudo -u yusheng yay -S balena-etcher'
    os.system(yaySoftwares)

# 配置中文输入法
def configChineseInput() ->None:
    cmd = 'pacman -S fcitx5 fcitx5-configtool fcitx5-qt fcitx5-gtk fcitx5-chinese-addons fcitx5-material-color'
    os.system(cmd)
    file1 = '/root/.pam_environment'
    file1_2 = '/home/yusheng/.pam_environment'
    code1 = '''
GTK_IM_MODULE DEFAULT=fcitx
QT_IM_MODULE  DEFAULT=fcitx
XMODIFIERS    DEFAULT=@im=fcitx
'''
    os.system('rm -rf ' + file1)
    os.system('rm -rf ' + file1_2)
    writeTxt(file1, code1)
    writeTxt(file1_2, code1)
    os.system('chown yusheng:yusheng ' + file1_2)
    
    file2 = '/root/.xprofile'
    file2_2 = '/home/yusheng/.xprofile'
    code2 = 'fcitx5 &'
    os.system('rm -rf ' + file2)
    os.system('rm -rf ' + file2_2)
    writeTxt(file2, code2)
    writeTxt(file2_2, code2)
    os.system('chown yusheng:yusheng ' + file2_2)
    
    os.system('mkdir -p /root/.config/fcitx5/conf/')
    file3 = '/root/.config/fcitx5/conf/classicui.conf'
    os.system('mkdir -p /home/yusheng/.config/fcitx5/conf/')
    os.system('chown yusheng:yusheng /home/yusheng/fcitx5/')
    os.system('chown yusheng:yusheng /home/yusheng/fcitx5/conf/')
    file3_2 = '/home/yusheng/.config/fcitx5/conf/classicui.conf'
    code3 = '''
Vertical Candidate List=False
PerScreenDPI=True
Font="思源黑体 CN Medium 10"
Theme=Material-Color-DeepPurple
'''
    os.system('rm -rf ' + file3)
    os.system('rm -rf ' + file3_2)
    writeTxt(file3, code3)
    writeTxt(file3_2, code3)
    os.system('chown yusheng:yusheng ' + file3_2)
    
# 配置 smb
def setSamba() ->None:
    code = '''
[Unit]
Description = Mount Samba disk
Requires    = network-online.target
After       = network-online.target systemd-resolved.service
Wants       = network-online.target systemd-resolved.service

[Mount]
What        = //10.10.10.1/www.phicomm.com_usb1_1
Where       = /shared
Type        = cifs
Options     = defaults,guest,vers=1.0
TimeoutSec  = 10

[Install]
WantedBy    = multi-user.target
'''
    file = '/usr/lib/systemd/system/shared.mount'
    os.system('rm -rf ' + file)
    writeTxt(file, code)
    
    installSmb = 'pacman -S cifs-utils'
    os.system(installSmb)
    
    enableSmb = 'systemctl enable shared.mount'
    os.system(enableSmb)
    
    enableNetworkOnline = 'systemctl enable NetworkManager-wait-online.service'
    os.system(enableNetworkOnline)
    
# 配置 virtscreen
# 很慢，放在最后
def configVirtSreen() ->None:
    file = '/etc/X11/xorg.conf.d/30-virtscreen.conf'
    code =  '''
Section     "Device"
Identifier  "intelgpu0"
Driver      "intel"
Option      "VirtualHeads"  "1"
EndSection
'''
    os.system('rm -rf ' + file)
    writeTxt(file, code)
    cmd = 'sudo -u yusheng yay -S virtscreen'
    os.system(cmd)
    
def configVim():
    file = '/etc/vimrc'
    code = '''
set nu
set ai!
set ruler
set cindent
set hlsearch
set nobackup
set t_Co=256
set tabstop=4
set showmatch
set autoindent
set cursorline
set smartindent
set history=1000
setlocal et sta sw=4 sts=4

set encoding=utf-8
set fileencodings=utf-8,ucs-bom,gb

syntax on
" colorscheme evening

" for gVim.
if has("gui_running")
    colorscheme mycolors
    set guifont=Source\ Code\ Pro:h13    
    " hide menu bar.
    set guioptions=m
    " remove right-hand scroll bar
    set guioptions-=r
    set nocompatible
    set backspace=indent,eol,start
else
    colorscheme mycolors
endif
'''
    os.system('rm -rf ' + file)
    writeTxt(file, code)
    colorsFile = '/usr/share/vim/vim82/colors/mycolors.vim'
    colorsCode = '''
set background=dark
hi clear
if exists("syntax_on")
  syntax reset
endif

let g:colors_name = "mycolors"

hi Normal       term=none       cterm=none  ctermfg=51          ctermbg=0       guifg=Cyan      guibg=#313131   gui=none
hi LineNr       term=none       cterm=none  ctermfg=25          ctermbg=0       guifg=#946300   guibg=#313131   gui=none
hi Comment      term=none       cterm=none  ctermfg=DarkGray    ctermbg=0       guifg=DarkGray  guibg=#313131   gui=none
hi Constant     term=none       cterm=none  ctermfg=208         ctermbg=0       guifg=#81c100   guibg=#313131   gui=none
hi Special      term=none       cterm=none  ctermfg=DarkMagenta ctermbg=0       guifg=Red       guibg=#313131   gui=none
hi Identifier   term=underline  cterm=none  ctermfg=Cyan        ctermbg=0       guifg=#40ffff   guibg=#313131   gui=none
hi Statement    term=none       cterm=none  ctermfg=190         ctermbg=0       guifg=#aa4444   guibg=#313131   gui=none
hi PreProc      term=underline  cterm=none  ctermfg=LightBlue   ctermbg=0       guifg=#ff80ff   guibg=#313131   gui=none
hi Type         term=underline  cterm=none  ctermfg=199         ctermbg=0       guifg=#60ff60   guibg=#313131   gui=none
hi Function     term=none       cterm=none  ctermfg=106         ctermbg=0       guifg=Yellow    guibg=#313131   gui=none
hi Repeat       term=underline  cterm=none  ctermfg=Red         ctermbg=0       guifg=Red       guibg=#313131   gui=none
hi Operator     term=none       cterm=none  ctermfg=165         ctermbg=0       guifg=LightRed  guibg=#313131   gui=none
hi Ignore       term=none       cterm=none  ctermfg=black       ctermbg=0       guifg=White     guibg=#313131   gui=none
hi Error        term=reverse    cterm=none  ctermfg=White       ctermbg=Red     guifg=White     guibg=Red       gui=none
hi Todo         term=standout   cterm=none  ctermbg=Yellow      ctermfg=Red     guifg=Yellow    guibg=Red       gui=none

" Common groups that link to default highlighting.
" You can specify other highlighting easily.
hi String          term=none    cterm=none  ctermfg=166         ctermbg=0       guifg=#ff5500   guibg=#313131   gui=none
hi Character       term=none    cterm=none  ctermfg=166         ctermbg=0       guifg=#ff5500   guibg=#313131   gui=none
hi Number          term=none    cterm=none  ctermfg=84          ctermbg=0       guifg=#aaff7f   guibg=#313131   gui=none
hi Boolean         term=none    cterm=none  ctermfg=147         ctermbg=0       guifg=#acb2ff   guibg=#313131   gui=none
hi Float           term=none    cterm=none  ctermfg=228         ctermbg=0       guifg=#ffaa7f   guibg=#313131   gui=none
hi Conditional     term=none    cterm=none  ctermfg=93          ctermbg=0       guifg=#aa55ff   guibg=#313131   gui=none
hi Label           term=none    cterm=none  ctermfg=177         ctermbg=0       guifg=#ffaaff   guibg=#313131   gui=none
hi Keyword         term=none    cterm=none  ctermfg=191         ctermbg=0       guifg=#ffff7f   guibg=#313131   gui=none
hi Exception       term=none    cterm=none  ctermfg=196         ctermbg=0       guifg=#ff0000   guibg=#313131   gui=none
hi Include         term=none    cterm=none  ctermfg=36          ctermbg=0       guifg=#00aa7f   guibg=#313131   gui=none
hi Define          term=none    cterm=none  ctermfg=85          ctermbg=0       guifg=#72e5aa   guibg=#313131   gui=none
hi Macro           term=none    cterm=none  ctermfg=85          ctermbg=0       guifg=#72e5aa   guibg=#313131   gui=none
hi PreCondit       term=none    cterm=none  ctermfg=28          ctermbg=0       guifg=#00aa00   guibg=#313131   gui=none
hi StorageClass    term=none    cterm=none  ctermfg=39          ctermbg=0       guifg=#0081bd   guibg=#313131   gui=none
hi Structure       term=none    cterm=none  ctermfg=201         ctermbg=0       guifg=#ff00ff   guibg=#313131   gui=none
hi Typedef         term=none    cterm=none  ctermfg=58          ctermbg=0       guifg=#555500   guibg=#313131   gui=none
hi Tag             term=none    cterm=none  ctermfg=51          ctermbg=0       guifg=Cyan      guibg=#313131   gui=none
hi SpecialChar     term=none    cterm=none  ctermfg=51          ctermbg=0       guifg=Cyan      guibg=#313131   gui=none
hi Delimiter       term=none    cterm=none  ctermfg=51          ctermbg=0       guifg=Cyan      guibg=#313131   gui=none
hi SpecialComment  term=none    cterm=none  ctermfg=51          ctermbg=0       guifg=Cyan      guibg=#313131   gui=none
hi Debug           term=none    cterm=none  ctermfg=51          ctermbg=0       guifg=Cyan      guibg=#313131   gui=none
set background=dark
hi clear
if exists("syntax_on")
  syntax reset
endif

let g:colors_name = "mycolors"

hi Normal       term=none       cterm=none  ctermfg=51          ctermbg=0       guifg=Cyan      guibg=#313131   gui=none
hi LineNr       term=none       cterm=none  ctermfg=25          ctermbg=0       guifg=#946300   guibg=#313131   gui=none
hi Comment      term=none       cterm=none  ctermfg=DarkGray    ctermbg=0       guifg=DarkGray  guibg=#313131   gui=none
hi Constant     term=none       cterm=none  ctermfg=208         ctermbg=0       guifg=#81c100   guibg=#313131   gui=none
hi Special      term=none       cterm=none  ctermfg=DarkMagenta ctermbg=0       guifg=Red       guibg=#313131   gui=none
hi Identifier   term=underline  cterm=none  ctermfg=Cyan        ctermbg=0       guifg=#40ffff   guibg=#313131   gui=none
hi Statement    term=none       cterm=none  ctermfg=190         ctermbg=0       guifg=#aa4444   guibg=#313131   gui=none
hi PreProc      term=underline  cterm=none  ctermfg=LightBlue   ctermbg=0       guifg=#ff80ff   guibg=#313131   gui=none
hi Type         term=underline  cterm=none  ctermfg=199         ctermbg=0       guifg=#60ff60   guibg=#313131   gui=none
hi Function     term=none       cterm=none  ctermfg=106         ctermbg=0       guifg=Yellow    guibg=#313131   gui=none
hi Repeat       term=underline  cterm=none  ctermfg=Red         ctermbg=0       guifg=Red       guibg=#313131   gui=none
hi Operator     term=none       cterm=none  ctermfg=165         ctermbg=0       guifg=LightRed  guibg=#313131   gui=none
hi Ignore       term=none       cterm=none  ctermfg=black       ctermbg=0       guifg=White     guibg=#313131   gui=none
hi Error        term=reverse    cterm=none  ctermfg=White       ctermbg=Red     guifg=White     guibg=Red       gui=none
hi Todo         term=standout   cterm=none  ctermbg=Yellow      ctermfg=Red     guifg=Yellow    guibg=Red       gui=none

" Common groups that link to default highlighting.
" You can specify other highlighting easily.
hi String          term=none    cterm=none  ctermfg=166         ctermbg=0       guifg=#ff5500   guibg=#313131   gui=none
hi Character       term=none    cterm=none  ctermfg=166         ctermbg=0       guifg=#ff5500   guibg=#313131   gui=none
hi Number          term=none    cterm=none  ctermfg=84          ctermbg=0       guifg=#aaff7f   guibg=#313131   gui=none
hi Boolean         term=none    cterm=none  ctermfg=147         ctermbg=0       guifg=#acb2ff   guibg=#313131   gui=none
hi Float           term=none    cterm=none  ctermfg=228         ctermbg=0       guifg=#ffaa7f   guibg=#313131   gui=none
hi Conditional     term=none    cterm=none  ctermfg=93          ctermbg=0       guifg=#aa55ff   guibg=#313131   gui=none
hi Label           term=none    cterm=none  ctermfg=177         ctermbg=0       guifg=#ffaaff   guibg=#313131   gui=none
hi Keyword         term=none    cterm=none  ctermfg=191         ctermbg=0       guifg=#ffff7f   guibg=#313131   gui=none
hi Exception       term=none    cterm=none  ctermfg=196         ctermbg=0       guifg=#ff0000   guibg=#313131   gui=none
hi Include         term=none    cterm=none  ctermfg=36          ctermbg=0       guifg=#00aa7f   guibg=#313131   gui=none
hi Define          term=none    cterm=none  ctermfg=85          ctermbg=0       guifg=#72e5aa   guibg=#313131   gui=none
hi Macro           term=none    cterm=none  ctermfg=85          ctermbg=0       guifg=#72e5aa   guibg=#313131   gui=none
hi PreCondit       term=none    cterm=none  ctermfg=28          ctermbg=0       guifg=#00aa00   guibg=#313131   gui=none
hi StorageClass    term=none    cterm=none  ctermfg=39          ctermbg=0       guifg=#0081bd   guibg=#313131   gui=none
hi Structure       term=none    cterm=none  ctermfg=201         ctermbg=0       guifg=#ff00ff   guibg=#313131   gui=none
hi Typedef         term=none    cterm=none  ctermfg=58          ctermbg=0       guifg=#555500   guibg=#313131   gui=none
hi Tag             term=none    cterm=none  ctermfg=51          ctermbg=0       guifg=Cyan      guibg=#313131   gui=none
hi SpecialChar     term=none    cterm=none  ctermfg=51          ctermbg=0       guifg=Cyan      guibg=#313131   gui=none
hi Delimiter       term=none    cterm=none  ctermfg=51          ctermbg=0       guifg=Cyan      guibg=#313131   gui=none
hi SpecialComment  term=none    cterm=none  ctermfg=51          ctermbg=0       guifg=Cyan      guibg=#313131   gui=none
hi Debug           term=none    cterm=none  ctermfg=51          ctermbg=0       guifg=Cyan      guibg=#313131   gui=none
'''
    os.system('rm -rf ' + colorsFile)
    writeTxt(colorsFile, colorsCode)


def configBash():
    code = '''
\nPS1='\\[\\e[1;33m\\][\\[\\e[1;31m\\]\\u@\\h \\[\\e[1;36m\\]\\w\\[\\e[1;33m\\]]\\[\\e[1;35m\\]\\$ \\[\\e[0m\\]'
\nalias ls='ls --color=auto'
'''
    file = '/root/.bashrc'
    with open(file, 'a+') as f:
        f.write(code)
        f.close()

    code2 = '''
\nPS1='\\[\\e[1;33m\\][\\[\\e[1;32m\\]\\u@\\h \\[\\e[1;36m\\]\\w\\[\\e[1;33m\\]]\\[\\e[1;35m\\]\\$ \\[\\e[0m\\]'
\nalias ls='ls --color=auto'
    '''
    file2 = '/home/yusheng/.bashrc'
    with open(file2, 'a+') as f:
        f.write(code2)
        f.close()

    
def main():
    PrintInfo.print_warmming('Checking your opearator system...')
    if not checkOs():
        PrintInfo.print_errors('The system only runing Linux!')
        sys.exit()
    PrintInfo.print_pass('OK!')

    PrintInfo.print_warmming('Setting pacman software source...')
    setPacmanSoftwareSource()
    PrintInfo.print_pass('OK!')

    PrintInfo.print_warmming('installing yay software helper...')
    installYayHelper()
    PrintInfo.print_pass('OK!')
    
    PrintInfo.print_warmming('config Chinese input...')
    configChineseInput()
    PrintInfo.print_pass('OK!')
    
    PrintInfo.print_warmming('config vim...')
    configVim()
    PrintInfo.print_pass('OK!')
    
    PrintInfo.print_warmming('config bash...')
    configBash()
    PrintInfo.print_pass('OK!')

    PrintInfo.print_warmming('installing prerequisite softwares...')
    installPrerequisiteSoftwares()
    PrintInfo.print_pass('OK!')

    PrintInfo.print_warmming('installing VirtScreen...')
    configVirtSreen()
    PrintInfo.print_pass('OK!')
    
if __name__ == "__main__":   
    main()
 
