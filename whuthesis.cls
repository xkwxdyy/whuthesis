\NeedsTeXFormat{LaTeX2e}
\RequirePackage{l3keys2e}
\def\whu@d@te{2024/03/27}
\def\whu@versi@n{0.0.1}
\ProvidesExplClass{whuthesis}{\whu@d@te}{\whu@versi@n}{Thesis template for Wuhan University}

\keys_define:nn { whu/class }
  {
    library .code:n = \__whu_load_library:n {#1}
  }

\ProcessKeysPackageOptions { whu/class }

% 消除 xeCJK 的警告
\PassOptionsToPackage{silent}{xeCJK}

\LoadClass{book}

\RequirePackage{ctex}
\RequirePackage{whu}