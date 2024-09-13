" sets
set ai et hls ic is nu noswf rnu sc sta udf
set sts=0 ts=8 sw=4 " mouse=a

" binds
nnoremap <Esc><Esc> :nohlsearch<CR>

" exe
autocmd filetype cpp nnoremap <F7> :w <bar> !g++ % -std=c++20 -o %:r && ./%:r <CR>
autocmd filetype cpp nnoremap <F12> :w <bar> !g++ % -std=c++20 -o %:r && ./%:r < ./in.txt <CR>

autocmd filetype python nnoremap <F7> :w <bar> !$(which python) % <CR>
autocmd filetype python nnoremap <F12> :w <bar> !$(which python) % < ./in.txt <CR>
