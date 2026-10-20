# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           gunit
%define go_import_path  github.com/smarty/gunit

Name:           go-github-smarty-gunit
Version:        1.6.0
Release:        %autorelease
Summary:        xUnit-style test framework for Go
License:        MIT AND BSD-3-Clause AND Apache-2.0
URL:            https://github.com/smarty/gunit
#!RemoteAsset:  sha256:4847d48561a8208f50e3491407408f3bf2b368fe59fa2c40087f408f590919f2
Source0:        https://github.com/smarty/gunit/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Go vet rejects a non-constant Fatalf format; reports must be printed literally.
Patch2000:      2000-fix-fatalf-format-string.patch

BuildOption(prep):  -n gunit-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
# TestShouldEqual_TimeValues panics without the America/Denver and New_York zones.
BuildRequires:  tzdata

Provides:       go(github.com/smarty/gunit) = %{version}
Provides:       go(github.com/smartystreets/gunit) = %{version}

%description
Gunit provides suite setup and teardown hooks, assertions, and
convenience functions for xUnit-style Go tests.

%install -a
# Preserve the import path used before the repository moved to Smarty.
install -d %{buildroot}%{go_sys_gopath}/github.com/smartystreets
ln -s ../smarty/gunit %{buildroot}%{go_sys_gopath}/github.com/smartystreets/gunit

%files
%doc README.md
%license LICENSE.md assert/assertions/internal/go-diff/LICENSE assert/assertions/internal/go-render/LICENSE assert/assertions/internal/oglematchers/LICENSE
%{go_sys_gopath}/%{go_import_path}
%{go_sys_gopath}/github.com/smartystreets/gunit

%changelog
%autochangelog
