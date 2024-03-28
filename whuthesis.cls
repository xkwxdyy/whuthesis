\NeedsTeXFormat{LaTeX2e}
\RequirePackage{l3keys2e}
% \whu@date 和 \whu@version 为 whuthesis 的日期和版本号
% \whu@d@te 和 \whu@versi@n 为上游的 CusTeX 的日期和版本号
\def\whu@date{2024/03/28}
\def\whu@version{0.0.1}
\ProvidesExplClass{whuthesis}{\whu@date}{\whu@version}{Thesis template for Wuhan University}

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