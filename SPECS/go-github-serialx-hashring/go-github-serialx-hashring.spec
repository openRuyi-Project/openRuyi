# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: wangyf0611 <wangyufeng@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           hashring
%define go_import_path  github.com/serialx/hashring

Name:           go-github-serialx-hashring
Version:        0+git20180504.49a4782
Release:        %autorelease
Summary:        Implements consistent hashing that can be used when
License:        MIT
URL:            https://github.com/serialx/hashring
VCS:            git:https://github.com/serialx/hashring.git
#!RemoteAsset:  sha256:540468a75f9f8b664ab19a87ed3ea02351c9bb08a21877fa864e6219438cc299
Source0:        https://github.com/serialx/hashring/archive/49a4782e9908.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n hashring-49a4782e9908fe098c907022a1bd7519c79803d6

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/serialx/hashring) = %{version}

%description
This package provides the github.com/serialx/hashring Go module source.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
