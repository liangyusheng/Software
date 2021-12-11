" local syntax file - set colors on a per-machine basis:
" vim: tw=0 ts=4 sw=4
" Vim color file
"
" Winows    $gVimPath/colors/$thisFile.vim
" Linux     /usr/share/vim/vim80/colors/$thisFile.vim
"
" vimrc     colors $thisFile.vim

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
