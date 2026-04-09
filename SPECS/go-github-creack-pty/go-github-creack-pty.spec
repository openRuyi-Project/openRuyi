# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           pty
%define go_import_path  github.com/creack/pty

Name:           go-github-creack-pty
Version:        1.1.24
Release:        %autorelease
Summary:        PTY interface for Go
License:        MIT
URL:            https://github.com/creack/pty
#!RemoteAsset
Source0:        https://github.com/creack/pty/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/creack/pty) = %{version}

%description
Pty is a Go package for using unix pseudo-terminals.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
