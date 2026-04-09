# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           image
%define go_import_path  golang.org/x/image

Name:           go-golang-x-image
Version:        0.34.0
Release:        %autorelease
Summary:        Go supplementary image libraries
License:        BSD-3-Clause
URL:            https://golang.org/x/image
VCS:            git:https://github.com/golang/image
#!RemoteAsset
Source0:        https://github.com/golang/image/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/text)

Provides:       go(golang.org/x/image) = %{version}

Requires:       go(golang.org/x/text)

%description
This repository holds supplementary Go image packages.

%prep
%autosetup -n %{_name}-%{version}

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
