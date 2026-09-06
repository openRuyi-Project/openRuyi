# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           gcfg.v1
%define go_import_path  gopkg.in/gcfg.v1
# The types tests assert legacy strconv behavior that changed in Go 1.26.
%define go_test_exclude %{go_import_path}/types

Name:           go-gopkg-gcfg.v1
Version:        1.2.3
Release:        %autorelease
Summary:        INI-style configuration reader for Go
License:        BSD-3-Clause
URL:            https://github.com/go-gcfg/gcfg
#!RemoteAsset:  sha256:3d60ba7a07e7d7d831a756f565c7fdc75895f294b2b69185674bb0ed70622645
Source0:        https://github.com/go-gcfg/gcfg/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(gopkg.in/warnings.v0)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(gopkg.in/warnings.v0)

%description
Gcfg reads INI-style configuration files into Go structs with support for
sections, subsections, and user-defined types.

%files
%doc README
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
