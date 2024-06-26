"Sets
set relativenumber
set ignorecase
set hlsearch
set title
set incsearch
set autoindent
set noerrorbells
inoremap <C-x> <C-n>

"Syntax
syntax on

"Commands
nnoremap <silent> <Esc><Esc> <Esc>:nohlsearch<CR><Esc>
autocmd filetype cpp nnoremap <F6> :w <bar> !g++ % -std=c++20 -o %:r && ./%:r <CR>
