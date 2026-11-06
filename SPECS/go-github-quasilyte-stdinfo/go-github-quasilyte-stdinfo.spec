# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           stdinfo
%define go_import_path  github.com/quasilyte/stdinfo
%define commit_id       f7386bf0256791d0b89fae7718fb9274230edded

Name:           go-github-quasilyte-stdinfo
Version:        0+git20261022.f7386bf
Release:        %autorelease
Summary:        Go standard library package information
License:        MIT
URL:            https://github.com/quasilyte/stdinfo
#!RemoteAsset:  sha256:12f6e890780fdfc6a957372dd0a9c07e8359f77e90d0128d9cafaaf8560375ed
Source0:        https://github.com/quasilyte/stdinfo/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/quasilyte/stdinfo) = %{version}

%description
Go standard library package information.
This package contains the complete upstream Go source and test data.

%prep
%autosetup -p1 -n stdinfo-%{commit_id}

%files
%license LICENSE
%{go_sys_gopath}/github.com/quasilyte/stdinfo

%changelog
%autochangelog
