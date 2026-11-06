# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           pty
%define go_import_path  github.com/kr/pty

Name:           go-github-kr-pty
Version:        1.1.8
Release:        %autorelease
Summary:        Compatibility wrapper for the historical Go PTY import path
License:        MIT
URL:            https://github.com/kr/pty
#!RemoteAsset:  sha256:9258c76d18238fe6c4f5238a777a204f1e88e6e965eb75688daf74d280bebdae
Source0:        https://github.com/kr/pty/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/creack/pty)

Provides:       go(github.com/kr/pty) = %{version}

Requires:       go(github.com/creack/pty)

%description
This library preserves the github.com/kr/pty API by forwarding calls
to the maintained github.com/creack/pty implementation.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
