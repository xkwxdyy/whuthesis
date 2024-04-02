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
\def\whu@date{2024/03/28}
\def\whu@version{0.0.1}
\ProvidesExplClass{whuthesis}{\whu@date}{\whu@version}{Thesis template for Wuhan University}

\keys_define:nn { whu/class }
  {
    library .code:n = 
      { \PassOptionsToPackage { library = {#1} } { whu } }
  }


\ProcessKeyOptions [ whu / class ]

% 消除 xeCJK 的警告
\PassOptionsToPackage { silent } { xeCJK }


\RequirePackage { whu }

\LoadClass { book }

\RequirePackage { ctex }