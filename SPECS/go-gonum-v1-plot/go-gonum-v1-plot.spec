# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           plot
%define go_import_path  gonum.org/v1/plot
# Circular dependency & Can't stand more tests - 251
# Also the last two only works on amd64
%define go_test_exclude_glob %{shrink:
    gonum.org/v1/gonum*
    gonum.org/v1/plot/palette/moreland
    gonum.org/v1/plot/plotter
    gonum.org/v1/plot/vg/vgsvg
    gonum.org/v1/plot/vg/vgtex
    gonum.org/v1/plot/text
}

Name:           go-gonum-v1-plot
Version:        0.16.0
Release:        %autorelease
Summary:        A repository for plotting and visualizing data
License:        BSD-3-Clause
URL:            https://github.com/gonum/plot
#!RemoteAsset
Source0:        https://github.com/gonum/plot/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}
BuildOption(check):  -short -skip TestDrawGlyphBoxes

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(codeberg.org/go-fonts/latin-modern)
BuildRequires:  go(codeberg.org/go-fonts/liberation)
BuildRequires:  go(codeberg.org/go-latex/latex)
BuildRequires:  go(codeberg.org/go-pdf/fpdf)
BuildRequires:  go(git.sr.ht/~sbinet/gg)
BuildRequires:  go(github.com/ajstarks/svgo)
BuildRequires:  go(golang.org/x/image)
BuildRequires:  go(rsc.io/pdf)

Provides:       go(gonum.org/v1/plot) = %{version}

Requires:       go(codeberg.org/go-fonts/latin-modern)
Requires:       go(codeberg.org/go-fonts/liberation)
Requires:       go(codeberg.org/go-latex/latex)
Requires:       go(codeberg.org/go-pdf/fpdf)
Requires:       go(git.sr.ht/~sbinet/gg)
Requires:       go(github.com/ajstarks/svgo)
Requires:       go(golang.org/x/image)
Requires:       go(rsc.io/pdf)

%description
gonum/plot is the new, official fork of code.google.com/p/plotinum. It
provides an API for building and drawing plots in Go. *Note* that this
new API is still in flux and may change. See the wiki for some example
plots (http://github.com/gonum/plot/wiki/Example-plots).

For additional Plotters, see the Community Plotters
(https://github.com/gonum/plot/wiki/Community-Plotters) Wiki page.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
