\NeedsTeXFormat{LaTeX2e}
\ProvidesExplClass{xdyydoc}{2024-04-17}{0.0.1}{xdyy doc class}


\prg_generate_conditional_variant:Nnn \tl_if_blank:n { v } { T, F, TF }


\keys_define:nn { xdyydoc } 
  {
    unknown .code:n = \PassOptionsToClass{#1}{cusdoc} 
  }

\ProcessKeyOptions


\InputIfFileExists{xdyydoc.cfg}{}{}

\PassOptionsToPackage { most } { tcolorbox }
\LoadClass { whudoc }

% 定义键值对输出
% https://github.com/stone-zeng/fduthesis/blob/d84e0dd7df657d47943e98c98ff843cc1336bc5f/source/fduthesis-doc.dtx#L1901-L1907
\def\breakablethinspace{\hskip 0.16667em\relax}
\DeclareDocumentCommand\kv{mm}
  % {\texttt{#1\breakablethinspace=\breakablethinspace#2}}
  {
    \key{#1}
    \breakablethinspace=\breakablethinspace
    \opt{#2}
  }

\RequirePackage { dirtree }  % 排版模板构成的目录树


\DeclareDocumentEnvironment { quotation } { +b }
  {
    \group_begin:
      \kaishu
      #1
    \group_end:
  }
  {
  }

\tcolorboxenvironment { quotation }
  {
    enhanced~jigsaw, 
    parbox = false,
    breakable,
    before~upper = \quad,
    left = 3mm,
    top  = 4mm,
    bottom = 4mm,
    right = 3mm,
    % blanker,
    frame~hidden,
    % boxrule = 0pt,
    before~skip = 10pt,
    after~skip = 10pt,
    borderline~west = {1mm}{0pt}{gray},
    colback = lightgray!20!white,
  }

\cs_new_protected_nopar:Npn \zhfile #1
  {
    \group_begin:
      《\kaishu #1》
    \group_end:
  }

\bool_new:N \l__xdyydoc_refinfo_itemize_bool
\bool_new:N \l__xdyydoc_refinfo_show_localfile_bool
\tl_new:N \l_xdyydoc_refinfo_date_tl
\tl_new:N \l_xdyydoc_refinfo_localfile_tl
\keys_define:nn { xdyydoc / refinfo }
  {  
    title .tl_set:N = \l_xdyydoc_refinfo_title_tl,
    date .code:n = 
      {
        \bool_set_true:N \l__xdyydoc_refinfo_itemize_bool
        \tl_set:Nn \l_xdyydoc_refinfo_date_tl { #1 }
      },
    localfile .code:n =
      {
        \bool_set_true:N \l__xdyydoc_refinfo_itemize_bool
        \tl_set:Nn \l_xdyydoc_refinfo_localfile_tl 
          {
            \href{#1}{ \l_xdyydoc_refinfo_title_tl }
          }
      },
    show-localfile .bool_set:N = \l__xdyydoc_refinfo_show_localfile_bool,
    show-localfile .default:n = true,
  }
\NewDocumentCommand \refinfo  { m }
  {
    \keys_set:nn { xdyydoc / refinfo } { #1 }
    \begin{Framed}
      [
        frame = 
          {
            \setlength{\fboxsep}{\whuframesep}
            \setlength{\fboxrule}{\whuframerule}
            \fcolorbox{black}{gray!10!white}
          }
      ]
      \begin{center}
        \Large \bfseries \l_xdyydoc_refinfo_title_tl
      \end{center}
      \bool_if:NT \l__xdyydoc_refinfo_itemize_bool
        { \begin{itemize} }
        \__xdyydoc_refinfo_content:nn { date } { 时间：}
        \bool_if:NT \l__xdyydoc_refinfo_show_localfile_bool
          { \__xdyydoc_refinfo_content:nn { localfile } { 本地文件：} }
      \bool_if:NT \l__xdyydoc_refinfo_itemize_bool
        { \end{itemize} }
    \end{Framed}
  }

\cs_new_protected:Npn \__xdyydoc_refinfo_content:nn #1#2
  {
    \tl_if_blank:vF { l_xdyydoc_refinfo_ #1 _tl }
      {
        \item #2 \tl_use:c { l_xdyydoc_refinfo_ #1 _tl }
      }
  }