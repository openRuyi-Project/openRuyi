# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           atomic
%define go_import_path  go.uber.org/atomic

Name:           go-uber-atomic
Version:        1.12.0
Release:        %autorelease
Summary:        Wrapper types for sync/atomic which enforce atomic access
License:        MIT
URL:            https://github.com/uber-go/atomic
#!RemoteAsset:  sha256:a90f965f58ed3e095a19fea1e62aadf4f163b69efd5086c4789b3e1e6ccd56af
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
