# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           mapfs
%define go_import_path  github.com/josharian/mapfs

Name:           go-github-josharian-mapfs
Version:        0+git20261030.095c008
Release:        %autorelease
Summary:        A fork of the Go standard library's testing/fstest MapFS
License:        BSD-3-Clause
URL:            https://github.com/josharian/mapfs
#!RemoteAsset:  sha256:f1a5b5f30c989dee3526fd4c0879b4badb08533b896c3471e922ddb8cd15aff9
Source0:        https://github.com/josharian/mapfs/archive/095c008854e6.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}

%description
MapFS is a fork of the Go standard library's testing/fstest MapFS package.

%files
%doc readme.md
%license license
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
