# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           editorconfig
%define go_import_path  mvdan.cc/editorconfig
%define core_test_commit 772112adb7aec5fffedf869d0d5a54c8374a0547

Name:           go-mvdan-editorconfig
Version:        0.3.0
Release:        %autorelease
Summary:        EditorConfig parser for Go
License:        BSD-3-Clause
URL:            https://github.com/mvdan/editorconfig
#!RemoteAsset:  sha256:f85e873f891f843c9b3a2a94ce95cc6ed94a9303b7c8fe6d69bf6d529d3b8850
Source0:        https://github.com/mvdan/editorconfig/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
# Restore the editorconfig-core-test submodule revision pinned by upstream.
#!RemoteAsset:  sha256:8ed5b62da05455cdd3cc3f0c1cda6628355aa2f5952e6749c11e7a451fd1bd09
Source1:        https://github.com/editorconfig/editorconfig-core-test/archive/%{core_test_commit}.tar.gz#/%{_name}-core-test-%{core_test_commit}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Declare the CMake policy baseline required by current CMake.
Patch2000:      2000-Declare-CMake-compatibility-for-core-tests.patch
# Avoid CMake 4 deprecation output breaking multiline output assertions.
Patch2001:      2001-Raise-CMake-policy-baseline-for-CMake-4.patch

BuildOption(prep):  -N

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  cmake

Provides:       go(%{go_import_path}) = %{version}

%description
This package parses EditorConfig files and resolves the properties that apply
to a path.

%prep -a
%patch -P 2000 -p1
rm -rf core-test
mkdir -p core-test
tar -xf %{SOURCE1} --strip-components=1 -C core-test
pushd core-test
%patch -P 2001 -p1
popd

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
