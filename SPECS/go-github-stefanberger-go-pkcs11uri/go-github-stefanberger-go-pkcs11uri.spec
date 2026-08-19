# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: Apache-2.0

%define _name           go-pkcs11uri
%define go_import_path  github.com/stefanberger/go-pkcs11uri
%define commit_id       78284954bff6dcce7888166bb79bbba93bea0879

Name:           go-github-stefanberger-go-pkcs11uri
Version:        0+git202608018.7828495
Release:        %autorelease
Summary:        PKCS#11 URI parser for Go
License:        Apache-2.0
URL:            https://github.com/stefanberger/go-pkcs11uri
#!RemoteAsset:  sha256:203de9053f63a4bfc4703bfcd223400b7b852ad30bcf82d5c9185990cb1e20bd
Source0:        https://github.com/stefanberger/go-pkcs11uri/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/stefanberger/go-pkcs11uri) = %{version}

%description
Parser and formatter for PKCS#11 URIs written in Go.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
