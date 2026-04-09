# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           goleak
%define go_import_path  go.uber.org/goleak

Name:           go-uber-goleak
Version:        1.3.0
Release:        %autorelease
Summary:        Goroutine leak detector
License:        MIT
URL:            https://github.com/uber-go/goleak
#!RemoteAsset
Source0:        https://github.com/uber-go/goleak/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(go.uber.org/goleak) = %{version}

Requires:       go(github.com/stretchr/testify)

%description
Goroutine leak detector to help avoid Goroutine leaks.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
