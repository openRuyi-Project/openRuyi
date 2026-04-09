# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           latex
%define go_import_path  codeberg.org/go-latex/latex

Name:           go-codeberg-go-latex-latex
Version:        0.2.0
Release:        %autorelease
Summary:        Go package for LaTeX
License:        BSD-3-Clause
URL:            https://codeberg.org/go-latex/latex
#!RemoteAsset
Source0:        https://codeberg.org/go-latex/latex/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}
BuildOption(check):  -skip TestRenderer

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(codeberg.org/go-fonts/dejavu)
BuildRequires:  go(codeberg.org/go-fonts/latin-modern)
BuildRequires:  go(codeberg.org/go-fonts/liberation)
BuildRequires:  go(codeberg.org/go-fonts/stix)
BuildRequires:  go(codeberg.org/go-pdf/fpdf)
BuildRequires:  go(git.sr.ht/~sbinet/gg)
BuildRequires:  go(golang.org/x/image)

Provides:       go(codeberg.org/go-latex/latex) = %{version}

Requires:      go(codeberg.org/go-fonts/dejavu)
Requires:      go(codeberg.org/go-fonts/latin-modern)
Requires:      go(codeberg.org/go-fonts/liberation)
Requires:      go(codeberg.org/go-fonts/stix)
Requires:      go(codeberg.org/go-pdf/fpdf)
Requires:      go(git.sr.ht/~sbinet/gg)
Requires:      go(golang.org/x/image)

%description
This is a package holding Go tools for LaTeX.

This package is supposed to provide features akin to MathJax or
matplotlib's TeX capabilities. ie: it is supposed to be able to
draw mathematical equations, in pure-Go.

This package is NOT SUPPOSED to be a complete typesetting system
like LaTeX or TeX.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
