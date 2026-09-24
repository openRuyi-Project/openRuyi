# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: wangyf0611 <wangyufeng@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           stack
%define go_import_path  github.com/go-stack/stack

Name:           go-github-go-stack-stack
Version:        1.8.0
Release:        %autorelease
Summary:        Implements utilities to capture, manipulate, and format call stacks
License:        MIT
URL:            https://github.com/go-stack/stack
VCS:            git:https://github.com/go-stack/stack.git
#!RemoteAsset:  sha256:3b8987e137d76f4f35db1e8005ec7fb766b68eed8cac0ca0b795ac43cd72b319
Source0:        https://github.com/go-stack/stack/archive/v1.8.0.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n stack-1.8.0

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/go-stack/stack) = %{version}

%description
This package provides the github.com/go-stack/stack Go module source.

%files
%doc README.md
%license LICENSE.md
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
