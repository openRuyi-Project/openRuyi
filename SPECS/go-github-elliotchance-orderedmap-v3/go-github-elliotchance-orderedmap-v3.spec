# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           orderedmap
%define go_import_path  github.com/elliotchance/orderedmap/v3
%define go_source_subdir v3
# Tests require an unavailable test-only dependency.
%define go_test_exclude_glob %{go_import_path}*

Name:           go-github-elliotchance-orderedmap-v3
Version:        3.1.1
Release:        %autorelease
Summary:        Generic ordered map implementation for Go
License:        MIT
URL:            https://github.com/elliotchance/orderedmap
#!RemoteAsset:  sha256:6ffc6b0417c85053a3ff463668724e25f9e01498cfe12090718a71ffd38d265f
Source0:        https://github.com/elliotchance/orderedmap/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# The tagged archive contains the whole repository.  Build and install only
# the v3 module, rather than copying the repository root to the v3 import path.

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/elliotchance/orderedmap/v3) = %{version}

%description
Generic Go ordered map implementation that preserves insertion order.

%install
pushd %{go_source_subdir}
%buildsystem_golangmodules_install
popd

%check
pushd %{go_source_subdir}
%buildsystem_golangmodules_check
popd

%files
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
