\NeedsTeXFormat{LaTeX2e}
\ProvidesExplClass{xdyydoc}{2024-04-17}{0.0.1}{xdyy doc class}


\keys_define:nn { xdyydoc } 
  {
    unknown .code:n = \PassOptionsToClass{#1}{cusdoc} 
  }
\ExplSyntaxOff

\ProcessKeyOptions


\InputIfFileExists{xdyydoc.cfg}{}{}

\LoadClass{cusdoc}


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


\RequirePackage { dirtree }  % 排模板构成的目录树