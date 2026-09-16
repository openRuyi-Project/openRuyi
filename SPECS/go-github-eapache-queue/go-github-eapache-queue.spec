# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           queue
%define go_import_path  github.com/eapache/queue

Name:           go-github-eapache-queue
Version:        1.1.0
Release:        %autorelease
Summary:        Fast ring-buffer queue for Go
License:        MIT
URL:            https://github.com/eapache/queue
#!RemoteAsset:  sha256:2be4716ba2bba5f7c125a8fe72ba534f02cf0d7d98d3a372d4ebe54b170f7329
Source0:        https://github.com/eapache/queue/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/eapache/queue) = %{version}

%description
queue is a fast ring-buffer queue for Go, used by IBM Sarama.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
