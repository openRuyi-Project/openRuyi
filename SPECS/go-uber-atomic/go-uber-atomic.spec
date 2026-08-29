# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           atomic
%define go_import_path  go.uber.org/atomic

Name:           go-uber-atomic
Version:        1.11.0
Release:        %autorelease
Summary:        Wrapper types for sync/atomic which enforce atomic access
License:        MIT
URL:            https://github.com/uber-go/atomic
#!RemoteAsset:  sha256:cfe258c20d71ac4dbf0f716a23ed00c332b7f281180651e2a67ad40a8b0772cc
Source0:        https://github.com/uber-go/atomic/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/stretchr/testify)
# For tests.
BuildRequires:  tzdata

Provides:       go(go.uber.org/atomic) = %{version}

%description
Simple wrappers for primitive types to enforce atomic access.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
