# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           barcode
%define go_import_path  github.com/boombuler/barcode

Name:           go-github-boombuler-barcode
Version:        1.1.0
Release:        %autorelease
Summary:        a barcode creation lib for golang
License:        MIT
URL:            https://github.com/boombuler/barcode
#!RemoteAsset
Source0:        https://github.com/boombuler/barcode/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/boombuler/barcode) = %{version}

%description
This is a package for GO which can be used to create different types of
barcodes.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
