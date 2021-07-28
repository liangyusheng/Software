# /etc/bashrc
#
# System-wide .bashrc file for interactive bash(1) shells.
if [ -z "$PS1" ]; then
   return
fi

# PS1='\h:\W \u\$ '
# Make bash check its window size after a process completes
shopt -s checkwinsize

[ -r "/etc/bashrc_$TERM_PROGRAM" ] && . "/etc/bashrc_$TERM_PROGRAM"



# My settings.
#
#
# dir color.
  export CLICOLOR=1
  export LSCOLORS=exdxfxgxcxhhbxcxgxExEx 
#
#
# PS1='\[\e[1;32m\]\h\[\e[1;30m\]: \[\e[1;34m\]\w\n\[\e[0m\]\[\e[0;30m\]\u\$ '
  PS1='\[\e[1;32m\]\h\[\e[1;30m\]: \[\e[1;34m\]\w\n\[\e[0m\]\u\$ '
#
# PS1='\[\e[1;35m\][     ------>  定义左边的“[”为：洋红粗体
#			 ------>  “\[”一段不显示字串的开始
#			 ------>  “/e” 转义序列开始，等同于 “/033”
#			 ------>  “[” 字体颜色开始
#			 ------>  “1；”粗体；“0”默认
#			 ------>  “35m”洋红
#			 ------>  “\]”一段不显示字串的结束
#			 ------>  “[”提示符左边的“[”
# \[\e[1;33m\]\u@\h      ------>  定义“\u@\h”为；黄色粗体
# \[\e[1;31m\]\w         ------>  定义“\w”为：红色粗体
# \[\e[1;35m\]]          ------>  定义右边的“]”为：洋红粗体
# \[\e[1;36m\]\$         ------>  定义“\$”为：青色粗体
# \[\e[0m\]'             ------>  文本颜色复位
#
# 可选的颜色代码：
# 30（黑色）、31（红色）、32（绿色）、33（黄色）、
# 34（蓝色）、35（洋红）、36（青色）、37（白色）。
#
# 常用的转义字符解释：
# \u ：当前用户的账号名称
# \h ：仅取主机的第一个名字，如上例，则为fc4，.linux则被省略
# \H ：完整的主机名称。例如：我的机器名称为：fc4.linux，则这个名称就是fc4.linux
# \w ：完整的工作目录名称。家目录会以 ~代替
# \W ：利用basename取得工作目录名称，所以只会列出最后一个目录
# \$ ：提示字符，如果是root时，提示符为：# ，普通用户则为：$
# \# ：下达的第几个命令
# \n ：新建一行
# \d ：代表日期，格式为weekday month date，例如：”Mon Aug 1″
# \t ：显示时间为24小时格式，如：HH：MM：SS
# \T ：显示时间为12小时格式
# \A ：显示时间为24小时格式：HH：MM
# \v ：BASH的版本信息
