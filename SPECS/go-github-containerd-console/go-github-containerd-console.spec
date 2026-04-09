# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           console
%define go_import_path  github.com/containerd/console

Name:           go-github-containerd-console
Version:        1.0.5
Release:        %autorelease
Summary:        console package for Go
License:        Apache-2.0
URL:            https://github.com/containerd/console
#!RemoteAsset
Source0:        https://github.com/containerd/console/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/sys)

Provides:       go(github.com/containerd/console) = %{version}

Requires:       go(golang.org/x/sys)

%description
console is a Golang package for dealing with consoles.
Light on deps and a simple API.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
