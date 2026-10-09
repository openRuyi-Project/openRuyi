# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: wangyf0611 <wangyufeng@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           godirwalk
%define go_import_path  github.com/karrick/godirwalk

Name:           go-github-karrick-godirwalk
Version:        1.10.0
Release:        %autorelease
Summary:        Provides functions to read and traverse directory trees
License:        BSD-2-Clause
URL:            https://github.com/karrick/godirwalk
VCS:            git:https://github.com/karrick/godirwalk.git
#!RemoteAsset:  sha256:70e0f389574074eae0de6fe3c91bb1d57d44d1ab62abda311e07a066aed25d73
Source0:        https://github.com/karrick/godirwalk/archive/v1.10.0.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n godirwalk-1.10.0

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/karrick/godirwalk) = %{version}

%description
This package provides the github.com/karrick/godirwalk Go module source.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
