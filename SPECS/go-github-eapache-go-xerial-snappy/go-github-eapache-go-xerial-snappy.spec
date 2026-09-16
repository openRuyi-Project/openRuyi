# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-xerial-snappy
%define go_import_path  github.com/eapache/go-xerial-snappy
%define commit_id       c322873962e393e443b7efa5969edac6884adfa1

Name:           go-github-eapache-go-xerial-snappy
Version:        0+git20260907.c322873
Release:        %autorelease
Summary:        Xerial-compatible Snappy framing for Go
License:        MIT
URL:            https://github.com/eapache/go-xerial-snappy
#!RemoteAsset:  sha256:dbafa8774ae3a79b013c9d28ec804151b59d098ed8f76ec93eac3ddce75a1eb9
Source0:        https://github.com/eapache/go-xerial-snappy/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/golang/snappy)

Provides:       go(github.com/eapache/go-xerial-snappy) = %{version}

Requires:       go(github.com/golang/snappy)

%description
go-xerial-snappy implements the Xerial Snappy framing format used by
Kafka clients such as IBM Sarama.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
