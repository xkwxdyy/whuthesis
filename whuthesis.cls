%%  whuthesis
%%  Copyright (C) 2024 Kangwei Xia <https://github.com/xkwxdyy>
%% 
%%  This work may be distributed and/or modified under the
%%  conditions of the LaTeX Project Public License, either
%%  version 1.3c of this license or (at your option) any later
%%  version. The latest version of this license is in:
%% 
%%    http://www.latex-project.org/lppl.txt
%% 
%%  and version 1.3 or later is part of all distributions of
%%  LaTeX version 2008 or later.
%% 
%%  This work has the LPPL maintenance status `maintained'.
%% 
%%  The Current Maintainer of this work is Kangwei Xia <kangweixia_xdyy@163.com>.
%%
%% This work consists of the files whu.sty, whuthesis.cls .
%%
\NeedsTeXFormat{LaTeX2e}
\RequirePackage{l3keys2e}
% \whu@date 和 \whu@version 为 whuthesis 的日期和版本号
% \whu@d@te 和 \whu@versi@n 为上游的 CusTeX 的日期和版本号
\def\whu@date{2024/04/06}
\def\whu@version{0.0.3}
\ProvidesExplClass{whuthesis}{\whu@date}{\whu@version}{Thesis template for Wuhan University}


\str_new:N \g__whu_type_str
\clist_new:N \g__whu_to_book_clist

\keys_define:nn { whu/class }
  {
    library .code:n = 
      { \PassOptionsToPackage { library = {#1} } { whu } }
  , type .choice:
  , type/electronic .code:n = 
      {
        \str_gset:Nn \g__whu_type_str { electronic }
        \clist_gput_right:Nn \g__whu_to_book_clist { a4paper, twoside }
      }
  , type/for-print .code:n = 
    {
      \str_gset:Nn \g__whu_type_str { for-print }
      \clist_gput_right:Nn \g__whu_to_book_clist { a4paper, twoside }
    }
  , type/for-library .code:n = 
    {
      \str_gset:Nn \g__whu_type_str { for-library }
      \clist_gput_right:Nn \g__whu_to_book_clist { a4paper, twoside, openany }
    }
  , type .initial:n = electronic
  }

\ProcessKeysOptions { whu/class }

\cs_new:Nn \__whu_type_electronic_setting: 
  { \__whu_type_electronic_additional_setting: }
\cs_new:Nn \__whu_type_electronic_additional_setting: { }
\cs_new:Nn \__whu_type_for_print_setting: 
  { \__whu_type_for_print_additional_setting: }
\cs_new:Nn \__whu_type_for_print_additional_setting: { }
\cs_new:Nn \__whu_type_for_library_setting: 
  {
    % 这样设置可以防止 \frontmatter 和 \mainmatter 里面的 \cleardoublepage 产生空白页
    \cs_set_eq:NN \__whu_cleardoublepage: \cleardoublepage
    \AddToHook { cmd / frontmatter / before }
      { \cs_set_eq:NN \cleardoublepage \newpage }
    \AddToHook { cmd / frontmatter / after }
      { \cs_set_eq:NN \cleardoublepage \__whu_cleardoublepage: }
    \AddToHook { cmd / mainmatter / before }
      { \cs_set_eq:NN \cleardoublepage \newpage }
    \AddToHook { cmd / mainmatter / after }
      { \cs_set_eq:NN \cleardoublepage \__whu_cleardoublepage: }

    % 2024-04-07 zepinglee 建议不用上面那样 hook，直接加一个 \@twosidefalse 即可，但是这样会影响页眉
    % \@twosidefalse
    \__whu_type_for_library_additional_setting:
  }
\cs_new:Nn \__whu_type_for_library_additional_setting: { } 

% 消除 xeCJK 的警告
\PassOptionsToPackage { silent } { xeCJK }



\seq_put_right:Nx \l_file_search_path_seq { ./module }
\seq_put_right:Nx \l_file_search_path_seq { ./library }
\seq_put_right:Nx \l_file_search_path_seq { ./library-cus }
\RequirePackage { whu }


% 要放在 whu 加载之后
\str_case:Vn \g__whu_type_str
  {
    { electronic } { \__whu_type_electronic_setting: }
    { for-print } { \__whu_type_for_print_setting: }
    { for-library } { \__whu_type_for_library_setting: }
  }
\PassOptionsToClass{ \g__whu_to_book_clist }{ book }
\LoadClass { book }


\RequirePackage { ctex }
\RequirePackage { graphicx }
\graphicspath { {./figures/} {./logo/} } 


\RequirePackage { tikzpagenodes }
\ExplSyntaxOff
\usetikzlibrary { positioning }
\ExplSyntaxOn

\RequirePackage { tabularray }

\AtEndPreamble
  {
    \RequirePackage { hyperref }
    \hypersetup 
      { 
        pdfencoding = auto,
        citecolor   = magenta,
        linkcolor   = blue,
        hidelinks
      }
  }