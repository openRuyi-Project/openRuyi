# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           goid
%define go_import_path  github.com/petermattis/goid
%define commit_id       269ab09b52619af7cedac9eb8ac39e877898d1dd

Name:           go-github-petermattis-goid
Version:        0+git20260823.269ab09
Release:        %autorelease
Summary:        Retrieve the current goroutine ID
License:        Apache-2.0
URL:            https://github.com/petermattis/goid
VCS:            git:https://github.com/petermattis/goid.git
#!RemoteAsset:  sha256:5870318c822a581c4dddd26d1add02423a2a82de79e9916670a35b613fb12736
Source0:        https://github.com/petermattis/goid/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{commit_id}

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/petermattis/goid) = %{version}

%description
Goid is a Go library for programmatically retrieving the identifier of the
currently executing goroutine across supported Go versions and architectures.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
