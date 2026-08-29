# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-events
%define go_import_path  github.com/docker/go-events
%define commit_id       e31b211e4f1cd09aa76fe4ac244571fab96ae47f

Name:           go-github-docker-go-events
Version:        0+git20260710.e31b211
Release:        %autorelease
Summary:        Go event dispatching primitives
License:        Apache-2.0
URL:            https://github.com/docker/go-events
#!RemoteAsset:  sha256:cb2afe191d70bfc7c339b71d6ea0e4803f765ed67e5e38dc6c8dcf42d972bd98
Source0:        https://github.com/docker/go-events/archive/%{commit_id}.tar.gz#/%{_name}-%{commit_id}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{commit_id}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/sirupsen/logrus)

Provides:       go(github.com/docker/go-events) = %{version}

Requires:       go(github.com/sirupsen/logrus)

%description
go-events provides queues, broadcasters, and retry helpers for Go event
processing.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
