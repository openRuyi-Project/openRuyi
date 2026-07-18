# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           xz
%define go_import_path  github.com/xi2/xz
%define commit_id       48954b6210f8d154cb5f8484d3a3e1f83489309e

Name:           go-github-xi2-xz
Version:        0+git20260718.48954b6
Release:        %autorelease
Summary:        Go package for native XZ decompression
License:        LicenseRef-openRuyi-Public-Domain
URL:            https://github.com/xi2/xz
#!RemoteAsset:  sha256:ad0fe70f3d775715b5229504a06120ea6abae8a5d98d83bd506da1edea780286
Source0:        https://github.com/xi2/xz/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/xi2/xz) = %{version}

%description
Package xz implements XZ decompression natively in Go.

%files
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
