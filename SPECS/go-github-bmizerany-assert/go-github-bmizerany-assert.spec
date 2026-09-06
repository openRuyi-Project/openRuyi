# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           assert
%define go_import_path  github.com/bmizerany/assert
%define commit_id       b7ed37b82869576c289d7d97fb2bbd8b64a0cb28
# The example intentionally compares unequal values to demonstrate failure output.
%define go_test_exclude %{go_import_path}/example

Name:           go-github-bmizerany-assert
Version:        0+git20260818.b7ed37b
Release:        %autorelease
Summary:        Assertions for Go tests
License:        MIT
URL:            https://github.com/bmizerany/assert
#!RemoteAsset:  sha256:bcbbd85bb420d7fe6be587cdf524b01faa30a0095a52345c075787616385f503
Source0:        https://github.com/bmizerany/assert/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Use the canonical module path in the legacy example test.
Patch2000:      2000-example-use-canonical-assert-import-path.patch

BuildOption(prep):  -n %{_name}-%{commit_id}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/kr/pretty)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/kr/pretty)

%description
Assert provides simple equality and error assertions for Go tests.

%files
%doc README.md
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
