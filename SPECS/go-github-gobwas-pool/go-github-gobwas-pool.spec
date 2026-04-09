# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           pool
%define go_import_path  github.com/gobwas/pool

Name:           go-github-gobwas-pool
Version:        0.2.1
Release:        %autorelease
Summary:        Go Pooling Helpers
License:        MIT
URL:            https://github.com/gobwas/pool
#!RemoteAsset
Source0:        https://github.com/gobwas/pool/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/gobwas/pool) = %{version}

%description
Tiny memory reuse helpers for Go.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
