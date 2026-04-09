# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-testing-interface
%define go_import_path  github.com/mitchellh/go-testing-interface

Name:           go-github-mitchellh-go-testing-interface
Version:        1.14.1
Release:        %autorelease
Summary:        Go (golang) library to expose *testing.T as an interface.
License:        MIT
URL:            https://github.com/mitchellh/go-testing-interface
#!RemoteAsset
Source0:        https://github.com/mitchellh/go-testing-interface/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/mitchellh/go-testing-interface) = %{version}

%description
go-testing-interface is a Go library that exports an interface that
*testing.T implements as well as a runtime version you can use in its
place.

The purpose of this library is so that you can export test helpers as a
public API without depending on the "testing" package, since you can't
create a *testing.T struct manually. This lets you, for example, use the
public testing APIs to generate mock data at runtime, rather than just
at test time.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
