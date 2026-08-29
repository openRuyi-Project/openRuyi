# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           term
%define go_import_path  github.com/moby/term

Name:           go-github-moby-term
Version:        0.5.2
Release:        %autorelease
Summary:        Terminal handling helpers from Moby
License:        Apache-2.0
URL:            https://github.com/moby/term
#!RemoteAsset:  sha256:59e529a9312d119489e081dd1ac56fc3e27ff4e4a7ea4df49430261aa570f472
Source0:        https://github.com/moby/term/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/creack/pty)
BuildRequires:  go(golang.org/x/sys)

Provides:       go(github.com/moby/term) = %{version}

Requires:       go(golang.org/x/sys)

%description
term provides Go helpers for terminal state, terminal size detection, and
standard stream handling used by Moby projects.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
