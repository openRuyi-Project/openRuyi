# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           profile
%define go_import_path  github.com/pkg/profile

Name:           go-github-pkg-profile
Version:        1.7.0
Release:        %autorelease
Summary:        Provides a simple way to manage runtime/pprof profiling of your Go application
License:        BSD-2-Clause
URL:            https://github.com/pkg/profile
#!RemoteAsset:  sha256:3688b8af441af9204950860d98807635e6fa5822bc7a1cc95b6b238c47cd38bb
Source0:        https://github.com/pkg/profile/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/felixge/fgprof)

Provides:       go(github.com/pkg/profile) = %{version}

Requires:       go(github.com/felixge/fgprof)

%description
Simple profiling support package for Go

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
