# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: wangyf0611 <wangyufeng@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           packd
%define go_import_path  github.com/gobuffalo/packd

Name:           go-github-gobuffalo-packd
Version:        0.3.0
Release:        %autorelease
Summary:        Go library for packd
License:        MIT
URL:            https://github.com/gobuffalo/packd
VCS:            git:https://github.com/gobuffalo/packd.git
#!RemoteAsset:  sha256:aedae215fadb688a0a66ed8d64eff44169ef517a4ea7b9defb0a2ed0cfd78185
Source0:        https://github.com/gobuffalo/packd/archive/v0.3.0.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n packd-0.3.0

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(github.com/gobuffalo/packd) = %{version}

%description
This package provides the github.com/gobuffalo/packd Go module source.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
