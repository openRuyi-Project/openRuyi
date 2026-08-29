# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           deepcopy
%define go_import_path  github.com/mohae/deepcopy
%define commit_id c48cc78d482608239f6c4c92a4abd87eb8761c90

Name:           go-github-mohae-deepcopy
Version:        0+git20260611.c48cc78
Release:        %autorelease
Summary:        Deep copy helper for Go values
License:        MIT
URL:            https://github.com/mohae/deepcopy
#!RemoteAsset:  sha256:6b171346026b553c49584c10a72267ebabae71e229b08c42cf9d23bd4ddcd6f2
Source0:        https://github.com/mohae/deepcopy/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
# TestTimeCopy needs IANA timezone data for America/New_York and Europe/Prague.
BuildRequires:  tzdata

Provides:       go(github.com/mohae/deepcopy) = %{version}

%description
deepcopy provides helpers for recursively copying Go values.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
