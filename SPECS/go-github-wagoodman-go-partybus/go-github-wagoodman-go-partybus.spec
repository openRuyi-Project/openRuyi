# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-partybus
%define go_import_path  github.com/wagoodman/go-partybus
%define commit_id       8ccac152c651

Name:           go-github-wagoodman-go-partybus
Version:        0+git20260718.8ccac15
Release:        %autorelease
Summary:        An event bus in go
License:        MIT
URL:            https://github.com/wagoodman/go-partybus
#!RemoteAsset:  sha256:3f648088141b5abda8039323f7b99f405530c4e42f0221d8ca2ebc6d72647394
Source0:        %{url}/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{commit_id}

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/wagoodman/go-partybus) = %{version}

%description
An event bus in go.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
