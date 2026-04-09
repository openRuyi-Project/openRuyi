# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-version
%define go_import_path  github.com/hashicorp/go-version

Name:           go-github-hashicorp-go-version
Version:        1.8.0
Release:        %autorelease
Summary:        A Go (golang) library for parsing and verifying versions and version constraints.
License:        MPL-2.0
URL:            https://github.com/hashicorp/go-version
#!RemoteAsset
Source0:        https://github.com/hashicorp/go-version/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/hashicorp/go-version) = %{version}

%description
go-version is a library for parsing versions and version constraints,
and
verifying versions against a set of constraints. go-version can sort a
collection of versions properly, handles prerelease/beta versions, can
increment versions, etc.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
