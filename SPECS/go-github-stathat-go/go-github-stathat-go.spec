# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go
%define go_import_path  github.com/stathat/go

Name:           go-github-stathat-go
Version:        1.0.0
Release:        %autorelease
Summary:        Go package for reporting stat counts and values to StatHat
License:        MIT
URL:            https://github.com/stathat/go
#!RemoteAsset
Source0:        https://github.com/stathat/go/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/stathat/go) = %{version}

%description
This is a Go package for posting stats to your StatHat account.

The easiest way to use the package is with the EZ API functions.  You
can add stats directly in your code by just adding a call with a new
stat name.  Once StatHat receives the call, a new stat will be created
for you.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%{?autochangelog}
