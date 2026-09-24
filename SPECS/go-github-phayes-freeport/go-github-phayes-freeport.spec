# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: wangyf0611 <wangyufeng@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           freeport
%define go_import_path  github.com/phayes/freeport

Name:           go-github-phayes-freeport
Version:        0+git20180830.95f893a
Release:        %autorelease
Summary:        Get a free open TCP port that is ready to use
License:        BSD-3-Clause
URL:            https://github.com/phayes/freeport
VCS:            git:https://github.com/phayes/freeport.git
#!RemoteAsset:  sha256:b6ee1f330bbc0fbb673fd4d7bed1f4c7a33566399159390545814847f21a9b82
Source0:        https://github.com/phayes/freeport/archive/95f893ade6f2.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n freeport-95f893ade6f232a5f1511d61735d89b1ae2df543

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/phayes/freeport) = %{version}

%description
This package provides the github.com/phayes/freeport Go module source.

%files
%doc README.md
%license LICENSE.md
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
