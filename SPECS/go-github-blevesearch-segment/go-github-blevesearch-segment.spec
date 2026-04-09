# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           segment
%define go_import_path  github.com/blevesearch/segment

Name:           go-github-blevesearch-segment
Version:        0.9.1
Release:        %autorelease
Summary:        A Go library for performing Unicode Text Segmentation as described in Unicode Standard Annex #29
License:        Apache-2.0
URL:            https://github.com/blevesearch/segment
#!RemoteAsset
Source0:        https://github.com/blevesearch/segment/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/blevesearch/segment) = %{version}

%description
A Go library for performing Unicode Text Segmentation as described in
Unicode Standard Annex #29 (http://www.unicode.org/reports/tr29/)

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
