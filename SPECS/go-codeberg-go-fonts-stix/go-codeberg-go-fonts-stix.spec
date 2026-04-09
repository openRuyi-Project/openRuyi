# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           stix
%define go_import_path  codeberg.org/go-fonts/stix

Name:           go-codeberg-go-fonts-stix
Version:        0.3.0
Release:        %autorelease
Summary:        STIX fonts for Go
License:        BSD-3-Clause
URL:            https://codeberg.org/go-fonts/stix
#!RemoteAsset
Source0:        https://codeberg.org/go-fonts/stix/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/image)

Provides:       go(codeberg.org/go-fonts/stix) = %{version}

Requires:       go(golang.org/x/image)

%description
This package provides the STIX fonts as importable Go packages.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
