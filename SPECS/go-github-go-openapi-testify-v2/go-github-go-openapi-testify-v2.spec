# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yihong <yihong.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           testify
%define go_import_path  github.com/go-openapi/testify/v2

# Only assert and require are consumed by errors/strfmt, and they are
# self-contained (spew/difflib vendored in ./internal). The optional enable/*,
# codegen and hack trees pull in golang.org/x/term, yaml, golang.org/x/tools
# etc.; scope the test run to the self-contained core that we ship for.
%global go_test_include %{shrink:
    github.com/go-openapi/testify/v2/assert
    github.com/go-openapi/testify/v2/require
}

Name:           go-github-go-openapi-testify-v2
Version:        2.4.2
Release:        %autorelease
Summary:        Self-contained testify fork used by the go-openapi projects
License:        Apache-2.0
URL:            https://github.com/go-openapi/testify
#!RemoteAsset:  sha256:f4070345d40c238af4b0fb372d0156a8d2e73ca233900074d1593495020092b3
Source0:        https://github.com/go-openapi/testify/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/go-openapi/testify/v2) = %{version}
Provides:       go(github.com/go-openapi/testify/v2/assert) = %{version}
Provides:       go(github.com/go-openapi/testify/v2/enable) = %{version}
Provides:       go(github.com/go-openapi/testify/v2/enable/colors) = %{version}
Provides:       go(github.com/go-openapi/testify/v2/enable/stubs) = %{version}
Provides:       go(github.com/go-openapi/testify/v2/enable/stubs/colors) = %{version}
Provides:       go(github.com/go-openapi/testify/v2/enable/stubs/yaml) = %{version}
Provides:       go(github.com/go-openapi/testify/v2/enable/yaml) = %{version}
Provides:       go(github.com/go-openapi/testify/v2/require) = %{version}

%description
A self-contained fork of stretchr/testify maintained by the go-openapi
project. It provides the assert and require assertion helpers (with spew
and difflib vendored internally) used by the test suites of
go-openapi/errors and go-openapi/strfmt.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
