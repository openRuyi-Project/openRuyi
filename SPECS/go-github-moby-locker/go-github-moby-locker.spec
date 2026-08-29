# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: tangyihong <yihong.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           locker
%define go_import_path  github.com/moby/locker

Name:           go-github-moby-locker
Version:        1.0.1
Release:        %autorelease
Summary:        This is a direct pull from https://github.com/moby/moby/tree/master/pkg/locker
License:        Apache-2.0
URL:            https://github.com/moby/locker
#!RemoteAsset:  sha256:524f312615b4dc06f0199612125a9e0481869a087875666e39f09873a09e24fc
Source0:        https://github.com/moby/locker/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/moby/locker) = %{version}

%description
locker provides a mechanism for creating per-key finer-grained locking in Go.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
