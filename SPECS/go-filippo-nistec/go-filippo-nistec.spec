# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           nistec
%define go_import_path  filippo.io/nistec

Name:           go-filippo-nistec
Version:        0.0.4
Release:        %autorelease
Summary:        NIST elliptic curve implementation for Go
License:        BSD-3-Clause
URL:            https://github.com/FiloSottile/nistec
#!RemoteAsset:  sha256:0f407deba2a914982ab08d09a43d5e1d9d6f07705ceb274aeb3af847beba8137
Source0:        https://github.com/FiloSottile/nistec/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(golang.org/x/sys)

%description
Nistec implements the elliptic curves defined by NIST SP 800-186 with
constant-time group operations.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
