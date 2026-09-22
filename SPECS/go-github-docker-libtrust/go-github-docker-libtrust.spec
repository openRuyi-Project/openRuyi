# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: wangyf0611 <wangyufeng@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           libtrust
%define go_import_path  github.com/docker/libtrust
%define go_test_exclude %{go_import_path}/tlsdemo

Name:           go-github-docker-libtrust
Version:        0+git20160708.aabc10e
Release:        %autorelease
Summary:        Go library for libtrust
License:        Apache-2.0
URL:            https://github.com/docker/libtrust
VCS:            git:https://github.com/docker/libtrust.git
#!RemoteAsset:  sha256:f57dc468339505a0ce7f248cbec13af5fd492cd7a885c50af70d9786144f4f91
Source0:        https://github.com/docker/libtrust/archive/aabc10ec26b7.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n docker.libtrust-aabc10ec26b754e797f9028f4589c5b7bd90dc20

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/docker/libtrust) = %{version}

%description
This package provides the github.com/docker/libtrust Go module source.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
