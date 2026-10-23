# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-httpheader
%define go_import_path  github.com/mozillazg/go-httpheader

Name:           go-github-mozillazg-go-httpheader
Version:        0.2.1
Release:        %autorelease
Summary:        Encode Go structs as HTTP header fields
License:        MIT
URL:            https://github.com/mozillazg/go-httpheader
#!RemoteAsset:  sha256:a6990188f680dd038b8edeb7d1576015e61c65b6e0ca532273dc06c527934446
Source0:        https://github.com/mozillazg/go-httpheader/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Upstream tests use an obsolete Errorf format that current Go vet rejects.
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/mozillazg/go-httpheader) = %{version}

%description
This Go library encodes struct fields into HTTP headers and decodes
header values back into structs. It is used by Tencent COS SDK v5.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
