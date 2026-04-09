# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           uniseg
%define go_import_path  github.com/rivo/uniseg

Name:           go-github-rivo-uniseg
Version:        0.4.7
Release:        %autorelease
Summary:        Unicode Text Segmentation, Word Wrapping, and String Width Calculation in Go
License:        MIT
URL:            https://github.com/rivo/uniseg
#!RemoteAsset
Source0:        https://github.com/rivo/uniseg/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/rivo/uniseg) = %{version}

%description
This Go package implements Unicode Text Segmentation according to
Unicode Standard Annex #29 (https://unicode.org/reports/tr29/), Unicode
Line Breaking according to Unicode Standard Annex #14
(https://unicode.org/reports/tr14/) (Unicode version 15.0.0), and
monospace font string width calculation similar to wcwidth
(https://man7.org/linux/man-pages/man3/wcwidth.3.html).

%files
%license LICENSE*
%doc README*
%{_datadir}/gocode/src/%{go_import_path}

%changelog
%autochangelog
