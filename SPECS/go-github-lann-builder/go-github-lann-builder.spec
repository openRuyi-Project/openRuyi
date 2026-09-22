# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: wangyf0611 <wangyufeng@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           builder
%define go_import_path  github.com/lann/builder

Name:           go-github-lann-builder
Version:        0+git20180802.47ae307
Release:        %autorelease
Summary:        Provides a method for writing fluent immutable builders
License:        MIT
URL:            https://github.com/lann/builder
VCS:            git:https://github.com/lann/builder.git
#!RemoteAsset:  sha256:4bb3af32496527fa569177f1f8fd3259faef7517d6e849d1b7aa38e97d0734e3
Source0:        https://github.com/lann/builder/archive/47ae307949d0.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n builder-47ae307949d02aa1f1069fdafc00ca08e1dbabac

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/lann/ps)

Provides:       go(github.com/lann/builder) = %{version}

Requires:       go(github.com/lann/ps)

%description
This package provides the github.com/lann/builder Go module source.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
