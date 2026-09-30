# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           builder
%define go_import_path  github.com/lann/builder
%define commit_id       47ae307949d02aa1f1069fdafc00ca08e1dbabac

Name:           go-github-lann-builder
Version:        0+git20260922.47ae307
Release:        %autorelease
Summary:        Fluent immutable builders for Go
License:        MIT
URL:            https://github.com/lann/builder
#!RemoteAsset:  sha256:4bb3af32496527fa569177f1f8fd3259faef7517d6e849d1b7aa38e97d0734e3
Source0:        https://github.com/lann/builder/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/lann/ps)

Provides:       go(github.com/lann/builder) = %{version}

Requires:       go(github.com/lann/ps)

%description
Fluent immutable builders for Go.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
