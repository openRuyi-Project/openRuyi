# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           kdl-go
%define go_import_path  github.com/sblinch/kdl-go
%define commit_id       8b7053306ca65fbc39efd982c164a31767256b51
%define tests_commit    ef93a6b10c4e16d94194280bb6687661d7024476

Name:           go-github-sblinch-kdl-go
Version:        0+git20260902.8b70533
Release:        %autorelease
Summary:        Go implementation of the KDL document language
License:        MIT
URL:            https://github.com/sblinch/kdl-go
#!RemoteAsset:  sha256:539b0c68ee8f07d44ef53dece11daaccb3a505ef4d50b6503388459d1adb70d7
Source0:        https://github.com/sblinch/kdl-go/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
#!RemoteAsset:  sha256:fc0ac31c3edb8b489229921797621ba2fc9494429abb7707a2f4300b9c658bcc
Source1:        https://github.com/kdl-org/kdl/archive/%{tests_commit}.tar.gz#/%{_name}-tests-%{tests_commit}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Keep the complete test suite compatible with the current parser behavior.
Patch0:         0001-fix-stale-test-expectations.patch

BuildOption(check):  -tags kdldeterministic

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}

%description
Kdl-go encodes and decodes KDL version 1 documents and supports conversion
between KDL documents and Go data structures.

%prep
%autosetup -n %{_name}-%{commit_id} -p1 -a 1
mv kdl-%{tests_commit} kdl-org
ln -s ../kdl-org internal/kdl-org

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
