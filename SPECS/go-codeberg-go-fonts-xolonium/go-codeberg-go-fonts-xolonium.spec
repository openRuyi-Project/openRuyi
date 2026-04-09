# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           xolonium
%define go_import_path  codeberg.org/go-fonts/xolonium

Name:           go-codeberg-go-fonts-xolonium
Version:        0.2.0
Release:        %autorelease
Summary:        Xolonium fonts for Go
License:        BSD-3-Clause
URL:            https://codeberg.org/go-fonts/xolonium
#!RemoteAsset
Source0:        https://codeberg.org/go-fonts/xolonium/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/image)

Provides:       go(codeberg.org/go-fonts/xolonium) = %{version}

Requires:       go(golang.org/x/image)

%description
This package provides the xolonium fonts as importable Go packages.

%prep -a
# Upstream import paths are so wrong...
grep -R "codeberg.org/go-fonts/xonolonium" -n . || :
sed -i 's|codeberg\.org/go-fonts/xonolonium|codeberg.org/go-fonts/xolonium|g' $(find . -name '*.go' -type f)

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
