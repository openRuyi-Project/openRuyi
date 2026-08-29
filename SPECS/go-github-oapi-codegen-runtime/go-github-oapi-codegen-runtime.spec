# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: tangyihong <yihong.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           runtime
%define go_import_path  github.com/oapi-codegen/runtime
# Optional strict middleware integrations need their web framework stacks.
%global go_test_exclude_glob %{shrink:
    %{go_import_path}/strictmiddleware/echo*
    %{go_import_path}/strictmiddleware/gin*
    %{go_import_path}/strictmiddleware/iris*
}

Name:           go-github-oapi-codegen-runtime
Version:        1.0.0
Release:        %autorelease
Summary:        Runtime helpers for oapi-codegen generated Go code
License:        Apache-2.0
URL:            https://github.com/oapi-codegen/runtime
#!RemoteAsset:  sha256:927082334aa76c0adc3799f2954fb4698407c94b73cba06a8a4539dff9f50e2c
Source0:        https://github.com/oapi-codegen/runtime/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/apapsch/go-jsonmerge/v2)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(github.com/oapi-codegen/runtime) = %{version}

Requires:       go(github.com/apapsch/go-jsonmerge/v2)
Requires:       go(github.com/google/uuid)
Requires:       go(github.com/stretchr/testify)

%description
This package provides runtime helper functions used by Go code generated
by oapi-codegen, including OpenAPI parameter and request handling helpers.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
