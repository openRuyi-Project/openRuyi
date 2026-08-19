# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           deck
%define go_import_path  github.com/google/deck

Name:           go-github-google-deck
Version:        1.1.0
Release:        %autorelease
Summary:        Record and replay Go program interactions
License:        Apache-2.0
URL:            https://github.com/google/deck
#!RemoteAsset:  sha256:448d91bc43df0a8a36774159d20fb27be339177b7a4a6c888caeb9f95909c7f0
Source0:        https://github.com/google/deck/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/golang/glog)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(golang.org/x/sys)

Provides:       go(github.com/google/deck) = %{version}

Requires:       go(github.com/golang/glog)
Requires:       go(golang.org/x/sys)

%description
Deck records and replays interactions with Go program backends.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
