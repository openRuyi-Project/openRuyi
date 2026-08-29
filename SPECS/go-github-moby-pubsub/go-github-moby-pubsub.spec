# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: tangyihong <yihong.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           pubsub
%define go_import_path  github.com/moby/pubsub

Name:           go-github-moby-pubsub
Version:        1.0.0
Release:        %autorelease
Summary:        Simple publish-subscribe package for Go
License:        Apache-2.0
URL:            https://github.com/moby/pubsub
#!RemoteAsset:  sha256:f0076b6a2c498dbbc27311d8b0035955a626f773137f62e25c386c1adc543562
Source0:        https://github.com/moby/pubsub/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/moby/pubsub) = %{version}

%description
pubsub is a simple, generic publish/subscribe package for Go.

%files
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
