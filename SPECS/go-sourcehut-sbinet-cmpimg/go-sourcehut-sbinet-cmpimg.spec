# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           cmpimg
%define go_import_path  git.sr.ht/~sbinet/cmpimg

Name:           go-sourcehut-sbinet-cmpimg
Version:        0.1.0
Release:        %autorelease
Summary:        simple package to compare images
License:        BSD-3-Clause
URL:            https://git.sr.ht/~sbinet/cmpimg
#!RemoteAsset
Source0:        https://git.sr.ht/~sbinet/cmpimg/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/image)
BuildRequires:  go(rsc.io/pdf)

Provides:       go(git.sr.ht/~sbinet/cmpimg) = %{version}

Requires:       go(golang.org/x/image)
Requires:       go(rsc.io/pdf)

%description
cmpimg is a simple package (extracted from Gonum/plot) to
compare images (PNG, JPEG, PDF, ...)

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
